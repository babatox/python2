new_file=('code.txt','x')
new_file.close()

import os
print("checking if file exists or not......")
  os.path.exists('code.txt')
else:
    print("file does not exist")

my_file = open('code.txt','w')
my_file.write("hi i am a penguin and i am 1 yr old")
my_file.close()

os.remove('code.txt')

os.rmdri('folder')