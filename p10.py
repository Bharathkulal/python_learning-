
cities = ["bidkalkatte","manglore","udupi","benglore","mysore"]
for city in cities:
    print(city)




for i in range(1,11):
    print(i)

num =[11,22,33,44,55,66,77,88,99]
for index,i in enumerate(num):
    print(f"{i} is in {index}th index")


for i in range(0,20,2):
    print(i,end="  " )

name = "bharath"
for letter in name:
    print(letter*2)
  
#tables

for i in range(1,11):
    print(f"2X{i}={2*1}")


for i in range(1,11):
    for j in range(1,11):
        print(f"{i}X{j}={i*j}")