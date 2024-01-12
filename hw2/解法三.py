#include <stdio.h>
#include <math.h>
//方法三：使用 pow 函數
int main() {
    int n;
    double result;

    printf("請輸入 n：");
    scanf("%d", &n);

    result = pow(2, n);

    printf("2 的 %d 次方為 %.0f\n", n, result);

    return 0;
}
//參考chatgpt並修改
