import pickle

with open('randomforest_pickle_kyle_92', mode='rb') as f:
    model = pickle.load(f)

with open('randomforest_pickle_kyle_92', mode='wb') as f:
    pickle.dump(model,f, pickle.HIGHEST_PROTOCOL)
    