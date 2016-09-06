# (c) 2016 JUIGIL KISHORE ALL RIGHTS RESERVED

import sys
import manager
import utilities


def main(file):
    # Load the ecg beat file
    data_matrix, label_matrix = utilities.load_train_file(file)

    # Get the wavelet features for every beat across all the ailments
    ecg_features = utilities.get_features(data_matrix)

    # Instantiate the CombinedNeuralNet algorithm to train the features
    algorithm = manager.CombinedNeuralNet(ecg_features, label_matrix)
    weights = algorithm.train()

if __name__ == "__main__":
    main(sys.argv[1])
