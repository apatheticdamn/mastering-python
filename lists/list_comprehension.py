numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
numbers_strings = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']

even_numbers = [number for number in numbers if number%2==0]
squared_numbers = [num*num for num in numbers]
squared_even_numbers = [n*n for n in numbers if n % 2 == 0]
squared_odd_numbers = [n*n for n in numbers if n % 2 != 0]
converted = [int(num) for num in numbers]


# for number in numbers:
#   if number % 2 == 0:
#     even_numbers.append(number)
print("Numbers:", numbers)
print("Even Numbers:", even_numbers)
print("Squared Numbers:", squared_numbers)
print("Squared Even Numbers:", squared_even_numbers)
print("Squared Odd Numbers:", squared_odd_numbers)
print("Converted into numbers:", converted)

words = ["programming", "exploit", "control", "phishing", "ddos"]
first_letters = [word[0] for word in words]

# for word in words:
# first_letter.append(word[0])
print("First letter of each word:", first_letters)

