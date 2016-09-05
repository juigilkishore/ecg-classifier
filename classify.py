# (c) 2016 JUIGIL KISHORE ALL RIGHTS RESERVED

import sys
import manager
import utilities


def main(file):
    ecg_test_samples = utilities.load_ecg_beat_file(file)
    ecg_test = {"untrained": ecg_test_samples}
    ecg_object_list = utilities.create_ecg_datatype(ecg_test)
    classifier = manager.Classifier(ecg_test_samples)
    print(classifier.LABEL)

if __name__ == "__main__":
    main(sys.argv[1])
