#####################################################################################################################
#Purpose: this package allows a user to input any factorable quadratic trinomial or binomial into its factored form
#Programmers: Rena Lu, Pavneet Kapoor, Saad Haq, Alex Nelson
#Last Modified: May 13, 2014
#####################################################################################################################

from math import *

def createArray(quadraticTrinomial):
    trinomial = quadraticTrinomial.split(' ')
    return trinomial

#Purpose: To find the number of terms in a given trinomial. Returns either a one or a two.
def findNumTerms(array):
    length = len(array)
    terms_in_array = 0
    if length == 3:
        terms_in_array = 2
    elif length == 5:
        terms_in_array = 3
    else:
        print ("Error, please check your input.")
    return terms_in_array


#Purpose: To Find the coefficients of a, b, and c. If not present in the equation it returns a 0 as the value.
#(continued) This means if you equation is 10x^2 - 10 it will return a as 10, b as 0 and c as -10).
def findCoefficients(array):
    #Sets up the local variables and also defines the coefficents array.
    terms = findNumTerms(array)
    leng_first = len(array[0])
    leng_second = len(array[2])
    coefficents = []
    
    #Finds the coefficent of term one (a)
    if array[0][0] == "x":
        a = 1
    elif array[0][0] == "-" and array[0][1] == "x":
        a = -1
    else:
        a = int(array[0][0 : leng_first - 3])
    coefficents.append(a)
    
    #Finds the coefficent of the second term.
    if array[2][0] == "x":
        b = 1
        c = 0
    elif array[2][leng_second - 1] == "x":
        b = int(array[2][0 : leng_second - 1])
        c = 0
    else:
        b = 0
        c = int(array[2])
        
    #Checks if the sign infront of the second term is a negative. If it is the number has its value reversed
    if array[1] == "-" and b > 0:
        b = -b
    elif array[1] == "-":
        c = -c
    
    #Adds the value of b to the array.
    coefficents.append(b)
    
    #Checks if there are 3 terms, if there are then it finds the value of c
    if terms == 3:
        c = int(array[4])
        if array[3] == "-":
            c = -c
    coefficents.append(c)

    return coefficents

#FINDS GCD BETWEEN TWO NUMBERS
def findCommonFactorTwo(numerator, denominator):
    if numerator < 0:
        numeratorNew = -numerator
    else:
        numeratorNew = numerator
        
    if denominator < 0:
        denominatorNew = -denominator
    else:
        denominatorNew = denominator
        
    if numeratorNew > denominatorNew:
        maximum = numeratorNew
        minimum = denominatorNew
    else:
        maximum = denominatorNew
        minimum = numeratorNew
        
    remainder = maximum%minimum
    
    while remainder > 0:
        maximum = minimum
        minimum = remainder
        remainder = maximum%minimum

    if numerator > 0:
        return minimum
    else:
        return -minimum
    
def findCommonFactorThree(coefficientA, coefficientB, coefficientC):

    #FINDS GCD OF GIVEN COEFFICIENTS
    GCDab = findCommonFactorTwo (coefficientA, coefficientB)
    GCDac = findCommonFactorTwo (coefficientA, coefficientC)
    GCDbc = findCommonFactorTwo (coefficientB, coefficientC)


    #FINDS THE GCD OF ALL PREVIOUS GCDS TO DETERMINE GREATEST COMMON FACTOR
    GCD1 = findCommonFactorTwo (GCDab, GCDac)
    GCD2 = findCommonFactorTwo (GCDab, GCDbc)
    GCD3 = findCommonFactorTwo (GCDac, GCDbc)

    commonFactor = min(GCD1, GCD2, GCD3)

    return commonFactor

#USE THE QUADRATIC FORMULA TO FIND FACOTRS OF A TRINOMIAL
def useQuadraticFormula(coefficientA, coefficientB, coefficientC):
    a = coefficientA
    b = coefficientB
    c = coefficientC
    
    bSqrMinusFourAc = b**2 - 4*a*c
    if bSqrMinusFourAc < 0:
        return "Not factorable"
    else:
        sqrtTerm = sqrt(bSqrMinusFourAc)
        if sqrtTerm%1 == 0:
            numeratorA = -b + sqrtTerm
            numeratorB = -b - sqrtTerm
            denom = 2*a
            reducefractionA = findCommonFactorTwo(numeratorA, denom)                          
            reducefractionB = findCommonFactorTwo(numeratorB, denom)
            
            if reducefractionA < 0:
                reducefractionA = -reducefractionA
            if reducefractionB < 0:
                reducefractionB = -reducefractionB
            reducedNumA = round(numeratorA/reducefractionA)
            reducedDenomA = round(denom/reducefractionA)
            reducedNumB = round(numeratorB/reducefractionB)
            reducedDenomB = round(denom/reducefractionB)               

            #RETURNS THE FACTORS IN AN ARRAY
            factorTerms = [reducedDenomA, reducedNumA, reducedDenomB, reducedNumB]
            return factorTerms
        else:
            return "Not factorable"

def factorTrinomial (trinomial):
    array = createArray (trinomial)
    NumTerms = findNumTerms(array)
    coefficients = findCoefficients(array)

    #IF THE QUADRATIC EXPRESSION HAS THREE TERMS
    if NumTerms == 3:
        commonFactor = findCommonFactorThree(coefficients[0],coefficients[1],coefficients[2])
        newCoeA = coefficients[0]/commonFactor
        newCoeB = coefficients[1]/commonFactor
        newCoeC = coefficients[2]/commonFactor

        factors = useQuadraticFormula(newCoeA, newCoeB, newCoeC)

        #IF THE QUADRATIC TRINOMIAL CANNOT BE COMMON FACTORED FIRST
        if commonFactor == 1:
            commonFactor=""
        elif commonFactor == -1:
            commonFactor="-"
        else:
            commonFactor=str(commonFactor)
            
        if factors == "Not factorable":

        #IF THE QUADRATIC TRINOMIAL CANNOT BE FACTORED AT ALL
            if commonFactor == "" or commonFactor =="-":
                return "not factorable"
            
            #IF THE QUADRATIC TRINOMIAL CANNOT BE FACTORED FURTHUR AFTER COMMON FACTORING
            else:
                if newCoeA == 1:
                    aTerm="x^2"
                elif newCoeA == -1:
                    aTerm="-x^2"
                else:
                    aTerm=str(round(newCoeA))+"x^2"

                if newCoeB == 1:
                    bTerm="+x"
                elif newCoeB==-1:
                    bTerm="-x"
                elif newCoeB>0:
                    bTerm="+"+str(round(newCoeB))+"x"
                elif newCoeB<0:
                    bTerm=str(round(newCoeB))+"x"
                    
                if newCoeC > 0:
                    cTerm="+"+str(round(newCoeC))
                else:
                    cTerm=str(round(newCoeC))

                return commonFactor + "("+ aTerm + bTerm + cTerm + ")"
            
        #IF THE TRINOMIAL CAN BE FACTORED INTO TWO SETS OF BRACKETS 
        else:
                
            if factors[0]==1:
                aTerm="x"
            else:
                aTerm=str(factors[0])+"x"

            if factors[1]>0:
                bTerm="-"+str(factors[1])               
            elif factors[1]<0:
                lengthB = len(str(factors[1]))
                bTerm="+"+str(factors[1])[1:(lengthB)]

            if factors[2]==1:
                cTerm="x"
            else:
                cTerm=str(factors[2])+"x"

            if factors[3]>0:
                dTerm="-"+str(factors[3])               
            elif factors[3]<0:
                lengthD = len(str(factors[3]))
                dTerm= "+" + str(factors[3])[1:(lengthD)]
                
            #PERFECT SQUARE
            if factors[0]==factors[2] and factors[1]==factors[3]:
                return commonFactor+"("+aTerm+bTerm+")^2"
            #OTHER CASES
            else:
                return commonFactor+"("+aTerm+bTerm+")("+cTerm+dTerm+")"

    #IF THE QUADRATIC EXPRESSION HAS TWO TERMS
    elif NumTerms == 2:

        #IF THE BINOMIAL IS MISSING THE b-TERM
        if coefficients[1]==0:
            commonFactor = findCommonFactorTwo(coefficients[0],coefficients[2])
            newCoeA = coefficients[0]/commonFactor
            newCoeC = coefficients[2]/commonFactor
            factors = useQuadraticFormula(newCoeA, 0, newCoeC)
            if commonFactor == 1:
                commonFactor=""
            elif commonFactor==-1:
                commonFactor="-"
            else:
                commonFactor=str(commonFactor)

            #COMMON FACTOR ONLY
            if factors=="Not factorable":
                if commonFactor != "" and commonFactor != "-":

                    if newCoeA == 1:
                        aTerm="x^2"
                    else:
                        aTerm=str(round(newCoeA))+"x^2"
                        
                    if newCoeC > 0:
                        cTerm="+"+str(round(newCoeC))
                    else:
                        cTerm=str(round(newCoeC))
                        
                    return commonFactor+"("+aTerm+cTerm+")"
                
                else:
                    return "not factorable"
                
            #DIFFERENCE OF SQUARES
            else:
                if factors[0] == 1:
                    aTerm= "x"
                elif factors[0] == -1:
                    aTerm= "-x"
                else:
                    aTerm= str(round(factors[0])) + "x"
                    
                if factors[1]>0:
                    bTerm=str(factors[1])
                    
                elif factors[1]<0:
                    lengthB = len(str(factors[1]))
                    bTerm=str(factors[1])[1:(lengthB)]

                return commonFactor + "(" + aTerm + "-"+bTerm + ")" + "(" + aTerm + "+"+bTerm + ")"
                    
        #IF THE BINOMIAL IS MISSING A c-TERM
        elif coefficients[2]==0:
                commonFactor = findCommonFactorTwo (coefficients[0],coefficients[1])
                newCoeA= coefficients[0]/commonFactor
                newCoeB= coefficients[1]/commonFactor

                if commonFactor == 1:
                    commonFactor=""
                elif commonFactor==-1:
                    commonFactor="-"
                else:
                    commonFactor=str(commonFactor)

                if newCoeA==1:
                    newCoeA=""
                else:
                    newCoeA=str(round(newCoeA))

                return commonFactor + "x(" + newCoeA+"x+" + str(round(newCoeB))+ ")"                
