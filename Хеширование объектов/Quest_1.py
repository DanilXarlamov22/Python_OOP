def hash_function(obj):
    obj = str(obj)
    temp1 = 0
    temp2 = 0
    for i in range(len(obj) // 2):
        temp1 += ord(obj[i]) * ord(obj[- i - 1])

    if len(obj) % 2 != 0:
        temp1 += ord(obj[len(obj) // 2])

    for i in range(len(obj)):
        if i % 2 == 0:
            temp2 += ord(obj[i]) * (i + 1)
        else:
            temp2 -= ord(obj[i]) * (i + 1)

    return (temp1 * temp2) % 123456791


print(hash_function('python'))
