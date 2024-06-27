from Models import *
from DAO import *
from datetime import datetime

class ControllerCategoria:
    def cadastraCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True

        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print("Nova categoria cadastrada com sucesso")
        else:
            print("Essa categoria ja existe")

a = ControllerCategoria()
a.cadastraCategoria('geladinho')