file_read=open('Codingal.txt','r')
print("file in read mode-")
print(file_read.read())
file_read.close()

file_write=open('Codingal.txt','w')
file_write.write("file in write mode......")       
file_write.write("HI! i am penguin.i am 1yr old.")     
file_write.close()   

file_append=open('Codingal.txt','a')
file_append.write("\n file in append mode")
file_append.write("HI! i am penguin.i am 1yr old.")
file_append.close()