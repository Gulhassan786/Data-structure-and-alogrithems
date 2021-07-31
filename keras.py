# from keras.datasets import mnist
# (train_data, train_labels), (test_data, test_labels) = mnist.load_data()


def Name(s):
    """
    :type s: str
    :rtype: int
    """
    temp = ""
    a = 0
    for i in s:
        if i not in temp:
            temp += i
        else:
            temp = temp[temp.index(i)+1]+i
        a = max(a, len(temp))
    return a


Name("glgfeg")
