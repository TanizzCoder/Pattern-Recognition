import numpy as np
m=np.array([[0.8,0.3],[0.2,0.7]])
def sridharacharya(a,b,c):
    if (b*b)-(4*a*c)==0:
        print("The matrix has a single eigen value.")
        r1=-b/(2*a)
        r2=0
        print("Eigen value of the matrix is ",r1)
        return (r1,r2)
    elif (b*b)-(4*a*c)<0:
        print("The eigen values of the matrix are complex roots.")
    elif (b*b)-(4*a*c)>0:
        print("The matrix has two eigen values.")
        r1=(-b+((b**2)-(4*a*c))**(1/2))/(2*a)
        r2=(-b-((b**2)-(4*a*c)))/(2*a)
        print("The eigen values of the matrix are",r1," and",r2,".")
        return (r1,r2)
r1,r2=sridharacharya(1,-1.5,0.5)
ev1=m[0][0]-r1+m[0][1]
ev2=m[1][0]+m[1][1]-r1
ev3=m[0][0]-r2+m[0][1]
ev4=m[1][0]+m[1][1]-r2
print("Corresponding eigen vectors of the matrix are",ev1,ev2,ev3," and",ev4)
