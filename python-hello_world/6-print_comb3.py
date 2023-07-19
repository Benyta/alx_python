for i in range(9):
    for j in range(i+1, 10):
        print("{:02d}, ".format(i) + "{:02d}".format(j), end='')
print()
