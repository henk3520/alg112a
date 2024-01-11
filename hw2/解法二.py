#include <stdio.h>
//方法二：使用 for 迴圈計算
int main() {
    int n;
    unsigned long long result = 1;

    printf("請輸入 n：");
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        result *= 2;
    }

    printf("2 的 %d 次方為 %llu\n", n, result);

    return 0;
}
