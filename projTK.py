from math import sqrt
import cmath

class obj():
    def _init_(self):
        self.pos1
        self.pos2
        self.pos3
        self.data

    def put_data(self,arr):
        self.pos1=arr[0]
        self.pos2=arr[1]
        self.pos3=arr[2]

    def findCircle(self) :
        f = (((self.pos1.real*self.pos1.real - self.pos3.real*self.pos3.real) * (self.pos1.real-self.pos2.real) + (self.pos1.imag*self.pos1.imag - self.pos3.imag*self.pos3.imag) *(self.pos1.real-self.pos2.real) + (self.pos2.real*self.pos2.real - self.pos1.real*self.pos1.real) * (self.pos1.real-self.pos3.real) +(self.pos2.imag*self.pos2.imag - self.pos1.imag*self.pos1.imag) * (self.pos1.real-self.pos3.real)) / (2 *((self.pos3.imag-self.pos1.imag) * (self.pos1.real-self.pos2.real) - (self.pos2.imag-self.pos1.imag) * (self.pos1.real-self.pos3.real))))
        g = (((self.pos1.real*self.pos1.real - self.pos3.real*self.pos3.real) * (self.pos1.imag-self.pos2.imag) + (self.pos1.imag*self.pos1.imag - self.pos3.imag*self.pos3.imag) * (self.pos1.imag-self.pos2.imag) +(self.pos2.real*self.pos2.real - self.pos1.real*self.pos1.real) * (self.pos1.imag-self.pos3.imag) + (self.pos2.imag*self.pos2.imag - self.pos1.imag*self.pos1.imag) * (self.pos1.imag-self.pos3.imag)) /(2 * ((self.pos3.real-self.pos1.real) * (self.pos1.imag-self.pos2.imag) - (self.pos2.real-self.pos1.real) * (self.pos1.imag-self.pos3.imag))))
        return (complex(-g,-f),sqrt(g * g + f * f - (-self.pos1.real*self.pos1.real - self.pos1.imag*self.pos1.imag -2 * g * self.pos1.real - 2 * f * self.pos1.imag)))
    
    def r_vect(self,arr):
        n=len(arr)
        i=0
        while (i<n):
            if (i+2<n):
                self.pos1=arr[i]
                self.pos2=arr[i+1]
                self.pos3=arr[i+2]
                print(obj.findCircle(self))
            elif (i==n-2):
                self.pos1=arr[n-2]
                self.pos2=arr[n-1]
                self.pos3=arr[0]
                print(obj.findCircle(self))
            else :
                self.pos1=arr[n-1]
                self.pos2=arr[0]
                self.pos3=arr[1]
                print(obj.findCircle(self))    

            i+=1


rad=obj()
arr=[complex(0.14842,0.2471) , complex (1.317931,-0.3137) , complex(-0.9317,0.8137414) , complex(1.491248,1.42452)]
rad.r_vect(arr)
