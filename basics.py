myname="Dev"
myage=16
print(myname)
print(myage)

myfriendlist=["nand","shiv","manthan"]
#myfriendlist[2]
#print(myfriendlist[2])
for friend in myfriendlist:
    print(friend)

count=6
while(count>=2):
    print(count)
    count=count-1

pocketmoney=input("enter the pocketmoney you get:")
print(pocketmoney)

age = int(input("Enteryour age: ")) 
if (age>18): 
    print("You are an adult. You can vote!")
elif (age>12): 
    print("You are a teenager and a rebel!")
else:
    print("You are still a kid. There is so much in the world for you to see.")

