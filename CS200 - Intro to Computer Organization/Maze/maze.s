# Maze
#==============================================================================
# BEGIN IMPLEMENTATION
#==============================================================================

#==============================================================================
# CONSTANTS
#==============================================================================
	.data
GRID_WIDTH:		.word	80		# need to add 1 to print as string
GRID_HEIGHT:	.word	23
GRID_SIZE:		.word	1840	# because I can't precalculate it in
								# MIPS like I could in MASM
NORTH:		.word	0
EAST:		.word   1
SOUTH:		.word	2
WEST:		.word	3
RGEN:		.word	1073807359	# a sufficiently large prime for rand
POUND:		.byte	35		# the '#' character
SPACE:		.byte	32		# the ' ' character
NEWLINE:	.byte	10		# the newline character

#==============================================================================
# STRING VARIABLES
#==============================================================================

rsdPrompt:	.asciiz "Enter a seed number (1073741824 - 2147483646): "
smErr1:		.asciiz "That number is too small, try again: "
bgErr:		.asciiz "That number is too large, try again: "
newLine:	.asciiz "\n"

#==============================================================================
# GLOBAL VARIABLES
#==============================================================================

grid:	.space	1841		# ((79 + 1) * 23) + 1 bytes reserved for grid
rSeed:	.word	0		# a seed for generating a random number

#==============================================================================
# FUNCTIONS
#==============================================================================
	.text
	.globl main

main:
	sw	$ra, 0($sp)		# save the return address
	jal	srand			# get a random seed
	jal	ResetGrid		# reset the grid to '#'s
	li	$t0, 1			# set up for start of generation at (1,1)
	sw	$t0, -4($sp)	# push first param
	sw	$t0, -8($sp) 	# push second param
	jal	Visit			# start the recursive generation
	jal	PrintGrid		# display the grid
	lw	$ra, 0($sp)		# restore the return address
	jr	$ra				# exit the program

ResetGrid:
	
	# save the registers
	sw	$s0, -4($sp)	# $s0 will be the loop counter
	sw	$s1, -8($sp)	# $s1 will hold the array bound
	sw	$s2, -12($sp)	# $s2 will be the grid base address
	sw	$s3, -16($sp)	# $s3 will hold the character
	sw	$s4, -20($sp)	# $s4 will hold the grid width
	sw  $s5, -24($sp)   # $s5 will hold the newline character
	sw	$s6, -28($sp)	# $s6 used for calculations
	# NOTICE THAT I DON'T BOTHER MOVING THE STACK POINTER
	
	# load the working values
	li	$s0, 1		# initialize the counter
	lw	$s1, GRID_SIZE	# initialize the array bound
	la	$s2, grid	# get the base address
	lb	$s3, POUND	# store the '#' ASCII code
	lw	$s4, GRID_WIDTH # store the grid width
	lb	$s5, NEWLINE	# store the newline ASCII code
  
ResetLoop:
	sb	$s3, 0($s2)			# put a '#' in the grid
	addi	$s0, $s0, 1		# increment the loop counter
	addi	$s2, $s2, 1		# point at next char position
	div	    $s0, $s4		# divide the counter by grid width
	mfhi	$s6				# get remainder in calculation register
	bnez	$s6, NoNewLine	# keep going
	
	sb	$s5, 0($s2)     	# put a newline in the grid
	addi	$s0, $s0, 1		# increment the loop counter
	addi	$s2, $s2, 1		# point at next char position
	
NoNewLine:
	blt	$s0, $s1, ResetLoop	# if less than end, loop again
	
	# when we fall out of the loop, restore the registers and return
	lw	$s0, -4($sp)	
	lw	$s1, -8($sp)	
	lw	$s2, -12($sp)	
	lw	$s3, -16($sp)	
	lw	$s4, -20($sp)	
	lw  $s5, -24($sp)
	lw	$s6, -28($sp)
	# IN A LANGUAGE WITH PUSH/POP, YOU WOULD HAVE TO POP THEM
	# FROM THE STACK IN THE REVERSE ORDER YOU PUSHED THEM.
	
	jr	$ra		# return

srand:
	# For this function, we only need to preserve 3 registers.  We use
	# $a0 and $v0 for I/0, and we use $s0 as a scratch register.

	# save the registers
	sw	$v0, -4($sp)	# $v0 will be the service code
	sw	$a0, -8($sp)	# $a0 will point to the grid string
	sw	$s0, -12($sp)	# $s0 will hold the input for testing
	
	# prompt for a random seed and get the value
	la	$a0, rsdPrompt
	li	$v0, 4			# print_string
	syscall

input10:
	li	$v0, 5		# read_int
	syscall
	li	$s0, 1073741823			# put 2147483646 in t0 for comparison
	bgtu	$v0, $s0, input11	# input bigger than 1073741823?
	la	$a0, smErr1				# no, point to error and
	li	$v0, 4					# print_string
	syscall
	j	input10					# try again

input11:
	li	$s0, 2147483646			# upper bound in register t0 for comparison
	bleu	$v0, $s0, input12	# less than or equal 2147483646?
	la	$a0, bgErr				# no, point to error and
	li	$v0, 4					# print_string
	syscall
	j	input10					# try again

input12:	
	# number is good, save and move on
	sw	$v0, rSeed
	
	# restore the registers
	lw	$v0, -4($sp)	
	lw	$a0, -8($sp)	
	lw	$s0, -12($sp)

	jr	$ra		# return

rand:
	# For this function, we only need to preserve 3 registers.  We use
	# $s0 - $s2 as scratch registers.

	# save the registers
	sw	$s0, -16($sp)	# $s0 random
	sw	$s1, -20($sp)	# $s1 will hold generator and min
	sw	$s2, -24($sp)	# $s2 will hold new seed and max
	
	# linear congruence
	lw	$s1, RGEN		# load the generator
	lw	$s2, rSeed		# last seed
	multu	$s1, $s2	# result goes in hi/lo registers
	mflo	$s2			# lo result is new seed
	mfhi	$s0			# hi result is new random
	sw	$s2, rSeed		# store the seed in memory

	# fit the random into the range
	lw	$s2, -12($sp)		# get the max
	lw	$s1, -8($sp)    	# get the min
	sub	$s2, $s2, $s1		# s2 is now range (max - min)
	addiu	$s2, $s2, 1		# increment the range
	divu	$s0, $s2		# remainder is in hi register
	mfhi	$s0				# get it back
	addu	$s0, $s0, $s1	# add the minimum to put it in range
	sw	$s0, -4($sp)		# store the random in the return

	# restore the registers
	lw	$s0, -16($sp)	
	lw	$s1, -20($sp)	
	lw	$s2, -24($sp)

	jr	$ra		# return
	
XYToIndex:
	# For this function, we only need to preserve 3 registers.  We use
	# $s0 - $s2 as scratch registers.
	
	# save the registers
	sw	$s0, -16($sp)	# $s0 will hold grid width
	sw	$s1, -20($sp)	# $s1 will hold x
	sw	$s2, -24($sp)	# $s2 will hold y
  
  	# get the values for our calculation
  	lw	$s0, GRID_WIDTH	# load the grid width
  	lw	$s1, -8($sp)	# load x
  	lw	$s2, -12($sp)	# load y
  	
  	# calculate and store in return
  	multu	$s0, $s2		# result goes in hi/lo registers
  	mflo	$s0				# hopefully only need LO
  	addu	$s0, $s0, $s1	# add x
  	sw	$s0, -4($sp)		# store result in return

  	# restore the registers
	lw	$s0, -16($sp)	
	lw	$s1, -20($sp)	
	lw	$s2, -24($sp)

	jr	$ra		# return

IsInBounds:
	# For this function, we only need to preserve 3 registers.  We use
	# $s0 - $s2 as scratch registers.
	
	# save the registers
	sw	$s0, -16($sp)	# $s0 will hold bounds for testing and return
	sw	$s1, -20($sp)	# $s1 will hold x
	sw	$s2, -24($sp)	# $s2 will hold y
  
  	# get the values for our calculation
  	lw	$s1, -8($sp)	# load x
  	lw	$s2, -12($sp)	# load y
  	
  	# test width
  	lw	$s0, GRID_WIDTH				# load the grid width
  	bgtu	$s1, $s0, OutOfBounds	# catches both >= grid width and < 0
  	
  	# test height
  	lw	$s0, GRID_HEIGHT			# load the grid height
  	bgeu	$s2, $s0, OutOfBounds	# catches both >= grid height and < 0
  	
  	li	$s0, 1						# neither failed, so set true (1)
  	sw	$s0, -4($sp)
  	j	EndBounds
  	
OutOfBounds:
	li	$s0, 0			# something failed, so set false (0)
	sw	$s0, -4($sp)

EndBounds:
  	# restore the registers
	lw	$s0, -16($sp)	
	lw	$s1, -20($sp)	
	lw	$s2, -24($sp)

	jr	$ra		# return

Visit:
    #
    #

    # Pushing current frame pointer onto the stack pointer
    sw      $fp, -12($sp)
    move    $fp, $sp
    addiu   $sp, $sp, -12

    # Preserve registers
    sw      $ra, -12($sp)
    sw      $s0, -16($sp)
    sw      $s1, -20($sp)
    sw      $s2, -24($sp)
    sw      $s3, -28($sp)
    sw      $s4, -32($sp)
    sw      $s5, -36($sp)
    sw      $s6, -40($sp)
    addiu   $sp, $sp, -40

    # Use local variables in registers
    addiu   $sp, $sp, -16
    lw      $s0, NORTH
    lw      $s1, WEST
    lw      $s2, EAST
    lw      $s3, SOUTH
    sw      $s0, 28($sp)
    sw      $s1, 24($sp)
    sw      $s2, 20($sp)
    sw      $s3, 16($sp)

    # Main Code
    la      $s7, -12($sp)
    lw      $t0, NORTH
    sw      $t0, 0($s7)
    lw      $t0, WEST
    sw      $t0, -4($s7)
    lw      $t0, EAST
    sw      $t0, -8($s7)
    lw      $t0, SOUTH
    sw      $t0, -12($s7)

    # Loop
    li      $t1, 0
    li      $t2, 4
    li      $t3, 0
    sw      $t3, -8($sp)
    li      $t3, 3
    sw      $t3, -12($sp)

Shuffle:
    jal rand
    lw     $t3, -4($sp)
    li     $t4, 4
    multi  $t3, 4
    mflo   $t3
    mult   $t1, $t4
    mflo   $t4
    sub    $s8, $s7, $t3
    sub    $s9, $s7, $t4
    lw     $t5, 0($s8)
    lw     $t6, 0($s9)
    sw     $t5, 0($s9)
    sw     $t6, 0($S8)
    addi   $t1, 1
    blt    $t1, $t2, Shuffle

    # Deaolocate local variables
    addiu   $sp, $sp, 16

    # Restore registers
    addiu   $sp, $sp, 40
    lw      $ra, -12($sp)
    lw      $s0, -16($sp)
    lw      $s1, -20($sp)
    lw      $s2, -24($sp)
    lw      $s3, -28($sp)
    lw      $s4, -32($sp)
    lw      $s5, -36($sp)
    lw      $s6, -40($sp)

    # Restore stack pointer and frame pointer
    move    $sp, $fp
    lw      $fp, -12($sp)

	jr	$ra

PrintGrid:

	# This is even easier than the C++ code because I've set the grid up as 
	# one long string so I can simply use a system service to print it to 
	# the console. Doing character by character printing in MASM was more 
	# complicated. We need to preserve 2 registers, $v0 and $a0 used for
	# this system service.

	# save the registers
	sw	$v0, -4($sp)	# $v0 will be the service code
	sw	$a0, -8($sp)	# $a0 will point to the grid string
	
	# load the values and print
	li	$v0, 4		# print service
	la	$a0, grid	# string to print
	syscall

	# restore the registers
	lw	$v0, -4($sp)	
	lw	$a0, -8($sp)	

	jr	$ra		# return
