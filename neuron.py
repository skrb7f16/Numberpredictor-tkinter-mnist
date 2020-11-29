from tensorflow import keras
import tensorflow as tf
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

digits=keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = digits.load_data()


train_images = train_images / 255.0

test_images = test_images / 255.0

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10,activation='softmax')
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])


x_val=train_images[:10000]
x_train=train_images[10000:]

y_val=train_labels[:10000]
y_train=train_labels[10000:]

fitModel=model.fit(x_train,y_train,epochs=6,validation_data=(x_val,y_val),verbose=1)
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=1)
model.save("numberRecognition.h5")




