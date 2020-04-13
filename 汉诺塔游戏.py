""" 汉诺塔游戏 """

def hanOi(n, x, y, z):
    # 这个函数的意思是 将 n 个盘子 从 x 移动到 z 上
    if n == 1:
        print(x, "->", z)
    else:
        hanOi(n-1, x, z, y)     #将n-1个盘子移动到y上
        print(x, "->", z)
        hanOi(n-1, y, x, z)


temp = input("总盘子数:")
guess = int(temp)
hanOi(guess, 'x', 'y', 'z')
        
        
