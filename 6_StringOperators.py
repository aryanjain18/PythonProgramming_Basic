#Concatenation +
x = "Aryan"
y = "Jain"
print(x+y)
print(x+" "+y)

#Repetition *
print(x*3)

#Slicing / Range Slicing [LL:UL]
x = "banana"
z = x[2] #Index{0,1,2,3...}; Index 2 = 3rd Character
print(z)
z = x[2:4] #Print from 3rd To 5th Posn.
print(z)
z = x[:3] #Print from 1st To 4th Posn.
print(z)
z = x[2:] #Print from 3rd To Last Posn.
print(z)

# %s & Its Uses.
name = "Aryan Jain"
print("Hello! My Name Is %s" %name) #This Is A Sinle Statement Printed
# %s = PlaceHolder
print("Hello My Name Is ", name) #This Is A LIST OF 2 Statements. ie Printed
