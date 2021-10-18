import pickle

file_path = 'data_cellphones.pkl'

with open(file_path, 'rb') as f:
    x = pickle.load(f)
print(x)