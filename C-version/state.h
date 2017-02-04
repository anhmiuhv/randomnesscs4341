#ifndef STATE_H
#define STATE_H

struct State {
    int binsize;
    int score;
    int *bins;
    int *dic;
};

void init_state(struct State *state, int binsize, int *list);

void delete_state(struct State *state);

void shuffle(struct State *state);

int score(struct State *state);

void new_state(struct State *new_state, struct State *state, int swap);
#endif
