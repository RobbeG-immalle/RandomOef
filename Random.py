import MyModule
print("Hello")
print("my name is {0}".format("Jeff"))

a = [1,2,5,12]
print("The list of numbers I made contains {0}".format(a))
a.append(35)
print(a);
b = [3,4,6,8]
c = a+b
print(c)

for i in range(12):
    print(i)

d = 5
if d > 4:
    print("Nice, d is {0} ".format(d))
else:
    print("Not so nice, d is {0}".format(d))

invoer = input("Do you like potatoes? ")
if "No" in invoer:
    print("die")
elif "Yes" in invoer:
    print("Good boi")
else:
    print("I said Yes or No")



