class Tarefa:
    def __init__(self, descricao, status="Pendente"):
        self.descricao = descricao
        self.status = status

    def concluir(self):
        self.status = "Concluído"

tarefas = []

def criar_tarefa(descricao, status):
    tarefas.append(Tarefa(descricao, status))

def listar_tarefas():
    for tarefa in tarefas:
        print("Descrição:", tarefa.descricao, "- Status:", tarefa.status)

def concluir_tarefa(descricao):
    for tarefa in tarefas:
        if tarefa.descricao == descricao:
            tarefa.concluir()

while True:
    print("1-Adicionar 2-Listar 3-Concluir 4-Sair")
    opcao = input("Escolha: ")
    match opcao:
        case "1":
            descricao = input("Descrição: ")
            status = input("Status (Pendente/Concluído): ")
            criar_tarefa(descricao, status)
        case "2":
            listar_tarefas()
        case "3":
            descricao = input("Descrição da tarefa a concluir: ")
            concluir_tarefa(descricao)
        case "4":
            break
        case _:
            print("Opção inválida.")