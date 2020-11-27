import pandas as pd 

def get_user_input(data_path):
    """
    This function simulates how to get data from the user 
    Here, we are only reading the file from a file path using pandas 
    we can extend this to a function that uses form or upload capabilty to get user data
    """
    data = pd.read_csv(data_path)
    return data 