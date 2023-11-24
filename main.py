def mainProgram():
    while True:
        print("Hello! Enter your choice:"
              "\n1. Open a Tab"
              "\n2. Close a Tab"
              "\n3. Switch Tab"
              "\n4. Display All Tabs"
              "\n5. Open Nested Tab"
              "\n6. Sort All Tabs"
              "\n7. Save Tabs"
              "\n8. Import Tabs"
              "\n9. Exit")
        option = input("")
        while not option.isdigit() or not (0 < int(option) <= 9):
            option = input("Please enter a valid option\t")


mainProgram()
