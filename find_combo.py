# a sample program for combo offer in which we passes a .csv file taht contains products name and price of tyhe produts
# and then we pass the lower range and upper range
# then find the lists of product and calculate the sum of price of corrosponding products
# and if it is lies between the lower and upper range then print the lists of products
import random as r
f=open('combo.csv','r') #give the file name that is .csv
dict1={}
list1=[]
list2=[]
combo_products=[]
x=0
for line in f:
    if x==0:
        x=x+1
        continue
    l=line.split(',')  #this is use to make list of string that present in  one line of .csv file
    list1.append(l[0]) #make a list for products name
    list2.append(l[1]) #make list for price
    dict1[l[0]]=l[1]   #make a dictonary of keys as product anme and value as price 
print("Enter the range that you want combo offer.")  
lower=int(input("Enter lower range:"))  
upper=int(input("Enter upper range:"))
for i in range(1,10):
    sum=0
    ran1=r.randint(2,5)   #take random number between 2 and 5
    ran2=r.sample(list1,ran1) #make list of random products between 2 and 5
    print(ran2)
    for i in ran2:
        sum=sum+int(dict1[i]) #calculate the sum of price 
    if sum<=upper and sum>=lower : 
        for i in range(1,2):
            combo_products.append(ran2) #make a list of product that sum lies between lower and upper limit
print("combo products name between ",lower," and ",upper," are :")
for i in combo_products:
    print(i,"\n")      #use to print the lists of products that have price range between lower and upper    
print("\n........... THANKS FOR SEARCHING COMBO OFFER............. ")            
f.close()    