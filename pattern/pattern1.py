rol,col=map(int,input().split(" "))
count=1
title=".|."
c=rol//2
for i in range(rol):
    if i==0 or i==rol-1:
        print(title.center(col,"-"))
    elif i<c:
        count=count+2
        print((title*count).center(col,"-"))
    elif c==i:
        print("WELCOME".center(col,"-"))
    elif i>c:
        print((title*count).center(col,"-"))
        count=count-2
        