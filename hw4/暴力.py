def brute_force_solver():
    epsilon = 0.0001
    lower_bound = -10
    upper_bound = 10

    solutions = []

    for x in range(lower_bound, upper_bound + 1):
        equation_value = x**2 - 3*x + 1
        if abs(equation_value) < epsilon:
            solutions.append(x)

    return solutions

solutions = brute_force_solver()

if solutions:
    print("解為：", solutions)
else:
    print("未找到解")
//參考chatgpt並修改
