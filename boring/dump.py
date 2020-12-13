#backslash allows youy to seperate in lines a statement \
#lists are mutable => in function, args as a list are a reference to them, not a copy
def func(ls):
    ls[0]=1

ls = [10,20,30]
print(ls)
func(ls)
print(ls)