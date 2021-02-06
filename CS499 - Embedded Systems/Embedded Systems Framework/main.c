/*
 *  Module:     Main
 *  File:       main.c
 */

#include "includes.h"

int main(void) {
    /* Connect LED to pin PC0 */
    OUTPUT |= (PORT_PIN << 0);

    /* Initialize timer */
    timer0_init();

    /* Loop forever */
    while (1) {
        /* Check if number of overflows = 12 */
        if (total_overflow >= 12) {
            /* Check if the timer count reaches 53 */
            if (TCNT0 >= 53) {
                TOGGLE ^= (PORT_PIN << 0); /* Toggles the LED */
                TCNT0 = 0; /* rest counter */
                total_overflow = 0; /* Reset overflow counter */
            }
        }
    }
}