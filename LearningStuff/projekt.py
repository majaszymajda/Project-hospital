from unittest.main import main
import tensorflow as tf
import pandas as pd
from keras.layers import Dense
import numpy as np
from sklearn.model_selection import train_test_split
import pandas
import random
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

class Classifier():
    def download_data_and_separe_data(self):

        clean_data = pd.read_csv("LearningStuff/dane.csv")
        y_data_set_column = ['wynik']
        x_data_set_column = ['Breathing Problem', 'Fever', 'Dry Cough', 'Sore throat', 'Running 0se',
            'Asthma', 'Chronic Lung Disease', 'Headache', 'Heart Disease',
            'Diabetes', 'Hyper Tension', 'Fatigue ', 'Gastrointestinal ',
                'Contact with COVID Patient',
            'Attended Large Gathering', 'Visited Public Exposed Places',
            'Family working in Public Exposed Places', 'Wearing Masks',
            'Sanitization from Market']

        X = clean_data[x_data_set_column]
        Y = clean_data[y_data_set_column]
        pd.options.display.float_format = '{:,.0f}'.format


        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=1)
        return  X_train, X_test, y_train, y_test


    def create_model(self):
        X_train, X_test, y_train, y_test = self.download_data_and_separe_data()
        # Configuration options
        n_features = 19
        n_classes = 4
        n_epochs = 50
        batch_size = 250
        verbosity = 1
        validation_split = 0.2


        # Create the model
        model = Sequential()
        model.add(Dense(32, activation='relu', input_dim=n_features))
        model.add(Dense(16, activation='relu'))
        model.add(Dense(8, activation='relu'))
        model.add(Dense(n_classes, activation='sigmoid'))

        # Compile the model

        model.compile(optimizer='adam',loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=['accuracy'])


        # Fit data to model
        model.fit(X_train, y_train,
                batch_size=batch_size,
                epochs=n_epochs,
                verbose=verbosity,
                validation_split=validation_split)

        # Generate generalization metrics
        score = model.evaluate(X_test, y_test, verbose=0)
        # print(f'Test loss: {score[0]} / Test accuracy: {score[1]}')
        return model


    def assigning_class(self, data, model):
        pred =  np.argmax(model.predict(data), axis=-1)
        return pred

    # podział danych 


    def get_patient(self, model):
        n = 5433 #number of records in file
        s = 300 #desired sample size
        filename = "LearningStuff/dane-kopia.csv"
        skip = sorted(random.sample(range(1,n+1),n-s)) #the 0-indexed header will not be included in the skip list
        df = pandas.read_csv(filename, skiprows=skip)

        pred = self.assigning_class(df, model)
        return pred
   
