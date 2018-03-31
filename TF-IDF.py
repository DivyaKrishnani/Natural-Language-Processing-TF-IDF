
import math
from textblob import TextBlob

docx1 = TextBlob("""NASA to explore how 3-year Mars mission could affect humans WASHINGTON: As a round-trip mission to Mars could last three years, NASA is calling for more research to understand how long-term experiences in space could affect the human body.
Typical missions to the International Space Station (ISS) last just six months. "To draw any conclusions about the cumulative effects of exposure to space, we need to observe more astronauts spending larger amounts of time in the space environment," said John Charles of the Human Research Programme at NASA's Johnson Space Center.
Combined with ongoing NASA studies, the new research could enable safer and more effective travel to destinations beyond low-Earth orbit.The US space agency hopes that such research will help it understand, prevent, diagnose, treat, mitigate and cure the potential health effects of prolonged spaceflight. "Scientists can use the information to predict physical and behavioural health trends," Charles said.
Proposals are due by January 4, 2018, and NASA expects in late summer 2018 to select 15 to 18 proposals for grants with a maximum duration of seven years.
NASA said scientists submitting proposals should consider a robust programme that could include as many as 30 astronauts -- 10 to
conduct shorter missions of up to two months, 10 as part of standard six-month missions, and 10 for one-year missions in space.
With information gained from the selected studies, NASA aims to address five hazards of human space travel - space radiation, isolation and confinement, distance from Earth, gravity fields (or lack thereof), and hostile/closed environments that pose great risks to the human mind and body in space.
"When the day comes for humans to launch on a journey to Mars, humanity will take another giant leap. The knowledge gained from this research could give NASA a running start," the US space agency said.""")


docx2 = TextBlob("""Python, from the Greek word (πύθων/πύθωνας), is a genus of
nonvenomous pythons[2] found in Africa and Asia. Currently, 7 species are
recognised.[2] A member of this genus, P. reticulatus, is among the longest
snakes known.""")

docx3 = TextBlob("""The Colt Python is a .357 Magnum caliber revolver formerly
manufactured by Colt's Manufacturing Company of Hartford, Connecticut.
It is sometimes referred to as a "Combat Magnum".[1] It was first introduced
in 1955, the same year as Smith &amp; Wesson's M29 .44 Magnum. The now discontinued
Colt Python targeted the premium revolver market segment. Some firearm
collectors and writers such as Jeff Cooper, Ian V. Hogg, Chuck Hawks, Leroy
Thompson, Renee Smeets and Martin Dougherty have described the Python as the
finest production revolver ever made.""")



def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

#returns the number of documents containing word
def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)

#computes "inverse document frequency" which measures how common a word is among all documents in bloblist.
def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))
    #ratio of the total number of documents to the number of documents containing word

#computes tf-idf
def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)


bloblist = [docx1,docx2,docx3]
for i, blob in enumerate(bloblist):  #loops over bloblist with automatic counter i
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words} #find tfidf of each word with score and stores in dict scores
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True) #returns the list of key-value pairs in the dictionary, sorted by value from highest to lowest
    for word, score in sorted_words:
        print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))


print(scores)

