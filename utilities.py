# (c) 2016 JUIGIL KISHORE ALL RIGHTS RESERVED

import numpy

import features
import manager

from constants import WAVELET_DECOMPOSITION_LEVEL, MOTHER_WAVELET


def load_ecg_beat_file(file_path):
    """Load a ecg file - single beat (.csv file)

    :param file_path: Path of the single ecg beat file
    :return: ecg single beat data from the file as list
    """
    # TODO: Complete this
    with open(file_path, 'r') as ecg_beat:
        pass
    return


def load_train_file(file_path):
    """Load a ecg file - single beat for different heart ailments

    :param file_path: Path of the single ecg beat file
    :return: Numpy matrix of ecg beat data (N x samples)and
             Numpy matrix of mapped heart ailment (N x 4)
    """
    # TODO: Complete this
    ecg_data = None
    ecg_label = None
    with open(file_path, 'r') as ecg_file:
        pass
    return ecg_data, ecg_label


def get_features(ecg_data):
    """Returns the wavelet features to be trained by the combined neural net
    algorithm

    :param ecg_data: Numpy matrix of ecg beat data (N x samples)
    :return: Numpy matrix of ecg beat features (N x 19)
    """
    ecg_features = []
    wavlet = features.WaveletFeatures(ecg_data, mother_wavelet=MOTHER_WAVELET,
                                      level=WAVELET_DECOMPOSITION_LEVEL)
    ecg_features = wavlet.get_features()
    return numpy.matrix(ecg_features)
