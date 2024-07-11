import tensorflow as tf 
import numpy as np 

model = tf.keras.models.load_model(r'C:\Users\LENOVO\Desktop\HCU\summer_4_1\deploy_models_test2\models\body_shape_model.h5')

def make_prediction(weight, height):
    weight = float(weight)
    height = float(height)
    data = np.array([[weight, height]])
    pred = model.predict(data)
    return "Fat" if pred > 0.5 else "Normal"