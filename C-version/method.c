#include "state.h"
#include "helper.h"
#include <sys/time.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct State hillclimbing(struct State state, int usecs) {
    struct State current_state;
    new_state(&current_state, &state, 0);
    struct State next_state;

    // variable sized array implementation
    // (because i'm too far gone to use std::vector)
    int max_size = 10000;
    struct State *potential_solution = calloc(max_size, sizeof(struct State));
    int solutions = 0;
    potential_solution[0] = current_state;
    solutions++;

    int count = 0;
    struct timeval beg;
    struct timeval end;
    gettimeofday(&beg, 0);
    do {
        current_state = potential_solution[solutions-1];
        new_state(&next_state, &current_state, 1);
        if (score(&next_state) > score(&current_state)) {
            delete_state(&current_state);
            current_state = next_state;
            count = 0;
        }
        else {
            delete_state(&next_state);
            count++;
        }
        potential_solution[solutions-1] = current_state;
        if (count == 100) {
            count = 0;
            solutions++;
            new_state(&current_state, &state, 0);
            shuffle(&current_state);
            potential_solution[solutions-1] = current_state;
        }
        // expand potential solution
        if (solutions == max_size - 10) {
            max_size += 10000;
            potential_solution = realloc(potential_solution, sizeof(struct State) * max_size);
        }
        gettimeofday(&end, 0);
    } while (elapsed_useconds(beg, end) < usecs);
    for (int i = 0; i < solutions; i++) {
        if (score(&current_state) < score(&potential_solution[i]))
            current_state = potential_solution[i];
    }
    free(potential_solution);
    return current_state;
}

struct State annealing(struct State state, double maxtemp, int usecs) {
    struct State current_state;
    new_state(&current_state, &state, 0);
    struct State next_state;

    // variable sized array implementation
    // (because i'm too far gone to use std::vector)
    int max_size = 10000;
    struct State *potential_solution = calloc(max_size, sizeof(struct State));
    int solutions = 0;
    potential_solution[0] = current_state;
    solutions++;

    int count = 0;
    double counttemp = 0;
    double temperature;
    struct timeval beg;
    struct timeval end;
    gettimeofday(&beg, 0);
    do {
        current_state = potential_solution[solutions-1];
        new_state(&next_state, &current_state, 1);
        double delta = score(&next_state) > score(&current_state);
        if (delta > 0) {
            delete_state(&current_state);
            current_state = next_state;
            count = 0;
        }
        else {
            temperature = (double) maxtemp - counttemp;
            if (temperature < 0) {
                temperature = 0.1;
            }
            double probabilitytaken = exp(delta/temperature);
            if (decision(probabilitytaken)) {
                delete_state(&current_state);
                current_state = next_state;
                counttemp += 1;
            }
            else delete_state(&next_state);
            count++;
        }
        potential_solution[solutions-1] = current_state;
        if (count == 100) {
            count = 0;
            solutions++;
            new_state(&current_state, &state, 0);
            shuffle(&current_state);
            potential_solution[solutions-1] = current_state;
        }
        // expand potential solution
        if (solutions == max_size - 10) {
            max_size += 10000;
            potential_solution = realloc(potential_solution, sizeof(struct State) * max_size);
        }
        gettimeofday(&end, 0);
    } while (elapsed_useconds(beg, end) < usecs);
    for (int i = 0; i < solutions; i++) {
        if (score(&current_state) < score(&potential_solution[i]))
            current_state = potential_solution[i];
    }
    free(potential_solution);
    return current_state;
}
