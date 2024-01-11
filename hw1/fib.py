#include <stdio.h>

int main() {
    int n, i;
    unsigned long long first = 0, second = 1, next;

    printf("輸入項：");
    scanf("%d", &n);

    printf("fibonacci列前 %d 項：\n", n);

    for (i = 0; i < n; i++) {
        if (i <= 1) {
            next = i;
        } else {
            next = first + second;
            first = second;
            second = next;
        }
        printf("%llu ", next);
    }

    return 0;
}
