import os

current_directory = os.getcwd()
commands = ["create_directory", "create_file", "list_directory", "change_directory", "nano", "exit"]

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

        if command == "exit":
            print("Exiting the Command Prompt...")
            break

        elif command in commands:
            print(f"Command '{command}' found!")

        else:
            print("Invalid command! Please try again.")

        if command != "exit":
            autocomplete_command(command)

def autocomplete_command(command):
    matching_commands = [c for c in commands if c.startswith(command)]

    if len(matching_commands) == 1:
        completed_command = matching_commands[0]
        print(f"Autocompleted command: {completed_command}")
    elif len(matching_commands) > 1:
        print("Too many options! Add more context to the word for autocomplete!")

command_prompt()
