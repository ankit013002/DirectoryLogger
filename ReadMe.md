# Log Directory Tree

This Python program logs the directory tree structure and optionally includes the content of files within the directories. The output is saved to a `directory_log.txt` file.

## Files

- `LogDir.py`: The main script that logs the directory tree.
- `directory_log.txt`: The file where the directory tree log is saved.
- `ReadMe.md`: This readme file.

## Usage

1. Run the `LogDir.py` script:
   ```sh
   python LogDir.py

Enter the directory path to log: /path/to/directory
Include directory 'subdir1'? (y/n): y
Include file 'file1.txt'? (y/n): y
Include directory 'subdir2'? (y/n): n
Include file 'file2.txt'? (y/n): y

Generated Directory Tree:
[D] subdir1
  - file1.txt
    Content: (file content)
- file2.txt
  Content: (file content)

Directory log saved to 'directory_log.txt'