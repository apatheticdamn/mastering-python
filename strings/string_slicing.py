'''String slicing in python programming is all about fetching a substring from a given string by slicing it from a 'start' index until a 'stop' index.

[start:stop:step]
'''

full_name = "Apathetic Damn"
first_name = full_name[0:9] # 9 is not included and we could also use [:9] and 9th index is included 
print(first_name)

print(first_name[::-1]) # for reversing a string value

last_name = full_name[10:14] # we could also use [10:]
print(last_name)

print(full_name[0:14:2]) # we could jump 2 steps and we could also use [0::2]

website1 = "https://github.com"
website2 = "https://google.com"
website3 = "https://wikipedia.com"

sliced_website = slice(8, -4) # it is for slicing or removing the https:// and .com

print(website1[sliced_website]) # very useful
print(website2[sliced_website])
print(website3[sliced_website])