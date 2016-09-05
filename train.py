# (c) 2016 JUIGIL KISHORE ALL RIGHTS RESERVED

import sys
import manager
import utilities


def main(file):
    # Load the ecg beat file
    ecg_training_samples = utilities.load_ecg_train_file(file)

    # Instantiate the ECGBeat object for every beat across all the ailments
    ecg_objects = utilities.create_ecg_datatype(ecg_training_samples)

    # Get the wavelet features for every beat across all the ailments
    ecg_features_list = utilities.get_ecg_features(ecg_objects)

    # Instantiate the CombinedNeuralNet algorithm to train the features
    algorithm = manager.CombinedNeuralNet(ecg_features_list)
    weights = algorithm.train()

if __name__ == "__main__":
    main(sys.argv[1])
