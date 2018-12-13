


import re
import os, sys


class Adder(object):

    #Initializing the class
    def __init__(self, n1, n2):
        self.one = n1
        self.two = n2

    #Adding two number
    def sum (self):
        s = self.one + self.two
        print("The sum is %d" %s)
        return s

    def f(self, a=2, b=3):
        print("The value of a and b are %d and %d " % (a, b))

    def ispalindrome(self, mystring):
        text = 'Anand'
        reverse_text = text[::-1]
        print(text)
        print(reverse_text)


    def readfile(self):
        try:
            fp = open("foo.txt")
            line = fp.readline()
        except FileNotFoundError as fe:
            print(fe)
        except Exception as e:
            print(e)



    def ispalindrome(self, mystring):
        text = mystring
        reverse_text = mystring[::-1]

        if (re.search(text, reverse_text)):
            print("It is palindrome")
            return True
        else:
            print("It is not palindrome")
            return False







adder1 = Adder(10, 2)
print(adder1.sum())
adder1.f(3)
adder1.f(3,4)
adder1.f(b=3, a=4)
adder1.ispalindrome("Anand")
adder1.readfile()
