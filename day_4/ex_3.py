"""
You are going to write a program which will mark a spot with an X.

In the starting code, you will find a variable called rows.

This rows contains a nested list. When map is printed this is what the nested list looks like:

['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']
In the starting code, we have used new lines (\n) to format the three rows into a square, like this:

['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
This is to try and simulate the coordinates on a real rows.
"""

row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']
rows = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

coord = input("Where do you want to put the treasure? ")

horizontal = int(coord[0])
vertical = int(coord[1])

rows[vertical - 1][horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")

