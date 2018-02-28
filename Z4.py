n = input()
for i in range(0,26):
    if((i+1)%int(n)==0):
        print(chr(i+97),chr(i+65))
