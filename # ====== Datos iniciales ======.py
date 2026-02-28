# ====== Datos iniciales ======

saldo = 0
pin_correcto:1234
movimientos = []

#====== Funciones ======
def verificar_pin():
    intentos = 3
    while intentos >= 0:
        pin = input("ingrese su pin: ")
        if pin == pin_correcto : 
            print("pin correcto\n")  
            return True
        else:
            intentos -= 1
            print(f"pin incorrecto. intentos restantes:{intentos}")

    return False


def consultar_saldo(saldo):
    print("su saldo actual es: {saldo}")
    return saldo

def retirar_dinero(saldo):
    cantidad = float(input("ingrese cantidad a retirar: "))
    if cantidad <= 0:
        print("cantidad invalida")
    elif cantidad > saldo:
        print("fondos insuficientes")
    else:
        saldo -= cantidad
        print("retiro exitoso")
        print("su nuevo saldo es $: {saldo}")
        return saldo
    
def depositar_saldo(saldo):
    cantidad= float("ingrese cantidad a depositar:")
    if cantidad <= 0:
        print("cantidad invalida")
    else:
        saldo += cantidad
        print("deposito exitoso")
        print(f"su nuevo saldo es: ${saldo}")
        return saldo

def transferir():
    global saldo
    cuenta_destino = input("Ingrese número de cuenta destino: ")
    cantidad = float(input("Ingrese monto a transferir: "))

    if cantidad <= 0:
        print(" Cantidad inválida.")
    elif cantidad > saldo:
        print("Fondos insuficientes.")
    else:
        saldo -= cantidad
        print(f"tansferencia realizada a la cuenta {cuenta_destino}")
        movimientos.append(f"Transferencia a {cuenta_destino}: -${cantidad}")

def pagar_servicio():
    global saldo
    servicio = input("Ingrese nombre del servicio (agua, luz, internet): ")
    cantidad = float(input("Ingrese monto a pagar: "))

    if cantidad <= 0:
        print("Cantidad inválida.")
    elif cantidad > saldo:
        print(" Fondos insuficientes.")
    else:
        saldo -= cantidad
        print(f"Pago de {servicio} realizado.")
        movimientos.append(f"Pago de {servicio}: -${cantidad}")


def consultar_movimientos():
    print("\n Historial de Movimientos:")
    if not movimientos:
        print("No hay movimientos registrados.")
    else:
        for mov in movimientos:
            print("-", mov)




def mostrar_menu():
    print("\n=====menu=====")
    print("1.consultar saldo")
    print("2. retirar dinero")
    print("3.depositar saldo")
    print("4.transferir")
    print("5.pagar servicio")
    print("6.consultar movimientos")
    print("7.salir")

#======programa inicial ======
def cajero():
    global saldo


    print("=====bienvenido al cajero automatico=====\n")

    if not verificar_pin():
        print("tarjeta bloqueada")
        return 


    while True:
         mostrar_menu()
         opcion=input("selecione una opcion: ")


         if opcion == "1":
             consultar_saldo()
         elif opcion == "2":
             retirar_dinero()
         elif opcion == "3":
             depositar_saldo()
         elif opcion =="4":
             transferir()
         elif opcion == "5":
             pagar_servicio()
         elif opcion == "6":
             consultar_movimientos

         
             



          
 








    
