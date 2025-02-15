# DividedDifference.py

def DividedDifference(data, i, j):

    if j == 0:
        return data[i][1]
    elif j == 1:
        return data[i][2]
    else:

        return (DividedDifference(data, i + 1, j - 1) - DividedDifference(data, i, j - 1)) / (data[i + j][0] - data[i][0])
