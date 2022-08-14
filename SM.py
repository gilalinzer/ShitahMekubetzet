from pprint import pprint

commentators = ['רש"י', 'חננאל', 'יהונתן', 'רא"ש', 'מהר״י', 'תוספות ה"ר ישעיה', 'מאירי', 'תוספות שאנץ', 'רשב"א']


commentatorMap = {
    'רשב"א': 'רשב"א',
    'והרשב"א': 'רשב"א',
    'הרשב"א': 'רשב"א',
    'רא"ש': 'רא"ש',
    'הרא"ש': 'רא"ש',
    'מאירי': 'מאירי',
    'המאירי': 'מאירי',
    'והמאירי': 'מאירי',
     'ישעיה': 'תוספות ה"ר ישעיה',
    'ישעיה': 'תוספות ה"ר ישעיה',
'מהר״י': 'מהר״י',
    'למהר"י': 'מהר״י',
    'ממהר"י': 'מהר״י',
    'ומהר"י': 'מהר״י',
    'חננאל': 'חננאל',
    'יהונתן': 'יהונתן',
    'רש"י': 'רש״י',
    'ורש"י': 'רש״י',
 'שאנץ' : 'תוספות שאנץ'
}
ans = {}

intros = ['תירץ','שתירץ']

text = open('/Users/gilalinzer/Alhatorah/STMK-BK.txt', 'r', encoding="UTF-8")

line = text.readline()
words = []
# while the line is actual text
while line != "":
    Line1 = line.split()
    for s in Line1:
        words.append(s)
    # move to next line of text
    line = text.readline()

# we now have a list of the text, paragraph by paragraph

countComm = 0
countSection = 0

section = ''
for word in words:

    # split up the paragraph into a list of each sentence

    # it's text of the peirush not the name of a person
    if word not in commentatorMap:
        section += " " + word
    else:  # it's the name of a commentator
        if word not in ans and section:  # if the commentator came at the end
            c = commentatorMap[word]
            # add that commentator's section to it's dictionary
            ans[c] = section
            # reset the section
        elif section:
            ans[word] += ('---------------------------' + section)

        elif not section or (section in commentatorMap):  # the name is before the comments
            temp = word

pprint(ans)
# changes made

# going t
