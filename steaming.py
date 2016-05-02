from PIL.WmfImagePlugin import word
__author__ = 'khalid'
#start declarations
#word starts with any of these prefixes.
prefixes = ['contra', 'hetero', 'circum', 'hyper',  'extra', 'inter', 'trans', 'super', 'intra', 'macro', 'micro', 'mono'
            , 'anti', 'post', 'ante', 'omni', 'homo', 'auto', 'com','sub', 'syn', 'con', 'dis', 'uni', 'tri', 'non', 'pre'
            , 'pro', 'de', 'en', 'ex', 'il', 'im', 'in', 'ir', 'co', 'un', 'an', 'a']

#word ends with any of these suffixes.
suffixes = ['ination', 'able', 'ation', 'ible', 'al', 'ial', 'ed', 'en', 'er', 'or', 'est', 'ful', 'ic', 'ing', 'ion', 'tion',
            'ition', 'ity', 'ty', 'ive', 'ative', 'itive', 'less', 'ly', 'ment', 'ness', 'ous', 'eous', 'ious', 'ies',
            'es', 'y', 's']
#other words will not be streamed
otherWords = ['computer', 'increment', 'table']
#end declarations

commingWord = raw_input(" please enter your word: ")

#start Delete prefix
def deletePrefix(word):
    for pref in prefixes:
        if word.startswith(pref):
            word = word.replace(pref, "")
    return word
#end Delete prefix
#start deletesuffixes
def deleteSuffix(word):
    for suff in suffixes:
        if word.endswith(suff):
            if suff in "ies":
                word2 = word.replace('ies', 'y')  #hoppies , movies will give error string
                return word2
            elif suff in "ation":
                word3 = word.replace('ation', 'e') #Organization
                return word3
            else:
                word = word.replace(suff, "")
    return word
#end deletesuffixes
#start main work with input word
if commingWord in otherWords:
    print(commingWord)
else:
    commingWord = deletePrefix(commingWord)
    commingWord = deleteSuffix(commingWord)
    print(commingWord)
#end main work with input word