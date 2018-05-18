# AI4IntelligentCustomerCare Accenture Hackathon

# Clustering based on customer classic info and Social affinities
This is an implementation of clustering algorithms for a consumer dataset. It was developped in 2 days for an internal Accenture hackathon.
The dataset can't not be published. You can find dummy examples in the file [clusters-examples.csv](clusters-examples.csv).

Authors: [Timo Johann](https://github.com/TimoJay), Cyril de Catheu  
Created: 17-05-2018  
Last Modified: 18-05-2018  
Tested on OS X Sierra, Windows 10  

## Requires:
Python >= ???: 
	Python package dependencies:  
		sklearn >= ???  
		numpy   >= ???  
		pandas  >= ???

## Prediction Technical Specifications:
### Data:
	The dataset was provided in the context of the an internal Accenture Hackathon. It will not be made public.  

 
### Input Features :
consumer_id - Not used  
exact_age - integer  
length_of_residence -  integer  
num_adults - integer  
gender - categorical  
homeowner - categorical   
pres_kids - categorical  
hh_marital_status - categorical   
dwell_type - categorical  
metro_nonmetro - categorical  
urban_rural_flag - categorical  
flag_pres_kids_true - categorical  
age_range - categorical  
consumer_id - Not used (duplicate)  
affinities - List of affinities ID  

### Feature encoding:
All categorical features are converted to binary using a one-hot encoder.  
The list of affinities ID is processed with a multiLabelBinarizer. This results in a very large number of columns. SEE NEXT STEPS.

### Feature normalization:
All numbers are scaled using a standard scaler. SEE NEXT STEPS (SHOULD BE REALS FEATURES ONLY)

### Machine Learning Algorithm:
#### KMeans

#### AffinityPropagation
		
#### AgglomerativeClustering
    
#### Birch

## Next Steps :	
Explore other solutions than multilabelBinarization on 50k values.
Normalize only real values.
Rework one-hot encoding.
Test other algorithms.
Tune  algorithms parameters.
PCA before/after clustering.
Run clustering on whole dataset, label the dataset with the results, run supervised algorithm to spot interesting features by clusters.


