import tkinter as tk
from tkinter import messagebox
import Gerenciar

priority_queue = Gerenciar.PriorityQueue()

def add_task():
    title = title_entry.get()
    description = description_entry.get()
    priority = priority_entry.get()

    if title and description and priority:
        try:
            priority = int(priority)
            if priority in [1, 2, 3, 4]:
                task = Gerenciar.Task(title, description, priority)
                priority_queue.add_task(task)
                title_entry.delete(0, tk.END)
                description_entry.delete(0, tk.END)
                priority_entry.delete(0, tk.END)
                messagebox.showinfo("Sucesso", "Tarefa adicionada com sucesso!")
            else:
                messagebox.showerror("Erro", "A prioridade deve ser um número entre 1 e 4.")
        except ValueError:
            messagebox.showerror("Erro", "A prioridade deve ser um número.")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos")

def remove_task():
    removed_task = priority_queue.remove_task()
    if removed_task:
        messagebox.showinfo("Sucesso", f"Tarefa removida: {removed_task.title}")
    else:
        messagebox.showinfo("Erro", "Não há tarefas na fila.")


def show_tasks():
    tasks = priority_queue.tasks
    task_list.delete(1.0, tk.END)
    if tasks:
        for _, task in tasks:
            task_list.insert(tk.END,
                             f"Título: {task.title}, Descrição: {task.description}, Prioridade: {task.priority}\n")
    else:
        task_list.insert(tk.END, "Não há tarefas na fila.")

root = tk.Tk()
root.title("Gerenciador de Tarefas")

tk.Label(root, text="Título da Tarefa").grid(row=0, column=0)
title_entry = tk.Entry(root)
title_entry.grid(row=0, column=1)

tk.Label(root, text="Descrição da Tarefa").grid(row=1, column=0)
description_entry = tk.Entry(root)
description_entry.grid(row=1, column=1)

tk.Label(root, text="Prioridade da Tarefa (1-Crítica, 2-Alta, 3-Média, 4-Baixa)").grid(row=2, column=0)
priority_entry = tk.Entry(root)
priority_entry.grid(row=2, column=1)

add_task_button = tk.Button(root, text="Adicionar Tarefa", command=add_task)
add_task_button.grid(row=3, column=0, columnspan=2)

remove_task_button = tk.Button(root, text="Remover Tarefa", command=remove_task)
remove_task_button.grid(row=4, column=0, columnspan=2)

show_tasks_button = tk.Button(root, text="Mostrar Tarefas", command=show_tasks)
show_tasks_button.grid(row=5, column=0, columnspan=2)

task_list = tk.Text(root, height=10, width=50)
task_list.grid(row=6, column=0, columnspan=2)

root.mainloop()