user_play = "y"

while user_play == "y":
    user_number = int(input("Enter a number"))

    #added in the 1 and +1 to account for range (which goes from 0 up until the user number)
    for x in range(1, user_number + 1):
        print (x)
    
    #print question to continue or kill the loop
    user_play = input("continue: (y)es or (n)no?")


name = "Jessica"
country = "USA"
age = 32
hourly_wage = 50
satisfied = True
daily_wage = hourly_wage * 8

print("The new employee is " + name + " and she is " + str(age)+ ". Her daily wage is " + str(daily_wage) + ".")

print(f"Satisfied: {satisfied}")

# range is the bottom number upto the last number in parenthesis. In this case, bottom number is 1 and goes up to 4, not 5
# this will print 1, 2, 3, 4 (up to 5, not including 5)
for x in range(5):
    print(x)

print("---------------------")    

for x in range(2,7):
    print (x)

print("---------------------")   

word = "coding"
for letter in word:
    print(letter)

print("---------------------")   

heroes = ["Dolly Parton", "Nick Offerman", "Frida Kahlo"]
for hero in heroes:
    print(hero)

#create a variable list and set is as a list
my_list = ["Jacob", 25, "Ahmed", 80]
print(my_list)

#append an element to the list (.append is a method of my_list)
my_list.append("Matt")
print(my_list)

#return the index of the first object with the matching value (.index is a method of my_list)
print(my_list.index("Matt"))

#change a specified element (could be any element) at the given index (in this case, we are changing the 3rd index)
# = is assignment in this case
my_list[3] = 85
print(my_list)

# return the length of the list
print(f"There are {len(my_list)} objects in the list" )

# remove an object from the list
my_list.remove("Matt")
print(my_list)

# .pop method removes an object at the index specified

my_list.pop(0)
print(my_list)

# creates a tuple. A tuple is a sequence of immutable python objects that cannot be changed

my_tuple = ("Python", 100, "VBA", False)
print(my_tuple)