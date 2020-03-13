import  copy
#列表,相当于修改了指向的地址
list1=[1,2,3,[8,9]]
list4 = copy.deepcopy(list1)
list2 = list1.copy()#使用两个地址
list3 = list1#使用一个地址
list2[0] = 4
list1[1] = 5
list3[3][1] = 100#会全部改变


print(list1)
print(list2)
print(list3)
print(list4)

#字典
list1={"name":"tom","age":18}
list2 = list1.copy()
list2["name"] = "tom2"
list1["age"] = 20
print(list1,list2)




