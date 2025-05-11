import pandas as pd


def open_excel_sheet(file_path, sheet_name=0):

    """
    Opens an Excel sheet and returns it as a pandas DataFrame.
    """

    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        return df
    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'")
        return None
    except ValueError:
         print(f"Error: Sheet '{sheet_name}' not found in '{file_path}'")
         return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


# Example usage:
file_path = "C:\\Users\\jrath\\OneDrive\\Desktop\\Kontent.xlsx"
df = open_excel_sheet(file_path)

if df is not None:
    print(df)
