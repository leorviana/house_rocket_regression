import pickle

class preprocessing(object):
    def __init__(self):
        self.scaler = pickle.load(open("scaler/mm_scaler.pkl", "rb"))
        
        
    def scaling(self, df):
        df = self.scaler.transform(df)
        
        return df