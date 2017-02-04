#include <time.h>
#include <stdlib.h>

int decision(float probability) {
    return ((float) rand() / (float) RAND_MAX) < probability;
}

int is_prime(int num) {
    if ((num < 2) || (num == 4) || (num == 6) || (num == 8) || (num == 9)) return 0;
    else return 1;
}

int elapsed_useconds(struct timeval beg, struct timeval end) {
    return (end.tv_sec*1000000 + end.tv_usec - beg.tv_sec*1000000 - beg.tv_usec);
}
