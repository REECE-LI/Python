import easygui as eg

msg_0 = '请写下你的联系方式'
title = '信息中心'

fieldNames = ["*用户名", "*真实姓名", "固定电话", "*手机号码", "QQ", "*E-mail"]
dicNames = {"用户名": "", "真实姓名": "", "固定电话": "", "手机号码": "", "QQ": "", "E-mail": ""}
fieldValues = []        ##存放 信息的地方 这是个列表
fieldValues = eg.multenterbox(msg_0, title, fieldNames)

while 1:
    if fieldValues == None:
        break
    errmsg = ""
    for i in range(len(fieldNames)):
        option = fieldNames[i].strip()      ## 消除首位的 空格
        if fieldValues[i].strip() == "" and option[0] =="*":
            errmsg += ('[%s]为必填项。\n\n' % fieldNames[i])
        dicNames[fieldNames[i].strip('*')] = fieldValues[i]
    if errmsg == "":
        break
    fieldValues = eg.multenterbox(errmsg, title, fieldNames, fieldValues)

print("用户资料如下：%s" % str(fieldValues))
print()
print()
print()
print(dicNames)
