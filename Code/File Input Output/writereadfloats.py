#!/usr/bin/python

# Write out high scores

numbers = [1.11, 1.22, 1.33, 1.44]
f = open('numbers.dat', 'wb')

for n in numbers:
	f.write(n)

f.close()

f = open('numbers.dat', 'rb')
fileContent = f.read()
f.close()

numItems = len(fileContent) / 4
format = "f" * numItems

for item in struct.unpack_from(format, fileContent):
	print item