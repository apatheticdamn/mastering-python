'''
Loop Control Statements = change a loops execution from its normal sequence

break = used to terminate the loop entirely
continue = skips to the next interation of the loop
pass = does nothing, acts as a placeholder
'''

while True:
    name = input("Enter your name: ").strip() # strip function for removing the spaces
    if name != "":
        print("Hello " + name.capitalize() + "!")
        break # it will terminate the loop after the statements fullfills its condition


phone_num = "123-456-7890"
for i in phone_num:
    if i == "-": # this statement will simply remove "-" dashes from the phone number
        continue # this will skips to the next iteration of the loop
    print(i, end="")


for i in range(0, 20):
    if i == 13:
        pass # pass does nothing that's why 13 is not printed
    else:
        print(i)
