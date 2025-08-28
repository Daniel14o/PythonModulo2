def consola(comando: str) -> str:
    """
    Desarrolla un programa que simule un menú de consola usando la estructura match-case. El programa mostrará una lista de comandos
     disponibles ("guardar", "cargar", "salir") y el usuario ingresará uno

    Comandos válidos:
    - "Imprimir": retorna "Guardando archivo..."
    - "Si el comando no es valido" retorna "Mostrar mensaje de error"..."
    - "salir": retorna "Saliendo del programa..."

    Parametros:
        comando (str): texto del comando.

	Conceptos aplicados: Bucle while, match-case, input(), lower().

    Retorna:
        str: Mensaje de resultado de la acción.
    """
    match comando.lower():
        case "Imprimir":
            return "Imprimiendo archivo..."
        case "Mostrar":
            return "Mostrando archivo..."
        case "Salir":
            return "Saliendo del programa..."
        case _:
            return "Comando no reconocido."


if __name__ == "__main__":
    while True:
        mensaje = input("Ingrese un comando (Imprimir/Mostrar/Salir): ").strip().lower().replace(" ","")
        resultado = consola(mensaje)
        print(resultado)
        if mensaje == "salir":
            break