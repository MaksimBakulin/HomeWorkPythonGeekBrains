import input_output as io
def Sum(a, b, c, d, e):
    if b + d >= 0:
        symbol = "+"
    else:
        symbol = ""
    result = f"{a + c}{symbol}{b + d}{e}"
    io.Output(result)
def Subtraction(a, b, c, d, e):
    if b - d >= 0:
        symbol = "+"
    else:
        symbol = ""
    result = f"{a - c}{symbol}{b - d}{e}"
    io.Output(result)
def Division(a, b, c, d, e):
    if ((b * c) - (a * d)) / (c ** 2 + d ** 2) >= 0:
        symbol = "+"
    else:
        symbol = ""
    result = f"{((a * c) + (b + d)) / (c ** 2 + d ** 2)}{symbol}{((b * c) - (a * d)) / (c ** 2 + d ** 2)}{e}"
    io.Output(result)
def Multiplication(a, b, c, d, e):
    if ((b * c) + (a * d)) >= 0:
        symbol = "+"
    else:
        symbol = ""
    result = f"{(a * c) - (b * d)}{symbol}{((b * c) + (a * d))}{e}"
    io.Output(result)