#include "state.h"
#include "helper.h"
#include <time.h>
#include <stdlib.h>
#include <string.h>

// fill an empty state's bins and dictionary
void init_state(struct State *state, int binsize, int *list) {
    state->binsize = binsize;
    state->bins = calloc(binsize * 3, sizeof(int));
    for (int i = 0; i < binsize*3; i++) {
        state->bins[i] = list[i];
        state->dic[list[i]+9]++;
    }
    // memcpy(state->bins, list, binsize * 3 * sizeof(int));
}

// remove an empty state's bins
void delete_state(struct State *state) {
    free(state->bins);
}

// shuffles a state in place
// shuffle algorithm from stack overflow
void shuffle(struct State *state) {
    int n = state->binsize * 3;
    for (int i = 0; i < n - 1; i++) {
        int j = i + rand() / (RAND_MAX / (n - i) + 1);
        int t = state->bins[j];
        state->bins[j] = state->bins[i];
        state->bins[i] = t;
    }
}

int score(struct State *state) {
    int score1 = 0;
    int score2 = 0;
    int score3 = 0;
    int sign = 1;
    for (int i = 0; i < state->binsize; i++) {
        score1 += sign*state->bins[i];
        sign *= -1;
    }
    for (int i = state->binsize; i < state->binsize*2 - 1; i++) {
        if (state->bins[i] < state->bins[i+1]) {
            score2 += 3;
        }
        else if (state->bins[i] == state->bins[i+1]) {
            score2 += 5;
        }
        else {
            score2 -= 10;
        }
    }
    for (int i = state->binsize*2; i < state->binsize*2 + state->binsize / 2; i++) {
        if (state->bins[i] < 0) {
            score3 -= 2;
        }
        else if (is_prime(state->bins[i])) {
            score3 += 4;
        }
        else {
            score3 -= state->bins[i];
        }
    }
    for (int i = state->binsize*2 + 1 + (state->binsize-1)/2; i < state->binsize*3; i++) {
        if (state->bins[i] < 0) {
            score3 += 2;
        }
        else if (is_prime(state->bins[i])) {
            score3 -= 4;
        }
        else {
            score3 += state->bins[i];
        }
    }
    state->score = score1+score2+score3;
    return score1 + score2 + score3;

}

// fill new_state with state, optional random swap
void new_state(struct State *new_state, struct State *state, int swap) {
    int *new_list = calloc(state->binsize*3, sizeof(int));
    memcpy(new_list, state->bins, state->binsize*3 * sizeof(int));
    if (swap) {
        int i, j;
        do {
            i = rand() % (state->binsize*3);
            j = rand() % (state->binsize*3);
        } while (i == j);
        int temp = new_list[i];
        new_list[i] = new_list[j];
        new_list[j] = temp;
    }
    init_state(new_state, state->binsize, new_list);
    free(new_list);
}

