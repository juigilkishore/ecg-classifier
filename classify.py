# (c) 2016 JUIGIL KISHORE ALL RIGHTS RESERVED

import sys
import manager
import utilities


def main(file):
    ecg_samples = utilities.load_ecg_sample_file(file)
    classifier = manager.Classifier(ecg_samples)
    print(classifier.LABEL)

if __name__ == "__main__":
    main(sys.argv[1])
