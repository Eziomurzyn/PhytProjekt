def max(a,b,c):
    if(a>b):
        if(a>c):
            return a
        else:
            return c
    else:
        if(b>c):
            return b
        else:
            return c


a=input()
b=input()
c=input()
  
print(max(int(a),int(b),int(c)))
