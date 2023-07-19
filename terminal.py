import os

current_directory = os.getcwd()

def execute_command(command):
    global current_directory

    parts = command.split()
    command_name = parts[0]

    if command_name == "mkdir":
        directory_name = parts[1]
        path = os.path.join(current_directory, directory_name)
        
        try:
            os.mkdir(path)
            print(f"Directory '{directory_name}' created successfully.")
        except FileExistsError:
            print(f"Directory '{directory_name}' already exists.")
        except Exception as e:
            print(f"An error occurred while creating the directory: {e}")
    
    elif command_name == "make":
        file_name = parts[1]
        file_content = " ".join(parts[2:])
        file_path = os.path.join(current_directory, file_name)

        try:
            with open(file_path, "w") as file:
                file.write(file_content)
            print(f"File '{file_name}' created successfully.")
        except Exception as e:
            print(f"An error occurred while creating the file: {e}")

    elif command_name == "ls":
        try:
            files = os.listdir(current_directory)
            print("Contents of the current directory:")
            for file in files:
                print(file)
        except Exception as e:
            print(f"An error occurred while listing the directory contents: {e}")

    elif command_name == "cd":
        try:
            if len(parts) > 1:
                directory_name = parts[1]
                current_directory = os.path.join(current_directory, directory_name)
            else:
                current_directory = os.path.expanduser("~")
            
            os.chdir(current_directory)
            print(f"Changed directory to '{current_directory}'")
        except Exception as e:
            print(f"An error occurred while changing the directory: {e}")

    else:
        print(f"Command '{command_name}' not recognized.")

def main():
    print("Welcome to the Terminal Simulator!")
    print("Enter 'exit' to quit the program.")

    while True:
        command = input(f"\n{current_directory} $ ")
        if command == "exit":
            break
        
        execute_command(command)

if __name__ == "__main__":
    main()