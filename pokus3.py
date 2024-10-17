def my_range(start, stop, step):
    result = []
    while start < stop:
        result.append(start)
        start += step
    return result

def my_enumerate(iterable, start = 0):
    result = []
    index = 0
    for value in iterable:
        result.append((index, value))
        index +=1
    return result

def my_enumerate(iterable, start = 0):
    result = []
    i = 0
    while i < len(iterable):
        result.append((i, iterable[1]))
        i += 1
    return result

def my_zip(*iterables):
    result = []
    length = len(iterables[0])
    for i in range(0, length):
        subresult = []
        for j in range(0, len(iterables)):
            subresult.append(iterables[j][i])
        result.append(tuple(subresult))
    return result




if __name__ == "__main__":
    print(list(zip([1, 2, 3], [4, 5 ,6], [7, 8, 9])))
    print(my_zip([1, 2, 3], [4, 5 ,6], [7, 8, 9]))