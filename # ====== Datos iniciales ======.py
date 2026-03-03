# ====== variables iniciales ======

saldo = 1000000
efectivo_cajero = 10000000
limte_diario = 2000000
PIN_USUARIO = 1234
retirado_hoy = 0
movimientos = []

#====== Funciones ======
def verificar_pin():
    intentos = 3
    while intentos >= 0:
        pin = input("ingrese su pin: ")
        if pin == PIN_USUARIO : 
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
        movimientos.append(f"retirar dinero: {cantidad}")
        return saldo

def retiro_rapido(saldo, cantidad, efectivo_cajero, limite_diario, retirado_hoy):

    opciones = [100000, 300000, 500000, 800000, 1000000]
    print("retiro rapido")
    print("opociones:", opciones)

    cantidad = int(input("seleccione el monto a retirar: "))

    if cantidad <= 0:
        print("monto invalido")
        return saldo, efectivo_cajero, retirado_hoy 
        
    
    elif cantidad > saldo:
        print("saldo insuficiente")
        return saldo, efectivo_cajero, retirado_hoy 
        

    elif cantidad > efectivo_cajero:
        print("cajero sin efectivo suficiente")
        return saldo, efectivo_cajero, retirado_hoy
        

    elif retirado_hoy + cantidad > limite_diario:
        print("supera el limite diario")
        return saldo, efectivo_cajero, retirado_hoy
        
   
    saldo -= cantidad
    efectivo_cajero -= cantidad
    retirado_hoy  += cantidad
    movimientos.append(f"retiro rapido: {cantidad}")
    print("retiro rapido exitoso")
    return saldo, efectivo_cajero, retirado_hoy
    
   
def depositar_saldo(saldo):
    cantidad= float(input("ingrese cantidad a depositar:"))
    if cantidad <= 0:
        print("cantidad invalida")
    else:
        saldo += cantidad
        print("deposito exitoso")
        print(f"su nuevo saldo es: ${saldo}")
        movimientos.append(f"deposito; {cantidad}")
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

def otros_movientos():
    global PIN_USUARIO
    print("otros movientos")
    print("1. cambiar PIN")
    print("2. volver")

    opcion = input("seleccione una opcion: ")

    if opcion == "1":
        pin_actual = input("ingrese su PIN actual: ")

        if pin_actual != PIN_USUARIO:
            print("PIN incorrecto, si ha olvidado su pin contacte a su banco o dirijase a una sucursal")
            return
        
        nuevo_pin = input("Ingrese el nuevo PIN (4 digitos)")

        if not nuevo_pin.isdigit() or len(nuevo_pin) != 4:
            print("el PIN debe tener exactamente 4 digitos")
            return
        
        confirmar_pin = input("confirme el nuevo PIN: ")

        if nuevo_pin != confirmar_pin:
            print("los PIN no coinciden")
            return
        
        PIN_USUARIO = nuevo_pin
        movimientos.append("camvio de PIN")
        print("PIN cambiado exitosa mente")
    
    elif opcion == "2":
        return
    else:
        print("opcion invalida")
 
def mostrar_menu():
    print("\n=====menu=====")
    print("1.consultar saldo")
    print("2.retirar dinero")
    print("3.retiro rapido")
    print("4.depositar saldo")
    print("5.transferir")
    print("6.pagar servicio")
    print("7.consultar movimientos")
    print("8.otros movimientos")
    print("9.salir")
    

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
             retiro_rapido()
         elif opcion == "4":
             depositar_saldo()
         elif opcion =="5":
             transferir()
         elif opcion == "6":
             pagar_servicio()
         elif opcion == "7":
             consultar_movimientos
         elif opcion == "8":
             otros_movientos()
         elif opcion == "9":
             print("gracias por usar el cajero")
             break
         else:
             print("opcion invalida intente de nuevo")
             

         
             



          
 








    
