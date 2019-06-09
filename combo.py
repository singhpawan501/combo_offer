import random as r
import string as s
f=open('combo.csv','w')
f.write("product_name,price\n")
for i in range(1,100):
    rand1=r.sample(s.ascii_letters,6)
    rand1=''.join(rand1)
    rand=r.randint(40,250)
    f.write(rand1)
    f.write(",")
    f.write(str(rand))
    f.write(",")
    f.write("\n")
print("writing in to combo.csv file has been DONE!")    
