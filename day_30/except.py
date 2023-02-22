# FILENOTFOUNDERROR
"""
with open('data.txt', 'r') as file:
    file.read()
"""

# KEYERROR
"""
my_dict = {"website": "asd"}
print(my_dict['age'])
"""

# INDEXERROR
"""
A = [1, 2, 3, 4, 5, 6, 7]
print(A[34])
"""

#TYPERROR
"""
text = 'asv'
text += 1
"""

"""
try:
    # Something that might
    # cause an exception
except:
    # Do this if there was
    # exception
else:
    # do this if there wasn't
    # exception
finally:
    # do this no matter what happends
"""


"""
try:
    d = {'data': "123445"}
    print(d['data'])
    file = open('data.txt')
except FileNotFoundError:
    file = open('data.txt', 'w')
    file.write('Something')
except KeyError as mesagge:
    print(f"There is not {mesagge}")
else:
    content = file.read()
    print(content)
finally:
    file.close()
"""
