from feyncreation.common import config
from feyncreation.common.particles import particle_styles, particle_dict  # Import styles for different particles
import os
import readline
from feyncreation.diagram_input import twotwo_input, vbf1_input, vbf2_input

# Improved path completer for both directories and files
def complete_path(text, state):
    """Function for path autocompletion."""
    if '~' in text:
        text = os.path.expanduser(text)
    
    line = readline.get_line_buffer()
    if os.path.isdir(text):
        return [os.path.join(text, name) + ('/' if os.path.isdir(os.path.join(text, name)) else '') 
                for name in os.listdir(text)][state]
    else:
        dirpath = os.path.dirname(text)
        filename = os.path.basename(text)
        return [os.path.join(dirpath, name) for name in os.listdir(dirpath or '.') 
                if name.startswith(filename)][state]

def setup_readline():
    """Set up the tab completion for paths."""
    readline.set_completer_delims(' \t\n=')
    readline.parse_and_bind("tab: complete")
    readline.set_completer(complete_path)

def parse_input_card(card_path):
    """Parses an input card and returns a dictionary of input values."""
    input_data = {}
    with open(card_path, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.split('=', 1)
                input_data[key.strip()] = value.strip().lower()
    return input_data

def get_user_input_from_card(card_path):
    """Generates a diagram based on the input card."""
    input_data = parse_input_card(card_path)
    diagram_class = input_data.get('diagram_class', 'twotwo')

    # Call the respective input handler based on the diagram class
    if diagram_class == 'twotwo':
        twotwo_input.handle_twotwo_card(input_data)
    elif diagram_class == 'vbf1':
        vbf1_input.handle_vbf1_card(input_data)
    elif diagram_class == 'vbf2':
        vbf2_input.handle_vbf2_card(input_data)
    else:
        print(f"Diagram class '{diagram_class}' not recognized.")

def get_user_input():
    """Main user input handler for feyncreation."""
    setup_readline()  # Enable tab completion
    
    # Print available particles at the start
    print("Available particles:")
    print(", ".join(particle_dict.keys()))
    
    use_card = input("Do you want to use an input card? (yes/no): ").lower()
    if use_card == 'yes':
        card_path = input("Enter the path to the input card: ").strip()
        if os.path.exists(card_path):
            get_user_input_from_card(card_path)
        else:
            print(f"Input card '{card_path}' not found.")
    else:
        diagram_class = input("Enter the class of diagram (e.g., 'twotwo', 'vbf1', 'vbf2'): ").lower()
        
        if diagram_class == 'twotwo':
            twotwo_input.handle_twotwo_input()
        elif diagram_class == 'vbf1':
            vbf1_input.handle_vbf1_input()
        elif diagram_class == 'vbf2':
            vbf2_input.handle_vbf2_input()
        else:
            print(f"Diagram class '{diagram_class}' not recognized.")

if __name__ == "__main__":
    get_user_input()

