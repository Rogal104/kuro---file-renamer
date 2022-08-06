import os
import random
import string

print(r'''
  ...     _M_
 /( )\    ( )
/ / \ \  / : \
~~\%/~~  \|:|/
 /   \    |||
/,,,,,\   ||| 

''')

def rename(path, fyle):
    r = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    #print("losu, " + random)
    
    #check czy plik z takom nazwom istnieje juz
    if os.path.isfile(path[:-len(fyle)] + r + ".py"):
        print("ty ale juz jest taka nazwa: " + random)
        rename(path, fyle)
    os.rename(path, path[:-len(fyle)] + r + ".py")

def kuro(dyr):
    fyles = os.listdir(dyr)
    for fyle in fyles:
        path = os.path.join(dyr, fyle)
        if os.path.isfile(path):
            rename(path, fyle)
            #change name to random
        elif os.path.isdir(path):
            print("chuj")
            kuro(path)


dyr = "./slup/"
kuro(dyr)

