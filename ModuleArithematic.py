def Add(no1,no2):
    return no1+no2

def Sub(no1,no2):
    return no1-no2

def Mul(no1,no2):
    return no1*no2

def Div(no1,no2):
    return no1/no2

def CheckPrime(no):
    counter=0
    #print(counter)
    if no > 1:
        for i in range(2,no):
            #print("i {}",format(i))
            if (no % i) == 0:
                counter=counter+i
                #print("Counter {}",format(counter))
                
    if counter==0:
            return True    

