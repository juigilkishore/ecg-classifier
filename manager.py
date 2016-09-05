# (c) 2016 JUIGIL KISHORE ALL RIGHTS RESERVED

import numpy

import labels
from features import WaveletFeatures
from constants import WAVELET_DECOMPOSITION_LEVEL


class ECGBeat(object):
    """
    ECGBeat Class to hold the single ecg beat's data and ailment
    """

    def __init__(self, samples, ailment):
        self.samples = numpy.matrix(samples)
        self.ailment = ailment
        self.num = len(samples)


class ECGBeatFeatures(object):
    """
    Class to extract and select features from the ecg beat
    """

    def __init__(self, samples, ailment):
        self.samples = samples
        self.ailment = ailment


class Classifier(object):
    """
    Manager class that passes the ECG samples through the trained algorithm
    """

    def __init__(self, samples):
        self.samples = numpy.matrix(samples)
        self.LABEL = labels.UNTRAINED
        self.pattern = WaveletFeatures(self.samples,
                                       WAVELET_DECOMPOSITION_LEVEL)
        self._routine()

    def _routine(self):
        self._feature_extraction()
        self._feature_selection()

    def _feature_extraction(self):
        pass

    def _feature_selection(self):
        pass


class CombinedNeuralNet(object):
    """
    Implements the combined neural network algorithm
    """
    def __init__(self, ecg_list):
        self.experiments = [(ecg.samples, ecg.ailment) for ecg in ecg_list]

    def train(self):
        pass

    def test(self):
        pass
