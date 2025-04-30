tarefas = []

def adicionar():
    desc = input("Descrição: ")
    status = input("Status (Pendente/Concluído): ")
    tarefas.append({"desc": desc, "status": status})

def listar():
    for t in tarefas:
        print("Desc:", t["desc"], "- Status:", t["status"])

def concluir():
    d = input("Desc para concluir: ")
    for t in tarefas:
        if t["desc"] == d:
            t["status"] = "Concluído"

while True:
    print("1-Adicionar 2-Listar 3-Concluir 4-Sair")
    o = input("Escolha: ")
    if o == "1":
        adicionar()
    elif o == "2":
        listar()
    elif o == "3":
        concluir()
    elif o == "4":
        break

