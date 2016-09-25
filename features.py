# (c) 2016 JUIGIL KISHORE ALL RIGHTS RESERVED

import pywt
import statistics

from constants import WAVELET_DECOMPOSITION_LEVEL, MOTHER_WAVELET


class WaveletFeatures(object):
    """
    Class to manage the wavelet features extraction and selection for the
    algorithm
    """

    def __init__(self, signal_matrix, mother_wavelet=MOTHER_WAVELET,
                 level=WAVELET_DECOMPOSITION_LEVEL):
        """Initialize the WaveletFeatures class
        :param signal: numpy matrix
        :param level: number level for decomposition
        """
        self.signal_matrix = signal_matrix
        self.level = level
        self.coefficients_matrix = None
        self.feature_matrix = None
        self._get_coefficients(signal_matrix, mother_wavelet, level)

    def _get_coefficients(self, signal_matrix, wavelet, level):
        """Evaluates the Wavelet coefficient for the ecg signal
        :param signal_matrix: numpy matrix
        :return: wavelet coefficients
        """
        coeffs_matrix = []
        for signal in signal_matrix:
            wavelet_coeff_list = []
            wavelet_coeff = pywt.wavedec(signal.tolist()[0],
                                          wavelet, level=level)
            for wc in wavelet_coeff:
                wavelet_coeff_list.append(wc.tolist())
            coeffs_matrix.append(wavelet_coeff_list)
        self.coefficients_matrix = coeffs_matrix

    def get_features(self):
        """Evaluates the features from the Wavelet coefficients. Mean, Average
        power, Standard deviation and the ratio of mean of the adjacent bands
        :return: Features
        """
        feature_matrix = []
        mean_list = []
        for beat in self.coefficients_matrix:
            feature = []
            for band in beat:
                _mean, _power, _std = self._evaluate_features(band)
                mean_list.append(_mean)
                feature = feature + [_mean, _power, _std]
            mean_nume, mean_deno = mean_list[:-1], mean_list[1:]
            feature = feature + [n/d for n, d in zip(mean_nume, mean_deno)]
            feature_matrix.append(feature)
        self.feature_matrix = feature_matrix
        return feature_matrix

    @staticmethod
    def _evaluate_features(band):
        """Helper method to evaluate the mean, average power, standard
        deviation of the wavelet coefficients in a band
        :param band: wavelet coefficients
        :return: mean, average power, standard deviation
        """
        _mean = statistics.mean([abs(v) for v in band])
        _pow = statistics.mean([v*v for v in band])
        _std = statistics.stdev(band)
        return _mean, _pow, _std
