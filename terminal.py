import os

current_directory = os.getcwd()

def create_directory(directory_name):
    try:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully!")
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists!")

def create_file(file_name):
    try:
        with open(file_name, 'w') as file:
            print(f"File '{file_name}' created successfully!")
    except:
        print(f"An error occurred while creating the file '{file_name}'.")

def list_directory_contents():
    contents = os.listdir(current_directory)
    if len(contents) == 0:
        print("The directory is empty.")
    else:
        print("Directory Contents:")
        for content in contents:
            print(content)

def change_directory(directory_name):
    try:
        os.chdir(directory_name)
        global current_directory
        current_directory = os.getcwd()
        print(f"Changed directory to '{current_directory}'")
    except FileNotFoundError:
        print(f"Directory '{directory_name}' does not exist!")
    except NotADirectoryError:
        print(f"'{directory_name}' is not a directory!")

def nano(file_name):
    try:
        os.system(f'nano {file_name}')
    except:
        print(f"An error occurred while opening the file '{file_name}' in nano.")

def command_prompt():
    print("Welcome to the Command Prompt!")
    print("Available commands: create_directory, create_file, list_directory, change_directory, nano, exit")

    while True:
        command = input("\nEnter a command: ")

        if command == "create_directory":
            directory_name = input("Enter the name of the directory: ")
            create_directory(directory_name)

        elif command == "create_file":
            file_name = input("Enter the name of the file: ")
            create_file(file_name)

        elif command == "list_directory":
            list_directory_contents()

        elif command == "change_directory":
            directory_name = input("Enter the name of the directory: ")
            change_directory(directory_name)

        elif command == "nano":
            file_name = input("Enter the name of the file: ")
            nano(file_name)

        elif command == "exit":
            print("Exiting the Command Prompt...")
            break

        else:
            print("Invalid command! Please try again.")

command_prompt()
