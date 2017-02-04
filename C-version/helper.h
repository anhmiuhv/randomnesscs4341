#ifndef HELPER_H
#define HELPER_H
#include <sys/time.h>

int decision(float probability);

int is_prime(int num);

int elapsed_useconds(struct timeval beg, struct timeval end);

#endif
