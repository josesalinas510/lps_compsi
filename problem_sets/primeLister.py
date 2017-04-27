primeNumbers = []


# list all of the prime numbers
for xNumbers in range(1, 10001):
	prime = True
    	for value in range(2,xNumbers):
        	if (xNumbers % value == 0):
           		prime = False
    	if prime:
		primeNumbers.append(xNumbers)
	



newFile = open("primes.txt", "w") 
for num in primeNumbers:
	newFile.write(str(num) + "\n")
newFile.close()



