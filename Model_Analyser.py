"""LUX AI
Timo Johann, Cyril de Catheu
05/18/2018
Purpose of the file : script to test different models.
"""

import pickle
import Model_Predictor


def analyse(clustering_algorithm, ntuples=100):
    print("START CLUSTERING")
    if (clustering_algorithm == "KMeans"):
        filename = "model_lux_ai_kmeans"
    elif (clustering_algorithm == "AffinityPropagation"):
        filename = "model_lux_ai_aff"
    elif (clustering_algorithm == "AgglomerativeClustering"):
        filename = "model_lux_ai_agg"
    elif (clustering_algorithm == "Birch"):
        filename = "model_lux_ai_birch"
    else:  # Default KMeans

        filename = "model_lux_ai_kmeans"

    #open the model
    modeller = pickle.load(open(filename + ".pickle",'rb'))
    model = modeller['model']
    test_lines = Model_Predictor.csv_opener()

    #Running on 25% of dataset is enough for testing
    test_lines = test_lines[:ntuples]

    #Cleanning lines: formating and removing NULL values
    test_lines2 = []
    for i in range(len(test_lines)):
         test_lines[i] = test_lines[i].split(" ")
         test_lines2.append([0 if e =='NULL' else e for e in test_lines[i]])

    #Process lines :mlb, le,encoder,scaler
    test_lines_processed = [Model_Predictor.inputDataPreProcessor(line, modeller['mlb'], modeller['le3'], modeller['le4'], modeller['le5'], modeller['le6'], modeller['le7'], modeller['le8'], modeller['le9'], modeller['le11'], modeller['encoder'], modeller['scaler']) for line in test_lines2]

    #Return clusters for all lines
    #depending on model loaded, change fit_predict by predict
    if(clustering_algorithm == 'Birch'):
        Y = [model.fit_predict([l])[0] for l in test_lines_processed]
    else:
        Y = [model.predict([l])[0] for l in test_lines_processed]

    print("ANALYSIS FINISHED \n Classification succcessful")
    return Y










