from fastapi import FastAPI
app = FastAPI()

@app.post("/Calculator")
def calculator(num1:int,num2:int,operand:str):
    if operand == "+":
        return num1+num2
    elif operand == "-":
        return num1-num2
    elif operand == "*":
        return num1*num2
    elif operand == "/":
        return num1/num2
    else:
        return {"Фича всё ещё в разработке"}