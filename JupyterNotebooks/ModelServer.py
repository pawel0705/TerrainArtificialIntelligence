#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img

import zmq
import numpy as np
from matplotlib import pyplot
import cv2


# In[2]:


model = load_model('model.h5')

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")


# In[ ]:


while True:
    
    print('w petli')
    bytes_received = socket.recv(3136)
    array_received = np.frombuffer(bytes_received, dtype=np.float32).reshape(28,28)

    pred = model.predict(array_received.reshape(1,784))

    bytes_to_send = pred.tobytes()
    socket.send(bytes_to_send)


# In[ ]:




