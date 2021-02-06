# TITLE fibonacci   (fibonacci.s)
# This program handles the I/O for a fibonacci function.

             .data
# variables
IntPrompt:   .asciiz "Enter a integer between 0 and 25: "
OutStr:      .asciiz "\nThe Fibonacci value is "
LowError:    .asciiz "\nYour input was too small.  Try again: "
HighError:   .asciiz "\nYour input was too large.  Try again: "
AgainStr:    .asciiz "\nWould you like to try again? (y/n): "
NewLine:     .asciiz "\n"

YesNoBuf:    .space  5   # Plenty of room for 'yes' or 'no'
IntIn:       .word   0
IntMin:      .word   0
IntMax:      .word   25

    .text
    .globl   main

again:                  # print a newline on subsequent returns to main
    la  $a0, NewLine    # point to NewLine
    li  $v0, 4          # print_string
    syscall

main:                   # start of the main procedure

 
    # Get an integer
    la  $a0, IntPrompt      # point to IntPrompt
    li  $v0, 4              # print_string
    syscall
    
GetInt: li  $v0, 5          # read_integer
    syscall
        move    $t0, $v0    # move input before it gets changed
    
    # check if below min
    lw  $a1, IntMin         # load our lower bound
    bge $v0, $a1, BigEnough # if good, try next check
    la  $a0, LowError       # point to Error string
    li  $v0, 4              # print_string
    syscall
    j     GetInt    

    # check if above max
BigEnough:
    lw  $a1, IntMax             # load our upper bound
    ble $v0, $a1, SmallEnough   # if good, try next check
    la  $a0, HighError          # point to Error string
    li  $v0, 4                  # print_string
    syscall
    j   GetInt  
    
SmallEnough:
    # save the input, just in case
    sw  $v0, IntIn
    
    # Print the text to go with the output
    la  $a0, OutStr     # point to OutStr
    li  $v0, 4          # print_string
    syscall

# Call your fib routine here.  When it returns, put the return value
# in $a0 and print it out.  Comment out the next block, which just
# prints out a dummy number.
    
Fib:
    sw    $fp, -12($sp)
    move  $fp, $sp
    addiu $sp, $sp, -12

    sw    $ra, -4($sp)
    sw    $s0, -8($sp)
    sw    $s1, -12($sp)
    sw    $sp, $sp, -12

    lw    $s0, -8($fp)
    bnez  $s0,  next_check_1
    sw    $s0, -4($fp)
    j FibEnd

    next_check_1:
        li  $s1, 1
        beq $s0, $s1, next_check_2
        sw  $s0, -4($sp)
        j FibEnd

    next_check_2:
        addiu $s0, $s0, -1
        sw    $s0, -8($sp)
        jal Fib

        lw    $s1, -4($sp)
        addiu $s0, $s0, -1
        sw    $s0, -8($sp)
        jal Fib

        lw    $s0, -4($sp)
        addiu $s0, $s0, $s1
        sw    $s0, -4($fp)
    # Print a dummy number for output testing.  16 is not a
    # valid return from fib() so I should not see it in anyone's
    # final output.
    #li  $a0, 16         # not a valid number
    #li  $v0, 1          # print_integer
    #syscall

    # Print a newline before continuing
    la  $a0, NewLine        # point to NewLine
    li  $v0, 4          # print_string
    syscall
    
    # Prompt to see if the user wants to do it again
    la  $a0, AgainStr   # point to AgainStr
    li  $v0, 4          # print_string
    syscall

    # Get the input
    la  $a0, YesNoBuf   # point to YesNoBuf
    li  $a1, 5          # length of buffer
    li  $v0, 8          # read_string
    syscall
    lb  $t0, YesNoBuf   # load the first character into $t0
    
    # Test if first character is 'Y'
    li  $t1, 89         # ASCII for 'Y'
    beq $t0, $t1, again # equal, so run program again
    
    # Test if first character is 'y'
    li  $t1, 121        # ASCII for 'y'
    beq $t0, $t1, again # equal, so run program again
    
    # Not 'yes', so assume 'no' and end program
    jr  $ra

# fib function goes below here:
FibEnd:
    addiu $sp, $sp, 12
    lw    $ra, -4($sp)
    lw    $s0, -8($sp)
    lw    $s1, -12($sp)

    move $sp, $fp
    lw   $fp, -12($sp)
    jr   $ra 
