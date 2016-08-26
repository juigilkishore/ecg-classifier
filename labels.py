# (c) 2016 JUIGIL KISHORE ALL RIGHTS RESERVED

import numpy

import constants


class Label(object):
    """Label class contains information on the heart ailment"""

    def __init__(self, **kwargs):
        self.LABEL = numpy.matrix(kwargs.get(constants.CODE))
        self.ailment = kwargs.get(constants.AILMENT)
        self.description = kwargs.get(constants.DESC)

ARRHYTHMIA0 = Label(**constants.arrhythmia0)
ARRHYTHMIA1 = Label(**constants.arrhythmia1)
TACHYCARDIA0 = Label(**constants.tachycardia0)
TACHYCARDIA1 = Label(**constants.tachycardia1)

# Untrained. Just a placeholder for ClassifierManager attribute
UNTRAINED = Label(**constants.untrained)
