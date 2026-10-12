def quick(a,l,h):
    if l<h:
        k=par(a,l,h)
        quick(a,l,k-1)
        quick(a,k+1,h)
def par(a,l,h):
    i=l
    j=h
    p=a[l]
    while(i<j):
        while a[i]<=p and i<j:
            i+=1
        while a[j]>p:
            j-=1
        if i<j:
            a[i],a[j]=a[j],a[i]
    a[l],a[j]=a[j],a[l]
    return j

a=list(map(int,input().split()))
quick(a,0,len(a)-1)
print(a)
