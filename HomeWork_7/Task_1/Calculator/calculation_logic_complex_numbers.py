import input_output as io
import logging as log
def Sum(a, b, c, d, e):
    if b + d >= 0:
        symbol = "+"
    else:
        symbol = ""
    result = f"{a + c}{symbol}{b + d}{e}"
    io.Output(result)
    log.Logging_complex(a, b, c, d, e, "+", result)
def Subtraction(a, b, c, d, e):
    if b - d >= 0:
        symbol = "+"
    else:
        symbol = ""
    result = f"{a - c}{symbol}{b - d}{e}"
    io.Output(result)
    log.Logging_complex(a, b, c, d, e, "-", result)
def Division(a, b, c, d, e):
    if ((b * c) - (a * d)) / (c ** 2 + d ** 2) >= 0:
        symbol = "+"
    else:
        symbol = ""
    result = f"{((a * c) + (b + d)) / (c ** 2 + d ** 2)}{symbol}{((b * c) - (a * d)) / (c ** 2 + d ** 2)}{e}"
    io.Output(result)
    log.Logging_complex(a, b, c, d, e, "/", result)
def Multiplication(a, b, c, d, e):
    if ((b * c) + (a * d)) >= 0:
        symbol = "+"
    else:
        symbol = ""
    result = f"{(a * c) - (b * d)}{symbol}{((b * c) + (a * d))}{e}"
    io.Output(result)
    log.Logging_complex(a, b, c, d, e, "*", result)