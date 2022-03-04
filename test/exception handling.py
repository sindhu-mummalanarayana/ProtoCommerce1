

try:
    a=5/0
except:
    print("exception handled")

#########Generic Exception Handling"###########
try:
    a = 5 / 0
except Exception as e:
    print(str(e)+" exception handled")

try:
    a = 5 / 0
except Exception as e:
    print(e.args[0]+" exception handled")

print("Hello World")


try:
    a = 5 / 0
except ZeroDivisionError:
    print("Zero Division error handled")
except Exception as e:
    print(str(e)+" exception handled")