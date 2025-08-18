#2
def move_zeros_to_end(lst):
    res = []
    zeros = []

    for i in lst:
        if i != 0:
            res.append(i)
        else:
            zeros.append(i)

    return res + zeros

print(move_zeros_to_end([1, 0, 2,  0, 0, 7, 2, 0]))



#3

        