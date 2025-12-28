import sys,os
def bad_function (  x ,  y ):
    result = x+y
    if (result>10):
        return True
    else:
        return False
class bad_class:
    def __init__(self,name):
        self.name=name
    def get_name(self):
        return self.name
def another_badly_formatted_function():
    a=1
    b=2
    c=3
    d=4
    e=5
    return a+b+c+d+e
DATA=[1,2,3,4,5]
for item in DATA:
    print(item)