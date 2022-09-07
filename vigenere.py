##Nicolás Gómez - Javiera Riveros
alfabeto = "abcdefghijklmnopqrstuvwxyz "
indexado1 = dict(zip(alfabeto, range(len(alfabeto))))
indexado2 = dict(zip(range(len(alfabeto)), alfabeto))


def encriptado(mensaje, passw):
    encriptado = ""
    mensaje_separado = [
        mensaje[i : i + len(passw)] for i in range(0, len(mensaje), len(passw))
    ]

    for separacion in mensaje_separado:
        i = 0
        for letra in separacion:
            numero = (indexado1[letra] + indexado1[passw[i]]) % len(alfabeto)
            encriptado += indexado2[numero]
            i += 1

    return encriptado


def desencriptado(cifrado, passw):
    desencriptado = ""
    encriptación_separada = [
        cifrado[i : i + len(passw)] for i in range(0, len(cifrado), len(passw))
    ]

    for separacion in encriptación_separada:
        i = 0
        for letra in separacion:
            numero = (indexado1[letra] - indexado1[passw[i]]) % len(alfabeto)
            desencriptado += indexado2[numero]
            i += 1

    return desencriptado


def main():
    mensaje = "hola"
    passw = "heropassword"
    msj_encriptado = encriptado(mensaje, passw)
    msj_desencriptado = desencriptado(msj_encriptado, passw)

    print("Mensaje Original: " + mensaje)
    print("Mensaje Encriptado: " + msj_encriptado)
    print("Mensaje Descencriptado: " + msj_desencriptado)


main()
