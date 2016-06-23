import turtle
numero= int(input("Ingrese un número IMPAR: "))
t=turtle.Pen()

for i in range (1,numero+1):
	v=(180-(90+90)/numero)

	t.forward(100)
	t.left(v)
turtle.getscreen()._root.mainloop()