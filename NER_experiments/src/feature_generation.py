# -*- coding:utf-8 -*-

import codecs
import config
from collections import deque
import normalization


LOC_gaz = dict()
ORG_gaz = dict()
PERS_gaz = dict()

def generate_6bi(features):   
    character_bigrams = []
    if(len(features[0]) > 1):
        character_bigrams.append(features[0][0:2])
        if(len(features[0]) > 2):
            character_bigrams.append(features[0][1:3])
            if(len(features[0]) > 3):
                character_bigrams.append(features[0][2:4])
                character_bigrams.append(features[0][-4:-2])
            else:
                character_bigrams.extend(['N','N'])
            character_bigrams.append(features[0][-3:-1])
        else:
            character_bigrams.extend(['N','N','N','N'])
            
        character_bigrams.append(features[0][-2:])
    else:
        character_bigrams = ['N','N','N','N','N','N'] 
    
    #features[1:1] = character_bigrams
    features.extend(character_bigrams)

def generate_6tri(features):
    character_trigrams = []
    if(len(features[0]) > 2):
        character_trigrams.append(features[0][0:3])
        if(len(features[0]) > 3):
            character_trigrams.append(features[0][1:4])
            if(len(features[0]) > 4):
                character_trigrams.append(features[0][2:5])
                character_trigrams.append(features[0][-5:-2])
            else:
                character_trigrams.extend(['N','N'])
            character_trigrams.append(features[0][-4:-1])
        else:
            character_trigrams.extend(['N','N','N','N'])
            
        character_trigrams.append(features[0][-3:])
    else:
        character_trigrams = ['N','N','N','N','N','N']
        
    #features[7:7] = character_trigrams
    features.extend(character_trigrams)
    
def generate_6quad(features):
    character_quadgrams = []
    if(len(features[0]) > 3):
        character_quadgrams.append(features[0][0:4])
        if(len(features[0]) > 4):
            character_quadgrams.append(features[0][1:5])
            if(len(features[0]) > 5):
                character_quadgrams.append(features[0][2:6])
                character_quadgrams.append(features[0][-6:-2])
            else:
                character_quadgrams.extend(['N','N'])
            character_quadgrams.append(features[0][-5:-1])
        else:
            character_quadgrams.extend(['N','N','N','N'])
            
        character_quadgrams.append(features[0][-4:])
    else:
        character_quadgrams = ['N','N','N','N','N','N']
        
    #features[13:13] = character_quadgrams
    features.extend(character_quadgrams)

#train_test_split_flag

#WP
def word_position(features):
    global absolute_position
    global sentence_counter

    features.append(str(round(float(absolute_position+1)/sentence_dic[sentence_counter],2)))

    absolute_position += 1
    if features[0] in [u'.', u'?', u'؟', u'!', u'·']:
        absolute_position = 0
        sentence_counter += 1
   
#WL
def word_length(features):
    features.append(str(len(features[0])))


#1gP
def word_unigram_probability(features):
    wup = float(token_dic[features[0]])/WORD_COUNT
    features.append(str(wup))

#1gPr
def word_with_previous_and_word_with_succeeding_word_unigram_ratio(features, token_index):
    wup = float(token_dic[token_list[token_index].split()[0]])/WORD_COUNT

    if token_index != 0:
        wup_pre = float(token_dic[token_list[token_index-1].split()[0]])/WORD_COUNT
        wwp_wur = round(wup/wup_pre,2)
    else:
        wwp_wur = 'N'

    if token_index != len(token_list)-1:
        wup_next = float(token_dic[token_list[token_index+1].split()[0]])/WORD_COUNT
        wws_wur = round(wup_next/wup,2)
    else:
        wws_wur = 'N'

    features.extend([str(wwp_wur), str(wws_wur)])

def features_that_account_for_dependence_between_words_in_a_named_entity(features):
    pass

def character_n_gram_probability(features):
    pass

def check_in_LOC_dictionary(features, index):
    if LOC_dic[index][0] == features[0]:
        features.append(LOC_dic[index][1])
    else:
        print("something wrong with index: " + str(index))

def check_in_ORG_dictionary(features, index):
    if ORG_dic[index][0] == features[0]:
        features.append(ORG_dic[index][1])
    else:
        print("something wrong with index: " + str(index))

def check_in_PERS_dictionary(features, index):
    if PERS_dic[index][0] == features[0]:
        features.append(PERS_dic[index][1])
    else:
        print("something wrong with index: " + str(index))

def dictionary_check(features, index):
        
    check_in_LOC_dictionary(features, index)
    check_in_ORG_dictionary(features, index)
    check_in_PERS_dictionary(features, index)



def generate_features(listOfFeatures, token_index):
    if config.generate_6bi:
        #print 'generating_6bi ...'
        generate_6bi(listOfFeatures)
    if config.generate_6tri:
        generate_6tri(listOfFeatures)
    if config.generate_6quad:
        generate_6quad(listOfFeatures)
    if config.word_position:
        word_position(listOfFeatures)
    if config.word_length:
        word_length(listOfFeatures)
    if config.word_unigram_probability:
        word_unigram_probability(listOfFeatures)
    if config.word_with_previous_and_word_with_succeeding_word_unigram_ratio:
        word_with_previous_and_word_with_succeeding_word_unigram_ratio(listOfFeatures, token_index)
    #features_that_account_for_dependence_between_words_in_a_named_entity(listOfFeatures)
    #character_n_gram_probability(listOfFeatures)
    if config.dictionaries:
        dictionary_check(listOfFeatures, token_index)

def generateFeatures(textFileName):
    ##check if file exist
    #filepath = os.getcwd()+'\content\sentences.amirapos'
    tokens = list()
    with codecs.open(config.working_dir+r'\\'+textFileName+r'.sentences.amirapos', encoding='utf-8') as amirapos:
        for line in amirapos:
            tokens.extend(line.strip().split())

    with codecs.open(config.working_dir+r'\\'+textFileName+r".features", encoding='utf-8', mode='w') as featurefile:
        token_index = 0
        for token in tokens:
            temp = token.split('@@@')
            features_list = [temp[0]]            
                
            generate_features(features_list, token_index)
            if config.POS:
                features_list.append(temp[1])

            token_index += 1
            featurefile.write('\t'.join(features_list))
            featurefile.write('\n')


def loadMergedDicts():    
    with codecs.open(r'gazetteers\PERS',encoding='utf-8') as PERSDic:
        for entry in PERSDic:
            PERS_gaz[entry.strip()] = ''

    with codecs.open(r'gazetteers\LOC',encoding='utf-8') as LOCDic:
        for entry in LOCDic:
            LOC_gaz[entry.strip()] = ''

    with codecs.open(r'gazetteers\ORG',encoding='utf-8') as ORGDic:
        for entry in ORGDic:
            ORG_gaz[entry.strip()] = ''

def generateVariations(astring, isMultipleWord):
    variations = [astring]
    if len(astring) < 3:
        return set(variations)
##    if not isMultipleWord:
##        
##    else:
    if astring.startswith('ولل'):
        variations.append(('ال'+astring[3:]).strip())
    elif astring.startswith('لل'):
        variations.append(('ال'+astring[2:]).strip())
    elif astring.startswith('ول'):
        variations.append((astring[2:]).strip())
        variations.append((astring[1:]).strip())
    elif astring.startswith('و'):
        variations.append((astring[1:]).strip())
    elif astring.startswith('ل'):
        variations.append((astring[1:]).strip())
    elif astring.startswith('ب'):
        variations.append((astring[1:]).strip())

    #print(set(variations))
    return set(variations)

def detect_names(n, tokens):
    gazFeatureList = list()
    n_tokens_list = list()
    count = 0;
    position = 0;

    if len(tokens) > 0:
        while count != n and len(tokens) > 0:
            n_tokens_list.append(tokens.popleft());
            count += 1;

        numberOfTokensToBeRemovedFromTheBeginning = 0;

        while len(n_tokens_list) > 0:
            numberOfTokensToBeRemovedFromTheBeginning = len(n_tokens_list)
            
            for x, token in enumerate(n_tokens_list):
                temp_str2 = ' '.join(n_tokens_list[:len(n_tokens_list) - x])
                found = False
                variationsSet = generateVariations(temp_str2, (len(n_tokens_list) - x)>1)
                
                for variation in variationsSet:
                    exceededByPrefix = "0"
                    if variation in LOC_gaz:
                        if variation != temp_str2:
                            exceededByPrefix = '1'
                        temp_token = [temp_str2, '1', exceededByPrefix]
                        gazFeatureList.append(temp_token)                    
                        n_tokens_list = n_tokens_list[numberOfTokensToBeRemovedFromTheBeginning:]
                        for z in range(numberOfTokensToBeRemovedFromTheBeginning):                        
                            if len(tokens) > 0:
                                n_tokens_list.append(tokens.popleft())
                        found = True
                        break
                    elif variation in PERS_gaz:
                        if variation != temp_str2:
                            exceededByPrefix = '1'
                        temp_token = [temp_str2, '2', exceededByPrefix]
                        gazFeatureList.append(temp_token)                   
                        n_tokens_list = n_tokens_list[numberOfTokensToBeRemovedFromTheBeginning:]
                        for z in range(numberOfTokensToBeRemovedFromTheBeginning):                        
                            if len(tokens) > 0:
                                n_tokens_list.append(tokens.popleft())
                        found = True
                        break
                    elif variation in ORG_gaz:
                        if variation != temp_str2:
                            exceededByPrefix = '1'
                        temp_token = [temp_str2, '3', exceededByPrefix]
                        gazFeatureList.append(temp_token)                   
                        n_tokens_list = n_tokens_list[numberOfTokensToBeRemovedFromTheBeginning:]
                        for z in range(numberOfTokensToBeRemovedFromTheBeginning):                        
                            if len(tokens) > 0:
                                n_tokens_list.append(tokens.popleft())
                        found = True
                        break
                if found:
                    break
                

                #remove n_tokens_list.Count-x from the list
                numberOfTokensToBeRemovedFromTheBeginning -= 1

            if numberOfTokensToBeRemovedFromTheBeginning == 0:
                temp_token = [temp_str2, '0', '0']
                gazFeatureList.append(temp_token)
                n_tokens_list = n_tokens_list[1:]
                if len(tokens) > 0:
                    n_tokens_list.append(tokens.popleft())

        return gazFeatureList
       
def generateFeaturesForTrainingAndTesting(corpus):
    latinwords_q = deque()
    tokenList = list()
    ANERCorpPOS_lines = list()
    
    with codecs.open(r'datasets\latinwords', encoding='utf-8') as latinwords:
        for latinword in latinwords:
            latinwords_q.append(latinword.strip())

    with codecs.open(r'datasets\00_ANERCorp_pos_stanford', encoding='utf-8') as ANERCorp_pos:
        for line in ANERCorp_pos:
            ANERCorpPOS_lines.append(line)
    
    with codecs.open(corpus, encoding='utf-8') as infile:
        featureslists = list()
        WORD_COUNT = 0
        for lineIndex, line in enumerate(infile):
            templist = line.strip().split()
            tokenPlusPOS = ANERCorpPOS_lines[lineIndex].strip().rpartition('/')
            if tokenPlusPOS[1] == '':
                print('ERrrrROR')
                break
            if tokenPlusPOS[0] != templist[0]:
                print(tokenPlusPOS[0])
                print(templist[0])
                break
##            term = normalization.removeDiacritics(templist[0])
##            if term.strip() != '':
##                templist[0] = term
                

            if len(templist) != 2:                
                print('error: check out line:', WORD_COUNT)
                break
            if templist[0] == 'رقمكوديتايا':
                templist[0] = latinwords_q.popleft()
            tokenList.append(templist[0])
            f_list = [templist[0],tokenPlusPOS[2]]
            generate_features(f_list, WORD_COUNT)
            f_list.extend(templist[1:])
            featureslists.append(f_list)
            WORD_COUNT += 1

    print(WORD_COUNT)    
    gazFeatureList = detect_names(7, deque(tokenList))    

    print('gazFeatureList:', len(gazFeatureList))

    #toksStatusList = list()
    tokenListIndex = 0
    
    print(len(gazFeatureList), len(featureslists[0]))
    for entry in gazFeatureList:
        #print (entry)
        toks = entry[0].strip().split()
        for i, tok in enumerate(toks):
            #print(tok, featureslists[tokenListIndex][0])
            #break
            if tok == featureslists[tokenListIndex][0]:
                if i == 0:
                    featureslists[tokenListIndex][-1:-1] = entry[1:]
                else:
                    featureslists[tokenListIndex][-1:-1] = [entry[1],'0']
            else:                
                print(tok)
                print(tokenListIndex, featureslists[tokenListIndex][0])
                print()
                #break
                
            tokenListIndex += 1
        
    with codecs.open("features/training_features", encoding='utf-8', mode='w') as trainingfile:
        with codecs.open("features/testing_features", encoding='utf-8', mode='w') as testingfile:
            sentence_flag = False
            #allfeatures = list()

            for line_count, features_list in enumerate(featureslists):
                if float(line_count)/WORD_COUNT < 0.8:
                    trainingfile.write('\t'.join(features_list))
                    trainingfile.write('\n')               
                elif sentence_flag == False:
                    if features_list[0] in [u'.', u'?', u'؟', u'!', u'·']:
                        sentence_flag = True
                    trainingfile.write('\t'.join(features_list))
                    trainingfile.write('\n')
                else:                    
                    testingfile.write('\t'.join(features_list))
                    testingfile.write('\n')

if __name__ == "__main__":
    loadMergedDicts()
    import sys
    p = r'datasets\00_ANERCorp_original'
    #generateFeaturesForTrainingAndTesting(sys.argv[1])
    generateFeaturesForTrainingAndTesting(p)


