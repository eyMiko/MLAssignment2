#-------------------------------------------------------------------------
# AUTHOR: Michael Tang
# FILENAME: naive_bayes.py
# SPECIFICATION: Using Naive bayes for predictions
# FOR: CS 4210- Assignment #2
# TIME SPENT: 2-3 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv

weather_training =  [] 
weather_testing = []
X = []
Y= []
testX = []
#reading the training data
#--> add your Python code here
with open('weather_training.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
             weather_training.append (row)
#transform the original training features to numbers and add to the 4D array X. For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here
# X =
for row in range(14):
    rowList = []
    for column in range(1, 5):
        if weather_training[row][column] in ['Sunny', 'Hot', 'High','Weak']:
            rowList.append(1)
        elif weather_training[row][column] in ['Overcast', 'Mild', 'Strong', 'Normal']:
            rowList.append(2)
        else:
            rowList.append(3)
    X.append(rowList)
#transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
# Y =
for a in range(len(weather_training)):
    if weather_training[a][5] == 'Yes':
        Y.append(1)
    else:
        Y.append(2)
#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the data in a csv file
#--> add your Python code here
with open('weather_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
             weather_testing.append (row)

for row in range(len(weather_testing)):
    rowList = []
    for column in range(1, 5):
        if weather_testing[row][column] in ['Sunny', 'Hot', 'High','Weak']:
            rowList.append(1)
        elif weather_testing[row][column] in ['Overcast', 'Mild', 'Strong', 'Normal']:
            rowList.append(2)
        else:
            rowList.append(3)
    testX.append(rowList)
#printing the header os the solution
print ("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) + "Humidity".ljust(15) + "Wind".ljust(15) + "PlayTennis".ljust(15) + "Confidence".ljust(15))

#use your test samples to make probabilistic predictions.
#--> add your Python code here
#-->predicted = clf.predict_proba([[3, 1, 2, 1]])[0]
for i in range(len(testX)):
    predicted = clf.predict([testX[i]])
    pred_prob = clf.predict_proba([testX[i]])[0]
    print(("{}".ljust(15) + "{}".ljust(15) + "{}".ljust(15) + "{}".ljust(15) + "{}".ljust(15) + "{}".ljust(15) + "{}".ljust(15)).format(weather_testing[i][0], weather_testing[i][1], weather_testing[i][2], weather_testing[i][3], weather_testing[i][4], predicted[0], pred_prob[0]))