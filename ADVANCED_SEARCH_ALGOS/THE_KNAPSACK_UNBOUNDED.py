def knapsack(itemWeights, itemValues, bagWeightLimit):

    # Set up a list that will hold optimum values for weights 1 to bagWeightLimit.
    # We give index zero a dummy value for convenience (which we won't use) as we
    # want to index bagValues from 1 rather than zero.
    bagValues = [0] * (bagWeightLimit + 1)

    for w in range(1, bagWeightLimit + 1):
        bestValueForWeight = 0
        for i in range(len(itemWeights)):
            if itemWeights[i] <= w:
                previousBagWeight = w - itemWeights[i]
                possibleBestValue = bagValues[previousBagWeight] + itemValues[i]
                if possibleBestValue > bestValueForWeight:
                    bestValueForWeight = possibleBestValue
        bagValues[w] = bestValueForWeight

    print('-----------------------------------------------------------------')
    print('Given a list of item weights', itemWeights, 'and a')
    print('parallel list of item values', itemValues)
    print()
    print('The optimum total value for a bag with a weight limit of', w, 'is', bagValues[bagWeightLimit])
    print('-----------------------------------------------------------------')


itemWeights = [1,5,3,4]
itemValues = [15,10,9,5]
bagWeightLimit = 8

knapsack(itemWeights, itemValues, bagWeightLimit)