# (c) 2016 JUIGIL KISHORE ALL RIGHTS RESERVED

import features
import manager

from constants import WAVELET_DECOMPOSITION_LEVEL


def load_ecg_beat_file(file_path):
    """Load a ecg file - single beat (.csv file)

    :param file_path: Path of the single ecg beat file
    :return: ecg single beat data from the file as list
    """
    # TODO: Complete this
    with open(file_path, 'r') as ecg_beat:
        pass
    return


def load_ecg_train_file(file_path):
    """Load a ecg file - single beat for different heart ailments

    :param file_path: Path of the single ecg beat file
    :return: ecg beat data from the file as dictionary with the (key, values)
    as (ailment name, data)
        {
         "arrythmia0": [...],
         "arrythmia0": [...],
         "tachycardia1": [...],
         ...
        }
    """
    # TODO: Complete this
    with open(file_path, 'r') as ecg_file:
        pass
    return


def create_ecg_datatype(ecg_data_points):
    """Returns list of ECGBeat objects for each beat

    :param ecg_data_points:
        {
            "arrythmia0": [...],
            "tachycardia1": [...],
            ...
        } in case of training data
        {
            "untrained": [...]
        } in case of test data
    :return: list of ECGBeat objects for each beat
    """
    return [manager.ECGBeat(data, ailment)
            for ailment, data in ecg_data_points]


def get_ecg_features(ecg_objects):
    """

    :param ecg_objects:
    :return:
    """
    for ecg in ecg_objects:
        wav = features.WaveletFeatures(ecg.samples,
                                       WAVELET_DECOMPOSITION_LEVEL)
        wav.wavelet_extraction()
        wav.wavelet_selection()
