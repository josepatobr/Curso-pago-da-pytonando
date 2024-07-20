import Controller
import os.path

def CriarArquivos(*nome):
    for i in nome:
         if not os.path.exists(i):
            with open(i, "w") as arq:
                arq.write("")
CriarArquivos("categoria.txt", "clientes.txt", "estoque.txt", "fornecedores.txt",
              "funcionarios.txt", "venda.txt")                



if __name__ == "__main__":
    while True:
        local = int(input("Digite 1 para acessar (Categorias) \n"
                          "Digite 2 para acessar (Estoque) \n"
                          "Digite 3 para acessar (Fornecedor) \n"
                          "Digite 4 para acessar (Cliente) \n"
                          "Digite 5 para acessar (Funcionario) \n"
                          "Digite 6 para acessar (Vendas) \n"
                          "Digite 7 para ver os produtos mais vendido \n"
                          "8 para sair \n"))
                          

        if local == 1:
            cat = Controller.ControllerCategoria()
            while True:
                decidir = int(input("Digite 1 para Cadastrar uma categoria \n"
                                    "Digite 2 para remover uma categoria \n"
                                    "Digite 3 para alterar uma categoria \n"
                                    "Digite 4 para mostrar todas as categorias registradas \n"
                                    "Digite 5 para sair \n"))
                if decidir == 1:
                    categoria = input("Digite a categoria que deseja cadastrar")
                    cat.cadastraCategoria(categoria)
                elif decidir == 2:
                    input("Digite a categoria que deseja remover")
                    cat.removerCategoria(categoria)
                elif decidir == 3:
                    input("Digite qual categoria defesa alterar")
                    categoria.alterarCategoria(categoria)
                elif decidir == 4:
                    cat.mostrarCategoria()
                elif decidir == 5:
                    break

        if local == 2:
            cat = Controller.ControllerEstoque()
            while True:
                decidir = int(input("Digite 1 para ver todos os estoques disponiveis \n"
                                    "Digite 2 para sair \n"))
                
                if decidir == 1:
                    cat.mostrarEstoque()
                elif decidir == 2:
                    break

        if local == 3:
            cat = Controller.ControllerFornecedor()
            while True:
                decidir = int(input("Digite 1 para Cadastrar uma fornecedor \n"
                                    "Digite 2 para remover uma fornecedor \n"
                                    "Digite 3 para alterar uma fornecedor \n"
                                    "Digite 4 para mostrar todas os fornecedor registrados \n"
                                    "Digite 5 para sair \n"))
                
                if decidir == 1:
                    nome = input("Digite o nome do Fornecedor \n")
                    cnpj = input("Digite o cnpj do Fornecedor \n")
                    telefone = input("Digite o telefone do Fornecedor \n")
                    categoria = input("Digite a categoria que ele prefere atuar")
                    cat.cadastrarFornecedor(nome, cnpj, telefone, categoria)
                
                elif decidir == 2:
                    input("Digite o Fornecedor que deseja remover")
                    cat.removerFonecedor()
                
                elif decidir == 3:
                    NomeFornecedor = input("Digite qual Fornecedor que deseja alterar")
                    NovoNome = input("Digite o novo nome do Fornecedor \n")
                    NovoCLT = input("Digite o novo CLT do Fornecedor \n")
                    NovoTelefone = input("Digite o novo Telefone do Fornecedor \n")
                    NovoCpf = input("Digite o novo CPF do Fornecedor \n")
                    NovoEmail = input("Digite o novo email do Fornecedor \n")
                    NovoEndereco = input("Digite o novo endereço do Fornecedor \n")
                    cat.alterarFornecedor(NomeFornecedor, NovoNome, NovoCLT, NovoTelefone, NovoCpf, NovoEmail, NovoEndereco)

                elif decidir == 4:
                    cat.mostrarFornecedor()
                elif decidir == 5: 
                    break

        if local == 4:
            cat = Controller.ControllerClientes()
            while True:
                decidir = int(input("Digite 1 para Cadastrar uma Cliente \n"
                                    "Digite 2 para remover uma Cliente \n"
                                    "Digite 3 para alterar uma Cliente \n"
                                    "Digite 4 para mostrar todas os fornecedor registrados \n"
                                    "Digite 5 para sair \n"))
             
                if decidir == 1:
                    nome = input("Digite o nome do Cliente \n")
                    telefone = int(input("Digite o telefone \n"))
                    cpf = int(input("Digite o cpf \n"))
                    email = input("Digite o email \n")
                    endereco = input("Digite o endereço")
                    cat.CadastrarClientes(nome, telefone, cpf, email, endereco)
                
                elif decidir == 2:
                    nome = input("Digite o nome do cliente que deseja remover")
                    cat.RemoverClientes(nome)
                
                elif decidir == 3:
                    NomeCliente = input("Digite qual cliente que deseja alterar")
                    NovoNome = input("Digite o novo nome do cliente \n")
                    NovoTelefone = int(input("Digite o novo Telefone do cliente \n"))
                    NovoCpf = int(input("Digite o novo CPF do cliente \n"))
                    NovoEmail = input("Digite o novo email do cliente \n")
                    NovoEndereco = input("Digite o novo endereço do cliente \n")
                    cat.AlterarCliente(NomeCliente, NovoNome, NovoTelefone, NovoCpf, NovoEmail, NovoEndereco)

                elif decidir == 4:
                    cat.MostrarClientes()
                
                elif decidir == 5:
                    break
        if local == 5:
                cat = Controller.ControllerFuncionario()
                while True:
                    decidir = int(input("Digite 1 para Cadastrar um funcionario \n"
                                        "Digite 2 para remover um funcionario \n"
                                        "Digite 3 para alterar um funcionario \n"
                                        "Digite 4 para sair \n"))
                    if decidir == 1:
                            nome = input("Digiteo o nome do funcionario \n")
                            clt = int(input("Digite o clt \n"))
                            telefone = int(input("Digite o telefone \n"))
                            cpf = int(input("Digite o cpf \n"))
                            email = input("Digite o email \n")
                            endereco = input("Digite o endereço")
                        
                            cat.CadastrarFuncionario(nome, clt, telefone, cpf, email, endereco)
                    elif decidir == 2:
                            nome = input("Digite o nome do funcionario que deseja remover")
                            cat.RemoverFuncionario(nome)
                    elif decidir == 3:
                            AlterarNome = input("Digite qual funcionario você deseja alterar")
                            NovoNome = input("Digite o novo nome do funcionario \n")
                            NovoClt = int(input("Digite o novo CLT \n"))
                            NovoTelefone = int(input("Digite o novo telefone \n"))
                            NovoCpf = int(input("Digite o novo CPF \n"))
                            NovoEmail = input("Digite o novo email \n")
                            NovoEndereco = input("Digite o novo endereço")
                            
                            cat.AlterarFuncionario( AlterarNome, NovoNome, NovoClt, NovoTelefone, NovoCpf, NovoEmail, NovoEndereco)

                    elif decidir == 4:
                        break
    
        if local == 6:
                cat = Controller.ControllerVenda()
                while True:
                    dicidir = int(input("Digite 1 para realizar uma venda \n"
                                        "Digite 2 para ver as vendas \n"
                                        "Digite 3 para sair \n"))  
                    if decidir == 1:
                        nome = input(" Digite o nome do Produto \n") 
                        vendedor = input("Digite o nome do vendedor \n")
                        comprador = input("Digite o nome do comprador \n")
                        quantidade = int(input("Digite a quantidade comprada"))
                        cat.cadastrarVenda(nome, vendedor, comprador, quantidade)

                    if decidir == 2:
                         dataInicio = input("Digite a data de inicio no formato dia/mmes/ano: \n")
                         dataTermino = input("Digite a data de inicio no formato dia/mmes/ano: \n")

                         cat.mostrarVenda(dataInicio, dataTermino)

        elif local == 7:
            a = Controller.ControllerVenda()
            a.relatorioProdutos()
        else: 
           break                   
                          
                          
                          
                          