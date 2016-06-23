import time

for t in range(0,500):
	t = time.localtime()
	hora = t[3]
	minutos = t[4]
	segundos = t[5]
	print((hora),":"+str(minutos),":"+str(segundos))
	time.sleep(1)
	
