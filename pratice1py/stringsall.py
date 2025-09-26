## ✅ Easy (40 Questions)

## 1. Create a string with your name and print it.

# stg="Naveen"
# stg1=input("enter the string:")
# print(stg)
# print(stg1)

## 2. Get the first character from the string.

# stg="naveen"
# print(stg[0])

# stg1=input("enter the string:")
# print(stg1[0])

## 3. Get the last character from the string.

# stg="Naveen"
# print(stg[-1])

# stg1=input("enter the string")
# print(stg1[-1])


## 4. Concatenate two strings.

# stg1=input("enter the first string:")
# stg2=input("enter the second string:")
# con=stg1 + stg2
# print(con)

## 5. Repeat a string 3 times.

# stg1=input("enter the string:")
# print(stg1*3)

## 6. Slice the first 5 characters.

# stg1=input("enter the string:")
# print(stg1[0:5])

## 7. Reverse a string using slicing.

# stg1=input("enter the string: ")
# print(stg1[::-1])

## 8. Check if a substring exists in a string.

# stg1=input("Enter the string: ")
# sub=input("enter the sub string: ")

# if sub in stg1:
#     print(sub,"yes it is there")
# else:
#     print("no sub string")


## 9. Find the length of a string.

# stg1=input("enter the string: ")
# print(len(stg1))

## 10. Convert string to uppercase.

# stg1=input("enter the string: ")
# print(stg1.upper())


## 11. Convert string to lowercase.

# stg1=input("enter the string: ")
# print(stg1.lower())

## 12. Capitalize the first letter.

# stg1=input("enter the string: ")
# print(stg1.capitalize())

## 13. Convert a string to title case.

# stg1=input("enter the string: ")
# print(stg1.title())

## 14. Remove leading spaces using lstrip().

# stg1="    hello  *  "
# print(stg1.lstrip())

## 15. Remove trailing spaces using rstrip().

# stg1=" *   hello    "
# print(stg1.rstrip())

## 16. Remove both ends' spaces using strip().

# stg1="   *    hello    *    "
# print(stg1.strip())

## 17. Replace all spaces with underscores.

# stg1="hello world good moring"
# print(stg1.replace(" ","_"))

## 18. Count how many times a character appears.

# stg1="heloooooloolo"
# ch="o"
# count=stg1.count(ch)
# print(count)

## 19. Find index of a character using find().

# stg1="goodmoringapple"
# print(stg1.find('a'))

## 20. Use rfind() to find last occurrence.

# stg1="goodmoringapple"
# print(stg1.rfind('p'))

## 21. Use index() to find substring position.

# stg1="naveenkumar"
# print(stg1.index('k'))

## 22. Split a string by spaces.

# stg1='naveen kumar sai'
# print(stg1.split(' '))

## 23. Join a list of words into a string.

# words=['naveen','kumar','sai']
# print(' '.join(words)))

## 24. Check if string starts with "Hello".

# stg1="hello world"
# print(stg1.startswith("hello"))

## 25. Check if string ends with "world".

# stg1="hello world"
# print(stg1.endswith("world"))

## 26. Check if a string is digit.

# stg1="1234567"
# stg2="naveen"
# stg3="naveen123"
# stg4="2345.95"
# print(stg1.isdigit())
# print(stg2.isdigit())
# print(stg3.isdigit())
# print(stg4.isdigit())


## 27. Check if a string is alphabet.

# stg1="naveen"
# stg2="naveen234"
# stg3="naveen sai"
# stg4="435nsvrr"
# print(stg1.isalpha())
# print(stg2.isalpha())
# print(stg3.isalpha())
# print(stg4.isalpha())

## 28. Check if a string is alphanumeric.
# stg1="naveen234"
# stg2="naveen sai"
# stg3="naveen@123"
# stg4="435nsvrr"
# print(stg1.isalnum())
# print(stg2.isalnum())
# print(stg3.isalnum())
# print(stg4.isalnum())

## 29. Get ASCII value of a character.
# print(ord('A'))
# print(ord('a'))
# print(ord('0'))
# print(ord('@'))
# print(ord(' '))
# print(ord('#'))


## 30. Convert ASCII to character.

# print(chr(97))
# print(chr(65))
# print(chr(48))
# print(chr(32))
# print(chr(64))
# print(chr(35))



## 31. Remove punctuation from string.

# import string
# stg1="Hello!!!, he said ---and went."
# nopun=stg1.translate(str.maketrans('','',string.punctuation))
# print(nopun)


## 32. Swap case of all characters.
# stg1="Hello World"
# print(stg1.swapcase())

## 33. Count total words in a string.
# stg1="hello world good moring"
# print(len(stg1.split()))

## 34. Count total sentences in a string.
# stg1="hello world. good moring. have a nice day."
# print(len(stg1.split('.')))

## 35. Convert string to list of characters.
# stg1="naveen"
# print(list(stg1))

## 36. Convert list of characters to string.
# chars=['n','a','v','e','e','n']
# print(''.join(chars))

## 37. Pad string to the left with * to length 10.
# stg1="naveen"
# print(stg1.rjust(10,'*'))

## 38. Center align string using center().
# stg1="naveen"
# print(stg1.center(10,'*'))

## 39. Format string with variables using f-string.
# name="naveen"
# age=24
# print(f"my name is {name} and my age is {age}")

## 40. Use % operator to format a string.
# name="naveen"
# age=24
# print("my name is %s and my age is %d"%(name,age))

## ⚙️ Medium (35 Questions)

## 41. Count number of vowels in a string.

# stg=input("enter the string: ")
# vowles='aeiouAEIOU'
# count=0
# for chr in stg:
#     if chr in vowles:
#         count+=1
# print(count)

## 42. Remove duplicate characters.

# stg=input("enter the string: ")
# result=" "
# for chr in stg:
#     if chr not in result:
#         result+=chr
# print(result)

## 43. Check if string is palindrome.

# stg=input("enter the string: ")
# if stg==stg[::-1]:
#     print("palidrome")
# else:
#     print("not a palidrome")

## 44. Replace all vowels with '*'.

# stg=input("enter the string:")
# vowels='aaeiouAEIOU'
# for chr in stg:
#     if chr in vowels:
#         stg=stg.replace(chr,"*")
# print(stg)

## 45. Check if two strings are anagrams.
stg1=input("enter the string1: ")
stg2=input("enter the string2:")

## 46. Find all occurrences of a substring.
## 47. Reverse each word in a sentence.
## 48. Find longest word in a sentence.
## 49. Extract digits from a string.
## 50. Remove digits from a string.
## 51. Convert camelCase to snake_case.
## 52. Count frequency of characters.
## 53. Keep only alphanumeric characters.
## 54. Capitalize first letter of each word.
## 55. Replace multiple spaces with single space.
## 56. Encode string with ROT13 cipher.
## 57. Mask a string like a password.
## 58. Add ordinal suffix to number string.
## 59. Implement custom trim function.
## 60. Find common characters in two strings.
## 61. Convert tab-separated string to list.
## 62. Count uppercase and lowercase characters.
## 63. Extract email from text string.
## 64. Count lines in a multi-line string.
## 65. Escape characters in a string.
## 66. Replace multiple substrings with map.
## 67. Parse key-value pairs from string.
## 68. Check for balanced parentheses.
## 69. Remove HTML tags from string.
## 70. Convert numeric string to int safely.
## 71. Count how many words start with a vowel.
## 72. Group words by first character.
## 73. Sort string by characters.
## 74. Remove nth character from a string.
## 75. Remove all whitespaces from string.

# 🔥 Hard (25 Questions)

# 76. Find longest substring without repeating characters.
# 77. Implement your own find() method.
# 78. Generate all permutations of characters.
# 79. Compress string using counts of repeated chars.
# 80. Pattern match with * and ? wildcards.
# 81. Implement string multiplication manually.
# 82. Remove stopwords from a sentence.
# 83. Implement Caesar cipher encode/decode.
# 84. Find all palindromic substrings.
# 85. Implement basic substring search (like KMP).
# 86. Replace only whole words in string.
# 87. Match nested brackets with stack.
# 88. Evaluate basic math expression string.
# 89. Parse JSON string without using json module.
# 90. Convert numeric words to digits ("one" → 1).
# 91. Decode Morse code string.
# 92. Detect and redact sensitive words.
# 93. Split long text into 160-char SMS chunks.
# 94. Implement Levenshtein (edit) distance.
# 95. Create acronym from sentence.
# 96. Evaluate postfix string expression.
# 97. Count overlapping substrings.
# 98. Validate email format using regex.
# 99. Parse query string into dictionary.
# 100. Tokenize sentence into words and punctuations.