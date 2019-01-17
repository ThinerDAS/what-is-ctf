#include "stdio.h"
#include "string.h"

//[i^ord(j) for i,j in zip(range(64),s+'\0')]
//yellowlite{c8db51ce70e1fe5118e8c9b5709718de_____my_fir57_r3___}
const char base[64] = {
    121, 100, 110, 111, 107, 114, 106, 110, 124, 108, 113, 104, 52, 105, 108, 58, 33, 114, 119, 36, 36, 112, 39, 113, 125, 44, 43, 42, 36, 120, 38, 124, 25, 67, 23, 20, 20, 28, 17, 22, 16, 77, 79, 116, 115, 114, 113, 112, 93, 72, 109, 85, 93, 71, 3, 0, 103, 75, 9, 100, 99, 98, 67, 63
};

int main()
{
    char buf[64];
    puts("Input flag:");
    fgets(buf, 64, stdin);
    for (int i = 0; i < 64; i++) {
        buf[i] ^= i;
    }
    if (!memcmp(buf, base, 64)) {
        puts("Correct");
    } else {
        puts("Wrong");
    }
    return 0;
}
