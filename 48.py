#48. l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4]
#l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4]
l=[1,2,5,6,7,9,10]
#m=l[0]
L=[]
k=0
j=1
p=0
for i in range(1,len(l)):
 
    if(l[i]-l[k]==1):
        j+=1
        k+=1
        print(j)
    
    else:
        k=k+1
        
        L.append(l[p:j])
        p=j
        j+=1
L.append(l[p:])
print(L)
    
        
    
        
