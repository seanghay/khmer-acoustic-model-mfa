## Train an Acoustic Model for Khmer language with Montreal Forced Aligner

We'll use [[High quality TTS data for Khmer (OpenSLR 42)]](https://www.openslr.org/42/) dataset for training the acoustic model.

### 1. Create Conda Environment

```shell
conda create -n aligner python=3.8 --yes
conda activate aligner
```

### 2. Install MFA

```shell
conda install -c conda-forge montreal-forced-aligner --yes
```

### 3. Download the data

```shell
# audio dataset
wget -O km_kh_male.zip https://www.openslr.org/resources/42/km_kh_male.zip

# pronouncing dictionary
wget -O lexicon.txt https://github.com/seanghay/khmer-acoustic-model-mfa/raw/main/lexicon.txt

# uncompress
unzip km_kh_male.zip
```

### 4. Preprocess the dataset

Create transcription for each audio files.

```shell
python preprocess.py
```

### 5. Train

```shell
mfa train --clean --speaker_characters 8 km_kh_male/wavs lexicon.txt khm_model.zip 
```

This will take quite some time. Once it's done, there will be `khm_model.zip` file which you can then use for forced alignment.


### 6. Forced Alignment

The output files will be in Praat TextGrid format.

```shell
mfa align --clean --speaker_characters 8 km_kh_male/wavs lexicon.txt khm_model.zip outputs
```