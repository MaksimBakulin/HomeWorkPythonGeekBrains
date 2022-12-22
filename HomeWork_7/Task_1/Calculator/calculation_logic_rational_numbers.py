import input_output as io
import logging as log
def Sum(a, b):
    c = a + b
    io.Output(c)
    log.Logging_rational(a, "+", b, c)
def Subtraction(a, b):
    c = a - b
    io.Output(c)
    log.Logging_rational(a, "-", b, c)
def Division(a, b):
    c = a / b
    io.Output(c)
    log.Logging_rational(a, "/", b, c)
def Multiplication(a, b):
    c = a * b
    io.Output(c)
    log.Logging_rational(a, "*", b, c)