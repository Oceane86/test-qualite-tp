# mon_code.py

def addition(a, b):
        """Fonction pour additionner deux nombres."""
        return a + b

def soustraction(a, b):
        """Fonction pour soustraire deux nombres."""
        return a - b

def multiplication(a, b):
        """Fonction pour multiplier deux nombres."""
        return a * b

def division(a, b):
        """Fonction pour diviser deux nombres."""
        if b != 0:
            return a / b
        else:
            raise ValueError("Division par zéro impossible")
