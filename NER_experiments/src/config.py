# -*- coding:utf-8 -*-
#warrning: don't put a backslash at the end of any string litral

NER_home = r'E:\google_drive\NER\tayawork-0.9' #don't put a backslash at the end of any string litral
AMIRA_home = r'E:\google_drive\NER\AMIRA-farag' #don't put a backslash at the end of any string litral
AMIRA_config = NER_home+r'\tayait\taps\ner\config\tayait.amiraconfig'
working_dir =  NER_home+r'\temp'
model_path = NER_home+r'\tayait\taps\ner\config\model'
output_path = r'C:\New'

# stemming stemming parameter disabled, just_waw_and_faa, larkey
normalization = True
stemming = False
POS = True
generate_6bi = True
generate_6tri = True
generate_6quad = True
word_position = False
word_length = False
word_unigram_probability = False
word_with_previous_and_word_with_succeeding_word_unigram_ratio = False
dictionaries = False
