import pandas as pd

def read_train_csv_data(file_path):
    try:
        train_data = pd.read_csv(file_path)
        return train_data
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("An error occurred:", e)

# Example usage
file_path = "path/to/your/train_data.csv"
train_data = read_train_csv_data(file_path)
print(train_data.head())
