rows = int(input("Input rows : ")) #horizontal rows
columns = int(input("Input columns : ")) #vertical columns
"""
2rows
3columns
@@@@
@@@@
@@@@
"""
character = ''
while len(character) != 1:
    character = input("Enter a single character for your board")

board = ''
for i in range(rows):
    for j in range(columns):
        board += character
    board += "\n"

print(board)
