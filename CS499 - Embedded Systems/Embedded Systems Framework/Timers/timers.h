/*
 *  Module:     Timers
 *  File:       timers.h
 */

/* Header guard */
#ifndef TIMERS_H
#define TIMERS_H

/* Function prototypes */
unsigned long clock_get_ticks();
unsigned long clock_diff_ms(long, long);
void timer0_init(void);
ISR(TIMER0_OVF_vect);
int main(void);

#endif
/* TIMERS_H 