class calculator:
    def add(self,a,b):
        return a+b
    
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    
    def div(self,a,b):
        if b != 0 :
            return a/b
        else:
            return  "Error: Division by zero is undefined."
    def mod(self,a,b):
        return a//b

        if b != 0 :
            return a%b
        else:
            return  "Error: Division by zero is undefined."

    def __str__(self)   :
         return "Calculator with basic arithmetic operations."


if __name__ == "__main__":
    cal = calculator()
    try:    
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print(f"{num1} + {num2} = {cal.add(num1, num2)}")
        print(f"{num1} - {num2} = {cal.sub(num1, num2)}")
        print(f"{num1} * {num2} = {cal.mul(num1, num2)}")
        print(f"{num1} / {num2} = {cal.div(num1, num2)}")
        print(f"{num1} % {num2} = {cal.mod(num1, num2)}")

    except ValueError as e:
        print(e)
    except Exception as e:
        print("An unexpected error occurred:", e)