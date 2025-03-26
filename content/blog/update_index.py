import os
import fileinput
import sys


def update_config_line(file_path, search_pattern, replacement_line):
    """
    Find and update a specific line in a configuration file.

    Args:
    file_path (str): Path to the configuration file
    search_pattern (str): Pattern to match the line to be replaced
    replacement_line (str): The new line to replace the matched line

    Returns:
    bool: True if line was updated, False if line was not found
    """
    line_updated = False

    try:
        # Use file input to read and write the file in-place
        with fileinput.input(files=(file_path), inplace=True) as file:
            for line in file:
                # Check if the line matches the search pattern
                if search_pattern in line:
                    # Replace the line with the new line
                    print(replacement_line.rstrip())
                    line_updated = True
                else:
                    # Print the original line
                    print(line.rstrip())

    except IOError as e:
        print(f"Error accessing file: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

    return line_updated


def find_config_line(file_path, search_pattern):
    """
    Find a specific line in a configuration file.

    Args:
    file_path (str): Path to the configuration file
    search_pattern (str): Pattern to match the line to be found

    Returns:
    str or None: The matched line if found, None otherwise
    """
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if search_pattern in line:
                    return line.strip()
        return None

    except IOError as e:
        print(f"Error accessing file: {e}")
        return None


def update_config_index(new_index):

    # Example usage
    config_file = 'c:\\etc\\properties.ini'

    # Example 1: Find a specific line
    search_pattern = 'blog_index='
    found_line = find_config_line(config_file, search_pattern)
    if found_line:
        print(f"Found line: {found_line}")
    else:
        print(f"No line containing '{search_pattern}' found.")

    # Example 2: Update a specific line
    update_pattern = 'blog_index='
    new_line = 'blog_index=' + convert_to_three_digit_string(new_index)

    if update_config_line(config_file, update_pattern, new_line):
        print("Configuration line updated successfully.")
    else:
        print("Failed to update configuration line.")


def convert_to_three_digit_string(number):
    """
    Convert an integer to a three-digit string.

    Args:
    number (int): The input number to convert

    Returns:
    str: A three-digit string representation of the number

    Raises:
    ValueError: If the number is negative or greater than 999
    """
    # Validate input range
    if number < 0 or number > 999:
        raise ValueError("Number must be between 0 and 999")

    # Convert to three-digit string using zfill
    return f"{number:03d}"

if __name__ == "__main__":
    update_config_index(43)