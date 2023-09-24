# Funções ----------------------------------------------------------------------------------------------------------
import menu_estudante as me

def opcaolista():
    lista_professores = me.carregar('professor.json')
    print("\n------ LISTA ------")
    print(f"\nTotal de professores cadastrados: {len(lista_professores)}\n")

    if len(lista_professores) == 0:
        print("\nA lista está vazia")
    else:
        for professor in lista_professores:
            print(f"Nome: {professor['nome']}, Codigo professor: {professor['codigo_professor']}, CPF: {professor['cpf']}")

def opcaoadicionar():
    lista_professores = me.carregar('professor.json')
    print("\n------ ADICIONAR ------\n")
    nome = input("\nDigite o nome do novo professor: ")
    while True:
        try: 
            matricula = int(input("\nDigite o número da matrícula: "))

            if any(professor['codigo_professor'] == matricula
            for professor in lista_professores):
                print("Esse código já existe, digite um código válido.")
                continue
            break
        except ValueError:
            print("\nValor inválido")

    cpf = input("\nDigite o número do CPF: ")

    # DICIONARIO 
    dados_professores = {
        'nome': nome,
        'codigo_professor': matricula,
        'cpf': cpf,
    }

    lista_professores.append(dados_professores)
    me.salvar(lista_professores, 'professor.json')

    print(f"""
Dados incluídos com sucesso: 

Nome: {nome}
codigo professor: {matricula}
CPF: {cpf}""")
 
def opcaoexcluir():
        while True:
            try:
                lista_professores = me.carregar('professor.json')
                buscar_matricula = int(input("\nDigite o número do código que deseja excluir: "))
                break
            except ValueError:
                print("\nvalor inválido")
        achou = False
        for matricula in lista_professores:
            if matricula ['codigo_professor'] == buscar_matricula:
                lista_professores.remove(matricula)
                print("Excluído!")
                achou = True
                me.salvar(lista_professores,'professor.json')
                break
        if not achou:
            print("\nCódigo não localizada")

def opcaoalteracaodados():

    while True:
        try:
            lista_professores = me.carregar('professor.json')
            buscar_matricula = int(input("\nDigite o número da matrícula que deseja alterar: "))
            break
        except ValueError:
            print("\nValor inválido")
            continue

    achou = False
    for matricula in lista_professores:
        if matricula['codigo_professor'] == buscar_matricula:
            print("\nProfessor encontrado, digite os novos dados abaixo:")
            

            while True:
                try: 
                    novamatricula = int(input("Digite o novo codigo: "))
                    break
                except ValueError:
                    print("Valor inválido")
            novonome = input("Digite o novo nome: ")
            novocpf = input("Digite o novo CPF: ")

            
            matricula['nome'] = novonome
            matricula['codigo_professor'] = novamatricula
            matricula['cpf'] = novocpf
            print("\nDados alterados com sucesso")
            achou = True
            break   

    if not achou:
        print("\nProfessor não localizado")

 
    me.salvar(lista_professores, 'professor.json')


#  Exibição do menu ------------------------------------------------------------------------------------------------

def menu_2_professor():
    opcao = "-1"
    while opcao != "5":
        opcao = input("""
----- MENU DO PROFESSOR -----

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

