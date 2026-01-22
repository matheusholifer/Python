import random

lista = [] # lista = list()

opcao = None # Cria uma váriavel sem valor

while opcao != 0:
    print("\n\tPress 0 to finish\n\tPress 1 to add an integer\n\tPress 2 to remove an integer\n\tPress 3 to view list status\n\tPress 4 to insert into a specified position\n\tPress 5 to remove all elements from the list.\n\tPress 6 to get the index of an element.\n\tPress 7 to count the number of times an element appears.\n\tPress 8 to sort the list items.\n\tPress 9 to reverse the order of the items in the list.")
    opcao = int(input("\t>>> "))

    match opcao:
        case 0:
            print("\nEnding the computer program...")

        case 1:
            numero = random.randint(1, 1000);
            lista.append(numero) # Adiciona um item ao fim da lista
            print(f"\nThe number {numero} was successfully entered!")

        case 2:
            removido = int(input("\nEnter the value you want to remove: "))
            if removido in lista:
                lista.remove(removido) # Remove o primeiro item cujo valor seja igual a x
                print(f"\nThe number {removido} was successfully removed!")
            else:
                print(f"The number {removido} is not on the list.")

        case 3:
            print(f"\nList data structure (size {len(lista)}): {lista}")

        case 4:
            numero = random.randint(1, 1000);
            posicao = int(input("\nEnter the position where you want to insert an element: "))
            lista.insert(posicao, numero) # Insere um item em uma posição dada.
            print(f"\nThe number {numero} was successfully entered!")

        case 5:
            lista.clear()  # Remove todos os itens da lista.
            if len(lista) == 0:
                print("\nAll items in the list were successfully removed.")

        case 6:
            numero = int(input("\nEnter the key of the element you wish to query: "))
            if numero in lista:
                print(f"\nThe index of the number {numero} is {lista.index(numero)}") # Retorna o índice do primeiro item com valor x

        case 7:
            numero = int(input("\nEnter the key of the element you wish to query: "))
            if numero in lista:
                print(f"The number {numero} appears {lista.count(numero)} time(s)") # Retorna o número de vezes que x aparece.

        case 8:
            lista.sort() # Ordena os itens da lista in place (na própria lista).
            print("List sorted successfully!")

        case 9:
            lista.reverse() # Inverte a ordem dos elementos.
            print("List elements successfully reversed!")

        case _: # Opção default
            print("\nInvalid option entered.")