def newton_solver(initial_guess, max_iterations=100, epsilon=0.0001):
    x = initial_guess

    for i in range(max_iterations):
        equation_value = x**2 - 3*x + 1
        derivative_value = 2*x - 3

        x = x - equation_value / derivative_value

        if abs(equation_value) < epsilon:
            print(f"{x}")
            return
    print("未找到解，達到最大迭代次數")

initial_guess = 0.0
newton_solver(initial_guess)
