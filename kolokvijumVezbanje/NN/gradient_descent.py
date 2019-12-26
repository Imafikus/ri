import numpy as np


def gradient_descent(f, gradient, x0, alpha, eps, max_iterations):
    """
    x_k+1 = x_k * -alpha*gradient(xk)

    f(x) = 1/2 * (x^2 + 10 * y^2)
    gradoent = (x, 10*y)
    """
    x = x0

    for i in range(max_iterations):
        x_new = x0 - alpha * gradient(x0)
        if(np.abs(f(x) - f(x_new)) < eps):
            break
        
        x = x_new
    
    converged = i != max_iterations
    return x, converged

def f(x):
    return 0.5 * (x[0]**2 + 10 * x[1]**2)

def gradient(x):
    return np.array([x[0], 10 * x[1]])

def find_local_optimum():
    x = np.array([3., 5.])
    alpha = 0.1
    eps = 0.01
    max_iterations = 1000

    print(gradient_descent(f, gradient, x, alpha, eps, max_iterations))


if __name__ == "__main__":
    find_local_optimum()