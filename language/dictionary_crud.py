
store = {}
index = 0
print("CRUD with dictionary")

def crud(index):
    while True:
        print("")
        print("----------------------------")
        print("1: Create")
        print("2: Read")
        print("3: Update")
        print("4: Delete")
        print("5: Exit")
        print("----------------------------")
        print("")

        choice = input("-> ")

        match choice:
            case "1":
                name = input("Name : ")
                store[index] = name
                index = index + 1

            case "2":
                print("1: Read all")
                print("2: Read by index")

                readChoice = input("-> ")

                match readChoice:
                    case "1":
                        print(store)

                    case "2":
                        readIndex = int(input("Index : "))
                        if readIndex >= index or readIndex < 0:
                            print("Invalid index. Read operation failed")
                        else:
                            print(store[readIndex])
                    
            case "3":
                updateIndex = int(input("Index : "))
                if updateIndex >= index or updateIndex < 0:
                    print("Invalid index. Update operation failed")
                else:
                    print("Enter new name :")
                    newName = input("-> ")
                    store[updateIndex] = newName
            case "4":
                deleteIndex = int(input("index : "))
                if deleteIndex >= index or deleteIndex < 0:
                    print("invalid index. Delete operation failed")
                else:
                    del store[deleteIndex]
            case "5":
                break
            case _:
                print("Enter choice")

crud(index)
