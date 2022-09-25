#time complexity -O(N^2)
#Space complexity-O(N^2)

def sameBsts(arrayOne, arrayTwo):
    # Write your code here.
    if len(arrayOne)!= len(arrayTwo):
        return False

    if len(arrayOne)==0 and len(arrayTwo)==0:
        return True

    if arrayOne[0]!=arrayTwo[0]:
        return False

   

    leftone=getsmaller(arrayOne)
    lefttwo=getsmaller(arrayTwo)
    rightone=getbigger(arrayOne)
    righttwo=getbigger(arrayTwo)

    return sameBsts(leftone,lefttwo) and sameBsts(rightone,righttwo)


def getsmaller(array):
    smaller=[]
    for i in range(1,len(array)):
        if array[i]<array[0]:
            smaller.append(array[i])
    return smaller


def getbigger(array):
    bigger=[]
    for i in range(1,len(array)):
        if array[i]>=array[0]:
            bigger.append(array[i])
    return bigger