def AcceptListElement(size):
    arr=[]
    for i in range(size):
        print("Enter Elements")
        no=int(input())
        arr.append(no)
    return arr

def CheckFrequency(arr,search):
    ans=0
    for i in range(len(arr)):
        #for j in range(len(arr)):
        if arr[i]==search:
            ans=ans=ans+1
        #else:
            #ans=arr[j]
    return ans

def main():
    listData=[]
    size=int(input("Enter size of List"))
    listData=AcceptListElement(size)
    print("Entered data is {}".format(listData))
    search=int(input("Enter integer to be searched:"))
    print(CheckFrequency(listData,search))

if __name__=="__main__":
	main()
