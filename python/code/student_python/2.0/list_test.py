
act = ["黄轩","大牛","冯小刚"]
Move =["访华","冯小刚",act,30]

#遍历所有的数据
for one in Move:
    print(one,end=",")#默认end="\n"

#插入信息
Move.insert(2,"出品人")
#修改数据
Move[4]=35
#最后新增
Move.append(9.0)
#获取前三项
print(Move[0:3])
#获取后三项
print(Move[-3:])

