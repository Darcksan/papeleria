__author__ = 'Juan Carlos Meza'

from memoria_Dinamica import *
papeleria = ['lapiz','boligrafo','libreta']
Precios = ['$5','$7','$10']
MateriaPrima = ['madera','Agua','alambre']

listas = memDinamica(papeleria)
listas.imprimirLista()
listas.agregarelementoarray('regla')
listas.imprimirLista()
listas.agregarelementoarray('goma')
listas.imprimirLista()
listas.imprimirLista()
listas.imprimirLista()


listas1 = memDinamica(Precios)
listas1.imprimirLista()
listas1.agregarelementoarray('$12')
listas1.imprimirLista()

listas2 = memDinamica(MateriaPrima)
listas2.imprimirLista()
listas2.agregarelementoarray('Mano de Obra')
listas2.imprimirLista()
listas2.imprimirLista()
listas2.imprimirLista()


