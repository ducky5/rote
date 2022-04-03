import spacy

nlp = spacy.load('en_core_web_sm')

text = """

NoLabel
I just write things here.

CUPID: a simple personality matching website that solves the problem of finding likeminded people.
March 11, 2022
The following is my white-paper for CUPID
(It is worth noting that although the term white-paper is usually used to describe an online document/text that aims to inform the reader about a solution to a problem usually in the context of computer science, this blog post is merely intended to promote a website I made a few months ago, and I use the term white-paper only in the sense that this is a presentation on what the website does and how it does it, if you are interested in investing (mainly to cover hosting costs) please comment your contact information under this blog and I will get to you as soon as I can )

THE PAPER

Finding friends is evidently easier now more than ever thanks to the internet, but that statement merely makes the problem of finding likemined people a layer harder to solve, finding friends is easier when you have a lot of choices to pick from than when you have only a few, the internet solves that problem so we don't have to worry about it.

The solution: Providing an online platform where people can meet their likeminded counterparts.

There are three problems we need to solve to achieve the aforementioned solution: 1)concluding that two people are likeminded, 2)providing the feature of communication through realtime messaging without resorting to a third party and 3)providing the feature of adding friends so that 'opportunities' aren't lost.

1) To conclude that two people are likeminded a function in the backend is called:

COMPATIBILITY = AICuser1 / Auser2 * 100
*AIC : from the perspective of user2, Assumptions In Common(AIC) are all the assumptions that user1 shares with user2.
*A : from the perspective of user2, Assumptions(A) are all of user2's assumptions.

In this way, compatibility between two users is calculated and the resulting percentage tells each user how much of their assumptions do they share with the other user, it is important to note also that the two ends will see different percentage values due to the varying A values. The percentages are shown on the profile-card of the listed profile in the list of profiles in the main page. (the website uses ajax, so the page will not take longer to load the longer the list of profiles gets, that is accomplished by attaching a button to the end of the profile list which the user can click to load more profiles from the backend, this is important for the user experience, the same ajax solution is used in the assumptions adding page).

2) To solve this, websockets are used to maintain a realtime messaging capability, users can text each other in realtime, however the UI is less conventional.

3) users can add other users as well as remove them.




Comments

Popular posts from this blog
Blockchain and cryptocurrency: a simple but deep enough introduction
January 28, 2022
Blockchain is a type of Distributed Ledger Technology(DLT), using a Peer-to-Peer(P2P) network to maintain a decentralized method of keeping reliable information, and contrary to popular belief, Blockchain and Bitcoin are not the same thing, cryptocurrency and Blockchain do not mean the same thing, Blockchain is a type of database where instead of having a central database where all data is kept, it keeps data in a distributed fashion, meaning that the database itself is not on one central 'host' computer but on multiple computers, the computers in a network are usually referred to as nodes, so your phone is a node if it is connected to a computer network, due to the decentralized way in which Blockchain networks are implemented, no one node has an 'original' or 'main' database, all nodes on the network can have a copy of the entire Blockchain if they want that, in the case of a public or permissionless Blockchain anyone can join the network whereas in a private
READ MORE
Powered by Blogger
Report Abuse

Archive"""

doc = nlp(text)

word_dict = {}

# count word occurences
for word in doc:
    word = word.text.lower()
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

# score sentences
sents = []
sent_score = 0

for index, sent in enumerate(doc.sents):
    for word in sent:
        word = word.text.lower()
        sent_score += word_dict[word]
    sents.append((sent.text.replace('\n', ' '), sent_score/len(sent), index))

# sort sentences
sents = sorted(sents, key=lambda x: -x[1])
# sents = sorted(sents[:3], key=lambda x: x[2])

# return summary
summary = ''
for sent in sents:
    summary += sent[0] + ' '

print(summary)
