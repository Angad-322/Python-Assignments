#PRIME NUMBERS
# integers = range(10)
# some_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
# all_primes = []
# for i in integers:
#     is_prime = True
#     for prime in some_primes:
#         if i % prime == 0 and i != prime:
#             is_prime = False
#     if is_prime:
#         all_primes.append(i)

# del all_primes[0]
# print(all_primes)

#TRANSOFRM TO ABSOLUTE VALUES IF NEGATIVE, OTHERWISE SQAURE THEM
# numbers = [1, -2, 3, 4]
# mapped_numbers = list(map(lambda x: x ** 2 if x > 0 else abs(x), numbers)) 
# print(mapped_numbers)  

#VALID E-MAIL FILTER
# email_spam = ["john@company.com", "inavlid.email", "bob@.com", "alice@company.com"]
# valid_emails = list(filter(lambda x: "@company.com" in x, email_spam))
# print(valid_emails)

#FILE PATH EXTRACTOR
# files = ["docs/file1.txt", "docs/subfolder/file2.txt", "images/photo.jpg"]
# extensions = list(map(lambda x: x[-3:], files))
# print(extensions)

#NUMBERS 1 - 30 WHOSE SUM OF DIGITS IS 5, (DOUBT)
numbers = list(range(30))
stringed_numbers = list(map(lambda x: str(x), numbers))
list_numbers = list(map(lambda y: list(map(lambda x: int(x), y)), stringed_numbers))
sum_numbers = list(filter(lambda x: sum(x) == 5, list_numbers))
print(sum_numbers)