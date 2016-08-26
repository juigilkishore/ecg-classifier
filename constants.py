# (c) 2016 JUIGIL KISHORE ALL RIGHTS RESERVED

CODE = "code"
AILMENT = "ailment"
DESC = "description"

untrained = {
    CODE: [],
    AILMENT: "NOT-APPLICABLE",
    DESC: "NOT-APPLICABLE"
}
arrhythmia0 = {
    CODE: [0, 0, 0, 1],
    AILMENT: "ARRHYTHMIA_TYPE_1",
    DESC: "empty"}

arrhythmia1 = {
    CODE: [0, 1, 0, 0],
    AILMENT: "ARRHYTHMIA_TYPE_2",
    DESC: "empty"}

tachycardia0 = {
    CODE: [0, 0, 1, 0],
    AILMENT: "TACHYCARDIA_TYPE_1",
    DESC: "empty"}

tachycardia1 = {
    CODE: [1, 0, 0, 0],
    AILMENT: "TACHYCARDIA_TYPE_2",
    DESC: "empty"}

heart_aberrations = {
    "arrythmia0": arrhythmia0,
    "tachycardia0": tachycardia0,
    "arrythmia1": arrhythmia1,
    "tachycardia1": tachycardia1
}

WAVELET_DECOMPOSITION_LEVEL = 4
