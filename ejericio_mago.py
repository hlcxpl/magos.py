# Definir los datos
nombres = [
    "Harry Houdini",
    "Newton",
    "David Blaine",
    "Hawking",
    "Messi",
    "Teller",
    "Einstein",
    "Pele",
    "Juanes",
]

magos = ["Harry Houdini", "David Blaine", "Teller"]
cientificos = ["Newton", "Hawking", "Einstein"]


def hacer_grandioso(magos):
    return [f"El gran {mago}" for mago in magos]


def filtrar_nombres():
    magos_grandiosos = hacer_grandioso(magos)
    otros = [
        nombre
        for nombre in nombres
        if nombre not in magos and nombre not in cientificos
    ]
    return nombres, magos_grandiosos, cientificos, otros


def imprimir_lista(titulo, lista):
    print(f"\n{titulo}")
    print("-" * len(titulo))
    for item in lista:
        print(item)


nombres_completos, magos_grandiosos, cientificos_lista, otros = filtrar_nombres()


imprimir_lista("Lista Completa de Nombres", nombres_completos)
imprimir_lista("Magos Grandiosos", magos_grandiosos)
imprimir_lista("Científicos", cientificos_lista)
imprimir_lista("Otros", otros)
