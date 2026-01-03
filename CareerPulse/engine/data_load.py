import pandas as pd

def load_dataset(path) :
    try :
        df = pd.read_csv(path)
        return df
    except :
        print(10*"-")
        print("Error in loading dataset")
        print(10*"-")
        return None