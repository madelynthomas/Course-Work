//
//  quick_sort.c
//  Sorting Algorithms
//
//

#include <stdio.h>

void quick_sort(int *array, long size) {
    int pointer = array[size / 2];
    int *left = array;
    int *right = array + size - 1;
    if (size < 2)
        return;
    while (left <= right) {
        if (*left < pointer) {
            left++;
            continue;
        }
        if (*right > pointer) {
            right--;
            continue;
        }
        int temp = *left;
        *left++ = *right;
        *right-- = temp;
    }
    quick_sort(array, right - array + 1);
    quick_sort(left, array + size - left);
    
}

int main () {
    int i;
    int array[] = {52, 40, -26, 82, 0, 89, 13, 3, 52, 32};
    long size = sizeof(array) / sizeof(array[0]);
    
    printf("Unsorted Array: ");
    for (i = 0; i < size; i++)
        printf("%d ", array[i]);
    printf("\n");
    
    quick_sort(array, size);
    
    printf("Sorted Array: ");
    for(i = 0; i < size; i++)
        printf("%d ", array[i]);
    printf("\n");
    
    return 0;
}
