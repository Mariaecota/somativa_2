import json
# A função carregar_lista é usada para carregar uma lista de um arquivo JSON. Ela verifica se o arquivo existe e o carrega. Se o arquivo não for encontrado, retorna uma lista vazia.#

# Função para carregar uma lista de um arquivo JSON





def carregar_lista(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            lista = json.load(arquivo)
        return lista
    except FileNotFoundError:
        return []
    









# A função verificar_codigo verifica se um código existe em uma lista. Ela percorre a lista e verifica se algum item possui o código especificado.


# Função para verificar se um código existe em uma lista
def verificar_codigo(codigo, lista):
    return any(item.get('codigo') == codigo for item in lista)




# Carregar listas de estudantes, professores e disciplinas
lista_estudantes = carregar_lista('estudantes.json')
lista_professores = carregar_lista('professores.json')
lista_disciplinas = carregar_lista('disciplinas.json')

# Perguntar ao usuário pelo código
codigo = input("Digite o código que deseja verificar: ")

# Verificar se o código é válido em alguma das listas
if verificar_codigo(codigo, lista_estudantes):
    print("O código pertence a um estudante.")
elif verificar_codigo(codigo, lista_professores):
    print("O código pertence a um professor.")
elif verificar_codigo(codigo, lista_disciplinas):
    print("O código pertence a uma disciplina.")
else:
    print("Código não encontrado em nenhuma lista.")
