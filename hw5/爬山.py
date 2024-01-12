import random

def hillClimbing(f, p, h=0.01):
    failCount = 0
    while (failCount < 10000):
        fnow = f(*p)  # fnow 是目前的高度
        p1, f1 = neighbor(f, p, h)
        if f1 >= fnow:
            fnow = f1
            p = p1
            print('p=', p, 'f(p)=', fnow)
            failCount = 0
        else:
            failCount = failCount + 1
    return (p, fnow)

def f(x, y, z):
    return -1*(x**2 + y**2 + z**2)

def neighbor(f, p, h):
    # 生成鄰居點
    p1 = [p[i] + random.uniform(-h, h) for i in range(len(p))]
    # 計算目標函數值
    f1 = f(*p1)
    return p1, f1

# 初始點
initial_point = [2, 1, 3]
# 執行爬山演算法
result = hillClimbing(f, initial_point)
print("最大值所在位置:", result[0], "最大值:", result[1])
//參考chatgpt並修改
