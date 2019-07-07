import  os
ret=os.path.abspath(__file__)
print(ret)
ret2=os.path.dirname(ret)
print(ret2)
ret3=os.path.join(ret2,"hello")
print(ret3)