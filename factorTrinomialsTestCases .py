######################################################################################################
#Purpose: this program includes a wide variety of cases that tests the package factorTrinomialTool.py
#Programmers: Rena Lu, Pavneet Kapoor, Saad Haq, Alex Nelson
#Last Modified: May 13, 2014
#######################################################################################################


from factorTrinomialTools import *

#QUADRATIC EXPRESSIONS WITH THREE TERMS
print ("Tests on quadratic expressions with three terms (the trinomials)")
print ()

#FACTORABLE TRINOMIALS
print ("    Factorable trinomials")
trinomial = "x^2 + 3x - 4" #-->> a=1
print (trinomial + " can be factored into " + factorTrinomial( trinomial ))

trinomial = "3x^2 - 10x - 8"#-->> a!=0, b<0
print (trinomial + " can be factored into " + factorTrinomial( trinomial ))

trinomial = "6x^2 + x - 1" #-->> b=1
print (trinomial + " can be factored into " + factorTrinomial( trinomial ))

trinomial = "-x^2 - x + 6" #-->> a=-1, b=-1
print (trinomial + " can be factored into " + factorTrinomial( trinomial ))

trinomial = "-2x^2 - 2x + 12" #-->> a<0, and a!=-1
print (trinomial + " can be factored into " + factorTrinomial( trinomial ))

trinomial = "-3x^2 - 7x + 6" #-->> a<0, and a!=-1
print (trinomial + " can be factored into " + factorTrinomial( trinomial ))

trinomial = "2x^2 + 6x - 8" #-->> Common factor of coefficients != 1
print (trinomial + " can be factored into " + factorTrinomial( trinomial ))

print ()
#PERFECT SQUARES
print ("    Perfect Squares")
trinomial = "x^2 + 6x + 9" #-->> a=1
print (trinomial + " can be factored into " + factorTrinomial( trinomial ))

trinomial = "4x^2 - 12x + 9" #-->> a!=1
print (trinomial + " can be factored into " + factorTrinomial( trinomial ))

trinomial = "2x^2 + 12x + 18" #-->> Common factor of coefficients != 1
print (trinomial + " can be factored into " + factorTrinomial( trinomial ))

print ()

#TRINOMIALS THAT CAN BE COMMON FACTORED ONLY
print ("    Trinomials that can be common factored only")
trinomial = "2x^2 + 12x + 34"
print (trinomial + " can be factored into " + factorTrinomial( trinomial ))

trinomial = "-2x^2 - 12x - 34" #-->> a<0
print (trinomial + " can be factored into " + factorTrinomial( trinomial ))

print ()

#UNFACTORABLE TRINOMIALS
print ("    Trinomials that cannot be factored")
trinomial = "x^2 + 6x + 17"
print (trinomial + " is " + factorTrinomial( trinomial ))

trinomial = "-x^2 + 6x + 17"
print (trinomial + " is " + factorTrinomial( trinomial ))

trinomial = "2x^2 - x + 3"
print (trinomial + " is " + factorTrinomial( trinomial ))

print()
print()

#QUADRATIC EXPRESSIONS WITH TWO TERMS
print ("Tests on quadratic expressions with three terms (the binomials)")
print ()

#BINOMIALS WHERE c-Term = 0
print ("    Binomials missing a 'c' term")
trinomial = "x^2 + 3x" #-->> a=1
print (trinomial + " can be factored into " + factorTrinomial( trinomial ))

trinomial = "2x^2 + 4x" #-->> a!=1
print (trinomial + " can be factored into " + factorTrinomial( trinomial ))

trinomial = "4x^2 + 8x"
print (trinomial + " can be factored into " + factorTrinomial( trinomial ))

print ()

#BINOMIALS WHERE b-Term = 0
print ("    Binomials missing a 'b' term")

#DIFFERENCE OF SQUARES BINOMIALS
print ("        Difference of squares")

trinomial = "x^2 - 4" #-->> a=1
print (trinomial + " can be factored into " + factorTrinomial( trinomial ))

trinomial = "16x^2 - 25" #-->> a!=1
print (trinomial + " can be factored into " + factorTrinomial( trinomial ))

trinomial = "32x^2 - 50" #-->> common factor of coefficients != 1
print (trinomial + " can be factored into " + factorTrinomial( trinomial ))

trinomial = "-x^2 + 4" #-->> common factor = -1
print (trinomial + " can be factored into " + factorTrinomial( trinomial ))

trinomial = "-2x^2 + 8" #--> common factor < 0, common factor != -1
print (trinomial + " can be factored into " + factorTrinomial( trinomial ))

print ()

#BINOMIALS MISSING A B-TERM THAT CAN ONLY BE COMMON FACTORED
print ("         Common factor only")

trinomial = "4x^2 + 8"
print (trinomial + " can be factored into " + factorTrinomial( trinomial ))

trinomial = "2x^2 + 4"
print (trinomial + " can be factored into " + factorTrinomial( trinomial ))

print ()

#BINOMIALS MISSING A B-TERM THAT CANNOT BE FACTORED
print ("        Unfactorable Binomials")

trinomial = "x^2 + 4"
print (trinomial + " is " + factorTrinomial( trinomial ))

trinomial = "16x^2 + 25" 
print (trinomial + " is " + factorTrinomial( trinomial ))







