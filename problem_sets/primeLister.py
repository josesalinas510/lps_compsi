# empty list to add prime numbers
primeNumbers = []


# all values from 1 to 10000
for xNumbers in range(1, 10001):
	prime = True
# divides all numbers from 1 to 10000 with numbers from 2 to all numbers from 1 to 10000
    	for value in range(2,xNumbers):
# if the remainder is 0, then the number is NOT prime since there are more than one factors
        	if (xNumbers % value == 0):
           		prime = False
# if the number is prime, then it is added to an empty list
    	if prime:
		primeNumbers.append(xNumbers)
	


# opens a new file called "primes.txt" and allows the program to write into the file
newFile = open("primes.txt", "w") 
# puts every number inside the list "primeNumbers" into the file with a break after each line
for num in primeNumbers:
	newFile.write(str(num) + "\n")
# closes the file
newFile.close()



