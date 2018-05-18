"""LUX AI
Timo Johann, Cyril de Catheu
05/18/2018
Purpose of the file : Module to preprocess the data,
create the different encoders and create and save a prediction model"""

import sys
sys.setrecursionlimit(1000000000)

import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, MultiLabelBinarizer, StandardScaler
from sklearn.cluster import KMeans, AffinityPropagation, AgglomerativeClustering, Birch

csvfile = 'DataServices_StatSocial_Taxonomy.csv' #The StatSocialData ,2 files joined on consumerID with sql
CLUSTERING_ALGORITHM = "KMeans" #possible values: KMeans, AffinityPropagation; AgglomerativeClustering; Birch

def spliter(element):
    return element.split(",")


def preprocess(filename, ntuples):
    df2 = pd.read_csv(filename)

    df = df2[:ntuples]

    del df['dataservices_datastream_raw_consumer_id']
    # Transform string list into list of string
    #df['affinities'] = pd.Series(df['dataservices_statsocial_raw_affinities'].apply(spliter), index=df.index)
    df = df.assign(affinities=pd.Series(df['dataservices_statsocial_raw_affinities'].apply(spliter)))

    # delete old list of affinities
    del df["dataservices_statsocial_raw_affinities"]

    #deleting the id column added during join
    del df["dataservices_statsocial_raw_consumer_id"]

    #binarize the affinities
    mlb = MultiLabelBinarizer()
    X = mlb.fit_transform(df["affinities"])
    df = df.join(pd.DataFrame(X, columns=mlb.classes_))

    #deleting the old addinities column
    del df["affinities"]

    #fill nan values
    df.replace([np.inf, -np.inf], np.nan)
    df = df.fillna(0)
    return df,mlb


def train(CLUSTERING_ALGORITHM, input_data, ntuples=2000):
    print("START TRAINING - Get a coffee")
    #first prepocessing steps
    data, mlb = preprocess(input_data, ntuples)


    #Transtype the df to np array to fit into sklearn functions
    data_array = data.values

    """Processing of all the string columns (categorical values)"""
    #create label encoder for each of the categorical values
    #column 3
    le3 = LabelEncoder()
    new_column3 = le3.fit_transform(data_array[:, 3].astype(str))
    # replace old column with integers
    data_array[:, 3] = new_column3

    #column 4
    le4 = LabelEncoder()
    new_column4 = le4.fit_transform(data_array[:, 4].astype(str))
    # replace old column with integers
    data_array[:, 4] = new_column4

    #column 5
    le5 = LabelEncoder()
    new_column5 = le5.fit_transform(data_array[:, 5].astype(str))
    # replace old column with integers
    data_array[:, 5] = new_column5

    #column 6
    le6 = LabelEncoder()
    new_column6 = le6.fit_transform(data_array[:, 6].astype(str))
    # replace old column with integers
    data_array[:, 6] = new_column6

    #column 7
    le7 = LabelEncoder()
    new_column7= le7.fit_transform(data_array[:, 7].astype(str))
    # replace old column with integers
    data_array[:, 7] = new_column7

    #column 8
    le8 = LabelEncoder()
    new_column8= le8.fit_transform(data_array[:, 8].astype(str))
    # replace old column with integers
    data_array[:, 8] = new_column8

    #column 9
    le9 = LabelEncoder()
    new_column9= le9.fit_transform(data_array[:, 9].astype(str))
    # replace old column with integers
    data_array[:, 9] = new_column9

    #column 11
    le11 = LabelEncoder()
    new_column11= le11.fit_transform(data_array[:, 11].astype(str))
    # replace old column with integers
    data_array[:, 11] = new_column11

    #transtyping the remaining string column
    data_array = data_array.astype(np.float64)

    #one hot encoding of all labelEncoded columns
    enc = OneHotEncoder('auto', [3,4,5,6,7,8,9,11], sparse=False)
    enc = enc.fit(data_array)
    data_array = enc.transform(data_array)

    #Scaling of the data
    scaler = StandardScaler()
    scaledData = scaler.fit_transform(data_array)


    """All algorithms that were tested. 
    Uncomment one and comment the others.
    Don't forget to change the pickle dump filename"""

    #possible values: KMeans, AffinityPropagation; AgglomerativeClustering; Birch
    if (CLUSTERING_ALGORITHM == "KMeans"):
        kmeans = KMeans(n_clusters=14)
        model = kmeans.fit(scaledData)
        filename = "model_lux_ai_kmeans"
    elif(CLUSTERING_ALGORITHM == "AffinityPropagation"):
        aff = AffinityPropagation()
        model = aff.fit(scaledData)
        filename = "model_lux_ai_aff"
    elif(CLUSTERING_ALGORITHM == "AgglomerativeClustering"):
        agg = AgglomerativeClustering(n_clusters=8, affinity='cosine', linkage='average');
        model = agg.fit(scaledData);
        filename = "model_lux_ai_agg"
    elif(CLUSTERING_ALGORITHM == "Birch"):
        birch = Birch(n_clusters=8)
        model = birch.fit(scaledData)
        filename = "model_lux_ai_birch"
    else: #Default KMeans
        kmeans = KMeans(n_clusters=14)
        model = kmeans.fit(scaledData)
        filename = "model_lux_ai_kmeans"

    #Saving model, data and every processing functions into pickle binary
    pickle.dump({'model': model, 'data': scaledData,'mlb': mlb , 'le3': le3, 'le4': le4, 'le5': le5, 'le6': le6, 'le7': le7, 'le8': le8, 'le9': le9, 'le11': le11,'encoder': enc, 'scaler': scaler}, open(filename + ".pickle", 'wb'))

    #Transform the non scaled data into dataframe again to write it into csv
    #This csv file has business value
    final = pd.DataFrame(data=data_array[1:,1:], index=data_array[1:,0], columns=data_array[0,1:])
    final.to_csv('statsocial_preprocessed-notScaled.csv')
    print("TRAINING Finished \n Model succcessfully trained")

