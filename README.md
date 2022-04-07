Insect classification model made using tensorflow-keras

# INTRO

This is my second project in machine learning, in which I tried to repeat the same project, Insect classification model pytorch, but this time using another popular deep learning framework -Tensorflow/Keras. There are a lot of examples and explanations online and it's also less verbose than Pytorch, so creating the model itself was easier but once you make a mistake it is harder to debug. Another big difference I noticed, as a beginner in machine learning, is that Tensorflow seems like a completely new language.

## Project Description:
- this is a small and demonstrative project that classifies 12 different insects and returns their latin names
- those insects are: Adalia bipunctata', Calliteara pudibunda, Cerambyx cerdo, Gryllotalpa gryllotalpa, Lucanus cervus, Mantis religiosa, Melolontha melolontha, Phyrrochorus apterus, Rhaphigaster nebulosa, Sesia apiformis, Tettigonia viridissima, Xylocopa violacea.
- image classification is done by using torch 1.10.2, matplotlib 3.5.1 for visualization and scikit-learn 1.0.2 for making a confusion matrix
- model was fed with 5200 images of 12 different insects splited in 3 folders: training, validation and test
- final model was trained using resnet18 which showed high accuracy on test images >94%

to run the model:
- clone the repository
- install requirements.txt
- run pytorch_insect_classification_model.ipynb

### Ploted results and confusion matrix:
![bugs](https://user-images.githubusercontent.com/89583742/162262535-3fc48dac-bbd3-4dc6-939b-8507e697619a.png)

![confusion](https://user-images.githubusercontent.com/89583742/162262572-46973925-9f2f-452a-b40c-18896a652f1a.png)

## FRONTEND part of the project

to install frontend:
 - install NodeJS and NPM
 - install dependencies in frontend folder cd Desktop/Insects/frontend by typing npm install --from-lock-json and then npm audit fix
 - copy and rename .env.example to .env and change REACT_APP_API_URL to API URL if needed

to run frontend:
 - go to frontend folder
 - run the frontend by typing npm run start in cmd
 
![Screenshot](https://user-images.githubusercontent.com/89583742/161758722-7c66f494-c27d-4f99-a1bd-1d9c8e5eef51.jpg)




