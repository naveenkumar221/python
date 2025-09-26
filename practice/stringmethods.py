#string methods 
str="naveenkumarkethyreddy"
print(len(str))  # length of the given string  
print(str.upper())  # write the string in the capital letters
print(str.lower())  # write the stringbin the lower case leters

str2="   hello   world     "
print(str2.strip())     # it remove the white spaces from the both ends right and left
print(str2.lstrip())    # it remove space form the left side only
print(str2.rstrip())    # it removes the space from the right side

#Example
str2="************hello   world***********"
print(str2.strip('*'))     # it remove the white spaces from the both ends right and left
print(str2.lstrip('*'))    # it remove space form the left side only
print(str2.rstrip('*'))    # it removes the space from the right side

str3='i am java programmer'
print(str3.replace('java','python'))    # replacing the all values inthe string

list=['i ','a ','python','trainer']
print(' '.join(list))                # join the different typle of elements into single line


# Dictonary methods

# it store data in the form of key and values

# len(): return the number of keyvalues pairs
# keys(): returns the list of all keys within a dictonary
# values(): returns the list of all values within a dictonary 
# update(): it as update the dictonary value 