#dictionary

birthday={
    "bharath":"29-05-2007",
    "manvith":"18-06-2013",
    "lalitha":"17-06-1988"
}

print(birthday)
print(type(birthday))
print(len(birthday))
print(birthday.keys())
print(birthday.items())
print(birthday.values())
print(birthday.get("manjunath","notfound"))
birthday["manjunath"]="02-02-1985"
print(birthday)