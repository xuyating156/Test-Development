total = 0
def isLeap(year):
    if( year%4==0 and year%100!=0) or (year%4==0 and year%400==0):
        #print ("%d年是闰年"%year)
        return 1
    else:
        #print("%d年不是闰年"%year)
        return 0

def printInfo(name,age=30):
    print("你好%s,年龄是：%d"%(name,age))

def getMoney(month,*money):
    all = 0
    global total
    for one in money:
        all+=one
    total+=all
    print("%d月收支共计%d远,全部%d元"%(month,all,total))

# def getConsume()

if __name__ == "__main__":

    yearl = int(input("请输入年份："))
    re = isLeap(yearl)
    if re==1:
        print ("%d年是闰年"%yearl)
    else :
        print ("%d不年是闰年"%yearl)

    printInfo("tom",26)
    printInfo("tom1")

    m1=10.2
    m2=20
    m3=65
    getMoney(1,m1)
    getMoney(2,m1,m2)
    getMoney(3,m2,m3,m1)






