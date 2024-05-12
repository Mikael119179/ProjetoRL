#temos o import heapq para fornece uma implementação de fila de prioridade.
import heapq
#representa um nó em uma lista encadeada.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#A classe Task é definida com três atributos: title, description e priority. Esses atributos representam as informações associadas a uma tarefa.
class Task:
    def __init__(self, title, description, priority):
        self.title = title
        self.description = description
        self.priority = priority
#Essa classe representa uma fila de prioridade, onde as tarefas são organizadas com base em sua prioridade.
class PriorityQueue:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        heapq.heappush(self.tasks, (task.priority, task))

    def remove_task(self):
        if self.tasks:
            return heapq.heappop(self.tasks)[1]
        else:
            return None
#representa uma lista encadeada.  ela possui os seguintes metodos 
class LinkedList:
    #O construtor inicializa os atributos head e tail como None.
    def __init__(self):
        self.head = None
        self.tail = None
# Adiciona um novo nó contendo data ao final da lista.
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
#Imprime os elementos da lista.
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")
#Chama o método append(data) para adicionar uma tarefa à lista.
    def add_task(self, data):
        self.append(data)
# Remove um nó com o valor data da lista.
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

#o progama começa um loop ate q o usuario escolha a opção 4
if __name__ == "__main__":
    priority_queue = PriorityQueue()

    while True:
        print("\nDigite:")
        print("1 - Adicionar tarefa")
        print("2 - Remover tarefa")
        print("3 - Mostrar lista de tarefas")
        print("4 - Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            title = input("Digite o título da tarefa: ")
            description = input("Digite a descrição da tarefa: ")
            priority = input("Digite a prioridade da tarefa (1-Crítica, 2-Alta, 3-Média, 4-Baixa): ")
            task = Task(title, description, int(priority))
            priority_queue.add_task(task)
        elif choice == "2":
            removed_task = priority_queue.remove_task()
            if removed_task:
                print(f"Tarefa removida: {removed_task.title}")
            else:
                print("Não há tarefas na fila.")
        elif choice == "3":
            print("Fila de tarefas:")
            for _, task in priority_queue.tasks:
                print(f"Título: {task.title}, Descrição: {task.description}, Prioridade: {task.priority}")
        elif choice == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


