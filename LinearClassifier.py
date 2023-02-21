# Starter code for CS 165B HW2 Winter 2023

def column(matrix, i):
    return [row[i] for row in matrix]

def run_train_test(training_input, testing_input):

    from math import sqrt
    """
    Implement the training and testing procedure here. You are permitted
    to use additional functions but DO NOT change this function definition. 
    You are permitted to use the numpy library but you must write 
    your own code for the linear classifier. 

    Inputs:
        training_input: list form of the training file
            e.g. [[3, 5, 5, 5],[.3, .1, .4],[.3, .2, .1]...]
        testing_input: list form of the testing file

    Output:
        Dictionary of result values 

        IMPORTANT: YOU MUST USE THE SAME DICTIONARY KEYS SPECIFIED
        
        Example:
            return {
                "tpr": #your_true_positive_rate,
                "fpr": #your_false_positive_rate,
                "error_rate": #your_error_rate,
                "accuracy": #your_accuracy,
                "precision": #your_precision
            }
    """


    # TODO: IMPLEMENT

    # First line of data indicates number of lines for each class
    sizesTraining = training_input[0]
    sizesTesting = testing_input[0]

    # Extracting specific number of lines per class for training
    features = sizesTraining[0]
    sizeA = sizesTraining[1]
    sizeB = sizesTraining[2]
    sizeC = sizesTraining[3]

    # Extracting specific number of lines per class for testing
    featuresTest = sizesTesting[0]
    sizeAtest = sizesTesting[1]
    sizeBtest = sizesTesting[2]
    sizeCtest = sizesTesting[3]

    # Remove the first line to leave us only with feature data for each class
    training_input.remove(training_input[0])
    testing_input.remove(testing_input[0])

    # Gathering training data for class A (and clearing the data from matrix at the same time)
    A = []
    for i in range(sizeA):
        A.append(training_input[0])
        training_input.remove(training_input[0])

    # Gathering training data for class B (and clearing the data from matrix at the same time)
    B = []
    for i in range(sizeB):
        B.append(training_input[0])
        training_input.remove(training_input[0])

    # Gathering training data for class A (and clearing the data from matrix at the same time)
    C = []
    for i in range(sizeC):
        C.append(training_input[0])
        training_input.remove(training_input[0])

    # Gathering test data for class A (and clearing the data from matrix at the same time)
    testA = []
    for i in range(sizeAtest):
        testA.append(testing_input[0])
        testing_input.remove(testing_input[0])

    # Gathering test data for class B (and clearing the data from matrix at the same time)
    testB = []
    for i in range(sizeBtest):
        testB.append(testing_input[0])
        testing_input.remove(testing_input[0])

    # Gathering test data for class A (and clearing the data from matrix at the same time)
    testC = []
    for i in range(sizeCtest):
        testC.append(testing_input[0])
        testing_input.remove(testing_input[0])

    centrA = [] # Initializing centroid variable for classA
    centrB = [] # Initializing centroid variable for classB
    centrC = [] # Initializing centroid variable for classC

    predA = [] # Initializing array variable for classA
    predB = [] # Initializing array variable for classB
    predC = [] # Initializing array variable for classC

    # Computing centroid for Class A
    for j in range(features):
        centrA.append(sum(A[i][j] for i in range(sizeA)) / sizeA)
    
    # Computing centroid for Class B
    for j in range(features):
        centrB.append(sum(B[i][j] for i in range(sizeB)) / sizeB)

    # Computing centroid for Class C
    for j in range(features):
        centrC.append(sum(C[i][j] for i in range(sizeC)) / sizeC)

    # Initializing performance evaluation metric variables for Class A
    aTP = 0
    aFP = 0
    aTN = 0
    aFN = 0

    # Initializing performance evaluation metric variables for Class A
    bTP = 0
    bFP = 0
    bTN = 0
    bFN = 0

    # Initializing performance evaluation metric variables for Class A
    cTP = 0
    cFP = 0
    cTN = 0
    cFN = 0

    # Processing test data for Class A
    for a in testA:
        distA = sqrt(sum(pow((a[j]-centrA[j]), 2 ) for j in range(featuresTest)))
        distB = sqrt(sum(pow((a[j]-centrB[j]), 2 ) for j in range(featuresTest)))
        distC = sqrt(sum(pow((a[j]-centrC[j]), 2 ) for j in range(featuresTest)))

        if(distA <= distB and distA <= distC):
            predA.append(a)
            aTP = aTP + 1
            bTN = bTN + 1
            cTN = cTN + 1


        if(distB < distA and distB <= distC):
            predB.append(a)
            bFP = bFP + 1
            aFN = aFN + 1
            cTN = cTN + 1

        if(distC < distA and distC < distB):
            predC.append(a)
            cFP = cFP + 1
            aFN = aFN + 1
            bTN = bTN + 1

    # Processing test data for Class C
    for b in testB:
        distA = sqrt(sum(pow((b[j]-centrA[j]), 2 ) for j in range(featuresTest)))
        distB = sqrt(sum(pow((b[j]-centrB[j]), 2 ) for j in range(featuresTest)))
        distC = sqrt(sum(pow((b[j]-centrC[j]), 2 ) for j in range(featuresTest)))


        if(distA <= distB and distA <= distC):
            predA.append(b)
            aFP = aFP + 1
            bFN = bFN + 1
            cTN = cTN + 1

        
        if(distB < distA and distB <= distC):
            predB.append(b)
            bTP = bTP + 1
            aTN = aTN + 1
            cTN = cTN + 1

        if(distC < distA and distC < distB):
            predC.append(b)
            cFP = cFP + 1
            aTN = aTN + 1
            bFN = bFN + 1

    # Processing test data for Class C
    for c in testC:
        distA = sqrt(sum(pow((c[j]-centrA[j]), 2 ) for j in range(featuresTest)))
        distB = sqrt(sum(pow((c[j]-centrB[j]), 2 ) for j in range(featuresTest)))
        distC = sqrt(sum(pow((c[j]-centrC[j]), 2 ) for j in range(featuresTest)))


        if(distA <= distB and distA <= distC):
            predA.append(c)
            aFP = aFP + 1
            bTN = bTN + 1
            cFN = cFN + 1

        if(distB < distA and distB <= distC):
            predB.append(c)
            bFP = bFP + 1
            aTN = aTN + 1
            cFN = cFN + 1

        if(distC < distA and distC < distB):
            predC.append(c)
            cTP = cTP + 1
            aTN = aTN + 1
            bTN = bTN + 1

    # Calculating individual True Positive Rates
    aTPR = aTP / (aTP + aFN)
    bTPR = bTP / (bTP + bFN)
    cTPR = cTP / (cTP + cFN)

    # Calculating individual False Positive Rates
    aFPR = aFP / (aFP + aTN)
    bFPR = bFP / (bFP + bTN)
    cFPR = cFP / (cFP + cTN)

    # Calculating individual Error Rates
    aERR = (aFP + aFN) / (aTP + aFN + aFP + aTN)
    bERR = (bFP + bFN) / (bTP + bFN + bFP + bTN)
    cERR = (cFP + cFN) / (bTP + bFN + bFP + bTN)

    # Calculating individual Acurracies
    aACC = (aTP + aTN) / (aTP + aFN + aFP + aTN)
    bACC = (bTP + bTN) / (bTP + bFN + bFP + bTN)
    cACC = (cTP + cTN) / (bTP + bFN + bFP + bTN)

    # Calculating individual Precisions
    aPRE = aTP / (aTP + aFP)
    bPRE = bTP / (bTP + bFP)
    cPRE = cTP / (cTP + cFP)

    # Calculating average True Positive Rate among the 3 classes 
    TPR = (aTPR + bTPR + cTPR) / 3
    TPR = round(TPR, 2) # Round to two significant figures

    # Calculating average False Positive Rate among the 3 classes 
    FPR = (aFPR + bFPR + cFPR) / 3
    FPR = round(FPR, 2) # Round to two significant figures

    # Calculating average Error Rate among the 3 classes 
    ERR = (aERR + bERR + cERR) / 3
    ERR = round(ERR, 2) # Round to two significant figures

    # Calculating average Accuracy the 3 classes 
    ACC = (aACC + bACC + cACC) / 3
    ACC = round(ACC, 2) # Round to two significant figures

    # Calculating average Precision the 3 classes 
    PRE = (aPRE + bPRE + cPRE) / 3
    PRE = round(PRE, 2) # Round to two significant figures

    # Printing results
    return {
                "tpr": TPR,
                "fpr": FPR,
                "error_rate": ERR,
                "accuracy": ACC,
                "precision": PRE
            } 

    pass

#######
# The following functions are provided for you to test your classifier.
######
def parse_file(filename):
    """
    This function is provided to you as an example of the preprocessing we do
    prior to calling run_train_test
    """
    with open(filename, "r") as f:
        data = [[float(y) for y in x.strip().split(" ")] for x in f]
        data[0] = [int(x) for x in data[0]]

        return data

if __name__ == "__main__":
    """
    You can use this to test your code.
    python hw2.py [training file path] [testing file path]
    """
    import sys

    training_input = parse_file(sys.argv[1])
    testing_input = parse_file(sys.argv[2])

    run_train_test(training_input, testing_input)

