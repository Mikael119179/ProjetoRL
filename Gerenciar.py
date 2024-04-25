class Gerenciar:
    def __init__(self):
        self.lista_tarefa = {}

    def add(self, tarefa):
        key = len(self.lista_tarefa) + 1
        self.lista_tarefa[key] = tarefa
        print("Tarefa adicionada com sucesso!")
        print(self.lista_tarefa)

    def remove(self, tarefa):
        for i, j in self.lista_tarefa.items():
            if j == tarefa:
                self.lista_tarefa.pop(i)
                print("Tarefa removida com sucesso!")
                return
            print("Tarefa não encontrada.")

    def att(self):
        print("Status: ")
        for i, j in self.lista_tarefa.items():
            print(f"{i} - {j}")


gerenciador = Gerenciar()

while True:

    print("\nAperte:")
    print("1 - Adicionar")
    print("2 - Remover")
    print("3 - Atualizar")
    print("4 - Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        tarefa = input("Digite o nome da tarefa a ser adicionada: ")
        gerenciador.add(tarefa)
    elif opcao == "2":
        tarefa = input("Digite o nome da tarefa a ser removida: ")
        gerenciador.remove(tarefa)
    elif opcao == "3":
        gerenciador.att()
    elif opcao == "4":
        print("Saindo...")
        break
    else:
            print("Opção inválida. Por favor, digite um número de 1 a 4.")

