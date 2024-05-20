from art import tprint

# Transliterater By TEHSEEN AJMAL 2022-CE-53
# This transliterator can transliterate a sentence not only a single word
"""this Roman urdu to urdu Transliterator is not perfect but can easily translate double letters with single sound
 like,kh,ch,th,dh,gh,xh,sh,bh,ph,etc_______"""

# ____sample words____ : results

# tehseen : تحسیں
# haathi : ہاتھی
# doodh : دودھ
# shukria : شُکریا
# ghazal : غَزَل
# khaalid : خالد
# kahaan gai thay : کَہاں گے تھے

lang2 = {'5': '5', '3': '3', '': '', 'آ': 'aa', 'ا': 'a', 'ب': 'b', 'ت': 't', 'پ': 'p', 'ٹ': 't', 'ث': 's', 'ج': 'j',
         'چ': 'ch', 'ح': 'h', 'اح': 'ah', 'خ': 'kh', 'د': 'd', 'ڈ': 'd', 'ذ': 'z',
         'ر': 'r', 'ڑ': 'r', 'ز': 'z', 'ژ': 'y', 'س': 's', 'ش': 'sh', 'ص': 's', 'ض': 'z', 'ط': 't', 'ظ': 'z', 'ع': '',
         'غ': 'gh', 'ف': 'f', 'ق': 'q', 'ک': 'k'
    , 'گ': 'g', 'ل': 'l', 'م': 'm', 'ن': 'n', 'ں': 'n', 'و': 'o', 'وا': 'wa', 'ؤ': '', 'ہ': 'h', 'ھ': 'h', 'ی': 'ee',
         'یہ': 'y', 'ئ': 'ai', 'ے': 'ai', 'ۓ': 'ay', 'َ': 'a', 'ُ': 'u', 'ِ': 'i'}
lang1 = {'': '', '_': '', 'a': 'َ', 'aa': 'ا', 'ai': 'ے', 'ate': 'یٹ', 'ap': 'یپ', 'bh': 'بھ', 'b': 'ب', 'c': 'ک',
         'ch': 'چ', 'd': 'د', 'dh': 'دھ', 'e': '', 'ee': 'ی', 'f': 'ف', 'g': 'گ', 'al': 'ع', 'gh': 'غ', 'ghar': 'گھر',
         'h': 'ح',
         'he': 'ہ', 'i': 'ِ', 'ii': 'ی', 'ia': 'یا', 'j': 'ج', 'k': 'ک', 'khal': 'خ', 'khan': 'کھ', 'l': 'ل', 'm': 'م',
         'n': 'ن', 'noo': 'ں', 'o': 'و', 'p': 'پ', 'pe': 'پ', 'ph': 'پھ', 'q': 'ق', 'r': 'ر', 's': 'س', 'sh': 'ش',
         't': 'ت', 'th': 'تھ', 'u': 'ُ', 'v': 'و', 'w': 'و', 'xi': 'ز', 'x': 'کس', 'xh': 'چھ''', 'y': 'ی', 'ay': 'ے',
         'z': 'ز', 'llah': 'للہ'}


def english(x):
    input_value = x
    orignal = input_value
    # ________________ if multiple words are entered
    word = orignal.split(' ')
    g = ''
    a = []
    # mea is for translation or meaning___________________________________________
    mea = []
    lang1 = {'': '', '_': '', 'a': 'َ', 'aa': 'ا', 'ai': 'ے', 'ate': 'یٹ', 'ap': 'یپ', 'bh': 'بھ', 'b': 'ب', 'c': 'ک',
             'ch': 'چ', 'd': 'د', 'dh': 'دھ', 'e': '', 'ee': 'ی', 'f': 'ف', 'g': 'گ', 'al': 'ع', 'gh': 'غ',
             'ghar': 'گھر', 'h': 'ح',
             'he': 'ہ', 'i': 'ِ', 'ii': 'ی', 'ia': 'یا', 'j': 'ج', 'k': 'ک', 'khal': 'خ', 'khan': 'کھ', 'l': 'ل',
             'm': 'م',
             'n': 'ن', 'noo': 'ں', 'o': 'و', 'p': 'پ', 'pe': 'پ', 'ph': 'پھ', 'q': 'ق', 'r': 'ر', 's': 'س', 'sh': 'ش',
             't': 'ت', 'th': 'تھ', 'u': 'ُ', 'v': 'و', 'w': 'و', 'xi': 'ز', 'x': 'کس', 'xh': 'چھ''', 'y': 'ی',
             'ay': 'ے',
             'z': 'ز', 'llah': 'للہ'}
    temp = 0
    print("Input -- ",input_value)
    indexes = 0
    # This will check double words with single sound:______________________like: ch, th, kh etc
    for round in range(len(word)):
        h = []
        h = word[round]
        llahindex = h.find('llah')
        chindex = h.find('ch')
        gharindex = h.find('ghar')
        thindex = h.find('th')
        hoindex = h.find('ho')
        ateindex = h.find('ate')
        apindex = h.find('ap')
        ppindex = h.find('pp')
        xhindex = h.find('xh')
        iaindex = h.find('ia')
        aiindex = h.find('ai')
        eeindex = h.find('ee')
        aaindex = h.find('aa')
        shindex = h.find('sh')
        khindex = h.find('kh')
        llindex = h.find('ll')
        ooindex = h.find('oo')
        ssindex = h.find('ss')
        bhindex = h.find('bh')
        ahaindex = h.find('aha')
        iiindex = h.find('ii')
        ayindex = h.find('ay')
        eaindex = h.find('ea')
        haiindex = h.find('hai')
        haindex = h.find('ha')
        dhindex = h.find('dh')
        phindex = h.find('ph')
        ghindex = h.find('gh')
        alindex = h.find('ali')
        umindex = h.find('uma')
        a = []
        # checking the special cases:+++++++++++++++++++++++++++++++++++++
        for i in h:
            a.append(i)
        if alindex == 0 or umindex == 0:
            a[0] = 'al'
        if a[0] == ' ':
            a.pop(0)
        if a[0] == 'x':
            a[0] = 'xi'
        if a[0] == 'i':
            a[0] = 'aa'
        if a[0] == 'u':
            a[0] = 'aa'
        if a[0] == 'a':
            a[0] = 'aa'
        if a[-1] == 'i':
            a[-1] = 'ii'
        if a[0] == 'e':
            a[0] = 'aa'
        if a[-1] == 'a':
            a[-1] = 'aa'
        if a[-1] == 'n':
            a[-1] = 'noo'
        if a[-1] == 'u':
            a[-1] = 'o'
        for k in range(len(a) - 1):
            if a[k] == a[k + 1]:
                a[k + 1] = ''
        # ____may be it can create a problem , but we can remove it because some words have double letter
        # ____and have double letter sound : I don't know the exact example.

        # ---------------------------------------------------------------------------------------
        # to replace the original letter with the letter having most probability
        if (khindex != -1) or (shindex != -1) or (a[0] == 'g' and a[1] == 'h') or (aiindex != -1) or (
                haiindex != -1) or (
                gharindex != -1) or (apindex != -1) or (iiindex != -1) or (iaindex != -1) or (hoindex != -1) or \
                (eeindex != -1) or (xhindex != -1) or (chindex != -1) or (aaindex != -1) or (llindex != -1) or \
                (bhindex != -1) or (ppindex != -1) or (eaindex != -1) or (ayindex != -1) or (ahaindex != -1) or \
                (ateindex != -1) or (ssindex != -1) or (ooindex != -1) or (hoindex != -1) or (thindex != -1) or \
                (dhindex != -1) or (ghindex != -1) or (llahindex != -1):

            if khindex > -1:
                temp_ho = 1
                if len(a) - khindex > 4:
                    if khindex == (len(a) - 2):
                        a[khindex] = 'khal'
                    elif a[khindex + 4] == 'n':
                        a[khindex] = 'khan'
                        a[(khindex + 1)] = '_'
                    else:
                        a[khindex] = 'khal'
                        a[(khindex + 1)] = '_'
                else:
                    a[khindex] = 'khan'
                    a[(khindex + 1)] = '_'
            if haindex == 0:
                if haindex > -1:
                    if len(a) > haindex + 2:
                        if a[haindex + 2] == 'th':
                            a[haindex] = 'he'
                        elif len(a) > haindex + 3:
                            if a[haindex + 3] == 'th':
                                a[haindex] = 'he'
            if phindex > -1:
                a[phindex] = 'ph'
                a[phindex + 1] = ''
                temp_ho = 1
            if a[0] == 'g' and a[1] == 'h':
                a[0] = ''
                a[1] = 'gh'
            if eeindex > -1:
                a[eeindex] = 'ee'
                a[(eeindex + 1)] = '_'
            if iiindex > -1:
                a[iiindex] = 'ee'
                a[(iiindex + 1)] = '_'
            if chindex > -1:
                a[chindex] = 'ch'
                a[chindex + 1] = ''
            if shindex > -1:
                a[shindex] = 'sh'
                a[(shindex + 1)] = '_'
            if gharindex > -1:
                a[gharindex] = 'ghar'
                a[gharindex + 1] = ''
                a[gharindex + 3] = ''
            if thindex > -1:
                a[thindex] = 'th'
                a[(thindex + 1)] = ''
            if aaindex > -1:
                a[aaindex] = 'aa'
                a[(aaindex + 1)] = ''
                indexes += 1
            if llindex > -1:
                a[llindex] = 'l'
                a[(llindex + 1)] = ''
            if ssindex > -1:
                a[ssindex] = 's'
                a[(ssindex + 1)] = ''
            if ooindex > -1:
                a[ooindex] = 'o'
                a[(ooindex + 1)] = ''
            if ppindex > -1:
                a[ppindex] = '_'
                a[(ppindex + 1)] = 'p'
            if a[apindex - 1] == 'aa':
                a[apindex + 1] = 'p'
            elif apindex > -1:
                a[(apindex + 1)] = 'ap'
            if bhindex > -1:
                a[bhindex] = 'bh'
                a[(bhindex + 1)] = ''
            if ahaindex > -1:
                a[(ahaindex + 1)] = 'he'
            if ateindex > -1:
                a[(ateindex + 1)] = 'ate'
            if iaindex > -1:
                a[iaindex] = 'ia'
                a[(iaindex + 1)] = ''
            if eaindex > -1:
                a[eaindex] = 'ia'
                a[(eaindex + 1)] = ''
            if a[hoindex - 1] == ('khal' or 'khan'):
                a[hoindex] = '_'
            elif hoindex > -1:
                a[hoindex] = 'he'
            if haiindex > -1:
                a[haiindex] = 'he'
            if xhindex > -1:
                a[xhindex] = 'xh'
                a[(xhindex + 1)] = ''

            if ayindex > -1:
                if word[round][-1] != 'y':
                    a[ayindex] = 'y'
                    a[ayindex + 1] = '_'
                else:
                    a[ayindex] = 'ay'
                    a[ayindex + 1] = '_'
            if aiindex == (len(h) - 2):
                a[aiindex] = 'ai'
                a[(aiindex + 1)] = ''
            elif aiindex > -1:
                a[aiindex] = 'ee'
                a[aiindex + 1] = ''
            if dhindex > -1:
                a[dhindex] = 'dh'
                a[dhindex + 1] = ''
            if ghindex > -1:
                a[ghindex] = 'gh'
                a[ghindex + 1] = ''
            if llahindex > -1:
                a[llahindex] = 'llah'
                a[llahindex + 1] = ''
                a[llahindex + 2] = ''
                a[llahindex + 3] = ''
            # ----------------------------------------------------------------------------------------------------
            # ~~~~~~Loops :-------------------------------------------------------------------------------
            # loops to check again if some cases are multiple times:
            '''temp_str=''
                    for letter in a:
                        temp_str+=letter
                    h=temp_str'''
            h = ''
            for letter in word[round]:
                h += letter
            for index in range(len(h)):
                eeindex2 = h.find('ee', eeindex + 1, len(h))
                if eeindex2 > -1:
                    eeindex = eeindex2
                    break
            for index in range(len(h)):
                aaindex2 = h.find('aa', aaindex + 1, len(h))
                if aaindex2 > -1:
                    aaindex = aaindex2
                    break
            for index in range(len(h)):
                shindex2 = h.find('sh', shindex + 1, len(h))
                if shindex2 > -1:
                    shindex = shindex2
                    break
            for index in range(len(h)):
                khindex2 = h.find('kh', khindex + 1, len(h))
                if khindex2 > -1:
                    khindex2 = khindex2
                    break
            for index in range(len(h)):
                llindex2 = h.find('ll', llindex + 1, len(h))
                if llindex2 > -1:
                    llindex = llindex2
                    break
            for index in range(len(h)):
                chindex2 = h.find('ch', chindex + 1, len(h))
                if chindex2 > -1:
                    chindex = chindex2
                    break
            for index in range(len(h)):
                gharindex2 = h.find('ghar', gharindex + 1, len(h))
                if gharindex2 > -1:
                    gharindex = gharindex2
                    break
            for index in range(len(h)):
                thindex2 = h.find('th', thindex + 1, len(h))
                if thindex2 > -1:
                    thindex = thindex2
                    break
            for index in range(len(h)):
                hoindex2 = h.find('ho', hoindex + 1, len(h))
                if hoindex2 > -1:
                    hoindex = hoindex2
                    break
            for index in range(len(h)):
                ateindex2 = h.find('ate', ateindex + 1, len(h))
                if ateindex2 > -1:
                    ateindex = ateindex2
                    break
            for index in range(len(h)):
                apindex2 = h.find('ap', apindex + 1, len(h))
                if apindex2 > -1:
                    apindex = apindex2
                    break
            for index in range(len(h)):
                ppindex2 = h.find('pp', ppindex + 1, len(h))
                if ppindex2 > -1:
                    ppindex = ppindex2
                    break
            for index in range(len(h)):
                xhindex2 = h.find('xh', xhindex + 1, len(h))
                if xhindex2 > -1:
                    xhindex = xhindex2
                    break
            for index in range(len(h)):
                iaindex2 = h.find('ia', iaindex + 1, len(h))
                if iaindex2 > -1:
                    iaindex = iaindex2
                    break
            for index in range(len(h)):
                aiindex2 = h.find('ai', aiindex + 1, len(h))
                if aiindex2 > -1:
                    aiindex = aiindex2
                    break
            for index in range(len(h)):
                ooindex2 = h.find('oo', ooindex + 1, len(h))
                if ooindex2 > -1:
                    ooindex = ooindex2
                    break
            for index in range(len(h)):
                ssindex2 = h.find('ss', ssindex + 1, len(h))
                if ssindex2 > -1:
                    ssindex = ssindex2
                    break
            for index in range(len(h)):
                bhindex2 = h.find('bh', bhindex + 1, len(h))
                if bhindex2 > -1:
                    bhindex = bhindex2
                    break
            for index in range(len(h)):
                ahaindex2 = h.find('aha', ahaindex + 1, len(h))
                if ahaindex2 > -1:
                    ahaindex = ahaindex2
                    break
            for index in range(len(h)):
                iiindex2 = h.find('ii', chindex + 1, len(h))
                if iiindex2 > -1:
                    iiindex = iiindex2
                    break
            for index in range(len(h)):
                ayindex2 = h.find('ay', ayindex + 1, len(h))
                if ayindex2 > -1:
                    ayindex = ayindex2
                    break
            for index in range(len(h)):
                eaindex2 = h.find('ea', eaindex + 1, len(h))
                if eaindex2 > -1:
                    eaindex = eaindex2
                    break
            for index in range(len(h)):
                haiindex2 = h.find('hai', haiindex + 1, len(h))
                if haiindex2 > -1:
                    haiindex = haiindex2
                    break
            for index in range(len(h)):
                haindex2 = h.find('ha', haindex + 1, len(h))
                if haindex2 > -1:
                    haindex = haindex2
                    break
            for index in range(len(h)):
                dhindex2 = h.find('dh', dhindex + 1, len(h))
                if dhindex2 > -1:
                    dhindex = dhindex2
                    break
            for index in range(len(h)):
                phindex2 = h.find('ph', phindex + 1, len(h))
                if phindex2 > -1:
                    phindex = phindex2
                    break
            for index in range(len(h)):
                ghindex2 = h.find('gh', ghindex + 1, len(h))
                if ghindex2 > -1:
                    ghindex = ghindex2
                    break
            # ---------------------------------------------------------------------------
            # to checkh conditions again:
            # ~~~~~~~ kh check:-----------------------------------------------------------------------------------------------------
            if khindex > -1:
                if len(a) - khindex > 4:
                    if khindex == (len(a) - 2):
                        a[khindex] = 'khal'
                    elif a[khindex + 4] == 'n':
                        a[khindex] = 'khan'
                        a[(khindex + 1)] = '_'

                    else:
                        a[khindex] = 'khal'
                        a[(khindex + 1)] = '_'
                else:
                    a[khindex] = 'khan'
                    a[(khindex + 1)] = '_'
            # for haathi ___________________________________________
            if haindex == 0:
                if haindex > -1:
                    if len(a) > haindex + 2:
                        if a[haindex + 2] == 'th':
                            a[haindex] = 'he'
                        elif len(a) > haindex + 3:
                            if a[haindex + 3] == 'th':
                                a[haindex] = 'he'
            # ~~~~~~~ ee check:-----------------------------------------------------------------------------------------
            if eeindex > -1:
                a[eeindex] = 'ee'
                # a[(eeindex + 1)] = '_'
            # ~~~~~~~ ii check:--------------------------------------------------------------------------------------------
            if iiindex > -1:
                a[iiindex] = 'ee'
                a[(iiindex + 1)] = '_'
            # ~~~~~~~ gh check:--------------------------------------------------------------------------------------------
            if a[0] == 'g' and a[1] == 'h':
                a[0] = ''
                a[1] = 'gh'
            # ~~~~~~~ gharri
            # :---------------------------------------------------------------------------------------------
            if gharindex > -1:
                a[gharindex] = 'ghar'
                a[gharindex + 1] = ''
                a[gharindex + 3] = ''
            # ~~~~~~~ sh check
            # :-------------------------------------------------------------------------------------------
            if shindex > -1:
                a[shindex] = 'sh'
                # a[(shindex+1)] = ''
            # ~~~~~~~ aa check :----------------------------------------------------------------------------------
            if aaindex > -1:
                a[aaindex] = 'aa'
                # a[(aaindex+1)] = ''
            # ~~~~~~~ ll check :----------------------------------------------------------------------------------------
            if llindex > -1:
                a[llindex] = 'l'
                a[(llindex + 1)] = ''
            # ~~~~~~~ pp
            # check:--------------------------------------------------------------------------------------------
            if ppindex > -1:
                a[ppindex] = '_'
                a[(ppindex + 1)] = 'p'
            # ~~~~~~~ ap check:----------------------------------------------------------------------------------------
            if apindex > -1:
                if a[apindex - 1] == 'aa':
                    a[apindex + 1] = 'p'
                elif apindex > -1:
                    a[(apindex + 1)] = 'ap'
            # ~~~~~~~ bh check:--------------------------------------------------------------------------------------------
            if bhindex > -1:
                a[bhindex] = 'bh'
                a[(bhindex + 1)] = ''
            # ~~~~~~ aha check:--------------------------------------------------------------------------------------------
            if ahaindex > -1:
                a[(ahaindex + 1)] = 'he'
            # ~~~~~~ ate check:-------------------------------------------------------------------------------------------
            if ateindex > -1:
                a[(ateindex + 1)] = 'ate'
            # ~~~~~~ ia check:----------------------------------------------------------------------------------------------
            if iaindex > -1:
                a[iaindex] = 'ia'
                a[(iaindex + 1)] = ''
            # ~~~~~~ ea check:----------------------------------------------------------------------------------------
            if eaindex > -1:
                a[eaindex] = 'ia'
                a[(eaindex + 1)] = ''
            # ~~~~~~ ay check:---------------------------------------------------------------------------------------------
            if ayindex > -1:
                if word[round][-1] != 'y':
                    a[ayindex] = 'y'
                    a[(ayindex + 1)] = ''
                else:
                    a[ayindex] = 'ay'
            # ~~~~~~ ai check:----------------------------------------------------------------------------------------------
            if aiindex == (len(h) - 2):
                a[aiindex] = 'ai'
                a[(aiindex + 1)] = ''
            elif aiindex > -1:
                a[aiindex] = 'ee'
                a[aiindex + 1] = '_'
            if xhindex > -1:
                a[xhindex] = 'xh'
                a[(xhindex + 1)] = ''
            if a[hoindex - 1] == ('khal' or 'khan'):
                a[hoindex] = '_'
            elif hoindex > -1:
                a[hoindex] = 'he'
            if ssindex > -1:
                a[ssindex] = 's'
                a[(ssindex + 1)] = ''
            if ooindex > -1:
                a[ooindex] = 'o'
                a[(ooindex + 1)] = ''
            if haiindex > -1:
                a[haiindex] = 'he'
            if chindex > -1:
                a[chindex] = 'ch'
                a[chindex + 1] = ''
            if dhindex > -1:
                a[dhindex] = 'dh'
                a[dhindex + 1] = ''
            if ghindex > -1:
                a[ghindex] = 'gh'
                a[ghindex + 1] = ''
            if thindex > -1:
                a[thindex] = 'th'
                a[thindex + 1] = ''
            if phindex > -1:
                a[phindex] = 'ph'
                a[phindex + 1] = ''
            if llahindex > -1:
                a[llahindex] = 'llah'
                a[llahindex + 1] = ''
                a[llahindex + 2] = ''
                a[llahindex + 3] = ''
            temp += 1
        # ~~~~~~ printing urdu:----------------------------------------------------------------------------------------
        for j in a:
            mea.append(lang1[j])
        for prin in mea:
            print(prin, end='')
        print(' ', end='')
        mea = []
        # -----------------------------------------------------------------
        # for security: not needed
        gharindex = thindex = hoindex = ateindex = apindex = ppindex = xhindex = iaindex = aiindex = eeindex = aaindex = -1
        aaindex = shindex = khindex = llindex = ooindex = ssindex = bhindex = ahaindex = iiindex = ayindex = eaindex
        eaindex = haiindex
    print("\n"
          "------------------------------------------------------------------------------------------------------------"
          "---------------------------")


'''Tehseen Ajmal 2022-CE-53 , this is my 2nd transliterator
Urdu to Roman Urdu transliterator:
to make this transliterator work properly we have to add Aeraab in input
following are the sample words because urdu with aeraab is difficult to right these words can be checked
by putting these in input.
# _samples_:
       تحسین اَجمَل
       خالِد بِن ولید بِن وکیل بِن مُغیرہ بِن مُسکَان
       ایک عظیم شَخص
       شُکریہ
       صُبح بَخیر
       خُدا حافِظ
       یہ اُردُو سے اَنگَریزی تَرجُمہ ہے
       آج بارِش ہو رہی ہے
       کیا آپ کا نام احمَد ہے
aeraabs are compulsory to make this code work
'''
""" please remove the '#' to give input and cut the line 14"""


# print('if you want to give input please remove # (line 20 & 21) and put # (line 22)\n')
def urdu(x):
    input_value = x
    orignal = input_value
    # orignal='خالِد بِن ولید بِن وکیل بِن مُغیرہ بِن مُسکَان'
    word = orignal.split(' ')
    g = ''
    a = []
    # mea is for translation or meaning___________________________________________
    mea = []
    lang2 = {'5': '5', '3': '3', '': '', 'آ': 'aa', 'ا': 'a', 'ب': 'b', 'ت': 't', 'پ': 'p', 'ٹ': 't', 'ث': 's',
             'ج': 'j', 'چ': 'ch', 'ح': 'h', 'اح': 'ah', 'خ': 'kh', 'د': 'd', 'ڈ': 'd', 'ذ': 'z',
             'ر': 'r', 'ڑ': 'r', 'ز': 'z', 'ژ': 'y', 'س': 's', 'ش': 'sh', 'ص': 's', 'ض': 'z', 'ط': 't', 'ظ': 'z',
             'ع': '', 'غ': 'gh', 'ف': 'f', 'ق': 'q', 'ک': 'k'
        , 'گ': 'g', 'ل': 'l', 'م': 'm', 'ن': 'n', 'ں': 'n', 'و': 'o', 'وا': 'wa', 'ؤ': '', 'ہ': 'h', 'ھ': 'h',
             'ی': 'ee', 'یہ': 'y', 'ئ': 'ai', 'ے': 'ai', 'ۓ': 'ay', 'َ': 'a', 'ُ': 'u', 'ِ': 'i'}
    print('\033[1minput :\033[0m', orignal)
    for round in range(len(word)):
        h = []
        h = word[round]
        notfind = h.find('ئ')
        zabr = h.find('َ')
        pesh = h.find('ُ')
        zair = h.find('ِ')
        hafind = h.find('ح')
        wafind = h.find('وا')
        waofind = h.find('و')
        a = []
        for i in h:
            a.append(i)
        if notfind == -1:
            if a[-1] == 'ی':
                a[-1] = 'ِ'
        if a[0] == 'ی':
            a[0] = 'یہ'
        # ___in these quotes zabr zer and pesh are written
        if a[wafind - 1] == 'ُ':
            a[wafind] = ''
        if a[-1] == 'ہ':
            a[-1] = 'ا'
        if a[-1] == 'ح':
            a[-1] = 'اح'
        if a[0] == 'و':
            a[0] = 'وا'
        if hafind > 0:
            a[hafind] = 'اح'
        if a[0] == 'ع':
            a[0] = 'ا'
        if wafind > -1:
            a[wafind] = 'وا'
            a[wafind + 1] = ''
        if zabr > -1 or pesh > -1 or zair > -1:
            if a[zabr - 1] == 'ا':
                a[zabr - 1] = ''
            if a[pesh - 1] == 'ا':
                a[pesh - 1] = ''
            if a[abs(zair - 1)] == 'ا':
                a[zair - 1] = ''

        for j in a:
            mea.append(lang2[j])
        for prin in mea:
            print(prin, end='')
        print(' ', end='')
        mea = []
    print("\n"
          "------------------------------------------------------------------------------------------------------------"
          "---------------------------")

# Printing...............................
print("\033[1;36m")
tprint("Transliterater".center(70))
print("\033[0m")

print('\033[1mRULES FOR ENGLISH/ROMAN:\033[0m\n',
      ' ◈ This will work perfectly -- if you use "aa" for alif like khaalid, "xh" for "چھ" and also check sample phrases given in the code.')

print('\033[1mCHECK FOR ENGLISH/ROMAN:\033[0m\n',
      ' ◈ Please use samples to check best results and to understand writing style.\n',
      '   Please read 1st 10 lines of the code')

print('\033[1mIMPORTANT FOR URDU:\033[0m\n',
      ' ◈ With Aeraab (اعراب) this programme will work perfectly...')

print('\n', "\033[1;36m" + '-' *66," EXAMPLES ",'-'*66+ "\033[0m",'\n')

urdu('تحسین اَجمَل')
urdu('خالِد بِن ولید بِن وکیل بِن مُغیرہ بِن مُسکَان')
urdu('یہ اُردُو سے اَنگَریزی تَرجُمہ ہے')
urdu('خُدا حافِظ')

print('\033[1mIMPORTANT MESSAGE:\033[0m\n',
      ' Please read 1st lines of both code (1,20), (534,548) and also check the rules for ROMAN:\n',
      ' AGAIN: please use \'aa\' for alif between the word like khaana, khaalid, khaan you can use single a\n',
      ' in start and in end like ali, axha.\n',
      "◈ Enter 'Exit' to Exit...")

print("\033[1;36m" + "==" * 70 + "\033[0m")
print("Please Enter text in URDU with aeraabs or in ROMAN:")
while True:
    user_input = input('\nEnter Roman/Urdu...\n>>> ')
    if user_input.lower() == 'exit':
        break
    else:
        for char in user_input:
            if char in lang1:
                english(user_input)
                break
            elif char in lang2:
                urdu(user_input)
                break
