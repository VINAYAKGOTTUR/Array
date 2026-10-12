def tower(n,a,b,c):
    if n==1:
        print(f"move {a} to {c}")
    else:
        tower(n-1,a,c,b)
        print(f"move disk {a} to {c}")
        tower(n-1,b,a,c)
n=int(input())
tower(n,"A","B","C")