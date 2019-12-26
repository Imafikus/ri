import numpy as np 

def adam(x0, f, gradient, beta_1, beta_2, alpha, eps, max_iterations, precision):
    """
    m_k+1 = beta_1 * m_k + (1 - beta_1) * gradient(x_k);  ^m_k+1 = m_k+1 / (1 - beta_1 ^ (k+1))

    v_k+1 = beta_2 * v_k + (1 - beta_2) * (gradient(x_k)) ^2;  ^vk+1 = v_k+1 / (1 - beta_2 ^ (k+1))
    
    x_k+1 = x_k - alpha * ^m_k+1 / sqrt(eps * v_k+1)
    """

    m = 0
    v = 0
    x_old = x0

    for k in range(1, max_iterations+1):
        m = beta_1 * m + (1 - beta_1) * gradient(x_old)
        v = beta_2 * v + (1 - beta_2) * gradient(x_old) * gradient(x_old)

        m_hat = m / (1 - beta_1 ** k)
        v_hat = v / (1 - beta_2 ** k)

        x_new = x_old - alpha * m_hat / (np.sqrt(eps * v_hat) + eps)

        if abs(f(x_new) - f(x_old) < precision):
            break
        
        x_old = x_new

    converged = k != max_iterations
    return x_new, converged

def f(x):
    return 0.5 * (x[0]**2 + 10 * x[1]**2)

def gradient(x):
    return np.array([x[0], 10 * x[1]])

def main():
    alpha = 1
    beta_1 = 0.9
    beta_2 = 0.999
    eps = 1e-8
    precision = 1e-2
    x0 = np.array([3, 5])
    max_iterations = 1000

    print(adam(x0, f, gradient, beta_1, beta_2, alpha, eps, max_iterations, precision))



if __name__ == "__main__":
    main()

