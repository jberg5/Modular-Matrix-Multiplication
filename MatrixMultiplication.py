def multiply(X,Y):
    result = [[sum(a*b for a,b in zip(X_row,Y_col))%26 for Y_col in zip(*Y)] for X_row in X]
    return result

def displayMatrix(X):
    for line in X:
        print(line)


if __name__ == '__main__':
    X_rows = int(input("How many rows in the first matrix? "))
    Y_rows = int(input("How many rows in the second matrix? "))
    X = []
    Y = []
    for i in range(X_rows):
        row = [int(x) for x in input("Give me the space-separated values of row {} in matrix X ".format(i)).split()]
        X.append(row)

    for i in range(Y_rows):
        row = [int(y) for y in input("Give me the space-separated values of row {} in matrix Y ".format(i)).split()]
        Y.append(row)

    print("Great! Matrix X is:")
    displayMatrix(X)
    print("...and Y is:")
    displayMatrix(Y)
    print("...and X*Y mod 26 is:")
    displayMatrix(multiply(X,Y))
