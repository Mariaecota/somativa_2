#NOME: MARIA EDUARDA DA SILVA COTA

# Importações ------------------------------------------------------------------------------------------------------
import menu_professor as mp
import menu_estudante as me
import menu_professor as mp
import menu_disciplinas as md
import matriculas as mt
import turmas as tr


# Menu geral -------------------------------------------------------------------------------------------------------

def menugeral():

    opcao = "-1"
    while opcao != "9": 
        print("""\n
### MENU PRINCIPAL ###\n
(1) Gerenciar estudantes
(2) Gerenciar professores
(3) Gerenciar disciplinas
(4) Gerenciar turmas
(5) Gerenciar matrículas
(9) Sair\n""")
        opcao = input("Digite a opção desejada: ")
    
    #OPÇOES
        if opcao == "1":
            me.menu_2_estudante()

        elif opcao == "2":
            mp.menu_2_professor()

        elif opcao == "3":
            md.menu_2_disciplina()

        elif opcao == "4":
            tr.menu_2_turmas()

        elif opcao == "5":
            mt.menu_2_matriculas() 
        elif opcao == "9":
            break
        else:
            print("Opção inválida")
            input("Pressione ENTER para continuar")


menugeral()