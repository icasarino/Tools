from pwn import *

r = remote('''<host>''', '''<port>''')

line = ""
while True:
	line = r.recvline()
	print(line)
	
	'''
		Codigo/proceso a enviar
	'''
	
	rf = '''payload a enviar'''
	
	r.sendline(str(rf))


#r.interactive() -> Descomentar para iniciar sesion interactiva


