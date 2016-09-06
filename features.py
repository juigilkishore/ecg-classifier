# (c) 2016 JUIGIL KISHORE ALL RIGHTS RESERVED

import pywt
from constants import WAVELET_DECOMPOSITION_LEVEL, WAVELET


class WaveletFeatures(object):
    """
    Class to manage the wavelet features extraction and selection for the
    algorithm
    """

    def __init__(self, signal, level=WAVELET_DECOMPOSITION_LEVEL):
        """Initialize the WaveletFeatures class

        :param signal: python list of samples
        :param level: number level for decomposition
        """
        self.signal = signal
        self.level = level
        self.wavelet_coeff = None
        self.wavelet_features = None

    def wavelet_extraction(self):
        self.wavelet_coeff = pywt.wavedec(self.signal, 'db2', level=self.level)

    def wavelet_selection(self):
        features = []
        for band in self.wavelet_coeff:
            mean, power, std = self.calculate_features(band)
            features.extend(self.calculate_features(band))
        self.wavelet_features = features

    @staticmethod
    def calculate_features(band):
        return ["mean", "power", "standard deviation"]
