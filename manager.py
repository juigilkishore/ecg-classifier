# (c) 2016 JUIGIL KISHORE ALL RIGHTS RESERVED

import numpy

import labels
from features import WaveletFeatures
from constants import WAVELET_DECOMPOSITION_LEVEL


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
