from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
from skimage import transform

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


MODEL = tf.keras.models.load_model("saved_models/best_model.pb") #path to our trained model

CLASS_NAMES = ['adalia bipunctata', 'calliteara pudibunda', 'cerambyx cerdo', 'gryllotalpa gryllotalpa', 'lucanus cervus', 'mantis religiosa', 'melolontha melolontha', 'phyrrochorus apterus', 'rhaphigaster nebulosa', 'sesia apiformis', 'tettigonia viridissima', 'xylocopa violacea']

@app.get("/ping")
async def ping():
    return "Bok! Za sada radi :D"

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

@app.post("/predict")
async def predict(
    file: UploadFile = File(...) #  <====== ime file mora biti kao i u postman-u ===========>
):
    image = read_file_as_image(await file.read())
    np_image = image.astype('float32') / 255
    np_image = transform.resize(np_image, (224, 224, 3))
    np_image = np.expand_dims(np_image, axis=0)

    predictions = MODEL.predict(np_image)

    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8001)

