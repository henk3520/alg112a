#include <stdio.h>
//方法一：直接使用指數運算子
int main() {
    int n;
    unsigned long long result;

    printf("請輸入 n：");
    scanf("%d", &n);

    result = 1ULL << n;

    printf("2 的 %d 次方為 %llu\n", n, result);

    return 0;
}
//參考chatgpt並修改
