# Code for generating Fibonacci sequence
seq=[1,1]
i=1
for i in range(0,8):
   # print (i)
    a=seq[i]
    i+=1
    b=seq[i]
    c=a+b
    seq.append(c)
print (seq)

    
    
