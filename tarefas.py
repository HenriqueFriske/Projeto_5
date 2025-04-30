tarefas = []


def criar_tarefa(descricao, status):
    tarefas.append({"descricao": descricao, "status": status})

def listar_tarefas():
    for tarefa in tarefas:
        print("Descrição:", tarefa["descricao"], "- Status:", tarefa["status"])

def concluir_tarefa(descricao):
    for tarefa in tarefas:
        if tarefa["descricao"] == descricao:
            tarefa["status"] = "Concluído"
while True:
    print("1-Adicionar 2-Listar 3-Concluir 4-Sair")
    opcao = input("Escolha: ")
    if opcao == "1":
        criar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        concluir_tarefa()
    elif opcao == "4":
        break
