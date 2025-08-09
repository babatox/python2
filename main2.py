file = open('Codingal.txt','r')
print(file.readline())
file.close()

file = open('Codingal.txt','r')
print("\n Reading multiple lines  \n")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file = open('Codingal.txt','r')
for line in file:
    print(line)
file.close()    