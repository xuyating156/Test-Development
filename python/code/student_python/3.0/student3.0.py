
if __name__ == "__main__":
# 1.以列表的形式存储三位同学的信息，并打印
    student1 = [100,"tom",16,1.65,85,72]
    student2 = [102, "tom2", 17, 1.68]
    student3 = [103, "tom3", 18, 1.66]
    print("1学号：%d,姓名：%s,年龄：%d，身高：%.2f，成绩：%d，成绩：%d"%(student1[0], student1[1], student1[2], student1[3], student1[4], student1[5]))
    print("1学号：%d,姓名：%s,年龄：%d，身高：%.2f，" % (student2[0], student2[1], student2[2], student2[3]))
    print("1学号：%d,姓名：%s,年龄：%d，身高：%.2f，" % (student3[0], student3[1], student3[2], student3[3]))


# 2.对同学“tom”进行增删改查操作
    student1.insert(3,"nan")#新增
    student2.insert(3, "nu")
    student3.insert(3, "nan")
    del student1[-1]#删除
    student1.pop()#删除
    student1[2]=17#修改
    print(student1)

#3.将所有同学信息存储与列表中,并打印所有学生信息
    allStudent = [student1,student2,student3]
    for one in allStudent:
        print("2学号：%d,姓名：%s,年龄：%d，性别：%s,身高：%.2f，"%(one[0], one[1], one[2], one[3], one[4]))

#4.新增一个同学到学生列表中
    # id= int(input("请输入学号："))
    # name =input("请输入姓名：")
    # age= int(input("请输入年龄："))
    # sex = input("请输入性别：")
    # height = float(input("请输入身高："))
    # allStudent.append([id,name,age,sex,height])
    # print(allStudent)

#5.修改学生列表中的数据
#修改身高
    allStudent[2][4] = 1.80
#修改学号为102 的年龄
    for one in allStudent:
        if one[0]==102:
            one[2]= 20
            print("3学号：%d,姓名：%s,年龄：%d，性别：%s,身高：%.2f，" % (one[0], one[1], one[2], one[3], one[4]))

#6.从学生列表中删除某个同学信息
    #删除第一个同学
    #del allStudent[0]
    #allStudent.pop(0)

#7.根据条件查找所有符合条件的同学信息
    #查找所有男生
    for one in allStudent:
        if one[3]=="nan":
            print("4学号：%d,姓名：%s,年龄：%d，性别：%s,身高：%.2f，" % (one[0], one[1], one[2], one[3], one[4]))
    #查找年龄大于18
    for one in allStudent:
        if one[2]>18:
            print("5学号：%d,姓名：%s,年龄：%d，性别：%s,身高：%.2f，" % (one[0], one[1], one[2], one[3], one[4]))

#8.改用字典保存一个同学的信息，将所有同学的信息保存于列表中,并打印
    allStudent2 = []
    while True:
        id= int(input("请输入学号(00:退出)："))
        if id == 00:
            break
        name =input("请输入姓名：")
        age = int(input("请输入年龄："))
        sex = input("请输入性别：")
        height = float(input("请输入身高："))
        oneStudentDict ={"id":id,
                         "name":name,
                         "age":age,
                         "sex":sex,
                         "height":height
                         }
        allStudent2.append(oneStudentDict)
        for one in allStudent2:
            print("6学号：%d,姓名：%s,年龄：%d，性别：%s,身高：%.2f，" % (one["id"], one["name"], one["age"], one["sex"], one["height"]))

