# Programa que describe una boleta de pago para un trabajador mediante POO
# Se basa en descuentos al salario bruto del mes por renta, fonavi y afp
# Se toman en cuenta las horas extras realizadas al mes

class Trabajador():
    
    def __init__(self, nombre):
        self.nombre = nombre

    def pagos(self, hextra, turno):   
        if turno == "diurno":
            return hextra * 10
        elif turno == "nocturno":
            return hextra * 15
        else:
            print("turno no se acepta")

    def descuento(self, sueldo):    
        renta = sueldo * 0.1
        fonavi = sueldo * 0.07
        afp = sueldo * 0.03
        return sueldo - renta - fonavi - afp 


trabajador = Trabajador(input("Ingrese nombre del trabajador: "))

extra = trabajador.pagos(int(input("Ingrese las horas extras: ")), input("Indique si el turno es diurno/nocturno: "))

descuentos = trabajador.descuento(float(input("Ingrese el sueldo bruto por mes: ")))

print("El salario neto es de:", descuentos+float(extra))       