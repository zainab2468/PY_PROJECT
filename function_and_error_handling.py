#x = sum(list)
#y = len(list)


def mean(x,y):
    try:
        result = x // y
        print(result)
    except ZeroDivisionError:
        print("Division by zero")
    else:
        print("The average of numbers in list is", result)
    finally:
        print("done")

mean(24,4)

