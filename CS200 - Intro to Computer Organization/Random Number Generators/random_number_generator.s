# 
# Random Number Generator
#
#

                    .data

get_low_num:        .asciiz "Enter a low number: "
get_high_num:       .asciiz "Enter a high number: "
get_seed_num:       .asciiz "Enter a seed number: "
get_total_num:      .asciiz "Numbers to generate: "
new_line:           .asciiz "\n"
prime_num           .word 100 # Replace with very LARGE prime
low_num             .word 0
high_num            .word 0
counter             .word 0
seed                .word 0

                    .text
                    .globl main

main:

    li      $v0, 4
    la      $a0, get_low_num
    syscall

    li      $v0, get_low_num
    syscall
    sw      $v0, low_num

    li      $v0, 4
    la      $a0, new_line
    syscall

    li      $v0, get_high_num
    syscall
    sw      $v0, high_num

    li      $v0, 4
    la      $a0, new_line
    syscall

    li      $v0, get_seed_num
    syscall
    sw      $v0, seed

    li      $v0, 4
    la      $a0, new_line
    syscall

    li      $v0, get_total_num
    syscall
    sw      $v0, counter

    li      $v0, 4
    la      $a0, new_line
    syscall

    lw      $t0, prime_num
    lw      $t1, low_num
    lw      $t2, high_num
    lw      $t7, counter 

loop:
    # LINERAR CONGRUENCE
    lw      $t3, seed
    mult    $t0, $t3
    mfhi    $t4
    mflo    $t3
    sw      $t3, seed

    # RANGE FITTING
    sub     $t5, $t2, $t1 # SUBTRACT LOW FROM HIGH IN $t5
    addi    $t5, $t5, 1 # ADD 1 TO t5
    div     $t4, $t5
    mfhi    $t5
    add     $t5, $t5, $t1

    li      $v0, 1
    move    $a0, $t5
    syscall

    li      $v0, 4
    la      $a0, new_line
    syscall
    
    addi    $t7, $t7, -1
    bgtz    $t7, loop

#input1:
##    
#    li $v0, 5
#    syscall
#    bgtz $v0, input2
#    la $v0, $t8, fail
#    li $v0,  4
#    syscall
#    j input1

end:

    li      $v0, 10
    syscall
