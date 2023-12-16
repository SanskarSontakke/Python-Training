# import math
# print(math.floor(26.11))
# print(math.cos(26.11))

# #---------------------------------------------------------------------------------------------------------------------


# a = 1              ##integer variable
# b = 2              ##integer variable
# c = "Sanskar"      ##string variable
# d = 3.4            ##floating variable
# print(a+b)
# print(c)
# print(d)

# print(type(a))     ##tells variable type
# print(type(b))     ##tells variable type
# print(type(c))     ##tells variable type
# print(type(d))     ##tells variable type

# #---------------------------------------------------------------------------------------------------------------------

# str1 = "sanskar"                     ##string
# str2 = "my name is sanskar sontakke" ##string
# print(str1)
# print(str1.capitalize())             ##capitalizes first letter
# print(str2.capitalize())             ##capitalizes first letter

# print(str1.find("sanskar"))          ##finds any substring
# print(str2.find("sanskar"))          ##finds any substring

# print(str1.upper())                  ##converts string to upper case
# print(str1.lower())                  ##converts string to lower case
# print(str2.upper())                  ##converts string to upper case
# print(str2.lower())                  ##converts string to lower case


# #---------------------------------------------------------------------------------------------------------------------


# items = [1,"Sanskar",3]                ##stores many values & called as list
# items[0] = "Sayli"                     ##changes value of a list
# print(items)                
# print(type(items))                     ##tells type



# #---------------------------------------------------------------------------------------------------------------------


# tup1 = (1,2,3)              ##works like a list and called as tuple
# #tup1[2] = 4                ##changes value but value of tuple cannot be changed so it shows error
# print(tup1)                 
# print(type(tup1))           ##tells type


#---------------------------------------------------------------------------------------------------------------------

dict1 = {}                      ##creates a dictonary
print(type(dict1))              ##tells type

dict1["Sanskar"] = 100     ##adds a value to the dictonary 
dict1["Sayli"] = 10        ##adds a value to the dictonary
dict1["Swapnali"] = 50     ##adds a value to the dictonary

print(dict1.get("Sanskar"))     ##tells value of a variable
print(dict1.get("Sayli"))       ##tells value of a variable
print(dict1.get("Swapnali"))    ##tells value of a variable

print(dict1.items())            ##prints variables with values
print(dict1.keys())             ##prints only variables




