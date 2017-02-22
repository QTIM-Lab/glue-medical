from glue_medical import setup
from glue_medical.nifti.nifti_factory import nifti_reader

setup()

data = nifti_reader('C:/Users/abeers/Documents/GitHub/Public_QTIM/qtim_tools/qtim_tools/test_data/test_data_features/MRBrainTumor2.nii.gz')
print data[0]

print data[0].coords.pixel2world(5,6,7)
