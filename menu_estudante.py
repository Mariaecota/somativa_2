import json

# Funções ----------------------------------------------------------------------------------------------------------

def salvar(lista, nome_arquivo):

    with open(nome_arquivo, "w") as f:

        json.dump(lista, f , indent=4)

def carregar(nome_arquivo):

    try:
        with open(nome_arquivo, "r") as arquivo:

            data = json.load(arquivo)

        return data

    except:
        return []

def opcaolista():
    lista_estudantes = carregar('estudante.json')
    print("\n------ LISTA ------")
    print(f"\nTotal de estudantes cadastrados: {len(lista_estudantes)}\n")

    if len(lista_estudantes) == 0:
        print("A lista está vazia\n")
    else:
        for aluno in lista_estudantes:
            print(f"Nome: {aluno['nome']}, Matrícula: {aluno['matricula']}, CPF: {aluno['cpf']}")

def opcaoadicionar():
    lista_estudantes = carregar('estudante.json')
    print("\n------ ADICIONAR ------\n")
    nome = input("Digite o nome do aluno: ")
    while True:
        try: 
            matricula = int(input("Digite o número da matrícula: "))
            
            if any(aluno['matricula'] == matricula
            for aluno in lista_estudantes):
                print("Essa matricula já existe, digite uma matricula válida.")
                continue
            break
        except ValueError:
            print("Valor inválido")

    cpf = input("Digite o número do CPF: ")

    # DICIONARIO 
    dados_aluno = {
        'nome': nome,
        'matricula': matricula,
        'cpf': cpf,
    }

    lista_estudantes.append(dados_aluno)
    salvar(lista_estudantes, 'estudante.json')

    print(f"""
Dados incluídos com sucesso: 

Nome: {nome}
Matrícula: {matricula}
CPF: {cpf}""")
 
def opcaoexcluir():
        while True:
            try:
                lista_estudantes = carregar('estudante.json')
                buscar_matricula = int(input("\nDigite o número da matricula que deseja excluir: "))
                break
            except ValueError:
                print("\nvalor inválido")
        achou = False
        for matricula in lista_estudantes:
            if matricula ['matricula'] == buscar_matricula:
                lista_estudantes.remove(matricula)
                print("\nExcluído!")
                achou = True
                salvar(lista_estudantes,'estudante.json')
                break
        if not achou:
            print("\nMatricula não localizada")

def opcaoalteracaodados():

    while True:
        try:
            lista_estudantes = carregar('estudante.json')
            buscar_matricula = int(input("\nDigite o número da matrícula que deseja alterar: "))
            break
        except ValueError:
            print("\nValor inválido")
            continue
    achou = False
    for matricula in lista_estudantes:
        if matricula['matricula'] == buscar_matricula:
            print("\nAluno encontrado, digite os novos dados abaixo:")
            
       
            while True:
                try: 
                    novamatricula = int(input("\nDigite a nova matrícula : "))
                    break
                except ValueError:
                    print("\nValor inválido")
            novonome = input("\nDigite o novo nome: ")
            novocpf = input("\nDigite o novo CPF: ")

        
            matricula['nome'] = novonome
            matricula['matricula'] = novamatricula
            matricula['cpf'] = novocpf
            
            print("\nDados alterados com sucesso")
            achou = True
            break   

    if not achou:
        print("\nAluno não localizado")

 
    salvar(lista_estudantes, 'estudante.json')

#  Exibição do menu ------------------------------------------------------------------------------------------------

def menu_2_estudante():
    opcao = "-1"
    while opcao != "5":
        opcao = input("""
            
----- MENU DO ESTUDANTE -----

1) Listar
2) Adicionar
3) Excluir
4) Alterar
5) Sair 
            
Digite a opção desejada: """)
#-------------------------------------------------------------------------------------------------------------------
#----------------------------------------------- 1° OPÇÃO / LISTA --------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------

        if opcao == "1":
            opcaolista()

#-------------------------------------------------------------------------------------------------------------------
#----------------------------------------------- 2° OPÇÃO / ADICIONAR ----------------------------------------------
#-------------------------------------------------------------------------------------------------------------------

        elif opcao == "2":
            opcaoadicionar()

# ------------------------------------------------------------------------------------------------------------------
#----------------------------------------------- 3° OPÇÃO / EXCLUIR ------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------

        elif opcao == "3":
            opcaoexcluir()

# ------------------------------------------------------------------------------------------------------------------
#----------------------------------------------- 4° OPÇÃO / ALTERAÇÃO DE DADOS--------------------------------------
# ------------------------------------------------------------------------------------------------------------------

        elif opcao == "4":
            opcaoalteracaodados()

# ------------------------------------------------------------------------------------------------------------------
#----------------------------------------------- 5° OPÇÃO / SAIR ---------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------


        elif opcao == "5":
            break
        else:
            print("Opção invalida")

