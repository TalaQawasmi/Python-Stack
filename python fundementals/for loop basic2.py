1>>
def biggie(li):
    for i in range(len(li)):
        if li[i] < 0:
            li[i] = "big"
    print(li)

biggie([-1, 3, 5, -5])

2>>
def countPositives(li):
    count =0
    for i in range(len(li)):
        if li[i]>0:
            count +=1
    li[len(li)-1]=count
    print(li)
countPositives([-1,1,1,1])

3>>
def sum(li):
    sum = 0
    for i in range(len(li)):
        sum += li[i]
    print(sum)
sum([1,2,3,4])

4>>
def avg(li):
    count=0
    sum =0
    for i in range(len(li)):
        count +=1
        sum += li[i]
    print(sum/count)
avg([1,2,3,4])

5>>
def lengthList(li):
    count=0
    for i in range(len(li),0,-1):
        count +=1
    print(count)
lengthList ([37,2,1,-9])

6>>
def min(li):
    if len(li) == 0:
        print("False")
        return False
    min=li[0]
    for i in range(len(li)):
        if li[i] < min:
            min = li[i]
    print(min)
min([])

7>>
def max(li):
    if len(li) == 0:
        print("False")
        return False
    max=li[0]
    for i in range(len(li)):
        if li[i] > max:
            max = li[i]
    print(max)
min([37,2,1,-9])

8>>
def ultimateAnalysis(li):
    sum = 0
    min =li[0]
    max =li[0]
    count = 0
    for i in range(len(li)):
        sum+=li[i]
        count+=1
        if li[i]< min:
            min = li[i]
        if li[i] > max:
            max = li[i]
    print({"'sumTotal':"sum",","'average':", sum/count,",", "'minimum':",min,",","'maximum':",max})
ultimateAnalysis([37,2,1,-9])

9>>
def reverse(li):
    print(li[::-1])
reverse([37,2,1,-9])



    