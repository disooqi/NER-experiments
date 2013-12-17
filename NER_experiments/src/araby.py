#!/usr/bin/python
# -*- coding=utf-8 -*-
#---
#
# ------------
# Description:
# ------------
#
# Arabic codes
#
# (C) Copyright 2010, Taha Zerrouki
# -----------------
#  $Date: 2010/03/01
#  $Author: Taha Zerrouki$
#  $Revision: 0.1 $
#  This program is written under the Gnu Public License.
#
"""
Arabic module
@author: Taha Zerrouki
@contact: taha dot zerrouki at gmail dot com
@copyright: Arabtechies, Arabeyes,  Taha Zerrouki
@license: GPL
@date:2010/03/01
@version: 0.1
"""
import re
#from stack import *
#class araby:
"""
the arabic chars contains all arabic letters, a sub class of unicode,
"""

COMMA            = u'\u060C'
SEMICOLON        = u'\u061B'
ar_QUESTION      = u'\u061F'
QUESTION         = u'\003F'
SPACE            = chr(32)
EXCLAMATION      = chr(33)   #u'\0021'
Quotation        = chr(34)   #u'\0022'
ar_PERCENT       = u'\u066a'
PERCENT          = chr(37)
LParenthesis     = chr(40)   #u'\0028'
RParenthesis     = chr(41)   #u'\0029'
Asterisk         = chr(42)
FULL_STOP        = chr(46)   #u'\002E'
Colon            = chr(58)
Bullet           = chr(8226)
Less_than        = chr(60)
Equals_sign      = chr(61)
Greater_than     = chr(62)


Leftpointing_double_angle_quotation_mark = chr(171)      #u'\00AB'
MIDDLE_DOT       = chr(183)
Rightpointing_double_angle_quotation_mark = chr(187)      #u'\00BB'
Left_double_quotation_mark  = chr(8220)
Right_double_quotation_mark = chr(8221)

HAMZA            = u'\u0621'
ALEF_MADDA       = u'\u0622'
ALEF_HAMZA_ABOVE = u'\u0623'
WAW_HAMZA        = u'\u0624'
ALEF_HAMZA_BELOW = u'\u0625'
YEH_HAMZA        = u'\u0626'
ALEF             = u'\u0627'
BEH              = u'\u0628'
TEH_MARBUTA      = u'\u0629'
TEH              = u'\u062a'
THEH             = u'\u062b'
JEEM             = u'\u062c'
HAH              = u'\u062d'
KHAH             = u'\u062e'
DAL              = u'\u062f'
THAL             = u'\u0630'
REH              = u'\u0631'
ZAIN             = u'\u0632'
SEEN             = u'\u0633'
SHEEN            = u'\u0634'
SAD              = u'\u0635'
DAD              = u'\u0636'
TAH              = u'\u0637'
ZAH              = u'\u0638'
AIN              = u'\u0639'
GHAIN            = u'\u063a'
TATWEEL          = chr(1600) #u'\u0640'
FEH              = u'\u0641'
QAF              = u'\u0642'
KAF              = u'\u0643'
LAM              = u'\u0644'
MEEM             = u'\u0645'
NOON             = u'\u0646'
HEH              = u'\u0647'
WAW              = u'\u0648'
ALEF_MAKSURA     = u'\u0649'
YEH              = u'\u064a'
MADDA_ABOVE      = u'\u0653'
HAMZA_ABOVE      = u'\u0654'
HAMZA_BELOW      = u'\u0655'

ar_ZERO             = u'\u0660'
ar_ONE              = u'\u0661'
ar_TWO              = u'\u0662'
ar_THREE            = u'\u0663'
ar_FOUR             = u'\u0664'
ar_FIVE             = u'\u0665'
ar_SIX              = u'\u0666'
ar_SEVEN            = u'\u0667'
ar_EIGHT            = u'\u0668'
ar_NINE             = u'\u0669'

# English Numbers
ZERO             = u'\u0030'
ONE              = u'\u0031'
TWO              = u'\u0032'
THREE            = u'\u0033'
FOUR             = u'\u0034'
FIVE             = u'\u0035'
SIX              = u'\u0036'
SEVEN            = u'\u0037'
EIGHT            = u'\u0038'
NINE             = u'\u0039'


DECIMAL          = u'\u066b'
THOUSANDS        = u'\u066c'
STAR             = u'\u066d'
MINI_ALEF        = u'\u0670'
ALEF_WASLA       = u'\u0671'
ar_FULL_STOP        = u'\u06d4'
BYTE_ORDER_MARK  = u'\ufeff'

# Diacritics
FATHATAN         = u'\u064b'
DAMMATAN         = u'\u064c'
KASRATAN         = u'\u064d'
FATHA            = u'\u064e'
DAMMA            = u'\u064f'
KASRA            = u'\u0650'
SHADDA           = u'\u0651'
SUKUN            = u'\u0652'

# Small Letters
SMALL_ALEF      =u"\u0670"
SMALL_WAW       =u"\u06E5"
SMALL_YEH       =u"\u06E6"
#Ligatures
LAM_ALEF                    =u'\ufefb'
LAM_ALEF_HAMZA_ABOVE        =u'\ufef7'
LAM_ALEF_HAMZA_BELOW        =u'\ufef9'
LAM_ALEF_MADDA_ABOVE        =u'\ufef5'
simple_LAM_ALEF             =u'\u0644\u0627'
simple_LAM_ALEF_HAMZA_ABOVE =u'\u0644\u0623'
simple_LAM_ALEF_HAMZA_BELOW =u'\u0644\u0625'
simple_LAM_ALEF_MADDA_ABOVE =u'\u0644\u0622'
# groups
LETTERS=u''.join([
        ALEF , BEH , TEH  , TEH_MARBUTA  , THEH  , JEEM  , HAH , KHAH ,
        DAL   , THAL  , REH   , ZAIN  , SEEN   , SHEEN  , SAD , DAD , TAH   , ZAH   ,
        AIN   , GHAIN   , FEH  , QAF , KAF , LAM , MEEM , NOON, HEH , WAW, YEH  ,
        HAMZA  ,  ALEF_MADDA , ALEF_HAMZA_ABOVE , WAW_HAMZA   , ALEF_HAMZA_BELOW  , YEH_HAMZA  ,
        ])

TASHKEEL =(FATHATAN, DAMMATAN, KASRATAN,
            FATHA,DAMMA,KASRA,
            SUKUN,
            SHADDA);
HARAKAT =(  FATHATAN,   DAMMATAN,   KASRATAN,
            FATHA,  DAMMA,  KASRA,
            SUKUN
            );
SHORTHARAKAT =( FATHA,  DAMMA,  KASRA, SUKUN);

TANWIN =(FATHATAN,  DAMMATAN,   KASRATAN);


LIGUATURES=(
            LAM_ALEF,
            LAM_ALEF_HAMZA_ABOVE,
            LAM_ALEF_HAMZA_BELOW,
            LAM_ALEF_MADDA_ABOVE,
            );
HAMZAT=(
            HAMZA,
            WAW_HAMZA,
            YEH_HAMZA,
            HAMZA_ABOVE,
            HAMZA_BELOW,
            ALEF_HAMZA_BELOW,
            ALEF_HAMZA_ABOVE,
            );
ALEFAT=(
            ALEF,
            ALEF_MADDA,
            ALEF_HAMZA_ABOVE,
            ALEF_HAMZA_BELOW,
            ALEF_WASLA,
            ALEF_MAKSURA,
            SMALL_ALEF,

        );
WEAK   = ( ALEF, WAW, YEH, ALEF_MAKSURA);
YEHLIKE= ( YEH,  YEH_HAMZA,  ALEF_MAKSURA,   SMALL_YEH  );

WAWLIKE     =   ( WAW,  WAW_HAMZA,  SMALL_WAW );
TEHLIKE     =   ( TEH,  TEH_MARBUTA );

SMALL   =( SMALL_ALEF, SMALL_WAW, SMALL_YEH)
MOON =(HAMZA            ,
        ALEF_MADDA       ,
        ALEF_HAMZA_ABOVE ,
        ALEF_HAMZA_BELOW ,
        ALEF             ,
        BEH              ,
        JEEM             ,
        HAH              ,
        KHAH             ,
        AIN              ,
        GHAIN            ,
        FEH              ,
        QAF              ,
        KAF              ,
        MEEM             ,
        HEH              ,
        WAW              ,
        YEH
    );
SUN=(
        TEH              ,
        THEH             ,
        DAL              ,
        THAL             ,
        REH              ,
        ZAIN             ,
        SEEN             ,
        SHEEN            ,
        SAD              ,
        DAD              ,
        TAH              ,
        ZAH              ,
        LAM              ,
        NOON             ,
    );
AlphabeticOrder={
                ALEF             : 1,
                BEH              : 2,
                TEH              : 3,
                TEH_MARBUTA      : 3,
                THEH             : 4,
                JEEM             : 5,
                HAH              : 6,
                KHAH             : 7,
                DAL              : 8,
                THAL             : 9,
                REH              : 10,
                ZAIN             : 11,
                SEEN             : 12,
                SHEEN            : 13,
                SAD              : 14,
                DAD              : 15,
                TAH              : 16,
                ZAH              : 17,
                AIN              : 18,
                GHAIN            : 19,
                FEH              : 20,
                QAF              : 21,
                KAF              : 22,
                LAM              : 23,
                MEEM             : 24,
                NOON             : 25,
                HEH              : 26,
                WAW              : 27,
                YEH              : 28,
                HAMZA            : 29,

                ALEF_MADDA       : 29,
                ALEF_HAMZA_ABOVE : 29,
                WAW_HAMZA        : 29,
                ALEF_HAMZA_BELOW : 29,
                YEH_HAMZA        : 29,
                }
NAMES ={
                ALEF             :  u"ألف",
                BEH              : u"باء",
                TEH              : u'تاء' ,
                TEH_MARBUTA      : u'تاء مربوطة' ,
                THEH             : u'ثاء' ,
                JEEM             : u'جيم' ,
                HAH              : u'حاء' ,
                KHAH             : u'خاء' ,
                DAL              : u'دال' ,
                THAL             : u'ذال' ,
                REH              : u'راء' ,
                ZAIN             : u'زاي' ,
                SEEN             : u'سين' ,
                SHEEN            : u'شين' ,
                SAD              : u'صاد' ,
                DAD              : u'ضاد' ,
                TAH              : u'طاء' ,
                ZAH              : u'ظاء' ,
                AIN              : u'عين' ,
                GHAIN            : u'غين' ,
                FEH              : u'فاء' ,
                QAF              : u'قاف' ,
                KAF              : u'كاف' ,
                LAM              : u'لام' ,
                MEEM             : u'ميم' ,
                NOON             : u'نون' ,
                HEH              : u'هاء' ,
                WAW              : u'واو' ,
                YEH              : u'ياء' ,
                HAMZA            : u'همزة' ,

                TATWEEL          : u'تطويل' ,
                ALEF_MADDA       : u'ألف ممدودة' ,
                ALEF_MAKSURA      : u'ألف مقصورة' ,
                ALEF_HAMZA_ABOVE : u'همزة على الألف' ,
                WAW_HAMZA        : u'همزة على الواو' ,
                ALEF_HAMZA_BELOW : u'همزة تحت الألف' ,
                YEH_HAMZA        : u'همزة على الياء' ,
                FATHATAN         : u'فتحتان',
                DAMMATAN         : u'ضمتان',
                KASRATAN         : u'كسرتان',
                FATHA            : u'فتحة',
                DAMMA            : u'ضمة',
                KASRA            : u'كسرة',
                SHADDA           : u'شدة',
                SUKUN            : u'سكون',
                }

stopwords = (u"بلا", u"فلا", u"ولا", u"ان", u"بعد", u"ضد", u"يلي", u"الى", u"في", u"من", u"حتى", u"وهو", u"يكون", u"به", u"وليس", u"أحد", u"على", u"وكان", u"تلك", u"كذلك", u"التي", u"وبين", u"فيها", u"عليها", u"إن", u"وعلى", u"لكن", u"عن", u"مساء", u"ليس", u"منذ", u"الذي", u"أما", u"حين", u"ومن", u"ليست", u"وكانت", u"أي", u"ما", u"عنه", u"حول", u"دون", u"مع", u"لكنه", u"ولكن", u"له", u"هذا", u"والتي", u"فقط", u"ثم", u"هذه", u"أنه", u"تكون", u"قد", u"بين", u"جدا", u"لن", u"نحو", u"كان", u"لهم", u"لأن", u"اليوم", u"لم", u"هؤلاء", u"فإن", u"فيه", u"ذلك", u"لو", u"عند", u"اللذين", u"كل", u"بد", u"لدى", u"وثي", u"أن", u"ومع", u"فقد", u"بل", u"هو", u"عنها", u"منه", u"بها", u"وفي", u"فهو", u"تحت", u"لها", u"أو", u"إذ", u"علي", u"عليه", u"كما", u"كيف", u"هنا", u"وقد", u"كانت", u"لذلك", u"أمام", u"هناك", u"قبل", u"معه", u"يوم", u"منها", u"إلى", u"إذا", u"هل", u"حيث", u"هي", u"اذا", u"او", u"و", u"لا", u"الي", u"إلي", u"مازال", u"لازال", u"لايزال", u"مايزال", u"اصبح", u"أصبح", u"أمسى", u"امسى", u"أضحى", u"اضحى", u"ظل", u"مابرح", u"مافتئ", u"ماانفك", u"بات", u"صار", u"وليست", u"إن", u"كأن", u"ليت", u"لعل", u"لاسيما", u"ولايزال", u"الحالي", u"ضمن", u"اول", u"وله", u"ذات", u"اي", u"بدلا", u"اليها", u"انه", u"الذين", u"فانه", u"وان", u"والذي", u"وهذا", u"لهذا", u"الا", u"فكان", u"ستكون", u"مما", u"أبو", u"بإن", u"الذي", u"اليه", u"يمكن", u"بهذا", u"لدي", u"وأن", u"وهي", u"وأبو", u"آل", u"الذي", u"هن", u"الذى", u"وكذلك", u"وما", u"ولهذا", u"وقبل", u"اما",  u"بتلك", u"بهذه", u"بذلك", u"لماذا", u"ماذا", u"لما", u"ولما", u"ولماذا", u"وماذا", u"ولم", u"مثل", u"مثلا", u"ابن", u"بعض", u"كلا", u"قال", u"قالت", u"لقد", u"ولقد", u"ولعل", u"انهم", u"ايضا", u"كل", u"وكل", u"بينهم", u"بين", u"بينما", u"بينهن", u"وبينما", u"وبين", u"بيننا", u"وبينهم", u"وايضا", u"وان", u"والى", u"وفي", u"واذا", u"لذا", u"ولذا", u"بحيث", u"وهل", u"ومنها", u"بما", u"وبما", u"سوف", u"لسوف", u"ولسوف", u"وسوف", u"أثناء", u"وأثناء",  u"اللتي", u"واللتي", u"باللتي", u"فاللتي", u"فيهم", u"")



