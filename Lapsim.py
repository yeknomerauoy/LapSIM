import math
import cmath

class lap():

    def _init_(self):
        self.pos1
        self.pos2
        self.pos3
        self.pos4
        self.data

    def put_data(self,arr):
        self.pos1=arr[0]
        self.pos2=arr[1]
        self.pos3=arr[2]
        self.pos4=arr[3]

    def find_circle(self):
        cx=(2(self.pos1.real+self.pos4.real)-2(self.pos1.imag+self.pos4.imag)*((self.pos3.real-self.pos2.real)/(self.pos3.imag-self.pos2.imag))+4*((self.pos2.imag+self.pos3.imag)/2)*((self.pos3.real-self.pos2.real)/(self.pos3.imag-self.pos2.imag))+4*((self.pos2.real+self.pos3.real)/2)/(m*m))/(4+((self.pos3.real-self.pos2.real)/(self.pos3.imag-self.pos2.imag))**2)
        cy=((self.pos2.imag+self.pos3.imag)/2)-((self.pos3.real-self.pos2.real)/(self.pos3.imag-self.pos2.imag))(cx-(self.pos2.real+self.pos3.real)/2)
        r=math.sqrt((cx-self.pos2.real)**2+(cy-self.pos2.imag)**2)
        print("Radius=",r)
        print("Centre=(",cx,",",cy,")")
    
rad=lap()
arr=[0,0,0,0]
for i in range(0,4):
    print("For point number ",i+1)
    x=int(input("Enter x:"))
    y=int(input("Enter y:"))
    arr[i]=complex(x,y)
rad.put_data(arr)
rad.find_circle()