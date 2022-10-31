name = "Mary"
age = 18
s1 = "My sister " + name + "got married at the age of " + str(age) + "."
s2 = "My sister {0} got married at the age of {1}".format(name, age)
s3 = "My sister {sister} got married at the age of {old}.".format(sister=name, old=age)
s4 = f"My sister {name} got maried at the age of {age}."
print(s1)
print(s2)
print(s3)
print(s4)