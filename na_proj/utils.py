import json

# Path to your JSON file
JSON_FILE_PATH = r"C:\Users\FAHIM\OneDrive\Documents\Desktop\proj.json"

def get_username():
    """Reads the JSON file and returns the username."""
    try:
        with open(JSON_FILE_PATH, 'r') as file:
            data = json.load(file)
        return data["db"]["username"]
    except FileNotFoundError:
        print("The JSON file was not found at the specified path.")
    except KeyError as e:
        print(f"Key error: {e} - Please check your JSON structure.")
    except json.JSONDecodeError:
        print("Error decoding JSON. Please ensure the file is formatted correctly.")
    return None  # Return None if an error occurs

def get_password():
    """Reads the JSON file and returns the password."""
    try:
        with open(JSON_FILE_PATH, 'r') as file:
            data = json.load(file)
        return data["db"]["password"]
    except FileNotFoundError:
        print("The JSON file was not found at the specified path.")
    except KeyError as e:
        print(f"Key error: {e} - Please check your JSON structure.")
    except json.JSONDecodeError:
        print("Error decoding JSON. Please ensure the file is formatted correctly.")
    return None  # Return None if an error occurs

