# cook your dish here
for t in range(int(input())):
    n=int(input())
    a=input()
    b=input()
    a,b=list(a),list(b)
    #print(a,b)
    a.sort()
    b.sort()
    if(a==b):
        print("YES")
    else:
        print("NO")