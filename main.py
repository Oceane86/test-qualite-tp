
class MathOperations:

    def addition(a, b):
        return a + b
    
    def division(a, b):
        if b == 0:
           raise ValueError("Division par zéro impossible")
        return a / b

    
    def soustraction(a,b):
        return a - b
    
    def multiplication(a,b):
        return a * b
    
    def power(base, exponent):
        if exponent >= 0:
            return base ** exponent
        else:
            return 1 / (base ** abs(exponent))
        


        
    def modulo(a, b):
        if b != 0:
            return a % b
        else:
            raise ValueError("Modulo by zero is undefined")
        
