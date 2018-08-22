import numpy as np

import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

# y = mx + b

xs = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=np.float64)
ys = np.array([3, 2, 1, 3, 7, 5, 5, 8, 11, 9], dtype=np.float64)

mean_of_x = np.mean(xs)
mean_of_y = np.mean(ys)


def m_and_b(x_array, y_array):
    numerator = 0
    denominator = 0
    for item in range(0, len(x_array)):
        numerator += (x_array[item] - mean_of_x) * (y_array[item] - mean_of_y)
        denominator += (x_array[item] - mean_of_x) ** 2
    m = numerator / denominator
    b = mean_of_y - (m * mean_of_x)
    return m, b


def do_the_math(predict_x):
    m, b = m_and_b(xs, ys)
    '''All this from line 31 to line 34 can be summarized by line 35'''
    regression_ys = []
    for x in xs:
        y = (m * x) + b
        regression_ys.append(y)
        '''regression_line = [(m * x) + b for x in xs]'''

    predict_y = (m * predict_x) + b

    print("Prediction is: " + str(predict_y))

    plt.scatter(xs, ys)
    plt.scatter(predict_x, predict_y, color='g')
    plt.plot(xs, regression_ys)
    plt.show()


if __name__ == '__main__':
    x = float(input('Enter a value of x: '))
    do_the_math(x)
    # TODO check if input is number
