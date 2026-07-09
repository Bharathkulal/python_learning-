print("hello world !")

#input output

boy_name=input("boy name : ")
boy_age=int(input("boy_age: "))

girl_name=input("girl name : ")
girl_age=int(input("girl age: "))
print(boy_name)
print(girl_name)
print(boy_age)
print(girl_age)
age_diff=abs(boy_age - girl_age )

print(boy_name + " loves " + girl_name) #normal concatenation

print(f"{boy_name}  loves  {girl_name} . age difference is :{age_diff}")