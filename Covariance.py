import numpy as np
n=int(input("Enter the value : "))
cov_matrix=np.zeros((2,2))
arr=[]
arr1=[]
for i in range(n):
    ele=int(input("Enter : "))
    arr.append(ele)
i=0
print("For second array")
for j in range(n):
    ele=int(input("Enter : "))
    arr1.append(ele)
j=0
sum1=0
sum2=0
sum3=0
arr=np.array(arr)
arr1=np.array(arr1)
x=(np.sum(arr))/n
y=(np.sum(arr1))/n
for i in range(n): #covarience of x,y 
    sum1=sum1+(arr[i]-x)*(arr1[i]-y)
final1=sum1/n    
for j in range(n): #varience of x
    sum2=sum2+((arr[j]-x)*(arr[j]-x))
final2=sum2/n
for k in range(n): #varience of y
    sum3=sum3+((arr1[k]-y)*(arr1[k]-y))
final3=sum3/n
cov_matrix[0][0]=final2
cov_matrix[0][1]=final1
cov_matrix[1][0]=final1
cov_matrix[1][1]=final3
print(cov_matrix) 
