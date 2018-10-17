__author_='Juan Carlos Meza'
class memDinamica:
    __listas=[]
    def __init__(self, list):
        self.__listas=list

    def agregarelementoarray(self,elemento):
        self.__listas.append(elemento)

    def imprimirLista(self):
        print(self.__listas)

