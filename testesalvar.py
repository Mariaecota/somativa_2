def opcaoadicionar():
    lista_turmas = me.carregar('turmas.json')
    lista_professores = me.carregar('professor.json')
    lista_disciplinas = me.carregar('disciplina.json')

    print("\n------ ADICIONAR ------")

    while True:
        try:
            codigo_turma = int(input("\nDigite o código da turma: "))
            
            # Verificar se o código da turma já existe em lista_turmas
            if any(turma['codigo_turma'] == codigo_turma for turma in lista_turmas):
                print("Esse código de turma já existe, digite um código válido")
            else:
                break  # Sai do loop se o código for válido
            
        except ValueError:
            print("\nValor inválido")
    
    while True:
        try: 
            codigo_professor = int(input("\nDigite o código do professor: "))
            
            # Verificar se o código do professor já existe em lista_professores
            if not any(professor['codigo_professor'] == codigo_professor for professor in lista_professores):
                print("Esse código de professor não existe, digite um código válido")
            else:
                break
            
        except ValueError:
            print("\nValor inválido")

    while True:
        try:
            codigo_disciplina = int(input("\nDigite o código da disciplina: "))
            
            # Verificar se o código da disciplina já existe em lista_disciplinas
            if not any(disciplina['codigo_disciplina'] == codigo_disciplina for disciplina in lista_disciplinas):
                print("Esse código de disciplina não existe, digite um código válido")
            else:
                break
                
        except ValueError:
            print("\nValor inválido")

    # DICIONARIO 
    dados = {
        'codigo_turma': codigo_turma,
        'codigo_professor': codigo_professor,
        'codigo_disciplina': codigo_disciplina,
    }

    lista_turmas.append(dados)
    me.salvar(lista_turmas, 'turmas.json')

    print(f"""
Dados incluídos com sucesso: 

Código da Turma: {codigo_turma}
Código do Professor: {codigo_professor}
Código da Disciplina: {codigo_disciplina}""")


