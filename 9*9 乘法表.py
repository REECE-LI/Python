for i in range(1, 10):
    for j in range(1, i+1):
        print(i, "*", j, "==", i*j, end = "\t")         #每次执行print会自动换行 需要加上end = "\t"

    print("\n")


#利用 format 来进行编写 运行速度  更快

for i in range(1, 10):
    for j in range(1, i+1):
        print("{} * {} = {}".format(i, j, i*j), end = "\t")         #每次执行print会自动换行 需要加上end = "\t"

    print("\n")

