# -*- coding:utf8 -*-
#بسم الله الرحمن الرحيم

import sys
import codecs

count = 0
true = 0
positive = 0
true_positive = 0
BETA = 1

##with codecs.open(sys.argv[1], encoding='utf-8') as testingfile:
##    for x, line in enumerate(testingfile):
##        tags = line.split()
##        if len(tags) > 1 and tags[-2] != 'O':
##            #print tags[-2], tags[-1]
##            if tags[-1] == tags[-2]:
##                true_positive += 1
##            else:
##                pass
##                #print(x+1)
##            true += 1
##
##        if len(tags) > 1 and tags[-1] != 'O':
##            #print tags[-2], tags[-1]
##            positive += 1

'''
Two states and three inputs:
possible_true_positive = False
possible_true_positive = True
inputs: O, startswith('B-'), startswith('I-')
'''

with codecs.open(sys.argv[1], encoding='utf-8') as testingfile:
    possible_true_positive = False 
    for x, line in enumerate(testingfile):
        tags = line.split()
        if possible_true_positive and tags[-2].startswith('B-'):
            true += 1
            if not tags[-1].startswith('I-'):###
                true_positive += 1 #counting the previous NE not current
            else:
                print(x)
            if tags[-1] != tags[-2]:
                possible_true_positive = False
            else:
                positive += 1
        elif not possible_true_positive and tags[-2].startswith('B-'):
            true += 1
            if tags[-1] == tags[-2]:
                possible_true_positive = True
                positive += 1
        elif possible_true_positive and tags[-2].startswith('I-'):
            if tags[-1] != tags[-2]:
                possible_true_positive = False
            if tags[-1].startswith('B-'):
                positive += 1
        elif not possible_true_positive and tags[-2].startswith('I-'):
            if tags[-1].startswith('B-'):
                positive += 1
        elif possible_true_positive and tags[-2] == 'O':
            if not tags[-1].startswith('I-'):###
                true_positive += 1 #counting the previous NE not current
            else:
                print(x)
            if tags[-1].startswith('B-'):
                positive += 1
            possible_true_positive = False
        elif not possible_true_positive and tags[-2] == 'O':
            if tags[-1].startswith('B-'):
                positive += 1
        else:
            raise Exception
        #print(x)
    else:
        if possible_true_positive:
            true_positive += 1
            
        


print ("True positive: ", str(true_positive))
print ("Positive: ", str(positive))
print ("True: ", str(true))

precision = 100*(float(true_positive)/positive)
recall = 100*(float(true_positive)/true)

print("precision: ", str(precision))
print("recall:    ", str(recall))

f = ((BETA*BETA+1) * (precision * recall)) / (BETA*BETA * (precision + recall))
print("F-measure: ", str(f))
        
