def m_c_d(a, b):
    While (a%b !=0):
        a2 = a
        b2 = b

        a = b2
        b = a2 % b2
     return n

class Fraction:
    def _init_( self, numerator, denominator):
        self.num = numerator
        self.den = denominator
    

    def show(self):
        print(self.num,"/", self.den)
    

    def _add_(self, fraction2):
        newNum = self.num*fraction2.den + self.den*fraction2.num
        newDen = self.den*fraction2.den
        common = m_c_d(newNum, newDen)
        return Fraction(newNum //common, newDen//common)
    
    def resta(self, fraction2):
        newNum = self.num*fraction2.den - self.den*fraction2.num
        newDen = self.den*fraction2.den
        common = m_c_d(newNum, newDen)
        return Fraction(newNum //common, newDen//common)
    

    def multiplicacion (self, otra):
        newNum = self.num* otra.num
        newDen = self.den * otra.den
        return Fraction(newNum, newDen)

    def dividir (self, otra):
        newNum = self.num * otra.den
        newDen = self.den * otra.num
        return Fraction(newNum, newDen)

    numerador1 = input("Ingrese el numerador de la primera fraccion: ")
    denominador1 = input("Ingrese el numerador de la primera fraccion: ")
    f1 = Fraction ( numerador1, denominador1)
    numerador2 = input("Ingrese el numerador de la segunda fraccion: ")
    denominador2 = input("Ingrese el numerador de la segunda fraccion: ")
    f2 = Fraction ( numerador2, denominador2)
    f3 = f1 + f2
    f4 = resta(f1,f2)
    f5 = multiplicacion(f1, f2)
    f6 = dividir(f1,f2)
    f3.show()
    f4.show()
    f5.show()
    f6.show()
    
