#
# BubbleSort
#

            .data
PrintTitle: .asciiz "BubbleSort\n"
DataSize:   .asciiz "How large of a data set would you like to sort? With a range of (1-10)"
GetInput:   .asciiz "Enter integers to sort followed by return: \n"
GetSpace:   .asciiz ","
NewLine:    .asciiz "\n"
PrintSort:  .asciiz "\nSorted Data\n"

            .text
            .globl main

main:
    move    $s0, $t0
    addi    $t1, 1
    add     $t2, $zero, $zero
    add     $t3, $zero, $zero
    add     $t4, $zero, $zero
    add     $t5, $zero, $zero
    add     $t6, $zero, $zero
    sub     $t7, $zero, 1
    
    li      $v0, 4
    la      $a0, PrintTitle
    syscall
    
    li      $v0, 4
    la      $a0, GetInput
    syscall

    add     $s1, $s0, $zero

ReadNums:
    li      $v0, 5
    syscall
    beq     $v0, $t7, BSort
    sb      $v0, 0($s1)
    addi    $s1, 1
    add     $t8, $s1, $zero
    j       ReadNums

BSort:
    add     $t6, $s0, $zero
    addi    $t5, 1
    sub     $s1, $s0, $t1
    beq     $s1, $s0, PrintNums
    add     $s2, $s0, $zero

PrintNums:
    li      $v0, 4
    la      $a0, PrintSort
    syscall

    li      $v0,5
    syscall

Display:
    li      $v0, 1
    lb      $a0, 0($t6)
    syscall

    li      $v0, 4
    la      $a0, GetSpace
    syscall

    addi    $t6, 1
    bne     $t6, $t8, Display
    jal     BSort
