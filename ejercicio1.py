# Ejercicio 1:
from datetime import datetime, timedelta

class Fecha:
    def __init__(self, dd=None, mm=None, aaaa=None):
        if (dd is None and mm is None and aaaa is None):
            fecha_hoy = datetime.datetime.now()
            dd = fecha_hoy.day
            mm = fecha_hoy.month
            aaaa = fecha_hoy.year
            self.fecha = datetime.datetime(aaaa, mm, dd)
        else:
            self.fecha = datetime.datetime(aaaa, mm, dd)

    def calcular_dif_fecha(self, dd, mm, aaaa):
        fecha2 = datetime.datetime(aaaa, mm, dd)
        diferencia = fecha2 - self.fecha
        return(f"{diferencia.days} días")

    def __str__(self):
        return self.fecha.strftime("%d/%m/%Y")

    def __add__(self, days):
        nueva_fecha = self.fecha + datetime.timedelta(days=days)
        return Fecha(nueva_fecha.day, nueva_fecha.month, nueva_fecha.year)

    def __eq__(self, other):
        return self.fecha == other.fecha


# Ejercicio 2:
class Alumno():
    def __init__(self, Nombre:str, DNI:int, FechaIngreso:datetime, Carrera):
        self.datos = {
            "Nombre":Nombre,
            "DNI":DNI,
            "Fecha de Ingreso":FechaIngreso,
            "Carrera":Carrera
        }

    def cambiar(self, Nombre=None, DNI=None, FechaIngreso=None, Carrera=None):
        if Nombre is not None:
            self.datos['Nombre'] = Nombre
        if DNI is not None:
            self.datos['DNI'] = DNI
        if FechaIngreso is not None:
            self.datos['Fecha de Ingreso'] = FechaIngreso
        if Carrera is not None:
            self.datos['Carrera'] = Carrera

    def antiguedad(self):
        fecha_actual = datetime.datetime.now()
        antiguedad = fecha_actual - self.datos['Fecha de Ingreso']
        return(antiguedad.days)

    def __str__(self):
        return f"{self.datos['Nombre']}, {self.datos['DNI']}, {self.datos['Carrera']}, {self.datos['Fecha de Ingreso'].strftime('%d-%m-%Y')}"
    
    def __eq__(self, other):
        return self.datos == other.datos
    

# Ejercicio 3:
import random

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada():
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.len = 0

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.primero is None:
            self.primero = self.ultimo = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.ultimo
            self.ultimo = nuevo_nodo
        self.len += 1

    def __iter__(self):
        valores = []
        current = self.primero
        while current:
            valores.append(current.valor)
            current = current.siguiente
        return iter(valores)

    def lista_ejemplo(self, cantidad):
        for _ in range(cantidad):
            Nombre = f"Alumno {random.randint(1, 100)}"
            DNI = random.randint(10000000, 45000000)
            FechaIngreso = datetime.now() - timedelta(days=random.randint(0, 365*4))
            Carrera = "Tec. en Programacion"

            alumno = Alumno(Nombre, DNI, FechaIngreso, Carrera)
            self.agregar(alumno)
        
        return self


# Ejercicio 4:
def ordenarLista(lista):
    if lista.len < 2:
        return lista # osea digamos ya estaria ordenada (y funciona de caso base)

    current = lista.primero
    while current.siguiente:
        siguiente = current.siguiente
        while siguiente:
            if current.valor.datos["Fecha de Ingreso"] > siguiente.valor.datos["Fecha de Ingreso"]:
                current.valor, siguiente.valor = siguiente.valor, current.valor
            siguiente = siguiente.siguiente
        current = current.siguiente
    
    return lista


# Ejercicio 5:
from pathlib import Path
import os

instancia = ListaDoblementeEnlazada()
lista_alumnos = instancia.lista_ejemplo(4)

path_actual = Path.cwd()
nuevo_path = path_actual / "nuevo_directorio"
nuevo_path.mkdir()

archivo = nuevo_path / "lista_alumnos.txt"
with open(archivo, 'w') as archivo:
    for alumno in lista_alumnos:
        archivo.write(f"{alumno}\n")

nuevo_path1 = path_actual / "nuevo_directorio2"
os.rename(nuevo_path, nuevo_path1)
