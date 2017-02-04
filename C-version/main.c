#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>
#include "state.h"
#include "helper.h"
#include "method.h"

int main(int argc, char* argv[])
{
    if (argc != 4) {
        printf("Usage: exec optimization filename time\n");
        return 1;
    }
    srand(time(NULL));
    FILE *file = fopen(argv[2], "r");
    int num;
    fscanf(file, "%d", &num);
    int array[num];
    for (int i = 0; i < num; i++) {
        fscanf(file, "%d", &array[i]);
    }
    struct State test;
    init_state(&test, num/3, array);
    shuffle(&test);
    struct State result;
    if (strcmp(argv[1], "hill") == 0) {
        result = hillclimbing(test, atoi(argv[3]));
    }
    else if (strcmp(argv[1], "annealing") == 0) {
        result = annealing(test, 12000.0, atoi(argv[3]));
    }

    for (int i = 0; i < num; i++) {
        printf("%d ", result.bins[i]);
    }
    printf("\n");
    printf("%d\n", score(&result));
    fclose(file);
    return 0;
}

        

