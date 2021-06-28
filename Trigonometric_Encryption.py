import math, string
import matplotlib.pyplot as plt
from edit_me import *



###### TEXT TO BE ENCRYPTED #######



class encrypter():

    def __init__(self, text):
        alphabets = [' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        Calphabets= string.ascii_uppercase
        self.a = a # - Vertical stretch  - similar to that amplitude of a sin graph
        self.p = p # - Period of the tangential graph 
        self.b = (math.pi)/p  # - B value from the transformation formula - pi/b 
        self.C = C # - Horizontal translation for the graph 
        self.hum = hum # - constant that separates the predetermined y values 
        self.d = d # - Vertical translation of the graph -- no effect on encryption
        self.inittext = ptext # - Text to be encrypted 
        self.xvalues = {}
        self.x_values = {}
        self.x_v = []
        for index, letter in enumerate(alphabets):
            x =  ((((0.6*self.p)/27)*index)+(0.2*self.p))
            self.x_v.append(x)
            self.xvalues[x] = letter
            self.x_values[letter] = x
        self.yvalues = {}
        self.y_values= {}
        self.y_v = []
        for index, letter in enumerate(alphabets):
            y = 26
            x = []
            m = ((index-(y/2))*self.hum)+self.d
            self.y_v.append(m)
            self.yvalues[m] = letter
            self.y_values[letter] = m
        self.real_values=dict(zip(self.x_v,self.y_v))
        self.realvalues=dict(zip(self.y_v,self.x_v))

        ##### Executing the functions ##### 
        self.encrypted = self.encrypt(self.inittext)
        self.decrypted = self.decrypter(self.encrypted)

    def tan(self, x):
        """
        Calculates the y value for a given x value on the tan graph 
        """
        graph = self.a * math.tan(self.b*(x-self.C)) + self.d
        return graph

    def arctan(self, x):
        """
        Calculates the inverse y value for a given x value on the inverse-tan graph 
        """
        graph = ((math.atan( (x -self.d) / (self.a) )) /self.b ) + self.C
        return graph


    def approximate(self,list, value):
        """
        Given a value and a list, finds the item within the list/array 
        that has the least absolute difference with the value
        """
        n = []
        for x in list:
            n.append(abs(value - x))
        idx = n.index(min(n))
        return list[idx]


    def encrypt(self, text):
        crpyt=[]
        for char in text.lower():
            xval = self.x_values[char]
            yval = self.tan(xval)
            close = self.approximate(self.y_v,yval)
            crpyt.append(self.yvalues[close])
        return "".join(crpyt)


    def decrypter(self, text):
        plain =[]
        alphabets = string.ascii_lowercase
        for char in text:
            xval = self.y_values[char]
            yval = self.arctan(xval)
            close = self.approximate(self.x_v,yval)
            plain.append(self.xvalues[close])
        return "".join(plain)

if __name__ == '__main__':
    enc = encrypter(ptext)
    print("your encrypted message is --",enc.encrypted)
    print("your decrypted message is --",enc.decrypted)
