with open('code.txt','w')as a file:
   file.write("hi i am a  pengiun and i am 1yr old")
file.close()   

with open('Codingal.txt','r') as file:
    data= file.readline()
    print("words in this file are...")
    for lines in data:
        word = lines.split()
        print(word)
    file.close()   