# Text-Summarizer-

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/entbappy/End-to-end-Text-Summarization
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n venv python=3.8 -y
```

```bash
conda activate venv/
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

### STEP 03- install the requirements for GPU acceleration (optional)
```bash
# Considering that current CUDA version compatible at time
# of building this repo with Pytorch is 11.8
conda install cudatoolkit=11.8
conda install cudnn = 8.9.2
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
```
### STEP 04- building the model
```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```