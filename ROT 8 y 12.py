##Nicolás Gómez - Javiera Riveros
def cifrado(palabra,clave):
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    secret = "".join([abc[(abc.find(c)+clave)%26] for c in palabra])
    return secret

def descifrado(palabra,clave):
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    secret = "".join([abc[(abc.find(c)-clave)%26] for c in palabra])
    return secret

mensaje='Hola'.upper()
Cifrar=cifrado(mensaje,8)
Descifrar=descifrado(Cifrar, 8)
print("Cifrado con Rot 8:",Cifrar)
print("Mensaje original:",Descifrar)

mensaje1='Adios'.upper()
Cifrar1=cifrado(mensaje1,12)
Descifrar1=descifrado(Cifrar1, 12)
print("\nCifrado con Rot 12:",Cifrar1)
print ("Mensaje original:",Descifrar1)

