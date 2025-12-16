from typing import Dict 
import pandas as pd

def read_csv(FILENAME):
    
    df = pd.read_csv(FILENAME, na_values=["", "NaN", "NULL", "--"])
    return df.to_dict(orient="list")

def write_csv(new_file_name: str, data: Dict, new_data: Dict) -> None:
    current_data = pd.DataFrame(data)
    new_entry_df = pd.DataFrame([new_data]) # wrap in list to create single-row DataFrame, since new_data is a simple dict, not dict of lists
    updated_data = pd.concat([current_data, new_entry_df], ignore_index=True)

    updated_data.to_csv(new_file_name, index=False)
    print("UPDATED DATA:", updated_data)
    return updated_data


def main():
    filename = "csv_sample.csv"

    # Read current config without truncating the file
    csv_content_dict = read_csv(filename)
    print(csv_content_dict)

    

    # Persist changes
    new_file_name = "updated_csv_sample.csv"
    new_entry = {"col_a": "John Doe", "col_b": 30, "col_c": 300} # simple dictionary, not dictionary of lists.
    


    updated_data = write_csv(new_file_name,  csv_content_dict, new_entry)
    
    updated_data.dropna(subset = ["col_b", "col_c"], inplace=True)
    print("DATA AFTER DROPPING NA:", "\n", updated_data)

    


if __name__ == "__main__":
   main()

