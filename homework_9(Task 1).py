print('Task 1')
myfile = open('myfile.txt', 'w')
myfile.write('Hello file world!')
myfile.close()

myfile = open('myfile.txt', 'r')
show = myfile.read()
print(show)
myfile.close()

