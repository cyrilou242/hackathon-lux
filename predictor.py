import pickle
import csv
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, MultiLabelBinarizer, StandardScaler
from sklearn.cluster import KMeans

def inputDataPreProcessor(inputData,mlb, le3, le4, le5, le6, le7, le8, le9, le11, encoder,scaler):
    """Takes in input a line from merged_table that was transformed in a list (or one line dataframe),
    transform it into a line that can be used by our model"""

    """MLB step"""
    #create a copy of the input list
    inputData_processed = inputData[:]
    #transform strin list into list of string in last column
    inputData_processed[-1] = inputData_processed[-1].split(",")

    #mlb in last column
    mlb_affinites = mlb.transform([inputData_processed[-1]])

    #delete old line
    del inputData_processed[-1]

    #add new mlb list to input_data
    inputData_processed += [int(e) for e in mlb_affinites[0]]


    """label encoding"""
    inputData_processed[3] = le3.transform([inputData_processed[3]])[0]
    inputData_processed[4] = le4.transform([inputData_processed[4]])[0]
    inputData_processed[5] = le5.transform([inputData_processed[5]])[0]
    inputData_processed[6] = le6.transform([inputData_processed[6]])[0]
    inputData_processed[7] = le7.transform([inputData_processed[7]])[0]
    inputData_processed[8] = le8.transform([inputData_processed[8]])[0]
    inputData_processed[9] = le9.transform([inputData_processed[9]])[0]
    inputData_processed[11] = le11.transform([inputData_processed[11]])[0]


    #we convert the remaning strings into ints
    inputData_processed =[float(e) for e in inputData_processed]

    """oneHotEncoding"""
    inputData_processed = encoder.transform([inputData_processed])[0]

    """Scaler"""
    inputData_processed = scaler.transform([inputData_processed])[0]

    return inputData_processed

def main(data_string, filename="model.pickle"):
    '''Load a model, then realize a prediction
    Input : line with same layout as in csv merged_Table'''

    #we suppose the filename is good and the model exists

    #open the model
    modeller = pickle.load(open(filename, 'rb'))

    #data will first come as a json through api call, but we supposed there are sent there as a coma separated string line
    inputData = data_string.split(" ") #TODO change separator if it's easier
    #removing NULL value
    inputData = [0 if e =='NULL' else e for e in inputData]

    input_processed_data = inputDataPreProcessor(inputData, modeller['mlb'], modeller['le3'], modeller['le4'], modeller['le5'], modeller['le6'], modeller['le7'], modeller['le8'], modeller['le9'], modeller['le11'],modeller['encoder'],modeller['scaler'])

    prediction = modeller['model'].predict([input_processed_data])

    return prediction


def excel_string_to_call_string(string):
    """USELESS Function to be able to copy paste lines from csv opened in excel
    Not really usefull for us but may be usefull for functional team"""
    """Form of line from csv opened in excel:
    1753340, 70, 41.0, 1.0, F, H, NULL, S, S, Metro, Urban, 0, 61 - 70, 1753340, "a1010,a17899,a31722,a31723,a42311,a42338,a48058,a7401,a792,a163,a2023,a31729,a54370,a114,a17706,a31728,a33321,a54366,a31230,a672,a704,a10242,a110,a42318,a791,a132,a193,a54471,a717,a397,a542,a100,a111,a164,a183,a245,a33320,a790,a127,a146,a151,a42132" """
    list_temp = string.split(', ')
    del list_temp[0]
    del list_temp[12]
    affinities_replacement = list_temp[-1].replace('"','')
    del list_temp[-1]
    list_temp.append(affinities_replacement)
    print(list_temp)
    s=""
    for e in list_temp:
        s+= e + " "
    s = s[:-1]
    return(s)

def csv_list_to_call_string(csv_list):
    """Function to be able to use main directly on csv lines"""
    list_temp = csv_list[:]
    del list_temp[0]
    del list_temp[12]
    s=""
    for e in list_temp:
        s+= e + " "
    s = s[:-1]
    return(s)


def csv_opener(filepath="model.pickle"):
    """open a csv file and return a list of string callable by the main function"""
    with open('merged_Table.csv') as csvfile:
        data = list(csv.reader(csvfile))
        data = data
        data.pop(0)
    data_string = [csv_list_to_call_string(e) for e in data]
    return data_string

"""This is the form of the input string I decided. It is different from the one in dataset sry"""
string1 = "70 41 1.0 F H NULL S S Metro Urban 0 61-70 a1010,a17899,a31722,a31723,a42311,a42338,a48058,a7401,a792,a163,a2023,a31729,a54370,a114,a17706,a31728,a33321,a54366,a31230,a672,a704,a10242,a110,a42318,a791,a132,a193,a54471,a717,a397,a542,a100,a111,a164,a183,a245,a33320,a790,a127,a146,a151,a42132"
prediction1 = main(string1, "yeah_model.pickle")

print(prediction1)

test_lines=csv_opener()[:5]

for v in test_lines:
    print(main(v,"yeah_model.pickle"))

