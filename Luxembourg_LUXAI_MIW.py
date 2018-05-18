"""LUX AI
Timo Johann, Cyril de Catheu
05/18/2018
Demonstration of our clustering solution for AI Hackathon Customer Care on SocialStat 2018"""

import Model_Training
import Model_Analyser
from collections import Counter



def main():
    """Starts demo"""
    BUILD_MODEL = False
    csvfile = 'StatSocialJoinedData.csv'  # The StatSocialData ,2 files joined on consumerID with sql
    CLUSTERING_ALGORITHM = "AffinityPropagation"  # possible values: KMeans, AffinityPropagation; AgglomerativeClustering; Birch
    if(BUILD_MODEL):
        Model_Training.train(CLUSTERING_ALGORITHM, csvfile, 8000)

    clusters = Model_Analyser.analyse(CLUSTERING_ALGORITHM, 7999)
    print(clusters)
    cluster_results = Counter(clusters)
    print(str(len(cluster_results.keys())) + " clusters identified")
    print(cluster_results)


if __name__ == "__main__":
    main()