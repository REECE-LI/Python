def people(name, *p):
    print(name)
    for i in p:
        print("可变参数部分:", i)

people('lmj', '21岁', '男')




###########################################

data = {'SEX': 'man', 'AGE': '21', 'HEIGHT': '175'}

def detail(name, number, **p):
    print('姓名:', name, "学号:", number, end = "")
    for i, j in p.items():
        print(i, j, end = '')
        

detail('李明骏', 201811030026, **data)


#############################################


def test(a, b, c = 1, *p, **k):
    print(
        'a = ', a,
        'b = ', b,
        'c = ', c,
        'p = ', p,
        'k = ', k
        )
