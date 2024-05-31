from Algorithm.Synergy.Synergy import *
import random

weightDP = {}
botChoiceList = [] # ingredient_robot

# Initialize each time playing a new game
def initialize_algorithm():
    weightDP = {}
    botChoiceList = [] # ingredient_robot
    botList = []

# Set DP table by initial selection
def initSynergy(botFirstSelect, botList):
    for name in Estimate_Synergy.getSynergyList():
        if (name == botFirstSelect) :
            continue
        weightDP[name] = [Estimate_Synergy[botFirstSelect].value[name]]
        weightDP[botFirstSelect] = [-1]
    botList.append(botFirstSelect)
        
# Function: Based on the selected ingredients, the ingredients with the largest synergy value are returned
# Output: Ingredients with the largest synergy value
def Greedy():
    greedDict = {}
    for name in Estimate_Synergy.getSynergyList():
        if (-1 in weightDP[name]): 
            continue
        greedDict[name] = max(weightDP[name])
    result = max(greedDict.values())

    for name in greedDict:
        if (greedDict[name] == result): 
            botChoiceList.append(name)
            return name

# Function: Update all the order of indexes to be updated in the DP table
# Input: Index to be updated
def updateDP(index, botSelect, botList):
    weightDP[botSelect].append(-1)
    # touring all the synergistic materials
    for name in Estimate_Synergy.getSynergyList():
        # Skip if there's -1
        if (-1 in weightDP[name]): 
            continue
        sum = 0
        # Compute the list selected by the robot and the material to be selected
        for i in botList:
            sum += Estimate_Synergy[name].value[i]
        weightDP[name].append(weightDP[botSelect][index - 1] + sum)
    
        
# Function: Output actual synergy score between currently selected materials
def sumSynergy(list):
    sum = 0
    for standard in list:
        for obj in list:
            if (standard == obj):
                continue
            sum += Synergy[standard].value[obj]
    sum = (int)(sum / 2)
    return sum

# -------------
# Implementing Robot Learning
# -------------
# Make a table of synergy scores that the robot guesses
# Based on that, I choose it in a greedy way
# If the score is lower than expected, lower the estimated synergy score
# If the score is higher than expected, it increases the estimated synergy score.

# 1. Create a robot guess synergy score table. Put in any value.
def random_estimation():
    already = []
    
    for ingredient1 in Estimate_Synergy:
        ingredient1 = ingredient1.name

        for ingredient2 in Estimate_Synergy:
            ingredient2 = ingredient2.name
            if ingredient2 in already:
                continue
            if ingredient1 == ingredient2:
                continue
            already.append(ingredient1)
            
            Estimate_Synergy.updateSynergy(ingredient1, ingredient2, random.randrange(3,25))
            

# 2. Based on this Synergy score table, run Greedy and updateDP functions
# See Greedy, updateDP functions above

# 3. Find the actual synergy score and the synergy score expected by the robot
# The actual synergy score is obtained by the sumSynergy function above

# Obtain robot expected synergy score
def estimate_sumSynergy(list):
    sum = 0
    for standard in list:
        for obj in list:
            if (standard == obj):
                continue
            sum += Estimate_Synergy[standard].value[obj]
    sum = (int)(sum / 2)
    return sum


# 4. Update expected synergy score (learning)
def learning(list, newChoice):
    true_score = sumSynergy(list)
    estimate_score = estimate_sumSynergy(list)
    difference = abs(true_score - estimate_score)

    scale = (int)(difference / (len(list) - 1))
    
    for ingredient in list:
        if ingredient == newChoice:
            continue
        if true_score > estimate_score:
            Estimate_Synergy.updateSynergy(newChoice, ingredient, scale, True)
        elif true_score < estimate_score:
            Estimate_Synergy.updateSynergy(newChoice, ingredient, -(scale), True)
