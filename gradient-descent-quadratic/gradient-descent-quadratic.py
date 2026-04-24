def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    x_previous = x0
    for step in range(0, steps):
        grad_f = 2*a*x_previous + b
        x_new = x_previous - lr*grad_f
        x_previous = x_new
    return x_previous