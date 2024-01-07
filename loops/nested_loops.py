'''
A nested loop means a loop statement inside another loop statement. That is why nested loops are also called “loop inside loops“
'''

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol you want to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()