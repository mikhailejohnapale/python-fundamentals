# 32-exceptions.py

try:
    file = open('samples.txt', 'r')
    file.write('This line will be written!')
except IOError:
    print('File does not exist!')
else:
    print('Written successfully!')
    file.close()
