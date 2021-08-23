def main():
    # Escribe tu código abajo de esta línea
    horas= int(input('Introduce las horas: '))
    horasseg = horas*3600
    minutos = int(input('Introduce los minutos: '))
    minutosseg= minutos*60
    segundos = int(input('Introduce los segundos: '))
    proceso1= horasseg+minutosseg+segundos
    horas2= int(input('Introduce las horas: '))
    horasseg2 = horas2*3600
    minutos2 = int(input('Introduce los minutos: '))
    minutosseg2= minutos2*60
    segundos2 = int(input('Introduce los segundos: '))
    proceso2= horasseg2+minutosseg2+segundos2
    print('proceso 1: ')
    print('proceso 2: ')

if __name__ == '__main__':
    main()
