
#open the model
import pickle
import predictor

modeller = pickle.load(open('yeah_model.pickle','rb'))
test_lines = predictor.csv_opener()






