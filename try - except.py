
try:
    num = eval(input("\n请输入一个整数："))
    print(num*3)

except NameError:
    print("输入错误，请输入一个整数")

        
try:
    temp = input("请输入一个数：")
except NameError:
    print("类型错误")
else:
    print(temp)
finally:
    print("厉害的呀！")
    
