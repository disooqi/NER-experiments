from araby import *

en_words = list()

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]

diacriticsNormTable = {
    FATHATAN:'',            DAMMATAN:'',
    KASRATAN:'',            FATHA:'',
    DAMMA:'',               KASRA:'',
    SHADDA:'',              SUKUN:''
    }

norm_table = {  ALEF_MADDA:ALEF,        ALEF_HAMZA_ABOVE:ALEF,
                ALEF_HAMZA_BELOW:ALEF,  ALEF:ALEF,
                BEH:BEH,                TEH:TEH,
                THEH:THEH,              JEEM:JEEM,
                HAH:HAH,                KHAH:KHAH,
                DAL:DAL,                THAL:THAL,
                REH:REH,                ZAIN:ZAIN,
                SEEN:SEEN,              SHEEN:SHEEN,
                SAD:SAD,                DAD:DAD,
                TAH:TAH,                ZAH:ZAH,
                AIN:AIN,                GHAIN:GHAIN,
                FEH:FEH,                QAF:QAF,
                KAF:KAF,                LAM:LAM,
                MEEM:MEEM,              NOON:NOON,
                HEH:HEH,                WAW:WAW,
                YEH:YEH,                TEH_MARBUTA:HEH+SPACE,
                YEH_HAMZA:YEH_HAMZA,    WAW_HAMZA:WAW_HAMZA,
                HAMZA:HAMZA,            ALEF_MAKSURA:YEH,

                LAM_ALEF:LAM+ALEF,       LAM_ALEF_HAMZA_ABOVE:LAM+ALEF,
                LAM_ALEF_HAMZA_BELOW:LAM+ALEF,
                LAM_ALEF_MADDA_ABOVE:LAM+ALEF,

                #Punctuations
                ar_QUESTION:ar_QUESTION,    SEMICOLON:SEMICOLON,
                COMMA:COMMA,                TATWEEL:'',
                ar_FULL_STOP:ar_FULL_STOP,  FULL_STOP:ar_FULL_STOP,
                PERCENT:ar_PERCENT,         ar_PERCENT:ar_PERCENT,
                DECIMAL:DECIMAL,            Colon:Colon,
                THOUSANDS:THOUSANDS,
                QUESTION:ar_QUESTION,       EXCLAMATION:EXCLAMATION,                
                LParenthesis:LParenthesis,  RParenthesis:RParenthesis,
                Quotation:Quotation,        BYTE_ORDER_MARK:BYTE_ORDER_MARK,
                STAR:'',                    Asterisk:'',
                Bullet:'',                  Equals_sign:'',
                Leftpointing_double_angle_quotation_mark:Quotation,
                Rightpointing_double_angle_quotation_mark:Quotation,
                Left_double_quotation_mark:Quotation,
                Right_double_quotation_mark:Quotation,
                Less_than:Quotation,        Greater_than:Quotation,
          
                ZERO:ZERO,              ONE:ONE,
                TWO:TWO,                THREE:THREE,
                FOUR:FOUR,              FIVE:FIVE,
                SIX:SIX,                SEVEN:SEVEN,
                EIGHT:EIGHT,            NINE:NINE,

                ar_ZERO:ZERO,           ar_ONE:ONE,
                ar_TWO:TWO,             ar_THREE:THREE,
                ar_FOUR:FOUR,           ar_FIVE:FIVE,
                ar_SIX:SIX,             ar_SEVEN:SEVEN,
                ar_EIGHT:EIGHT,         ar_NINE:NINE,     
                
    }

def encode(word):
    return u'رقمكوديتايا'

def removeDiacritics(token):
    token = token.strip()
    term = list()
    for char in token:
        if char in diacriticsNormTable:
            term.append(diacriticsNormTable[char])
        else:
            term.append(char)
            
    return ''.join(term).strip()

def fullyNormalize(token):
    token = removeDiacritics(token)
    term = list()
    for char in token:
        if char in norm_table:
            term.append(norm_table[char])
        elif char == MIDDLE_DOT and (len(token) == 1 or token.endswith(MIDDLE_DOT)):
            term.append(ar_FULL_STOP)            
        elif char in alpha:         
            term = encode(token)
            en_words.append(token)
            break        
        else:
            term.append(char)

    return ''.join(term).strip()
