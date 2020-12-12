import re
import os


def n_float(numero):
    """
    Comprueba si un valor ingresado es float, además de ello realiza
    la conversión
    """
    try:
        n = float(numero)
        return n
    except:
        numero = input('Valor ingresado no admitido, por favor volver a ingresar un valor: ')
        n_float(numero)

def ingreso_vendedores(vendedores=[]):
    """
    Permite el registro de vendedores
    """
    vendedor ={
        'nombre':'',
        'ventas':[]
    }
    # validando ingreso
    vendedor['nombre'] = input('ingrese nombre del vendedor: ')
    print('por favor ingrese las 5 ventas realizadas por el vendedor')
    
    vendedor['ventas'] = []
    for v in range(5):
        venta  = input(f'Ingrese la venta {v+1}:')
        venta = n_float(venta)
        vendedor['ventas'].append(venta)
    vendedores.append(vendedor)
    
    # valido ingreso de más vendedores
    respuesta = input('Desea seguir ingresando más vendedores? (y/n) ')
    
    if respuesta.lower() == 'n':
        print('Se realizó el registro de todos los vendedores!')
        return vendedores
    return ingreso_vendedores(vendedores)

def eval_vendedor(vendedores):
    """
    Realiza la evaluación de las ventas realizadas por los vendedores, según:

    vendedores comisión: Ventas mayores o iguales a 10000

    vendedores sin comisión: Ventas menores a 10000
    """
    comision = []
    no_comision = []
    for vendedor in vendedores:
        monto = sum(vendedor['ventas'])
        
        if monto >= 10**4:
            comision.append(vendedor['nombre'])
            continue
        no_comision.append(vendedor['nombre'])
    print('Los siguiente vendedores NO alcanzaron la cuota para la comisión: ')
    print(no_comision)
    
    print('Los siguiente vendedores alcanzaron la cuota para la comisión: ')
    print(comision)
    
def promedio_venta(vendedores):
    """
    Retorna las ventas total promedio
    """
    prom_total=0
    for vendedor in vendedores:
        vendedor['promedio'] = sum(vendedor['ventas'])/5
        prom_total = sum(vendedor['ventas'])
    
    print(f'El promedio de ventas total es: {prom_total/len(vendedores)}')

def min_max_prom(vendedores):
    """
    Retorna el valor mínimo y máximo de ventas promedio de un listado de vendedores.
    """
    prom = []
    for vendedor in vendedores:
        prom.append(vendedor['promedio'])
    
    min_p = min(prom)
    max_p = max(prom)
    min_n =[]
    max_n = []
    for vendedor in vendedores:
        if vendedor['promedio'] == min_p:
            min_n.append(vendedor['nombre'])
        elif vendedor['promedio'] == max_p:
            max_n.append(vendedor['nombre'])
    
    print(f'El promedio mínimo de ventas por vendedor fue de {min_p}, que pertenece a {min_n}')
    print(f'El promedio mínimo de ventas por vendedor fue de {max_p}, que pertenece a {max_n}')
    
def busqueda_nombre(nombre_b):
    """
    docstring
    """
    coincidencias = []
    for vendedor in vendedores:
        if nombre_b.lower() in vendedor['nombre'].lower():
            coincidencias.append(vendedor)
    print(f'Se encontraron las siguientes coincidencias para {nombre_b}')
    print(coincidencias)

if __name__ == "__main__":
    # Pregunta 1: registro vendedores
    vendedores = ingreso_vendedores()

    os.system('cls')

    for v in vendedores:
        print(v)
    print('\n\n')

    # Pregunta 2: alcanzaron comisión
    print('Calculando los vendedores que alcanzaron comisión...')
    eval_vendedor(vendedores)

    print('\n\n')

    # Pregunta 3: promedio de ventas total
    print('Calculando el promedio de ventas total...')
    promedio_venta(vendedores)
    print('\n\n')

    # Pregunta 4: promedio de venta más alto y más bajo
    print('Calculando el promedio de ventas mínimo y máximo ... ')
    min_max_prom(vendedores)

    print('\n\n')

    # Pregunta 5: Búsqueda vendedor
    nombre_b = input("Ingrese el nomnre del vendedor a buscar: ")
    busqueda_nombre(nombre_b)

