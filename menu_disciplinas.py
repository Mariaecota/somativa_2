# Funções ----------------------------------------------------------------------------------------------------------
import menu_estudante as me

def opcaolista():
    lista_disciplina = me.carregar('disciplina.json')
    print("\n------ LISTA ------\n")
    print(f"Total de disciplinas cadastradas: {len(lista_disciplina)}\n")

    if len(lista_disciplina) == 0:
        print("A lista está vazia\n")
    else:
        for disciplina in lista_disciplina:
            print(f"Nome: {disciplina['nome']}, Código: {disciplina['codigo']}")

def opcaoadicionar():
    lista_disciplina = me.carregar('disciplina.json')
    print("\n------ ADICIONAR ------\n")
    nome = input("Digite o nome da disciplina: ")
    while True:
        try: 
            codigo = int(input("Digite o código da disciplina: "))
            if any(i['codigo'] == codigo 
            for i in lista_disciplina):
                print("Esse código já existe, digite um código válido")
                continue
            break
        except ValueError:
            print("\nValor inválido")

    # DICIONARIO 
    disciplina = {
        'nome': nome,
        'codigo': codigo,
    }

    lista_disciplina.append(disciplina)
    me.salvar(lista_disciplina, 'disciplina.json')

    print(f"""
Dados incluídos com sucesso: 

nome: {nome}
codigo: {codigo}
""")
 
def opcaoexcluir():
        while True:
            try:
                lista_disciplina = me.carregar('disciplina.json')
                buscar_codigo = int(input("Digite o código que deseja excluir: "))
                break
            except ValueError:
                print("valor inválido")
        achou = False
        for codigo in lista_disciplina:
            if codigo ['codigo'] == buscar_codigo:
                lista_disciplina.remove(codigo)
                print("Excluído!")
                achou = True
                me.salvar(lista_disciplina,'disciplina.json')
                break
        if not achou:
            print("Código não localizado")

def opcaoalteracaodados():

    while True:
        try:
            lista_disciplina = me.carregar('disciplina.json')
            buscar_codigo = int(input("Digite o código da disciplina que deseja alterar: "))
            break
        except ValueError:
            print("\nValor inválido")
            continue

    achou = False
    for codigo in lista_disciplina:
        if codigo['codigo'] == buscar_codigo:
            print("\nDisciplina encontrada, digite os novos dados abaixo:")
            

            while True:
                try: 
                    novocodigo = int(input("Digite a nova matrícula: "))
                    break
                except ValueError:
                    print("\nValor inválido")
            
            novonome = input("\nDigite o novo nome: ")
            
            codigo['nome'] = novonome
            codigo['codigo'] = novocodigo
        
            print("\nDados alterados com sucesso")
            achou = True
            break   

    if not achou:
        print("\nDisciplina naaaaão localizada")

 
    me.salvar(lista_disciplina, 'disciplina.json')

#  Exibição do menu ------------------------------------------------------------------------------------------------

def menu_2_disciplina():
    opcao = "-1"
    while opcao != "5":
        opcao = input("""
            
----- MENU DISCIPLINAS -----

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