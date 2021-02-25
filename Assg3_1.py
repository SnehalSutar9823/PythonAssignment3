def AcceptListElement(size):
    arr=[]
    for i in range(size):
        print("Enter Elements")
        no=int(input())
        arr.append(no)
    return arr

def AddData(arr):
    ans=0
    for i in range(len(arr)):
        ans=ans+arr[i]
    return ans

def main():
    listData=[]
    size=int(input("Enter size of List"))
    listData=AcceptListElement(size)
    print("Entered data is {}".format(listData))
    print("Addition of all elements of list is ",AddData(listData))

if __name__=="__main__":
	main()
