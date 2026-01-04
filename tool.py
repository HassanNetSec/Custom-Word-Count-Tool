import sys

def wcTool():
    """
    Main function that handles the word count tool logic.
    Supports file input and stdin (pipe) input with various options.
    """
    # Parse command line arguments
    if len(sys.argv) == 3:
        # Format: python tool.py -c file.txt (option + filename)
        option = sys.argv[1]
        filename = sys.argv[2]
        
        # Execute appropriate function based on the option
        if option == '-c':
            character_or_byte_count_by_filename(filename)
        elif option == '-l':
            totalLine_by_filename(filename)
        elif option == '-w':
            worldCount_by_filename(filename)
        else:
            # Invalid option, print all stats
            print_all_stats(filename)
    
    elif len(sys.argv) == 2:
        # Could be: python tool.py file.txt OR cat file.txt | python tool.py -l
        arg = sys.argv[1]
        
        if arg.startswith('-'):
            # It's an option for stdin: cat file.txt | python tool.py -l
            content = sys.stdin.read()
            
            if arg == '-c':
                print(f"  {len(content.encode('utf-8'))}")
            elif arg == '-l':
                print(f"  {len(content.splitlines())}")
            elif arg == '-w':
                print(f"  {len(content.split())}")
            else:
                # Invalid option, print all stats
                lines = len(content.splitlines())
                words = len(content.split())
                bytes_count = len(content.encode('utf-8'))
                print(f"  {lines}  {words} {bytes_count}")
        else:
            # It's a filename: python tool.py file.txt
            print_all_stats(arg)
    
    else:
        # No arguments: cat file.txt | python tool.py
        content = sys.stdin.read()
        lines = len(content.splitlines())
        words = len(content.split())
        bytes_count = len(content.encode('utf-8'))
        print(f"  {lines}  {words} {bytes_count}")


def character_or_byte_count_by_filename(filename: str):
    """
    Count the number of bytes in a file.
    
    Args:
        filename (str): Path to the file to be analyzed
    
    Output:
        Prints byte count and filename in format: "  <count> <filename>"
    """
    try:
        with open(filename, 'rb') as fs:  # Open in binary mode for accurate byte count
            byte_count = len(fs.read())
            print(f"  {byte_count} {filename}")
    except FileNotFoundError:
        print(f"ccwc: {filename}: No such file or directory", file=sys.stderr)
    except Exception as e:
        print(f"ccwc: {filename}: {str(e)}", file=sys.stderr)


def totalLine_by_filename(filename: str):
    """
    Count the number of lines in a file.
    
    Args:
        filename (str): Path to the file to be analyzed
    
    Output:
        Prints line count and filename in format: "  <count> <filename>"
    """
    try:
        with open(filename, 'r', encoding='utf-8') as fs:
            lines = len(fs.readlines())
            print(f"  {lines} {filename}")
    except FileNotFoundError:
        print(f"ccwc: {filename}: No such file or directory", file=sys.stderr)
    except Exception as e:
        print(f"ccwc: {filename}: {str(e)}", file=sys.stderr)


def worldCount_by_filename(filename: str):
    """
    Count the number of words in a file.
    Words are separated by whitespace (spaces, tabs, newlines).
    
    Args:
        filename (str): Path to the file to be analyzed
    
    Output:
        Prints word count and filename in format: "  <count> <filename>"
    """
    try:
        with open(filename, 'r', encoding='utf-8') as fs:
            words = len(fs.read().split())
            print(f"  {words} {filename}")
    except FileNotFoundError:
        print(f"ccwc: {filename}: No such file or directory", file=sys.stderr)
    except Exception as e:
        print(f"ccwc: {filename}: {str(e)}", file=sys.stderr)


def print_all_stats(filename: str):
    """
    Print all statistics for a file: lines, words, and bytes.
    This mimics the default behavior of the Unix wc command.
    
    Args:
        filename (str): Path to the file to be analyzed
    
    Output:
        Prints all stats in format: "  <lines>  <words> <bytes> <filename>"
    """
    try:
        with open(filename, 'r', encoding='utf-8') as fs:
            content = fs.read()
            lines = len(content.splitlines())
            words = len(content.split())
            bytes_count = len(content.encode('utf-8'))
            print(f"  {lines}  {words} {bytes_count} {filename}")
    except FileNotFoundError:
        print(f"ccwc: {filename}: No such file or directory", file=sys.stderr)
    except Exception as e:
        print(f"ccwc: {filename}: {str(e)}", file=sys.stderr)


# Entry point: Execute the main function when script is run
if __name__ == "__main__":
    wcTool()
