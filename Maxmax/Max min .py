# assignment-1.-23-02-22
Write a program to maximum and minimum elements in the list


l=[]
n=int(input('enter n'))
for i in range(n):
   c=int(input())
   l.append(c)
min=l[0]
for i in range(1,n):
   if l[i]<min:
     min=l[i]
max=l[0]
for i in range(1,n):
   if l[i]>max:
     max=l[i]
 
print(min) 
print(max)


Enter n:4
23
25
36
63
minimum value: 63
maximum value: 23
