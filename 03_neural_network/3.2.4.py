import numpy as np
import matplotlib.pylab as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


if __name__ == '__main__':
    x = np.array([-1.0, 1.0, 2.0])
    print(sigmoid(x))

    t = np.array([1.0, 2.0, 3.0])
    print(1.0 + t)
    print(1.0 / t)

    x = np.arange(-5.0, 5.0, 0.1)
    y = sigmoid(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1) # y축 범위 지정
    plt.show()
