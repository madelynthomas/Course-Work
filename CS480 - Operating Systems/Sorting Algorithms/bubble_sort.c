//
//  bubble_sort.c
//  Sorting Algorithms
//
//

#include <stdio.h>

void bubble_sort (int *array, int size) {
    int i, temp = 1;
    while (size-- && temp) {
        for (i = temp = 0; i < size; i++) {
            if (array[i] <= array[i + 1])
                continue;
			temp = array[i], array[i] = array[i + 1], array[i + 1] = temp;
            temp = 1;
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
    
	bubble_sort(array, sizeof(array) / sizeof(array[0]));
 
    printf("Sorted Array: ");
    for(i = 0; i < size; i++)
        printf("%d ", array[i]);
    printf("\n");
    return 0;
}

