//
//  shell_sort.c
//  Sorting Algorithms
//
//

#include <stdio.h>

void shell_sort(int *array, int size) {
    int gap, i, j, k;
    for (gap = size; gap /= 2;) {
        for (i = gap; i < size; i++) {
            k = array[i];
            for (j = i; j>= gap && k < array[j - gap]; j -= gap) {
                array[j] = array[j - gap];
            }
            array[j] = k;
        }
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
    
    shell_sort(array, size);
    
    printf("Sorted Array: ");
    for(i = 0; i < size; i++)
        printf("%d ", array[i]);
    printf("\n");
 
    return 0;
}
