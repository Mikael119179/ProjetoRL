class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def add_task(self, data):
        self.append(data)

    def remove_task(self, data):
        current_node = self.head
        previous_node = None
        while current_node:
            if current_node.data == data:
                if previous_node:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                if current_node == self.tail:
                    self.tail = previous_node
                return
            previous_node = current_node
            current_node = current_node.next


if __name__ == "__main__":
    linked_list = LinkedList()

    while True:
        print("\nDigite:")
        print("1 - Adicionar tarefa")
        print("2 - Remover tarefa")
        print("3 - Mostrar lista de tarefas")
        print("4 - Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            task = input("Digite o nome da tarefa a ser adicionada: ")
            linked_list.add_task(task)
        elif choice == "2":
            task = input("Digite o nome da tarefa a ser removida: ")
            linked_list.remove_task(task)
        elif choice == "3":
            print("Lista de tarefas:")
            linked_list.print_list()
        elif choice == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
