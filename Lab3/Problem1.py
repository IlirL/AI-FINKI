from sklearn.tree import DecisionTreeClassifier

dataset = [[6.3, 2.3, 4.4, 1.3, 2],
           [6.4, 2.8, 5.6, 2.1, 0],
           [5.1, 3.3, 1.7, 0.5, 1],
           [5.1, 3.5, 1.4, 0.2, 1],
           [4.6, 3.1, 1.5, 0.2, 1],
           [5.8, 2.7, 5.1, 1.9, 0],
           [5.5, 3.5, 1.3, 0.2, 1],
           [5.7, 2.6, 3.5, 1.0, 2],
           [5.0, 3.5, 1.3, 0.3, 1],
           [6.3, 2.5, 5.0, 1.9, 0],
           [6.2, 2.2, 4.5, 1.5, 2],
           [5.0, 3.4, 1.6, 0.4, 1],
           [5.7, 4.4, 1.5, 0.4, 1],
           [4.9, 2.4, 3.3, 1.0, 2],
           [4.4, 2.9, 1.4, 0.2, 1],
           [5.5, 2.4, 3.7, 1.0, 2],
           [5.6, 2.5, 3.9, 1.1, 2],
           [5.6, 2.8, 4.9, 2.0, 0],
           [4.8, 3.4, 1.6, 0.2, 1],
           [5.6, 3.0, 4.5, 1.5, 2],
           [6.0, 3.0, 4.8, 1.8, 0],
           [6.3, 3.3, 4.7, 1.6, 2],
           [4.8, 3.0, 1.4, 0.1, 1],
           [7.9, 3.8, 6.4, 2.0, 0],
           [4.9, 3.0, 1.4, 0.2, 1],
           [4.3, 3.0, 1.1, 0.1, 1],
           [6.8, 3.2, 5.9, 2.3, 0],
           [5.6, 2.7, 4.2, 1.3, 2],
           [5.2, 4.1, 1.5, 0.1, 1],
           [6.2, 2.9, 4.3, 1.3, 2],
           [6.5, 2.8, 4.6, 1.5, 2],
           [5.4, 3.9, 1.3, 0.4, 1],
           [5.8, 2.6, 4.0, 1.2, 2],
           [5.4, 3.7, 1.5, 0.2, 1],
           [4.5, 2.3, 1.3, 0.3, 1],
           [6.3, 3.4, 5.6, 2.4, 0],
           [6.2, 3.4, 5.4, 2.3, 0],
           [5.7, 2.5, 5.0, 2.0, 0],
           [5.8, 2.7, 3.9, 1.2, 2],
           [6.4, 2.7, 5.3, 1.9, 0],
           [5.1, 3.8, 1.6, 0.2, 1],
           [6.3, 2.5, 4.9, 1.5, 2],
           [7.7, 2.8, 6.7, 2.0, 0],
           [5.1, 3.5, 1.4, 0.3, 1],
           [6.8, 2.8, 4.8, 1.4, 2],
           [6.1, 3.0, 4.6, 1.4, 2],
           [5.5, 4.2, 1.4, 0.2, 1],
           [5.0, 2.0, 3.5, 1.0, 2],
           [7.7, 3.0, 6.1, 2.3, 0],
           [5.1, 2.5, 3.0, 1.1, 2],
           [5.9, 3.0, 5.1, 1.8, 0],
           [7.2, 3.2, 6.0, 1.8, 0],
           [4.9, 3.1, 1.5, 0.2, 1],
           [5.7, 3.0, 4.2, 1.2, 2],
           [6.1, 2.9, 4.7, 1.4, 2],
           [5.0, 3.2, 1.2, 0.2, 1],
           [4.4, 3.2, 1.3, 0.2, 1],
           [6.7, 3.1, 5.6, 2.4, 0],
           [4.6, 3.6, 1.0, 0.2, 1],
           [5.1, 3.4, 1.5, 0.2, 1],
           [5.2, 2.7, 3.9, 1.4, 2],
           [6.4, 3.1, 5.5, 1.8, 0],
           [7.4, 2.8, 6.1, 1.9, 0],
           [4.9, 3.1, 1.5, 0.1, 1],
           [5.0, 3.5, 1.6, 0.6, 1],
           [6.7, 3.1, 4.7, 1.5, 2],
           [6.4, 3.2, 5.3, 2.3, 0],
           [6.3, 2.7, 4.9, 1.8, 0],
           [5.8, 4.0, 1.2, 0.2, 1],
           [6.9, 3.1, 5.4, 2.1, 0],
           [5.9, 3.2, 4.8, 1.8, 2],
           [6.6, 2.9, 4.6, 1.3, 2],
           [6.1, 2.8, 4.0, 1.3, 2],
           [7.7, 2.6, 6.9, 2.3, 0],
           [5.5, 2.6, 4.4, 1.2, 2],
           [6.3, 2.9, 5.6, 1.8, 0],
           [7.2, 3.0, 5.8, 1.6, 0],
           [6.5, 3.0, 5.8, 2.2, 0],
           [5.4, 3.9, 1.7, 0.4, 1],
           [6.5, 3.2, 5.1, 2.0, 0],
           [5.9, 3.0, 4.2, 1.5, 2],
           [5.1, 3.7, 1.5, 0.4, 1],
           [5.7, 2.8, 4.5, 1.3, 2],
           [5.4, 3.4, 1.5, 0.4, 1],
           [4.6, 3.4, 1.4, 0.3, 1],
           [4.9, 3.6, 1.4, 0.1, 1],
           [6.7, 2.5, 5.8, 1.8, 0],
           [5.0, 3.6, 1.4, 0.2, 1],
           [6.7, 3.3, 5.7, 2.5, 0],
           [4.4, 3.0, 1.3, 0.2, 1],
           [6.0, 2.2, 5.0, 1.5, 0],
           [6.0, 2.2, 4.0, 1.0, 2],
           [5.0, 3.4, 1.5, 0.2, 1],
           [5.7, 2.8, 4.1, 1.3, 2],
           [5.5, 2.4, 3.8, 1.1, 2],
           [5.1, 3.8, 1.9, 0.4, 1],
           [6.9, 3.1, 5.1, 2.3, 0],
           [5.6, 2.9, 3.6, 1.3, 2],
           [6.1, 2.8, 4.7, 1.2, 2],
           [5.5, 2.5, 4.0, 1.3, 2],
           [5.5, 2.3, 4.0, 1.3, 2],
           [6.0, 2.9, 4.5, 1.5, 2],
           [5.1, 3.8, 1.5, 0.3, 1],
           [5.7, 3.8, 1.7, 0.3, 1],
           [6.7, 3.3, 5.7, 2.1, 0],
           [4.8, 3.1, 1.6, 0.2, 1],
           [5.4, 3.0, 4.5, 1.5, 2],
           [6.5, 3.0, 5.2, 2.0, 0],
           [6.8, 3.0, 5.5, 2.1, 0],
           [7.6, 3.0, 6.6, 2.1, 0],
           [5.0, 3.0, 1.6, 0.2, 1],
           [6.7, 3.0, 5.0, 1.7, 2],
           [4.8, 3.4, 1.9, 0.2, 1],
           [5.8, 2.8, 5.1, 2.4, 0],
           [5.0, 2.3, 3.3, 1.0, 2],
           [4.8, 3.0, 1.4, 0.3, 1],
           [5.2, 3.5, 1.5, 0.2, 1],
           [6.1, 2.6, 5.6, 1.4, 0],
           [5.8, 2.7, 4.1, 1.0, 2],
           [6.9, 3.2, 5.7, 2.3, 0],
           [6.4, 2.9, 4.3, 1.3, 2],
           [7.3, 2.9, 6.3, 1.8, 0],
           [6.3, 2.8, 5.1, 1.5, 0],
           [6.2, 2.8, 4.8, 1.8, 0],
           [6.7, 3.1, 4.4, 1.4, 2],
           [6.0, 2.7, 5.1, 1.6, 2],
           [6.5, 3.0, 5.5, 1.8, 0],
           [6.1, 3.0, 4.9, 1.8, 0],
           [5.6, 3.0, 4.1, 1.3, 2],
           [4.7, 3.2, 1.6, 0.2, 1],
           [6.6, 3.0, 4.4, 1.4, 2]]

if __name__ == '__main__':

    train_set_1 = dataset[0:int(0.3 * len(dataset))]
    train_set_x_1 = [row[:-1] for row in train_set_1]
    train_set_y_1 = [row[-1] for row in train_set_1]

    train_set_2 = dataset[int(0.3*len(dataset)):int(0.6*len(dataset))]
    train_set_x_2 = [row[:-1] for row in train_set_2]
    train_set_y_2 = [row[-1] for row in train_set_2]

    train_set_3 = dataset[int(0.6*len(dataset)):]
    train_set_x_3 = [row[:-1] for row in train_set_3]
    train_set_y_3 = [row[-1] for row in train_set_3]

    classifier1 = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
    classifier2 = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
    classifier3 = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)

    classifier1.fit(train_set_x_1, train_set_y_1)
    classifier2.fit(train_set_x_2, train_set_y_2)
    classifier3.fit(train_set_x_3, train_set_y_3)

    test_from_input = [float(el) for el in input().split(', ')]
    test_from_input = test_from_input[:-1]

    prediction1 = classifier1.predict([test_from_input])[0]
    prediction2 = classifier2.predict([test_from_input])[0]
    prediction3 = classifier3.predict([test_from_input])[0]
    #
    # print(prediction1, prediction2, prediction3)
    # print(test_from_input[3])

    count_0, count_1, count_2 = 0,0,0

    if prediction1 == 0:
        count_0+=1
    elif prediction1 == 1:
        count_1+=1
    else:
        count_2 += 1

    if prediction2 == 0:
        count_0+=1
    elif prediction2 == 1:
        count_1+=1
    else:
        count_2+=1

    if prediction3 == 0:
        count_0+=1
    elif prediction3 == 1:
        count_1+=1
    else:
        count_2+=1


    print(f'Glasovi: {{0: {count_0}, 1: {count_1}, 2: {count_2}}}')

    # if count_0 == count_1 and count_2 == count_1:
    #     print("Predvidena klasa: unknown")

    # maximum_count = 0
    #
    # if count_1 > count_0 and count_1 > count_2:
    #     maximum_count = 1
    # elif count_1 > count_0 and count_2 > count_1:
    #     maximum_count = 2
    #
    # if (count_0 == count_1 and count_0 >= count_2) or (count_0 == count_2 and count_0 >= count_1) or (count_1 == count_2 and count_1 >=count_0):
    #     print("Predvidena klasa: unknown")
    # else:
    #     print(f'Predvidena klasa: {maximum_count}')


    flamur = 1
    flamur_0, flamur_1, flamur_2 = 0,0,0
    max = count_0
    if count_1 > max:
        max = count_1
    if count_2 > max:
        max = count_2

    if count_0 == max and count_1 == max:
        flamur = 0
    elif count_1 == max and count_2 == max:
        flamur = 0
    elif count_0 == max and count_2 == max:
        flamur = 0

    if count_0 == max:
        flamur_0 = 1
    elif count_1 == max:
        flamur_1 = 1
    elif count_2 == max:
        flamur_2 = 1

    if flamur == 0:
        print("Predvidena klasa: unknown")
    else:
        if flamur_0 == 1:
            print(f'Predvidena klasa: 0')
        elif flamur_1 == 1:
            print(f'Predvidena klasa: 1')
        elif flamur_2 ==1:
            print(f'Predvidena klasa: 2')
