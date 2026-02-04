studentMajor = input("What is your major?")
majorLength = len(studentMajor)
print("The length of " + studentMajor + ' is ' + str(majorLength) + " characters.")

lastIndex = majorLength - 1
print("The last character of your major is " + studentMajor[lastIndex] + ".")

phoneNumber = input("Please enter phone number in format xxx-xxx-xxxx: ")
areaCode = phoneNumber[0:3]
print("Area code for your phone number is: " + str(areaCode))
