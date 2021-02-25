from ModuleArithematic import *

def Addition(arr):
    ans=0
    for i in range(len(arr)):
        ans=ans+arr[i]
    return ans
def AcceptListElement(size):
    arr=[]
    for i in range(size):
        print("Enter Elements")
        no=int(input())
        arr.append(no)
    return arr

def ListPrime(arr):
    PrimeArr=[]
    for i in range(len(arr)):
        ans=CheckPrime(arr[i])
        if ans==True:
            PrimeArr.append(arr[i])
    print("List of Prime Numbers is ",PrimeArr)
    ans1=Addition(PrimeArr)
    print("Output",ans1)
    

def main():
    listData=[]
    size=int(input("Enter size of List"))
    listData=AcceptListElement(size)
    print("Entered data is {}".format(listData))
    ListPrime(listData)

if __name__=="__main__":
	main()
