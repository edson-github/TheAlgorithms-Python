import numpy as np

""" Here I implemented the scoring functions.
    MAE, MSE, RMSE, RMSLE are included.

    Those are used for calculating differences between
    predicted values and actual values.

    Metrics are slightly differentiated. Sometimes squared, rooted,
    even log is used.

    Using log and roots can be perceived as tools for penalizing big
    erors. However, using appropriate metrics depends on the situations,
    and types of data
"""

#Mean Absolute Error
def mae(predict, actual):
    predict = np.array(predict)
    actual = np.array(actual)

    difference = abs(predict - actual)
    return difference.mean()

#Mean Squared Error
def mse(predict, actual):
    predict = np.array(predict)
    actual = np.array(actual)

    difference = predict - actual
    square_diff = np.square(difference)

    return square_diff.mean()

#Root Mean Squared Error
def rmse(predict, actual):
    predict = np.array(predict)
    actual = np.array(actual)

    difference = predict - actual
    square_diff = np.square(difference)
    mean_square_diff = square_diff.mean()
    return np.sqrt(mean_square_diff)

#Root Mean Square Logarithmic Error
def rmsle(predict, actual):
    predict = np.array(predict)
    actual = np.array(actual)

    log_predict = np.log(predict+1)
    log_actual = np.log(actual+1)

    difference = log_predict - log_actual
    square_diff = np.square(difference)
    mean_square_diff = square_diff.mean()

    return np.sqrt(mean_square_diff)

#Mean Bias Deviation
def mbd(predict, actual):
    predict = np.array(predict)
    actual = np.array(actual)

    difference = predict - actual
    numerator = np.sum(difference) / len(predict)
    denumerator =  np.sum(actual) / len(predict)
    print(numerator)
    print(denumerator)

    return float(numerator) / denumerator * 100
