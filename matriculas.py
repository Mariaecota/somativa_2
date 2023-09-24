# Matrículas
# Código da turma (Número inteiro)
# Código do estudante (Número inteiro)
# Validação de dados na manipulação de turmas e matrículas (verificar se um código já existe antes de incluir uma nova turma/matrícula com o mesmo código).


import menu_estudante as me
import turmas as tms

def opcaolista():
    lista_matriculas = me.carregar('matriculas.json')
    print("\n------ LISTA ------\n")
    print(f"\nTotal de matriculas cadastradas: {len(lista_matriculas)}\n")

    if len(lista_matriculas) == 0:
        print("A lista está vazia\n")

    else:
        for matricula in lista_matriculas:
            print(f"Código da turma: {matricula['codigo_turma']}, Código do estudante: {matricula['matricula']}")

def opcaoadicionar():

    lista_matriculas = me.carregar('matriculas.json')
    lista_turmas = me.carregar('turmas.json')
    lista_estudantes = me.carregar('estudante.json')

    print("\n------ ADICIONAR ------")

    cod_turma = tms.verificar_codigo2("turma", lista_turmas, "codigo_turma")
    cod_estudantes = tms.verificar_codigo2("estudantes", lista_estudantes, "matricula")

    if cod_turma == 0 or cod_estudantes == 0:
            pass
    else:
        dados_matriculas =  {
        "codigo_turma": cod_turma, 
        "matricula": cod_estudantes
        }

    lista_matriculas.append(dados_matriculas)
    me.salvar(lista_matriculas, 'matriculas.json')

def opcaoexcluir():
    while True:
        try:
            lista_matriculas = me.carregar('matriculas.json')
            buscar_codigo = int(input("\nDigite o código do estudante que deseja excluir: "))
            break
        except ValueError:
            print("\nValor inválido")


    achou = False

    for i in lista_matriculas:
        if i['matricula'] == buscar_codigo:
            lista_matriculas.remove(i)
            print("\nExcluído!")
            achou = True
            break   

    if not achou:
        print("\nCódigo não localizado")

    me.salvar(lista_matriculas, 'matriculas.json')

def opcaoalteracaodados():

    while True:
        try:
            lista_matriculas = me.carregar('matriculas.json')
            lista_turmas = me.carregar('turmas.json')
            lista_estudantes = me.carregar('estudante.json')
            buscar_codigo = int(input("\nDigite o codigo estudante que deseja alterar: "))
            break

        except ValueError:
            print("\nValor inválido")
            continue
    achou = False
    for estudante in lista_matriculas:
        if estudante['matricula'] == buscar_codigo:
            print("\nEstudante encontrado, digite os novos dados abaixo: ")
            novo_codigo_estudante = tms.verificar_codigo2("estudantes", lista_estudantes, "matricula")
            novo_codigo_turma = tms.verificar_codigo2("turma", lista_turmas, "codigo_turma")

            estudante['matricula'] = novo_codigo_estudante
            estudante['codigo_turma'] = novo_codigo_turma

            
            achou = True   

    if not achou:
        print("\Estudante não localizado")

    if novo_codigo_estudante == 0 or novo_codigo_turma == 0:
        pass
    else:
        print("\nDados alterados com sucesso")
        me.salvar(lista_matriculas, 'matriculas.json')

def menu_2_matriculas():
    opcao = "-1"
    while opcao != "5":
        opcao = input("""
            
----- MENU MATRICULAS -----

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

# --------------------------------------------------------------------------------------------------------------
#----------------------------------------------- 3° OPÇÃO / EXCLUIR ------------------------------------------
#-------------------------------------------------------------------------------------------------------------

        elif opcao == "3":
            opcaoexcluir()

#-------------------------------------------------------------------------------------------------------------
#------------------------------------- 4° OPÇÃO / ALTERAÇÃO DE DADOS--------------------------------------
#-----------------------------------------------------------------------------------------------------------------

        elif opcao == "4":
            opcaoalteracaodados()

# ------------------------------------------------------------------------------------------------------------------
#----------------------------------------------- 5° OPÇÃO / SAIR ---------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------


        elif opcao == "5":
            break
        else:
            print("Opção invalida")