def say_hello(name=None):
    if name is None:
        print("Hello World")
    else:
        return f"hello,{name}"
say_hello("sindhu")