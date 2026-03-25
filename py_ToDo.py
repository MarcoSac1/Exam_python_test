def main():
    tasks = []
    while True:
        print("\n ==== To-Do List ====")
        print("1 Aggiungi un task")
        print("2 Mostra tasks")
        print("3 Contrassegna come completo")
        print("4 Esci")
        scelta = input("seleziona l'azione da compiere:")

        if scelta == "1":
            print()
            num_task= int(input("quanti task vuoi aggiungere ?"))

            for i in range(num_task):
                task = input("Inserisci la tua scelta! ")
                tasks.append({"task": task, "Completo": False})
                print("Task aggiunto!")
        
        elif scelta == '2':
            print("\nTasks:")
            if not tasks:
                print("La lista dei task e' vuota:")
            else:
                for index, task in enumerate(tasks):
                    status = "Completo" if task["Completo"] else "Non completo"
                    print(f"{index + 1}. {task['task']} - {status}")

        elif scelta == '3':
            task_index = int(input("Inserisci il numero del task da segnare come completo!: "))
            if 0 <= task_index < len(tasks):
                tasks[task_index]['Completo'] = True
                print("Task segnato come completo!")
            else:
                print("Numero task non valido!")

        elif scelta == '4':
            print("Uscendo dalla To-Do List.")
            break

        else:
            print("scelta non valida riprova.")

if __name__ == "__main__":
    main()

