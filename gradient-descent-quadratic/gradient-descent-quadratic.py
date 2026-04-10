def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # f(x) = ax^2 + bx + c
    x = float(x0)
    for _ in range(int(steps)):
        der = 2*a*x + b
        x = x - lr*der
    return x
    
    pass