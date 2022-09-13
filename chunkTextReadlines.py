# chunkTextReadlines.py
'''
Operations with text slicing and readlines method.
'''
#
# task1: I have long text. I want to divide it on the lines of chunks of 50 characters each one
#
inputFile3 = open('readlines2.txt', 'r')
outputFile = open('readlinesOk.txt', 'w')

# extract chunks of 50 characters from the text
book = inputFile3.read()  # simple string

i = 0
z = 50

for index in range(int(len(book)/50)):
    chunk = book[i:z]

    outputFile.write(chunk+'\n')

    i += 50
    z += 50

# rest of the text
slice = book[-(len(book) % 50):-1]
outputFile.write(slice)
print(f"slice:{slice}")
outputFile.close()

# I want to pack each chunk of 50 characters and remaining slice to the list.
inputFile = open('readlinesOk.txt', 'r')
listReadlines = inputFile.readlines()
print(f"\n\nlistReadlines:\n{listReadlines}")
inputFile.close()
