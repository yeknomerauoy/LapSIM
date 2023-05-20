import math
import cmath

def equation(x1,x2,x4,y1,y2,y4,xm,ym,m,cx):
    return(((x4-cx)**2 + (y4-(ym-m*(cx-xm)))**2)**0.5 - ((x2-cx)**2 + (y2-(ym-m*(cx-xm)))**2)**0.5) * ((((cx-x4) + (y4-(ym-m*(cx-xm)))*m)/(((x4-cx)**2 + (y4-(ym-m*(cx-xm)))**2)**0.5)) - ((cx-x2) + (y2-(ym-m*(cx-xm)))*m)/(((x2-cx)**2 + (y2-(ym-m*(cx-xm)))**2)**0.5)) + (((x1-cx)**2 + (y1-(ym-m*(cx-xm)))**2)**0.5 - ((x2-cx)**2 + (y2-(ym-m*(cx-xm)))**2)**0.5) * ((((cx-x1) + (y1-(ym-m*(cx-xm)))*m)/(((x1-cx)**2 + (y1-(ym-m*(cx-xm)))**2)**0.5)) - ((cx-x2) + (y2-(ym-m*(cx-xm)))*m)/(((x2-cx)**2 + (y2-(ym-m*(cx-xm)))**2)**0.5)+cx)


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
        x1=self.pos1.real
        y1=self.pos1.imag
        x2=self.pos2.real
        y2=self.pos2.imag
        x3=self.pos3.real
        y3=self.pos3.imag
        x4=self.pos4.real
        y4=self.pos4.imag
        xm=(x2+x3)/2
        ym=(y2+y3)/2
        m=(x3-x2)/(y3-y2)
        

        # Newton-Raphson iteration
        cx=1 #Initial guess
        
        for _ in range(1000000):
            cx_new = equation(x1,x2,x4,y1,y2,y4,xm,ym,m,cx)
            
            if abs(cx_new - cx) < 1e-6:
                break

            cx=cx_new
    
        cy=(((self.pos2.imag)+(self.pos3.imag))/2)-(((self.pos3.real)-(self.pos2.real))/((self.pos3.imag)-(self.pos2.imag)))*(cx-((self.pos2.real)+(self.pos3.real))/2)
        r=math.sqrt((cx-(self.pos2.real))**2+(cy-(self.pos2.imag))**2)
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
