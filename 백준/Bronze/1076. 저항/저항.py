
color = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
one = input()
two = input()
three = input()
register = ((color.index(one) * 10) + color.index(two)) * (10 ** color.index(three))
print(register)