
#open the model
import pickle
import predictor

modeller = pickle.load(open('yeah_model.pickle','rb'))
model = modeller['model']
test_lines = predictor.csv_opener()

#FIXME ONLY FOR DEBUG
test_lines = test_lines[:10]

for i in range(len(test_lines)):
    test_lines[i] = test_lines[i].split(" ")
    test_lines[i] = [0 if e =='NULL' else e for e in test_lines]
test_lines_processed = [predictor.inputDataPreProcessor(line, modeller['mlb'], modeller['le3'], modeller['le4'], modeller['le5'], modeller['le6'], modeller['le7'], modeller['le8'], modeller['le9'], modeller['le11'],modeller['encoder'],modeller['scaler']) for line in test_lines]
Y = [model.predict([l])[0] for l in test_lines_processed]

print(test_lines)
print(test_lines_processed)
print(Y)









