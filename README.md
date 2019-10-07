# FingersCounter

CNN multiclass classifier for counting number of fingers shown on one hand. Made with EduNet.

By Matas Gumbinas, 2019

## Introduction & acknowledgements

The sole goal of this work is to demonstrate **EduNet** NN (neural networks) modeling framework [1].  
For this task a Kaggle dataset "Fingers" by Pavel Koryakin [2] was used. The purpose of this  
dataset is to help create an image classifier that would count fingers on a hand from 0 to 5.

Results:  
During this work, using EduNet API, a Convolution Neural Network was created to be trained on the  
given dataset. Afterwards, the trained model was tested using unused part of the dataset meant for   
testing the trained models. The trained model reached 100% accuracy with training, validation and
testing datasets after 4 epochs.

List of references:  
1. EduNet. Numpy based educational neural networks modeling framework - from scratch  
(by Matas Gumbinas).  
https://github.com/gMatas/edunet
2. "Fingers" dataset (by Pavel Koryakin).  
https://www.kaggle.com/koryakinp/fingers

## Starting up

First, download EduNet python package from github [1] (v1.3.0-alpha.0 release) to the main  
directory (at ```fingers-counter/```). Or run the following git commands from your console/terminal  
starting from the main directory: 
```shell
git clone https://github.com/gmatas/edunet
cd edunet
git checkout v1.3.0-alpha.0
cd ..
```

Next, from the ```fingers-counter```project main directory run the following pip command to install the required python  
dependencies:
```shell
pip install -r requirements.txt
```

Finaly, before running this notebook, please run following commands: 
```shell
cd datasets
python fingers.py
cd ..
```

```fingers.py``` script will unzip "fingers.zip" file and read its contents to original "**fingers**" dataset. Afterwards  
it will generate a downsampled version of it to a directory "**fingers_32x32**". The following work will be done on  
the downsampled dataset.

*That's it! Have fun using this project!*
