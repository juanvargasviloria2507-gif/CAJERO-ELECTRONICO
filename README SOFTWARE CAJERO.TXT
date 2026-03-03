# GUIA INSTALACION DE SOFTWARE CAJERO AUTOMATICO

este script simula el funcionamiento basico de un cajero

## INSTALACION DE PYTHON

si ya lo tienes instalado,no es necesario que lo instales otravez

```bash
sudo apt update
sudo apt install python3 python3-pip
```

---

### EJECUTA EN LA CONSOLA

en la consola ejecuta

```bash
python nombre_del_archivo.py
```

---

#### VARIABLES

* saldo = 1000000 <!-- saldo que tiene el cliente en su cuenta -->
* efectivo_cajero:10000000 <!-- Efectivo que tiene el cajero en su caja fuerte -->
* limte_diario:2000000 <!-- limite diario de transferencias  -->
* PIN_USUARIO:1234 <!-- pin del usario  -->
* retirado_hoy:0 <!-- numero de retiros hechos por el usario en el dia  -->
* movimientos = [] <!-- movimientos realizados dentro de la cuenta por el usuario -->

---

##### FUNCIONES

* *verificar saldo*

```python
def verificar_pin():
    intentos = 3
    while intentos > 0:
        pin = input("Ingrese su PIN: ")
        if pin == PIN_USUARIO:
            print("PIN correcto\n")
            return True
        else:
            intentos -= 1
            print(f"PIN incorrecto. Intentos restantes: {intentos}")
    return False
```

* *consultar saldo*

```python
def consultar_saldo():
    print(f"su saldo actual es: {saldo}")
    return saldo
```

* *retirar dinero*

```python
def retirar_dinero():
    global saldo
    cantidad = float(input("ingrese cantidad a retirar: "))
    if cantidad <= 0:
        print("cantidad invalida")
    elif cantidad > saldo:
        print("fondos insuficientes")
    else:
        saldo -= cantidad
        print("retiro exitoso")
        print(f"su nuevo saldo es $: {saldo}")
        movimientos.append(f"retiro: {cantidad}")
    return saldo
```

* *retiro rapido*

```python
def retiro_rapido():
    global saldo, efectivo_cajero, retirado_hoy
    opciones = [100000, 300000, 500000, 800000, 1000000]
    print("retiro rapido")
    print("opociones:", opciones)
    cantidad = int(input("seleccione el monto a retirar: "))
    if cantidad <= 0:
        print("monto invalido")
    elif cantidad > saldo:
        print("saldo insuficiente")
    elif cantidad > efectivo_cajero:
        print("cajero sin efectivo suficiente")
    elif retirado_hoy + cantidad > limite_diario:
        print("supera el limite diario")
    else:
        saldo -= cantidad
        efectivo_cajero -= cantidad
        retirado_hoy += cantidad
        movimientos.append(f"retiro rapido: {cantidad}")
        print("retiro rapido exitoso")
        print(f"su nuevo saldo es: {saldo}")
```

* *depositar saldo*

```python
def depositar_saldo(saldo):
    cantidad= float("ingrese cantidad a depositar:")
    if cantidad <= 0:
        print("cantidad invalida")
    else:
        saldo += cantidad
        print("deposito exitoso")
        print(f"su nuevo saldo es: ${saldo}")
        movimientos.append(f"deposito; {cantidad}")
        return saldo
```

* *transferir*

```python
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
```

* *pagar servicio*

```python
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
```

* *consultar movimientos*

```python
def consultar_movimientos():
    print("\n Historial de Movimientos:")
    if not movimientos:
        print("No hay movimientos registrados.")
    else:
        for mov in movimientos:
            print("-", mov)
```

* *otros movimientos*

```python
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
```

* *mostrar menu*

```python
def mostrar_menu():
    print("\n=====menu=====")
    print("1.consultar saldo")
    print("2.retirar dinero")
    print("3.retiro rapido")
    print("4.depositar saldo")
    print("5.transferir")
    print("6.pagar servicio")
    print("7.otros movimientos")
    print("8.otros movimientos")
    print("9.salir")
```

### Programa principal

```python
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
```
