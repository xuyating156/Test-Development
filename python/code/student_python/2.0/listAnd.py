student1={"name":"tom1","age":20}
student2={"name":"tom2","age":22}
student3={"name":"tom3","age":21}

allList = [student1,student2,student3]
for one in allList:
    print("姓名："+one["name"]+",年龄："+str(one["age"])+"\n")

#s删除某个同学
delName ="tom2"
index = 0
for one in allList:
    if one["name"]==delName:
        del allList[index]
    index+=1
print(allList)

#删除某一列
for one in allList:
    one.pop("age")
print(allList)

#新增列表

student4={"name":"tom4","age":25}
allList.append(student4)
print(allList)









