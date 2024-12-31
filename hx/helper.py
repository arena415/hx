import os

def load_snippets():
    """
    Reads the 'examples.txt' file, parses snippet categories and code, and
    returns a dictionary where:
      - key = snippet name, e.g., "cv2.Canny"
      - value = snippet code
    """
    # Get the directory where this file is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.join(current_dir, 'data', 'examples.txt')

    if not os.path.exists(data_file):
        raise FileNotFoundError(f"Cannot find 'examples.txt' at {data_file}")

    with open(data_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by lines
    lines = content.splitlines()

    # Initialize variables
    snippets_dict = {}
    current_key = None
    current_code = []

    for line in lines:
        # Detect a new snippet header like: === cv2.Canny ===
        if line.startswith('=== ') and line.endswith('==='):
            # If there's an existing snippet being built, store it
            if current_key and current_code:
                snippets_dict[current_key] = "\n".join(current_code).strip()
            # Reset for new snippet
            current_key = line.replace('===', '').strip()
            current_code = []
        else:
            # Accumulate code lines
            current_code.append(line)

    # Store the last snippet if any
    if current_key and current_code:
        snippets_dict[current_key] = "\n".join(current_code).strip()

    return snippets_dict

def fprint():
    """
    List all available snippet categories.
    """
    snippets_dict = load_snippets()
    if not snippets_dict:
        print("No snippets available.")
        return
    print("Available snippet categories:")
    for key in sorted(snippets_dict.keys()):
        print(f" - {key}")

def helpx(key):
    """
    Print out the snippet code for the given key.
    Example: helpx('cv2.Canny')
    """
    snippets_dict = load_snippets()
    if key in snippets_dict:
        print(f"=== {key} ===")
        print(snippets_dict[key])
    else:
        print(f"No snippet found for '{key}'")

def main():
    """
    Entry point for the command-line interface.
    Usage:
        - To list all snippets: helpx
        - To get a specific snippet: helpx <snippet_name>
    """
    import sys

    args = sys.argv[1:]

    if not args:
        # No arguments passed, list all snippets
        fprint()
    elif args[0] in ['-h', '--help']:
        print("Usage:")
        print("  helpx                List all available snippet categories.")
        print("  helpx <snippet_name> Show the code snippet for the given snippet name.")
    else:
        # Assume the first argument is the snippet key
        key = ' '.join(args)
        helpx(key)

