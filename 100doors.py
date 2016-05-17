doors=[]
doors=doors+[0]*100
for i in range(1,101):
    for j in range(1,101):
        if (i%j==0):
            doors[i-1]=doors[i-1]+1
for i in range (100):
    if (doors[i]%2==1):
        print (i+1)
