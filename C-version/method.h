#ifndef METHOD_H
#define METHOD_H
#include "state.h"

struct State hillclimbing(struct State state, int usecs);

struct State annealing(struct State state, double maxtemp, int usecs);

#endif
