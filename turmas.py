# Funções ----------------------------------------------------------------------------------------------------------
import menu_estudante as me
# verificar se o código existe, se existir, não funciona
def verificar_codigo(codigo, lista, x): 
    while True:
        try: 
            matricula = int(input(f"\nDigite o código do(a) {codigo}: "))

            if any(item[x] == matricula
            for item in lista):

                print("Essa codigo já existe, digite uma codigo válido.")
                continue
            break
        except ValueError:
            print("\nValor inválido")
    return matricula
# verificar se o código existe, se existir, funciona
def verificar_codigo2(codigo, lista, x): 
    while True:
        try: 
            matricula = int(input(f"\nDigite o código do(a) {codigo} ou '0' para voltar: "))
            if matricula ==0:
                break
            if any(item[x] == matricula
            for item in lista):

                break
            continue
            
        except ValueError:
            print("\nValor inválido")
    return matricula

def opcaoadicionar():

    lista_turmas = me.carregar('turmas.json')
    lista_professores = me.carregar('professor.json')
    lista_disciplinas = me.carregar('disciplina.json')

    print("\n------ ADICIONAR ------")


    cod_turma = verificar_codigo("turma", lista_turmas, "codigo_turma")
    
    cod_prof = verificar_codigo2( "professor", lista_professores, "codigo_professor")

    cod_disc =  verificar_codigo2("disciplina", lista_disciplinas, "codigo")

    if cod_prof == 0 or cod_disc == 0:
        pass
    else:
        dados_turma = {
            'codigo_turma' : cod_turma, 
            'codigo_professor': cod_prof,
            'codigo_disciplina': cod_disc,
        }

        lista_turmas.append(dados_turma)
        me.salvar(lista_turmas, 'turmas.json')

def opcaolista():

    lista_turmas = me.carregar('turmas.json')
    print("\n------ LISTA ------\n")

    if len(lista_turmas) == 0:
        print("\nA lista está vazia")
    else:
        for turma in lista_turmas:
            print(f"Código da turma: {turma['codigo_turma']}, Código do professor: {turma['codigo_professor']}, Código da disciplina: {turma['codigo_disciplina']}")

def opcaoexcluir():
    while True:
        try:
            lista_turmas = me.carregar('turmas.json')
            buscar_codigo = int(input("\nDigite o código da turma que deseja excluir: "))
            break
        except ValueError:
            print("\nValor inválido")
    
    achou = False
    for turma in lista_turmas:
        if turma['codigo_turma'] == buscar_codigo:
            lista_turmas.remove(turma)
            print("\nExcluído!")
            achou = True
            break

    if not achou:
        print("\nCódigo não localizado")

    me.salvar(lista_turmas, 'turmas.json')

def opcaoalteracaodados():
    
    while True:
        try:
            lista_turmas = me.carregar('turmas.json')
            lista_professores = me.carregar('professor.json')
            lista_disciplinas = me.carregar('disciplina.json')
            buscar_codigo = int(input("\nDigite o codigo que deseja alterar: "))
            break
        except ValueError:
            print("\nValor inválido")
            continue
    achou = False
    for codigo in lista_turmas:
        if codigo['codigo_turma'] == buscar_codigo:
            print("\nTurma encontrada, digite os novos dados abaixo:")
            novaturma = int(input("\nDigite a nova matrícula (ou preencha com a anterior para manter): "))
        
            
            cod_prof = verificar_codigo2( "professor", lista_professores, "codigo_professor")

            cod_disc =  verificar_codigo2("disciplina", lista_disciplinas, "codigo")

        if cod_prof == 0 or cod_disc == 0:
       
            codigo['codigo_turma'] = novaturma
            codigo['codigo_professor'] = cod_prof
            codigo['codigo_disciplina'] = cod_disc

            achou = True   

    if not achou:
        print("\nDisciplina não localizada")
    elif cod_prof == 0 or cod_disc == 0:
        pass
    else:
        print("\nDados alterados com sucesso")
        me.salvar(lista_turmas, 'turmas.json')

#  Exibição do menu ------------------------------------------------------------------------------------------------

def menu_2_turmas():
    opcao = "-1"
    while opcao != "5":
        opcao = input("""
            
----- MENU TURMAS -----

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

