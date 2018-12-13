# Phoneme classification using GMMs

## Problem Statement:
Performing phoneme classification on the TIMIT dataset by training and testing gmm models for each phoneme.

## Procedure followed :
### 1. Preprocessing
       - Downloaded and extracted the timit dataset
       - Converted the wav files from NIST “SPHERE” file format to WAVE PCM format using “sphn_to_wav.py” file
       - Training and testing are in 2 separate ipynb files, 'train.ipynb' and 'test.ipynb' respectively.

### 2. Training
       - Used “import_timit.py” file to generate mfcc (13 dim), mfcc + delta (26 dim), mfcc + delta + delta (39 dim) features. They are saved in “features/” as train1.hdf, train2.hdf and train3.hdf respectively.
       - train.ipynb reads the mfcc features, extracts the feature and label array, and fits a gmm for each phoneme. 
       - The gmms are then saved onto the system using the pickle library 

### 3. Testing
       - Similar to the training process, mfcc features are generated, for the test directory of TIMIT
       - Feature and label array are extracted. This label array acts as the ground truth for the test dataset.
       - The trained gmms are loaded from disk. 
       - MAP rule is applied, to classify each feature vector in the sequence, for a given test file (40-way classification), and the predicted labels are stored in an array
       - Frame-level accuracy and Phoneme error rate are calculated using ground truth array and predicted labels array

## To run :
### 1. Training
    - To perform training, first extract mfcc features (including 0, 1 and 2 delta features) for each train and test, using the foll. command:
	Generic : 'python import_timit.py --timit <path of TIMIT directory> --n_delta <No of delta features to be added>'
	Sample  : 'python import_timit.py --timit TIMIT/ --n_delta 1'
    - Then check out the steps in train.ipynb

### 2. Testing
Check out the steps in test.ipynb

## Folders in repo:
    - features - Contain mfcc features, along with delta features(0,1,2), of training set and testing set  
    of TIMIT dataset. Saved as train1.hdf, train2.hdf, train3.hdf and a similar naming scheme for test set  
    too. **The folder is not uploaded here due to size constraints. See the last section, for the  
    downloadable google drive link.**
    - models - Contains pickled trained models for all phonemes
    - TIMIT - contains files of the TIMIT dataset
    - results - contains 2 files. The observations.txt file contains the results as observed.   
    The report.odt/pdf contains the discussion surrounding the observations as part of the entire report.

## Other files in repo:
    - per.py - The per.py file is imported as an external file in test.ipynb file, for using it's phoneme error rate functionality.
    - team_members.txr
    - requirements.txt
    - import_timit.py
    - train_wavs
    - test_wavs 
    - train.ipynb
    - test.ipynb
    - kaldi_60_48_39.map  (Preprocessing file) 
    - mapping.py          (Preprocessing file) 
    - maps                (Preprocessing file)

## Note:
The features directory was too large to upload, and can be downloaded from this link:
