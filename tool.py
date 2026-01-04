import sys

def wcTool():
    """
    Main function that handles the word count tool logic.
    Supports file input and stdin (pipe) input with various options.
    """
    # Check if filename is provided along with an option
    if len(sys.argv) > 2:
        filename = sys.argv[-1]  # Last argument is the filename
        option = sys.argv[1]      # First argument is the option flag
        
        # Execute appropriate function based on the option
        if option == '-c':
            character_or_byte_count_by_filename(filename)
        elif option == '-l':
            totalLine_by_filename(filename)
        elif option == '-w':
            worldCount_by_filename(filename)
        else:
            # If invalid option or no option, print all stats
            print_all_stats(filename)
    
    else:
        # Handle stdin input (when using pipes like: cat file.txt | python tool.py -l)
        content = sys.stdin.read()
        option = sys.argv[-1] if len(sys.argv) > 1 else None
        
        # Process stdin content based on the option
        if option == '-c':
            # Count bytes by encoding the content
            print(f"  {len(content.encode('utf-8'))}")
        elif option == '-l':
            # Count lines by splitting on newlines
            print(f"  {len(content.splitlines())}")
        elif option == '-w':
            # Count words by splitting on whitespace
            print(f"  {len(content.split())}")
        else:
            # Print all statistics if no specific option provided
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