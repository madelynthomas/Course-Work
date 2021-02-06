/*
 *  Module:     Timers
 *  File:       timers.c
 */

#include "includes.h"

/* Global variable to count the number of overflows */
volatile uint8_t total_overflow;

/* Initialize timer, interrupt and variable */
void timer0_init() {
    /* Set up timer with pre-scalar = 256 */
    TCCR |= (1 << CS02);

    /* Initialize counter */
    TCNT0 = 0;

    /* Enable overflow interrupt */
    TIMSK |= (1 << TOIE0);

    /* Enable glow interrupts */
    sei();

    /* Initialze overflow counter variable */
    total_overflow = 0;
}

/* TIMER0 overflow interrupt service routine
   called whenever TCNT0 overflows */
ISR(TIMER0_OVF_vect) {
    /* Keep a track of the number of overflows */
    total_overflow++;
}
