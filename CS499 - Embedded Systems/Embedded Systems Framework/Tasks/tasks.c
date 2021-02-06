/*
 *  Module:     Tasks
 *  File:       tasks.c
 */

/* Task basic structure */
typedef struct {
    unsigned long long created;
    unsigned int       interval;
    unsigned char      repeat;
    void               (*task)();
} TASK;

/* Create a task following the outline of the struct */
void create_task(TASK* t, void (*task)(), unsigned int interval, unsigned char repeat) {
    t->created  = clock_get_ticks();
    t->repeated = repeat;
    t->interval = interval;
    t->task     = task;
}