1>>
def countDown(num):
    li=[]
    for i in range(num,0,-1):
        li.append(i)
    print(li)
countDown(5)

2>>
def PrintReturn(li):
    if len(li) is 2:
        print("first value :", li[0])
        return li[1]
PrintReturn([2,4])

3>>
def firstPlusLength(li):
    print(li[0]+len(li))
firstPlusLength([1,4,6,3])

4>>
def values(li):
    newli=[]
    if len(li) < 2:
        return False
    print(li[2])
    for i in range(len(li)):
        if li[i]>=li[2]:
            newli.append(li[i])
    return newli
print (values([5,2,3,2,1,4]))

5>>
def valuesLength(size,value):
    li=[]
    for i in range (size):
        li.append(value)
    return li

print(valuesLength(4,4))

