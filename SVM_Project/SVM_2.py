import os
import numpy as np
import cv2
import pickle
import matplotlib.pyplot as plt
from sklearn.svm import SVC
import random
import time

''' comment shode chon yekbar etelat train ro zakhire kardim ta zamane ziyafi baray run kardanesh talaf nashe'''
# dir = 'images\\train'
# categories = ['0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9']
# train_data = []
# for category in categories:
#     path = os.path.join(dir , category)
#     label = categories.index(category)
#     for img in os.listdir(path):
#         imgpath = os.path.join(path , img)
#         digit_img = cv2.imread(imgpath , 0)
#         try:
#             digit_img = cv2.resize(digit_img , (50,50))
#             image = np.array(digit_img).flatten()
#             train_data.append([image , label])
#         except Exception as e:
#             pass


# pick_in = open('train_data.pickle' , 'wb')
# pickle.dump(train_data , pick_in)
# pick_in.close()
''' comment shode chon yekbar etelat test ro zakhire kardim ta zamane ziyafi baray run kardanesh talaf nashe'''
# dir = 'images\\test'
# categories = ['0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9']
# test_data = []
# for category in categories:
#     path = os.path.join(dir , category)
#     label = categories.index(category)
#     for img in os.listdir(path):
#         imgpath = os.path.join(path , img)
#         digit_img = cv2.imread(imgpath , 0)
#         try:
#             digit_img = cv2.resize(digit_img , (50,50))
#             image = np.array(digit_img).flatten()
#             test_data.append([image , label])
#         except Exception as e:
#             pass


# pick_in = open('test_data.pickle' , 'wb')
# pickle.dump(test_data , pick_in)
# pick_in.close()

start = time.time()

pick_in_train = open('train_data.pickle' , 'rb')
train_data = pickle.load(pick_in_train)
pick_in_train.close()

pick_in_test = open('test_data.pickle' , 'rb')
test_data = pickle.load(pick_in_test)
pick_in_test.close()

Xtrain = []
Ytrain = []
Xtest = []
Ytest = []
for x , y in train_data:
    Xtrain.append(x)
    Ytrain.append(y)

for x , y in test_data:
    Xtest.append(x)
    Ytest.append(y)

categories = ['0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9']
model = SVC(kernel='rbf')
model.fit(Xtrain , Ytrain)

yPredict = model.predict(Xtest)
acc = model.score(Xtest , Ytest)
print(f"Accuracy of this classification is : {acc}" )
end = time.time()
print("Execution time = " , end - start)

''' yek test kocholo'''
random_idx = random.randint(0 , len(Ytest))
mydigit = Xtest[random_idx].reshape(50,50)
print(f"According to the predictation the digit is {categories[yPredict[random_idx]]}")
plt.imshow(mydigit , cmap='gray')
plt.show()

