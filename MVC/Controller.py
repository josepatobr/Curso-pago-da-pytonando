from Models import *
from MVC.DAO import *
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
            estoque = DaoEstoque.ler()
        
            estoque = list(map(lambda x: Estoque(Produtos(x.produtos.nome, x.produto.preco, x.categoriaAlterada), x.quantidade)
                   if(x.produtos.categoria == categoriaAlterada) else (x), estoque))
        
        with open('estoque.txt', 'w') as arq:
            for i in estoque:
                arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria + "|" + str(i.quantidade))
                arq.writelines ("\n")
            else:
                print("a categoria que deseja alterar ja existe, no caso teria 2 nomes iguais")
                
                with open('categoria.txt', 'w') as arq: #abrimos o arquivo que iremos alterar e reescrevemos as coisas que mudamos
                    for i in x:
                        arq.writelines(i.categoria)
                        arq.writelines('\n')
    
    def mostrarCategoria(self,):
        categorias = DaoCategoria.ler()
        if len (categorias) == 0:
            print ("Categoria vazia!")                                                                                                                                                                                                                                          
        else:
            for i in categorias:
                print(f'categoria: {i.categoria}')


#a = ControllerCategoria()
#a.removerCategoria() #colocar o nome do negocio que você quer deletar     
#a.alterarCategoria() #colocar os nome que você quer alterar, ex: "(carne", "sorvete") assim a carne será alterada por sorvete


class ControllerEstoque:
    def cadastrarProdutos(self, nome, preco, categoria, quantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == categoria, y))
        est = list(filter(lambda x: x.produto.nome == nome, x))

        if len(h) > 0:
            if len(est) == 0:
                produto = Produtos(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print("produto cadastrado com sucesso")
            else:
                print("Produto ja existe")

    def removerProduto(self, nome):
        x = DaoEstoque.ler()
        est = list(filter(lambda x: x.produto.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].produto.nome == nome:
                    del x[i]
                    break
                print("produto foi removido")
        else:
            print("esse produto não existe")

            with open ('estoque.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" +
                                i.produto.categoria + "|" + str(i.quantidade))
                    arq.writelines('\n')
                else:
                    print("a categoria não existe")

        estoque = DaoEstoque.ler()
        
        estoque = list(map(lambda x: Estoque(Produtos(x.produtos.nome, x.produto.preco, "Sem categoria"), x.quantidade)
                   if(x.produtos.categoria == categoriaRemover) else (x), estoque))
        
        with open('estoque.txt', 'w') as arq:
            for i in estoque:
                arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria + "|" + str(i.quantidade))
                arq.writelines ("\n")



    def mostrarEstoque(self):
        estoque = DaoEstoque.ler()
        if len(estoque) == 0:
            print("estoque vazio")
        else:
            for i in Estoque:
                print("-----Produtos-----")
                print(f"nome: {i.produto.nome}\n"
                    f"preco: {i.produto.preco}\n"
                    f"categoria: {i.produto.categoria}\n"
                    f"quantidade: {i.produto.quantidade}")
class ControllerVenda:
    def cadastrarVenda(self, nomeProduto, vendedor, comprador, quantidadeVendida):
        x = DaoEstoque.ler()
        temp = []
        existe = False
        quantidade = False

        for i in x:
            if existe == False:
                if i.produto.nome == nomeProduto:
                    existe == True
                if i.quantidade >= quantidadeVendida:
                    quantidade = True
                    i.quantidade = int(i.quantidade) - int(quantidadeVendida)

            vendido = Venda(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), vendedor, comprador, quantidadeVendida)

            valorCompra = int(quantidadeVendida) * int(i.produto.preco)

            DaoVenda.salvar(vendido)
        temp.append([Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), i.quantidade])

        arq = open('estoque.txt', 'w') 
        arq.write("")
    
        for i in temp:
            with open('estoque.txt', 'a') as arq:
                    arq.writelines(i[0].nome + "|" + i[0].preco + "|" + i[0].categoria + "|" + str(i[1]))
                    arq.writelines ('\n')
            if existe == False:
                print("O produto não existe")
                return None
            elif not quantidade:
                print("não temos essa quantidade para vender")
                return None
            else:
                print("Venda realizada com sucesso")
                return valorCompra

    def relatorioProdutos(self):
        vendas = DaoVenda.ler()
        produtos = []
        for i in vendas:
            nome = i.itensVendido.nome
            quantidade = i.quantidadeVendida
            tamanho = list(filter(lambda x: x['produto'] == nome, produtos))
            if len(tamanho) > 0:
                produtos  = list(map(lambda x: {'produto': nome, 'quantidade':  int(x['quantidade']) + quantidade}
                if (x['produto'] == nome) else(x), produtos))
            else:
                produtos.append({'produto': nome, 'quantidade': int(quantidade)})
        ordenado = sorted(produtos, key=lambda k: k['quantidade'], reverse= True)
        print("esses são os produtos mais vendidos")  
        a = 1
        
        for i in ordenado:
            print(f"----------Produtos[{a}]----------")
            print(f"Produto: {i['produto']} \n"
                  f"quantidade: {i['quantidade']} \n")
            a += 1

    def mostrarVendas(self, dataInicio, dataTermino):
        vendas = DaoVenda.ler()
        dataInicial1 = datetime.strptime(dataInicio, '%d/%m/%Y')
        dataTermino1 = datetime.strptime(dataTermino, '%d/%m/%Y')

        vendasSelecionadas = list(filter(lambda x: datetime.strptime(x.data, '%d/%m/%Y') >= dataInicial1 and 
                                      datetime.strptime(dataTermino, '%d/%m/%Y' <= dataTermino1, vendas)))
    
        cont = 1
        total = 0
        for i in vendasSelecionadas:
            print(f"----------{cont}----------")
            print(f"nome: {i.itensVendido.nome} \n"
                f"categoria: {i.itensVendido.categoria} \n"
                f"data: {i.data} \n"
                f"quantidade: {i.quantidadeVendida} \n"
                f"clientes: {i.comprador} \n"
                f"vendedor: {i.vendedor}")
            total += int(i.itensVendido.preco) * int(i.quantidadeVendida)
            cont +=1
            print(f"Total vendido {total}")
class ControllerFornecedor:
    def cadastrarFornecedor(self, nome, cnpj, telefone, categoria):
        x = DaoFornecedor.ler()
        listacnpj = list(filter(lambda x: x.cnpj == cnpj, x))
        listatelefone = list(filter(lambda x: x.telefone == telefone, x))
        if len (listacnpj) > 0:
            print("Esse cnpj já existe")
        elif len (listatelefone) > 0:
            print("esse telefone ja existe")
        else:
            if len(cnpj) == 14 and len(telefone) <= 11 and len(telefone) >= 10:
                DaoFornecedor.salvar(Fornecedor(nome, cnpj, telefone, categoria))
            else:
                ("Digita um telefone ou cnpj válido")
    
    def alterarFornecedor(self, AlterarNome, NovoNome, NovoCnpj, NovoTelefone, NovaCategoria):
        x = DaoFornecedor.ler()
        est = list(filter(lambda x: x.nome == AlterarNome, x))
        if len(est) > 0:
            est = list(filter(lambda x: x.cnpj == NovoCnpj, x))
            if len(est) == 0:
                x = list(filter(lambda x: Fornecedor(NovoNome, NovoCnpj, NovoTelefone, NovaCategoria) if(x.NovoCnpj == 0, x) else (x,x)))
                print("Esse cnpj já existe")
        else:
            print(" O fornecedor que dejesa alterar não existe")
            with open('fornecedores.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')
                    print("Fornecedor alterado com sucesso")
    
    def removerFonecedor(self, nome):
        x = DaoFornecedor.ler()
        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                break
            print("Fornecedor foi deletado com sucesso")
        else:
            print("esse Fornecedor não existe")

        with open ('fornecedores.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.cnpj + "|" + i.telefone
                           + "|" + i.categoria)
            arq.writelines('\n')
            print("Fornecedor alterado com sucesso")

    def mostrarFornecedor(self):
        Fornecedores = DaoFornecedor.ler()
        if len(Fornecedores) == 0:
            print("Esta lista esta vazia")

            for i in Fornecedores:
                print("----------Fornecedores----------")
                print(f"categoria fornecida: {i.categoria} \n"
                      f"nome: {i.nome} \n"
                      f"telefone: {i.telefone} \n"                       
                      f"cnpj: {i.cnpj}")
class ControllerClientes:
    def CadastrarClientes(self, nome, telefone, cpf, email, endereco):
        x = DaoPessoa.ler()
        listarCPF = list(filter(lambda x: x.cpf == cpf, x))
        if len(listarCPF) > 0:
            print("Esse CPF ja existe!")
        else:
            if len(cpf) == 10 and len(telefone) >= 10 and len(telefone) <=11:
                DaoPessoa.salvar(Pessoa(nome, telefone, cpf, email, endereco))
                print("Cliente cadastrado com sucesso")
            else:
                print("ERRO")
                print("Você digitou algo errado")

    def AlterarCliente(self, AlterarNome, NovoNome, NovoTelefone, NovoCpf, NovoEmail, NovoEndereco):             
        x = DaoPessoa.ler()
        est = list(filter(lambda x: x.nome == AlterarNome, x))
        if len(est) > 0:
            x = list(filter(lambda x: Pessoa(NovoNome, NovoTelefone, NovoCpf, NovoEmail, NovoEndereco) if
                            (x.nome == AlterarNome) else (x), x))
        else:
            print("O cliente que deseja alterar não existe")
            
            with open('clientes.txt', 'a') as arq:
                for i in x:
                    arq.writelines(i.nome + "|" + i.telefone + "|" + i.cpf
                            + "|" + i.email + "|" + i.endereco)
                arq.writelines('\n')

    def RemoverClientes(self, nome):
        x = DaoPessoa.ler()
        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                break
            print("Cliente removido com sucesso")
        else:
            print("esse cliente não existe")
            return None
        
        with open ('clientes.txt', 'w') as arq:
            for i in x:
                    arq.writelines(i.nome + "|" + i.telefone + "|" + i.cpf
                            + "|" + i.email + "|" + i.endereco)
                    arq.writelines('\n')
            print("Clinte removido com sucesso")

    def MostrarClientes(self):
        clientes = DaoPessoa.ler()
        if len(clientes) == 0:
            print("Esta lista esta vazia")

            for i in clientes:
                print("----------Cliente----------")
                print(f"Nome: {i.nome} \n"
                      f"Telefone: {i.telefone} \n"
                      f"Endereco: {i.endereco} \n"                       
                      f"Email: {i.email}"
                      f"Cpf {i.cpf}")
class ControllerFuncionario: 
    def CadastrarFuncionario(self, clt, nome, telefone, cpf, email, endereco):
        x = DaoFuncionario.ler()
        listarCPF = list(filter(lambda x: x.cpf == cpf, x))
        listarCLT = list(filter(lambda x: x.clt == clt, x))
        if len(listarCPF) > 0:
            print("Esse CPF é de outra pessoa")
        elif len(listarCLT) > 0:
            print("Esse CLT é de outra pessoa")
        else:
            if len(cpf) == 11 and len(telefone) > 10 and len (telefone) <= 11:
                DaoFuncionario.salvar(Funcionario(clt, nome, telefone, cpf, email, endereco))
                print("Funcionario cadastrado com sucesso")
            else:
                print("Digite as informações correta")

    def AlterarFuncionario(self, AlterarNome, NovoClt, NovoNome, NovoTelefone, NovoCpf, NovoEmail, NovoEndereco):
        x = DaoFuncionario.ler()
        est = list(filter(lambda x: x.nome == AlterarNome, x))
        if len(est) > 0:
            x = list(filter(lambda x: Pessoa(NovoClt, NovoNome, NovoTelefone, NovoCpf, NovoEmail, NovoEndereco) if
                            (x.nome == AlterarNome) else (x), x))
        else:
            print("O Funcionario que deseja alterar não existe")
            
            with open('funcionarios.txt', 'a') as arq:
                for i in x:
                    arq.writelines(i.clt + "|" + i.nome + "|" + i.telefone + "|" + i.cpf
                            + "|" + i.email + "|" + i.endereco)
                arq.writelines('\n')
                print("Funcionario alterado com sucesso")

    def RemoverFuncionario(self, nome):
        x = DaoFuncionario.ler()
        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                break
            print("funcionario removido com sucesso")
        else:
            print("esse funcionario não existe")
            return None
        
        with open ('funcionarios.txt', 'w') as arq:
            for i in x:
                     arq.writelines(i.clt + "|" + i.nome + "|" + i.telefone + "|" + i.cpf
                            + "|" + i.email + "|" + i.endereco)
            arq.writelines('\n')
            print("Funcionario removido com sucesso")
