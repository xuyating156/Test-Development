
 #定义变量，存储学号，姓名，年龄，身高

if __name__ == "__main__":
    #定义第一个同学
    id1 =100
    name1="tom"
    age1 = 16
    height1 =1.75
    #定义第二个同学
    id2 =101
    name2="tom2"
    age2 = 17
    height2 =1.81
    #定义第三个同学
    id3 =102
    name3="tom3"
    age3 = 16
    height3 =1.72

    #打印
    print("学号：%d,姓名：%s,年龄：%d，身高：%.2f"%(id1,name1,age1,height1))
    print("学号：%d,姓名：%s,年龄：%d，身高：%.2f"%(id2, name2, age2, height2))
    print("学号：%d,姓名：%s,年龄：%d，身高：%.2f"%(id3, name3, age3, height3))

#求年龄平均值
    avg_he = (height2+height1+height3)/3
    print ("平均身高：%.2f"%(avg_he))
    avg_age = (age1+age2+age3)/3
    print("平均年龄：%d"%(avg_age))

#动态输入
    id4= int(input("请输入学号："))
    name4 =input("请输入姓名：")
    age4 = int(input("请输入年龄："))
    height4 = float(input("请输入身高："))
    print("学号：%d,姓名：%s,年龄：%d，身高：%.2f"%(id4, name4, age4, height4))

    for a in range(3,8,2):
        print(a)