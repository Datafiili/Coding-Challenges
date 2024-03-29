## ----- 10001st prime ----- ##
#Written By: Aarni Junkkala

#Problem
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10001st prime number?

#My thoughts:
#This problem is kinda weird one to me as in the problem 3 I used primes. Could it be that problem 3 could have been solved without primes?
#This problem is mostly testing old primes to new primes.

#Collects primes into a list and returns the prime of that index
primes = [2,3,5] #2,3,5 as base so rest of the numbers end with digit of 1,3,7 or 9
def CalculatePrimesIndex(i): #i = index
    global primes
   
    #If prime of the index isn't found, looks for it.
    if i > len(primes) - 1:
        num = primes[-1] + 1 #Starts from the one above last known prime
        
        while True:
            if str(num)[-1] in ["1","3","7","9"]: #Reduces amount of prosessing
                #Try to divide with every primenumber
                isPrime = True
                for k in range(len(primes)):
                    #if answer is integer, then number isn't a prime
                    if (num / primes[k]).is_integer() == True:
                        isPrime = False
                        break
                if isPrime == True:
                    primes.append(num)
                    #If enough primes have been calculated,
                    #then will break and return the correct prime
                    if i <= len(primes) - 1:
                        break
                num += 1
    return primes[i]

#Used for matematical usage, where prime1 = fisrt, where as in coding 0 is first.
def GetPrime(n):
    global primes
    if n - 1 > len(primes) - 1:
        CalculatePrimesIndex(n)
    return primes[n - 1]
    
print(GetPrime(10001))