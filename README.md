# AI4IntelligentCustomerCare Accenture Hackathon

# Clustering based on customer classic info and Social affinities
This is an implementation of clustering algorithms for a consumer dataset. It was developped in 2 days for an internal Accenture hackathon.
The dataset can't not be published. You can find dummy examples in the file [clusters-examples.csv](clusters-examples.csv).

Authors: [Timo Johann](https://github.com/TimoJay), Cyril de Catheu  - Fast paced pair programming  
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
The list of affinities ID is processed with a multiLabelBinarizer. This results in a very large number of columns. 

### Feature normalization:
All numbers are scaled using a standard scaler.

### Machine Learning Algorithm:
The detailed results of the different algorithms will not be made public.
#### KMeans
No interesting results. Too dig

#### AffinityPropagation
Really promising results, 4 relevant clusters.
		
#### AgglomerativeClustering
Not tested in depth
    
#### Birch
Not tested in depth

## Next Steps :
Explore other solutions than multilabelBinarization on 50k values.
Normalize only real values?
Rework one-hot encoding.
Test other algorithms.
Consider only some types of affinities (using the taxonomy of the activities)
Tune  algorithms parameters.
PCA before/after clustering.
Run clustering on whole dataset, label the dataset with the results, run supervised algorithm to spot interesting features by clusters.


