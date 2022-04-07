import os
import splitfolders

splitfolders.ratio("testno/photos", output="za_keras_splited", seed=1337, ratio=(0.7, 0.1, 0.2)) # ratio => 0.7 train, 0.1 val, 0.2 test