from Models import *
from DAO import *
from datetime import datetime

class ControllerCategoria:
    def cadastraCategoria(self, novaCategoria):
        existe = False #se o negocio quer você quer colocar não existe
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria: #ira adicionar como nova categoria
                existe = True   #ai essa categoria vai existir

        if not existe:  #se ela não existir
            DaoCategoria.salvar(novaCategoria)
            print("Nova categoria cadastrada com sucesso")
        else: #se ela ja existi
            print("Essa categoria ja existe")

    def removerCategoria( Self, categoriaRemover):
        x = DaoCategoria.ler() #ler um arquivo la no arquivo Dao
        cat = list(filter(lambda x: x.categoria == categoriaRemover, x)) #ir atras do nome do produto/objeto que você digitou "que existe"

        if len(cat) <= 0:  #se o produtor não existir
            print( "A categoria que você deseja remover não existe")
        else:  #se existir
            for i in range(len(x)): # x = DaoCategoria ta escrito na linha 20
                if x[i]. categoria == categoriaRemover:  # i = um valor
                    del x[i] #del deve ser delete
                    break
        print ("categoria removida com sucesso")    

        with open('categoria.txt', 'w') as arq: #aq você alterou a lista deletando algo
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')

    def alterarCategoria(self, categoriaAlterar, categoriaAlterada): #categoria que você vai alterar "futuro" e categoria que foi alterada "presente"
        x = DaoCategoria.ler() # lendo a lista criada la na Dao 

        cat = list(filter(lambda x: x.catetegoria == categoriaAlterar, x)) #cat é = uma lista que você procura algo que existe (lambda)
        #o lambda vai confirmar (ele vai ver se o item existe) o item que você quer alterar e vai alterar (o X significa DaoCategoria que ta na linha 38)

        if len (cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == categoriaAlterada, x)) #cat1 é = uma lista que irar filtrar a categoria que você quer alterar
            if len (cat) == 0:
                x = list(map(lambda x: Categoria(categoriaAlterada) if(x.categoria == categoriaAlterar) else(x,x)))
        # a categoria que você vai alterar tem que ser = a categoria que você quer alterar, se não for, a categoria não vai ser alterada
            else:
                print("a categoria que deseja alterar ja existe, no caso teria 2 nomes iguais")
        else:
            print("a categoria que deseja alterar não existe")
            with open('categoria.txt', 'w') as arq: #abrimos o arquivo que iremos alterar e reescrevemos as coisas que mudamos
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')

a = ControllerCategoria()
a.removerCategoria() #colocar o nome do negocio que você quer deletar     
a.alterarCategoria() #colocar os nome que você quer alterar, ex: "(carne", "sorvete") assim a carne será alterada por sorvete

