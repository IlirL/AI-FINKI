from sklearn.naive_bayes import GaussianNB

if __name__ == '__main__':

    dataset = [['1', '35', '12', '5', '1', '100', '0'], ['1', '29', '7', '5', '1', '96', '1'],
               ['1', '50', '8', '1', '3', '132', '0'], ['1', '32', '11.75', '7', '3', '750', '0'],
               ['1', '67', '9.25', '1', '1', '42', '0'], ['1', '41', '8', '2', '2', '20', '1'],
               ['1', '36', '11', '2', '1', '8', '0'], ['1', '59', '3.5', '3', '3', '20', '0'],
               ['1', '20', '4.5', '12', '1', '6', '1'], ['2', '34', '11.25', '3', '3', '150', '0'],
               ['2', '21', '10.75', '5', '1', '35', '0'], ['2', '15', '6', '2', '1', '30', '1'],
               ['2', '15', '2', '3', '1', '4', '1'], ['2', '15', '3.75', '2', '3', '70', '1'],
               ['2', '17', '11', '2', '1', '10', '0'], ['2', '17', '5.25', '3', '1', '63', '1'],
               ['2', '23', '11.75', '12', '3', '72', '0'], ['2', '27', '8.75', '2', '1', '6', '0'],
               ['2', '15', '4.25', '1', '1', '6', '1'], ['2', '18', '5.75', '1', '1', '80', '1'],
               ['1', '22', '5.5', '2', '1', '70', '1'], ['2', '16', '8.5', '1', '2', '60', '1'],
               ['1', '28', '4.75', '3', '1', '100', '1'], ['2', '40', '9.75', '1', '2', '80', '0'],
               ['1', '30', '2.5', '2', '1', '115', '1'], ['2', '34', '12', '3', '3', '95', '0'],
               ['1', '20', '0.5', '2', '1', '75', '1'], ['2', '35', '12', '5', '3', '100', '0'],
               ['2', '24', '9.5', '3', '3', '20', '0'], ['2', '19', '8.75', '6', '1', '160', '1'],
               ['1', '35', '9.25', '9', '1', '100', '1'], ['1', '29', '7.25', '6', '1', '96', '1'],
               ['1', '50', '8.75', '11', '3', '132', '0'], ['2', '32', '12', '4', '3', '750', '0'],
               ['2', '67', '12', '12', '3', '42', '0'], ['2', '41', '10.5', '2', '2', '20', '1'],
               ['2', '36', '11', '6', '1', '8', '0'], ['1', '63', '2.75', '3', '3', '20', '0'],
               ['1', '20', '5', '3', '1', '6', '1'], ['1', '34', '12', '1', '3', '150', '0'],
               ['2', '21', '10.5', '5', '1', '35', '0'], ['2', '15', '8', '12', '1', '30', '1'],
               ['1', '15', '3.5', '2', '1', '4', '1'], ['2', '15', '1.5', '12', '3', '70', '1'],
               ['1', '17', '11.5', '2', '1', '10', '0'], ['1', '17', '5.25', '4', '1', '63', '1'],
               ['2', '23', '9.5', '5', '3', '72', '0'], ['1', '27', '10', '5', '1', '6', '0'],
               ['1', '15', '4', '7', '1', '6', '1'], ['2', '18', '4.5', '8', '1', '80', '1'],
               ['2', '22', '5', '9', '1', '70', '1'], ['1', '16', '10.25', '3', '2', '60', '1'],
               ['2', '28', '4', '11', '1', '100', '1'], ['2', '40', '8.75', '6', '2', '80', '0'],
               ['2', '30', '0.5', '8', '3', '115', '1'], ['1', '34', '10.75', '1', '3', '95', '0'],
               ['1', '20', '3.75', '11', '1', '75', '1'], ['2', '35', '8.5', '6', '3', '100', '0'],
               ['1', '24', '9.5', '8', '1', '20', '1'], ['2', '19', '8', '9', '1', '160', '1'],
               ['1', '35', '7.25', '2', '1', '100', '1'], ['1', '29', '11.75', '5', '1', '96', '0'],
               ['2', '50', '9.5', '4', '3', '132', '0'], ['2', '32', '12', '12', '3', '750', '0'],
               ['1', '67', '10', '7', '1', '42', '0'], ['2', '41', '7.75', '5', '2', '20', '1'],
               ['2', '36', '10.5', '4', '1', '8', '0'], ['1', '67', '3.75', '11', '3', '20', '0'],
               ['1', '15', '10.5', '11', '1', '30', '1'], ['1', '15', '2', '11', '1', '4', '1'],
               ['2', '15', '2', '10', '3', '70', '1'], ['1', '17', '9.25', '12', '1', '10', '0'],
               ['1', '17', '5.75', '10', '1', '63', '1'], ['1', '23', '10.25', '7', '3', '72', '0'],
               ['1', '27', '10.5', '7', '1', '6', '0'], ['1', '15', '5.5', '5', '1', '6', '1'],
               ['1', '18', '4', '1', '1', '80', '1'], ['2', '22', '4.5', '2', '1', '70', '1'],
               ['1', '16', '11', '3', '2', '60', '1'], ['2', '28', '5', '9', '1', '100', '1'],
               ['1', '40', '11.5', '9', '2', '80', '0'], ['1', '30', '0.25', '10', '1', '115', '1'],
               ['2', '34', '12', '3', '3', '95', '0'], ['2', '20', '3.5', '6', '1', '75', '1'],
               ['2', '35', '8.25', '8', '3', '100', '0'], ['1', '24', '10.75', '10', '1', '20', '1'],
               ['1', '19', '8', '8', '1', '160', '1']]


    dataset = [[float(dataset[i][j]) for j in range(0, len(dataset[i]))] for i in range(0,len(dataset))]

    train_set = dataset[0:int(0.85*(len(dataset)))]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    test_set = dataset[int(0.85*(len(dataset))):]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    classifier = GaussianNB()
    classifier.fit(train_x, train_y)

    accuracy = 0

    for i in range(len(test_set)):
        prediction = classifier.predict([test_x[i]])[0]
        true = test_y[i]

        if prediction == true:
            accuracy+=1

    accuracy = accuracy / len(test_set)


    test_from_input = [float(el) for el in input().split(' ')]
    prediction_for_input = classifier.predict([test_from_input])[0]

    print(accuracy)
    print(int(prediction_for_input))
    print(classifier.predict_proba([test_from_input]))