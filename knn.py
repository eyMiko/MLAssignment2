    #-------------------------------------------------------------------------
# AUTHOR: Michael Tang
# FILENAME: knn.py
# SPECIFICATION: Utilizing KNeighbors classifier
# FOR: CS 4210- Assignment #2
# TIME SPENT: 1-2 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []
rate = correct = 0

#reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i > 0: #skipping the header
                 db.append (row)


#loop your data to allow each instance to be your test set
for i, instance in enumerate(db):

    #add the training features to the 2D array X removing the instance that will be used for testing in this iteration. For instance, X = [[1, 3], [2, 1,], ...]]. Convert each feature value to
    # float to avoid warning messages
    #--> add your Python code here
    # X =
        testSample = []
        X = []
        
        for row in range(len(db)):
            rowlist = []
            if i != row:
                for column in range(2):
                    rowlist.append(float(db[row][column]))
                X.append(rowlist)
            else:
                for column in range(2):
                    rowlist.append(float(db[row][column]))
                testSample.append(rowlist)
        #transform the original training classes to numbers and add to the vector Y removing the instance that will be used for testing in this iteration. For instance, Y = [1, 2, ,...]. Convert each
        #  feature value to float to avoid warning messages
        #--> add your Python code here
        # Y =
        Y = []
        for row in range(len(db)):
            if i != row:
                if db[row][2] == '+':
                    Y.append(float(1.0))
                else:
                    Y.append(float(2.0))
            else:
                if db[row][2] == '+':
                    pred = (float(1.0))
                else:
                    pred = (float(2.0))
        #store the test sample of this iteration in the vector testSample
        #--> add your Python code here
        #testSample =
        
        #fitting the knn to the data
        clf = KNeighborsClassifier(n_neighbors=1, p=2)
        clf = clf.fit(X, Y)
    
        
        #use your test sample in this iteration to make the class prediction. For instance:
        #class_predicted = clf.predict([[1, 2]])[0]
        #--> add your Python code here
        class_predicted = clf.predict(testSample)
        #compare the prediction with the true label of the test instance to start calculating the error rate.
        #--> add your Python code here
    
        if class_predicted == pred:
            correct += 1
#print the error rate
#--> add your Python code here
rate = (10.0 - correct) / 10.0 * 100
print("The error rate is: {}%".format(rate))
    
    
    
    
    
