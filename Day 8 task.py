import functools

list1=[1,2,3,4]
list2=[]
def fun(list1):
    for i in list1:
        if i%2==0:
            list2.append(i)
list3=filter(fun(list1),list2)
print(list(list3))

#out put   = [2, 4]