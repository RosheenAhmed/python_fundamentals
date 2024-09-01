# string are technically objects

# String methods:

# 1- upper ( This will convert string into upper case )
upper_case_variable = 'daniyal'
print(upper_case_variable.upper())

# 2- lower ( This will convert the string into lower case )
lower_case_variable = "DANIYAL"
print(lower_case_variable.lower())

# 3- find (This will search a substring in the string, if found this will return the index and if not
# this will return -1
quote = "This is a random quote to test find method of string"
print(quote.find("random")) # this line will print the index of find as it is present in quote
print(quote.find("hello")) # this will print -1 as it is not present in quote

# 4- replace
quote_two = "This is a random quote to test find method of string"
modified_quote = quote_two.replace("random", "specific")
print("Original quote: " + quote_two)
print("Modified quote: " + modified_quote)
