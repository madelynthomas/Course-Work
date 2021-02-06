//
//  insertion_sort.c
//  Sorting Algorithms
//
//

#include <stdio.h>

void insertion_sort(int *array, int size) {
    int i, j, value;
    for (i = 0; i < size; i++) {
        value = array[i];
        for (j = i; j > 0 && value < array[j - 1]; j--) {
            array[j] = array[j - 1];
        }
        array[j] = value;
        
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
 
    insertion_sort(array, size);
 
    printf("Sorted Array: ");
    for(i = 0; i < size; i++)
        printf("%d ", array[i]);
    printf("\n");
 
    return 0;
}
