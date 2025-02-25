import os

def log_directory(path, depth=0):
    tree = ""
    indent = "  " * depth
    
    if not os.path.exists(path):
        print("Path does not exist!")
        return ""
    
    for entry in os.listdir(path):
        entry_path = os.path.join(path, entry)
        if os.path.isdir(entry_path):
            choice = input(f"Include directory '{entry}'? (y/n): ").strip().lower()
            tree += f"{indent}[D] {entry}\n"
            if choice == 'y':
                tree += log_directory(entry_path, depth + 1)
        else:
            choice = input(f"Include file '{entry}'? (y/n): ").strip().lower()
            if choice == 'y':
                with open(entry_path, 'r', encoding='utf-8', errors='ignore') as file:
                    content = file.read()
                    tree += f"{indent}- {entry}\n"
                    tree += f"{indent}  Content: {content}\n"
            else:
                tree += f"{indent}- {entry}\n"
    return tree

def main():
    start_path = input("Enter the directory path to log: ").strip()
    log_result = log_directory(start_path)
    print("\nGenerated Directory Tree:")
    print(log_result)
    
    with open("directory_log.txt", "w", encoding="utf-8") as log_file:
        log_file.write(log_result)
    print("Directory log saved to 'directory_log.txt'")

if __name__ == "__main__":
    main()
