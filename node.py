# # import sys
# import tensorflow as tf
# import keras
# # import numpy
# import cv2     # Save image in set directory  # Read RGB image  i
# from keras.preprocessing.image import load_img,img_to_array,array_to_img,ImageDataGenerator
# import skimage
# # from skimage.transform import resize
# # from skimage.color import lab2rgb,rgb2lab,gray2rgb
# # from skimage.io import imsave
# import os
# import numpy as np
# from keras.models import Sequential,Model,load_model
# # from keras.layers import Conv2D, UpSampling2D, Input,Dropout
# # import matplotlib.pyplot as plt
# # from keras.optimizers import Adam
# # from keras.callbacks import EarlyStopping

# print("Test Path")
# testpath = "C: /Users/moham/Documents/IC_colorize/views/upload/image.png"
# print("start")
# vggmodel = keras.applications.vgg16.VGG16()
# newmodel = Sequential() 
# num = 0
# for i, layer in enumerate(vggmodel.layers):
#     if i<19:
#       newmodel.add(layer)
        
# newmodel.summary()
# for layer in newmodel.layers:
#   layer.trainable=False

# print("First model")
# cmodel = load_model("C:/Users/moham/Documents/IC_colorize/coloringmodel.h5")
# print("Second loaded")

# img = cv2.imread(testpath)

# img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# img = cv2.cvtColor(testpath,cv2.COLOR_RGB2GRAY)


# cv2.imwrite(testpath,img)

# # testpath = '/content/drive/My Drive/courtroom.jpg'

# test = img_to_array(img)
# test = skimage.transform.resize(test, (224,224), anti_aliasing=True)
# test*= 1.0/255
# lab = skimage.color.rgb2lab(test)
# l = lab[:,:,0]
# L = skimage.color.gray2rgb(l)
# L = L.reshape((1,224,224,3))
# #print(L.shape)
# vggpred = newmodel.predict(L)
# ab = cmodel.predict(vggpred)
# #print(ab.shape)
# ab = ab*128
# cur = np.zeros((224, 224, 3))
# cur[:,:,0] = l
# cur[:,:,1:] = ab
# # imsave("/content/drive/My Drive/ct22result.png", lab2rgb(cur))
# cv2.imwrite(testpath,skimage.color.lab2rgb(cur))


print(" Finished ")

# # var = r'C:\dummy_folder\a.txt' 
# # var.replace('\\', '/') print(var)

# # var= r'C:\dummy_folder\a.txt' 
# # code1.replace('\\', '/') 
# # print(code1)
# # mg = cv2.imread(code1)
# # print(code1)

# # print(mg)


# from keras.preprocessing.image import load_img,img_to_array,array_to_img,ImageDataGenerator
# # import skimage
# # from skimage.transform import resize
# # from skimage.color import lab2rgb,rgb2lab,gray2rgb
# # from skimage.io import imsave
# import os
# import cv2
# import numpy as np
# import keras
# from keras.models import Sequential,Model,load_model
# from keras.layers import Conv2D, UpSampling2D, Input,Dropout
# import matplotlib.pyplot as plt
# from keras.optimizers import Adam
# from keras.callbacks import EarlyStopping
# # %matplotlib inline


# model=load_model('coloringmodel.h5')
# # newmodel=load_model('vggmodel1.h5')
# vggmodel = load_model('vggmodelnew.h5')
# newmodel = Sequential() 
# num = 0
# for i, layer in enumerate(vggmodel.layers):
#     if i<19:
#       newmodel.add(layer)
        
# newmodel.summary()
# for layer in newmodel.layers:
#   layer.trainable=False

# print("Test Path")
# testpath = "C:/Users/moham/Documents/IC_colorize/views/upload/image.png"

# img = cv2.imread(testpath)

# img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)


# # cv2.imwrite(path,img)
# test = img_to_array(img)
# # test = resize(test, (224,224), anti_aliasing=True)
# test = cv2.resize(img, (224,224), interpolation = cv2.INTER_AREA)
# test = test.astype(float)
# test*= 1.0/255
# # lab = rgb2lab(test)
# lab = cv2.cvtColor(test,cv2.COLOR_RGB2LAB)

# l = lab[:,:,0]
# # L = gray2rgb(l)
# L = cv2.cvtColor(l,cv2.COLOR_GRAY2RGB)
# L = L.reshape((1,224,224,3))
# #print(L.shape)
# vggpred = newmodel.predict(L)
# ab = model.predict(vggpred)
# #print(ab.shape)
# ab = ab*128
# cur = np.zeros((224, 224, 3))
# cur[:,:,0] = l
# cur[:,:,1:] = ab
# # imsave("/content/drive/My Drive/ct22result.png", lab2rgb(cur))
# result = cv2.cvtColor(cur,cv2.COLOR_LAB2RGB)
# cv2.imwrite(testpath,result)


# print(" SAVED ")