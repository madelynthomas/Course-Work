//
//  selection_sort.c
//  Sorting Algorithms
//
//

#include <stdio.h>

void selection_sort (int *array, int size) {
    int i, j, min_index, temp;
    for (i = 0; i < size; i++) {
        for (j = i; j < size; j++) {
            if (array[j] < array[min_index])
                min_index = j;
        }
        temp = array[i];
        array[i] = array[min_index];
        array[min_index] = temp;
    }
}

int main () {
    int i;
    int array[] = {52, 40, -26, 82, 0, 89, 13, 3, 52, 32};
    int size = sizeof(array) / sizeof(array[0]);
 
    printf("Unsorted Array: ");
    for (i = 0; i < size; i++)
        printf("%d ", array[i]);
    printf("\n");
 
    selection_sort(array, size);
 
    printf("Sorted Array: ");
    for(i = 0; i < size; i++)
        printf("%d ", array[i]);
    printf("\n");
 
    return 0;
}
