from __future__ import  absolute_import
from Qshop.celery import app
@app.task
def taskExample():
    print("I am task Example")
    return "I am task Example"

@app.task
def add(x,y):
    return x+y
