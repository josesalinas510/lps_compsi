myContacts = { }






# code execution starts here
codeRunning = True


while codeRunning:

	print("(1) Add a phone number")
	print("(2) Print the full list of contacts")
	print("(3) Enter a name to retrieve the contacts's phone number")
	print("(0) Exit the Contact app")
	input = raw_input()

	if input == "1":
		print("What is the contact's name?")
		newContactName = raw_input()
		print("What is their phone number?")
		newContactNumber = raw_input()
		myContacts[newContactName] = newContactNumber
	elif input == "2":
		print(myContacts)
	elif input == "3":
		print("What is the contact name under?")
		Contact = raw_input()
		print(myContacts[Contact])
	elif input == "0":
		codeRunning = False

