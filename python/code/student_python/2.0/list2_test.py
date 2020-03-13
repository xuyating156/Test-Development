allStudent = []  # 保存所有同学信息
while 1:
        print("*******************")
        print("1.查看所有***************")
        print("2.新增*******************")
        print("3.修改*******************")
        print("4.查看部分*******************")
        print("5.查看姓名*************")

        select = int(input("输入选项"))
        if select ==1:
            for oneStu in allStudent:
                print("name:%s,age:%d"%(oneStu[0],oneStu[1]))
        elif select ==2:
            name =input("输入姓名")
            age = int (input("输入年龄"))
            #定义一个一维列表
            oneStudent=[name,age]
            allStudent.append(oneStudent)
        elif select==3:
            oldName =input("输入旧姓名")
            for oneStu in allStudent:
                if oneStu[0]==oldName:
                    newName = input("输入新姓名")
                    oneStu[0] =newName
                    break
            else  :
                print("查无此人")

        elif select==4:
            print(allStudent[0:3])
        elif select==5:
            for oneStu in allStudent:
                print(oneStu[0])

