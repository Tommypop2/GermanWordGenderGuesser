# GermanWordGenderGuesser

## About

This is a relatively simple neural network that aims to guess the gender of any german word given to it. The data used for training is in the data.txt file, and the version on this repo has been pre-trained to about 90% accuracy on this data set.

## How to run

- Install python from their [website](https://www.python.org/). This project was built on python 3.10.6
- Clone the repository, using `git clone https://github.com/Tommypop2/GermanWordGenderGuesser` from the terminal, or by clicking the 'Code' button on github and then clicking 'Download ZIP', which can then be unzipped
- Open the folder in terminal
- Install all required packages, which are, in this case, tensorflow and numpy, by running `pip install tensorflow`, followed by `pip install numpy` in the terminal
- There are two main files to directly interact with in this folder: `train.py`, and `predict.py`. `train.py` is used to train the model, but, as the model is pre-trained, you can simply run `predict.py`, by running `python predict.py`