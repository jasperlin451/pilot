#outputs all the possible combinations of times for a specific subject
#combination with replacement
#possibleTimes is scanned in from each subject as is numberofClasses
import itertools

def combinations(possibleTimes,numberofClasses):
    combo=[]
    for c in itertools.combinations_with_replacement(possibleTimes,numberofClasses):
        combo.append(c)
    return(combo)
