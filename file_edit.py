import pickle


def pickle_save(file, add):
    with open(add, 'wb') as handle:
        pickle.dump(file, handle, protocol=pickle.HIGHEST_PROTOCOL)

def pickle_read(add):
    with open(add, 'rb') as handle:
        b = pickle.load(handle)
    return b