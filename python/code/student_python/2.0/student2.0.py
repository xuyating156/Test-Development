
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

# 1.计算三名同学身高的最大值、最小值
    max = 0
    min =0
    if height1>height2 and height1>height3:
        max = height1
    elif height2>height1 and height2>height3:
        max = height2
    else :
        max =height3
    print("身高最高为：%.2f"%(max))
    if height1<height2 and height1<height3:
        min = height1
    elif height2<height1 and height2<height3:
        min = height2
    else :
        min =height3
    print("身高最底为：%.2f"%min)


# 2.动态输入N名学生的信息，并打印
#     for i in range(4):#输入0，1，2，3
#         id4= int(input("请输入学号："))
#         name4 =input("请输入姓名：")
#         age4 = int(input("请输入年龄："))
#         height4 = float(input("请输入身高："))
#         print("学号：%d,姓名：%s,年龄：%d，身高：%.2f"%(id4, name4, age4, height4))

    # while True:
    #     id4= int(input("请输入学号(0:退出)："))
    #     if id4 == 0:
    #         break
    #     name4 =input("请输入姓名：")
    #     age4 = int(input("请输入年龄："))
    #     height4 = float(input("请输入身高："))
    #     print("学号：%d,姓名：%s,年龄：%d，身高：%.2f"%(id4, name4, age4, height4))


# 3.已知班级有50个学生，学号从100依次增加，即100~149，现要求:
# 学号能被5整除的周一打扫卫生
# 能被4整除的周二打扫（不包括周一打扫的）
# 第一个能被5整除且能被3整除的学生为劳动委员
# 请分别打印出周一打扫、周二打扫、劳动委员的学生学号

    MyId = 100
    while MyId<=149:
        if MyId%5==0:
            print("周一打扫：",MyId)
            print("周1打扫：%d"%(MyId))
        MyId+=1

    MyId1=100
    while MyId1<=149:
        if MyId1%4 ==0 and MyId1%5!=0:
            print("周二打扫：",MyId1)
        MyId1+=1

    MyId2=100
    while MyId2<=149:
        if MyId2%3 ==0 and MyId2%5==0:
            print("劳动委员：",MyId2)
            break
        MyId2 += 1

    for i in range(100,150):
        if MyId2 % 3 == 0 and MyId2 % 5 == 0:
            print("劳动委员2：", MyId2)
            break
