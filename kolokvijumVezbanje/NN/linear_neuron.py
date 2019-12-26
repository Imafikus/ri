import numpy as np

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

def update_w(x, y, w):
    u = np.inner(x, w)
    o = sigmoid(u)

    delta_w = (y - o) * o * (1 - o) * x
    return w + delta_w

def main():
    X = np.array([[1, 0], [0, 1], [1, 1], [0, 0]])
    y = np.array([1, 1, 1, 0])
    w = np.array([0.5, 0.5])
    max_iterations = 1000
    n = X.shape[0]

    for i in range(max_iterations):
        k = np.random.randint(n)
        w = update_w(X[k], y[k], w)

    for i in range(n):
        o = sigmoid(np.inner(X[i], w))
        print(y[i], o)
    

if __name__ == "__main__":
    main()