from pprint import pprint

commentators = [' הרא"ש', ' תוספות ה"ר ישעיה']
ans = {}
intros = []

text = open('/Users/gilalinzer/Desktop/Alhatorah/STMK-BK.txt', 'r', encoding="UTF-8")

line = text.readline()
paragraphs = []
# while the line is actual text
while line != "":
    Line1 = line.split('\n\n')
    for s in Line1:
        paragraphs.append(s)
    # move to next line of text
    line = text.readline()

# we now have a list of the text, paragraph by paragraph

countComm = 0
countSection = 0

for paragraph in paragraphs:
    # split up the paragraph into a list of each sentence
    lines = paragraph.split('.')
    section = ''
    for sentence in lines:
        # it's text of the peirush not the name of a person
        if sentence not in commentators:
            section += sentence
        else:  # it's the name of a commentator
            if sentence not in ans and section:  # if the commentator came at the end
                # add that commentator's section to it's dictionary
                ans[sentence] = section
                # reset the section
            elif section:
                ans[sentence] += ('---------------------------' +section)

            elif not section or section in intros: # the name is before the comments
                temp = sentence
pprint(ans)

# going t
