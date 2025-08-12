#CHECK IF STRING IS PALINDROME
palindrome = input("Enter the string: ")
length = len(palindrome)

if length % 2 == 1:
    middle_str = palindrome[int(length / 2)]

else:
    middle_str = palindrome[int(length / 2) - 1: int(length / 2) + 1]

two_parts = palindrome.split(middle_str)
part1 = two_parts[0]
part2 = two_parts[1]
part1string = ""

for i in range(1, len(part1) + 1):
    part1string += part1[-i]

if len(palindrome) == 2 and palindrome[0] == palindrome[1]:
    print("String is a palindrome")

elif len(palindrome) == 1:
    print("String is a palindrome")

elif part1string == part2 and len(palindrome) != 2:
    print("String is a palindrome")

else:
    print("String is not a palindrome")



#FIND TOTAL NUMBER OF DIGITS (WITHOUT .ISDIGIT())
# digit_string = input("Enter string: ")
# digits = "1234567890"
# count = 0
# for i in digit_string:
#     if i in digits:
#         count += 1

# print(f"Amount of digits are {count}")



#FORM A STRING WITH FIRST 2 DIGITS AND LAST 2 DIGITS
# parent_string = input("Enter a string: ")
# first_part = parent_string[0:2]
# last_part = parent_string[len(parent_string) - 2 : len(parent_string)]
# final = first_part + last_part
# print(f"The final string is {final}")



#CHECK NUMBER OF WORDS IN A SENTENCE
# sentence = input("Enter a sentence string: ")
# refined_sentence = sentence.strip()
# listed_sentence = refined_sentence.split(" ")
# spaces = len(listed_sentence)
# print(f"Number of words: {spaces}")



#CHECK IF SUBSTRING IS IN A STRING
# string = input("Enter parent string: ")
# sub = input("Enter substring: ")
# if sub in string:
#     print("Substring is present in string")
# else:
#     print("Not present")