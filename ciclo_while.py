import calendar

def buscar_mes(año, mes):
    # Creamos un calendario para el mes y año especificados
    calendario = calendar.monthcalendar(año, mes)

    # Imprimimos el calendario
    print(calendar.month_name[mes], año)
    print("Lun Mar Mié Jue Vie Sáb Dom")
    for semana in calendario:
        for día in semana:
            if día == 0:
                print("  ", end="")
            else:
                print(f"{día:2}", end=" ")
        print()

def main():
    # Pedimos al usuario que ingrese el año y mes
    año = int(input("Ingrese el año: "))
    mes = int(input("Ingrese el mes (1-12): "))

    # Buscamos el mes
    buscar_mes(año, mes)

if __name__ == "__main__":
    main()
