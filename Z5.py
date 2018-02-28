N = input("Podaj zasieg: ")
list = []
for i in range(0,int(N)):
    k = input()
    list.append(int(k))

order = input("Rosnace (R) czy malejace (M): ")
if(order=='R'):
    list.sort()
else:
    list.sort(reverse=True)
    
for i in list:
    print(i)
