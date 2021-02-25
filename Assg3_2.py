def AcceptListElement(size):
    arr=[]
    for i in range(size):
        print("Enter Elements")
        no=int(input())
        arr.append(no)
    return arr

def ShowMaxData(arr):
    ans=0
    for i in range(len(arr)):
        #for j in range(len(arr)):
        if arr[i]>ans:
            ans=arr[i]
        #else:
            #ans=arr[j]
    return ans

def main():
    listData=[]
    size=int(input("Enter size of List"))
    listData=AcceptListElement(size)
    print("Entered data is {}".format(listData))
    print("Maximum of all elements is ",ShowMaxData(listData))

if __name__=="__main__":
	main()
