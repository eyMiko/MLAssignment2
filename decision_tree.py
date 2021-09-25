#-------------------------------------------------------------------------
# AUTHOR: Michael Tang
# FILENAME: decision_tree.py
# SPECIFICATION: Making a classifier.
# FOR: CS 4210- Assignment #2
# TIME SPENT: 3-4 Hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']
testX = []
testY = []
dbTest = []
c = 1

#read the test data and add this data to dbTest
with open('contact_lens_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
                dbTest.append(row)
        
           #transform the features of the test instances to numbers following the same strategy done during training, and then use the decision tree to make the class prediction. For instance:
           #class_predicted = clf.predict([[3, 1, 2, 1]])[0]           -> [0] is used to get an integer as the predicted class label so that you can compare it with the true label
           #--> add your Python code here
    for row in range(len(dbTest)):
        rowList = []
        for column in range(4):
            if dbTest[row][column] in ['Young', 'Myope', 'Yes', 'Normal']:
                rowList.append(1)
            elif dbTest[row][column] in ['Presbyopic', 'Hypermetrope', 'No', 'Reduced']:
                rowList.append(2)
            else:
                rowList.append(3)
        testX.append(rowList)

    for row in range(len(dbTest)):
        if dbTest[row][4] == 'Yes':
            testY.append(1)
        else:
            testY.append(2)

for ds in dataSets:

    dbTraining = []
    X = []
    Y = []
    testAccuracy = trainAccuracy = 1
    

    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append (row)

    #transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    #--> add your Python code here
    # X =
    for row in range(len(dbTraining)):
        rowList = []
        for column in range(4):
            if dbTraining[row][column] in ['Young', 'Myope', 'Yes', 'Normal']:
                rowList.append(1)
            elif dbTraining[row][column] in ['Presbyopic', 'Hypermetrope', 'No', 'Reduced']:
                rowList.append(2)
            else:
                rowList.append(3)
        X.append(rowList)

    #transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    #--> add your Python code here
    # Y =
    for row in range(len(dbTraining)):
        if dbTraining[row][4] == 'Yes':
            Y.append(1)
        else:
            Y.append(2)
          
    #loop your training and test tasks 10 times here
    for i in range (10):

       testCorrect = testIter = trainCorrect = trainIter = 0
       
       #fitting the decision tree to the data setting max_depth=3
       clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
       clf = clf.fit(X, Y)
       
       #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
       #--> add your Python code here
       
       train_class_predicted = clf.predict(X)
       for i in range(len(Y)):
           if train_class_predicted[i] == Y[i]:
               trainCorrect += 1
           trainIter += 1

       if trainCorrect/trainIter < trainAccuracy:
           trainAccuracy = trainCorrect/trainIter

       test_class_predicted = clf.predict(testX)
       for i in range(len(testY)):
           if test_class_predicted[i] == testY[i]:
               testCorrect += 1
           testIter += 1

       #find the lowest accuracy of this model during the 10 runs (training and test set)
       #--> add your Python code here
       if testCorrect/testIter < testAccuracy:
           testAccuracy = testCorrect/testIter
    #print the lowest accuracy of this model during the 10 runs (training and test set) and save it.
    #your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    #--> add your Python code here
    print("Training accuracy on contact_lens_training_{}: {}".format(c, trainAccuracy))
    print("Testing accuracy on contact_lens_training_{}: {}".format(c, testAccuracy))
    c+=1