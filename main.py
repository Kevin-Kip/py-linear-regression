from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

# y = mx + b

xs = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=np.float64)
ys = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=np.float64)


def m_and_b(x_array, y_array):
    m = ((mean(x_array) * mean(y_array)) - mean(x_array * y_array)) / (mean(x_array) * mean(x_array))
    b = mean(y_array) - (m * mean(x_array))
    return m, b


def do_the_math(predict_x):
    m, b = m_and_b(xs, ys)
    regression_line = [(m * x) + b for x in xs]

    predict_y = (m * predict_x) + b

    print("Prediction is: "+str(predict_y))

    plt.scatter(xs, ys)
    plt.scatter(predict_x, predict_y, color='g')
    plt.plot(xs, regression_line)
    plt.show()

if __name__ == '__main__':
    x = input('Enter a value of x: ')
    do_the_math(x)
    # TODO check if input is number