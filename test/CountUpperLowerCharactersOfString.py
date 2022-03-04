str1="Welcome To Automation"
lower=0
upper=0
for i in str1:
    if i.islower():
        lower +=1
    elif i.isupper():
        upper +=1

print("total uppercase letters:",upper)
print("total lowercase letters:",lower)