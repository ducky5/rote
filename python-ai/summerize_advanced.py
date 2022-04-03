import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

def summarize(text, per):
    nlp = spacy.load('en_core_web_sm')
    doc= nlp(text)
    tokens=[token.text for token in doc]
    word_frequencies={}
    for word in doc:
        if word.text.lower() not in list(STOP_WORDS):
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1
    max_frequency=max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word]=word_frequencies[word]/max_frequency
    sentence_tokens= [sent for sent in doc.sents]
    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent]=word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent]+=word_frequencies[word.text.lower()]
    select_length=int(len(sentence_tokens)*per)
    summary=nlargest(select_length, sentence_scores,key=sentence_scores.get)
    final_summary=[word.text for word in summary]
    summary=''.join(final_summary)
    return summary

text = """
The scene is total chaos: a woman and all her purse's contents in middair as she trips over a child's toy, a man hastily trying to gather his spilled laundry, a screaming child weaving through the crowd. Somewhere, in the midst of it all, is the person you've been looking for: wearing a red and white striped shirt, black rimmed glasses and a lopsided cap. There he is! There's Waldo.

Many of us have fond memories of Waldo. But while he looms large in our imagination, our childhood searches for Waldo typically stayed pretty small – Waldo is a tiny person in the middle of lots of other tiny things.

And that's what this post is about: wee things. Specifically, the wee things that we see as part of graphics, maps, visualizations (wee things in space) as well as the wee things we experience as part of interactions, navigation, and usability (wee things in time). This means everything from sequences of small graphics that help us make comparisons, to tiny locator maps that help orient us within a larger graphic, to navigation icons that give hints about how we should make our way around a page.

Waldo, and the eternal search for him, can actually tell us quite a lot about design. In many ways, Waldo is a great example of what NOT to do when using wee things in your own work. So with Waldo as our anti-hero, let's take a look at how people read and interpret small visual forms, why tiny details can be hugely useful, and what principles we can apply to make all these little images and moments work for us as designers.

Wee Things In Space
Probably the most immediate definition of wee things are things that are physically small: little things on a page. We see these all the time in news graphics, and we're probably familiar with some of their forms: small multiples, sparklines, icons, etc. I'll go into more details about all of these.

These visual forms work because they serve as extensions of our mind – they are cognitive tools that complement our own mental abilities. They do this by recording information for us to make use of later, lending a hand to our (pretty terrible) working memories, helping us search and discover and recognize. We'll take a look at one task in particular they are great at: letting us make comparisons.

Make Comparisons

Tiny sequences of graphics, also known as small multiples, are great ways to help our brains compare. They are so successful because we don’t have to rely on working memory – every bit of information is in front of us at the same time. This means that we can easily see changes, patterns or differences.

Here are a bunch of examples of small multiples in the wild – maps and planets, first lady hair styles and telegraph signals, food trucks, fashion color trends and dressing appropriately for different climates, the distribution of deaths in the 1870’s and last but not least, Bill Murray’s hats.

Drought’s Footprint, NY Times Kepler’s Tally of Planets, NY Times
Strands of American History, NY Times (L) and The Conspicuous Telegraph, Scientific American (R)

 Trucks on a Roll, NY Magazine
Front Row to Fashion Week, NY Times (L) and Weather people (R)


Statistical Atlas of the Ninth Census (L) and Bill Murray Loves Hats, Derek Eads (R)

The reason we can make comparisons so easily is because these small multiples take advantage of the built-in capabilities of our visual system. Specifically, something called preattentive processing.

Preattentive Processing
Table of Preattentive Features, Design for Information, Isabel Meirelles
Technically, preattentive processing refers to "cognitive operations that can be performed prior to focusing attention on any particular region of an image.” But basically, it means the stuff you notice right away. Our brains aren't like scanners, they throw away most of what the eyes see. But they are good at perceiving simple visual features like color or shape or size, and in fact they do it amazingly fast without any conscious effort. That means we can tell immediately when a part of an image is different from the rest, without really having to focus on it. Our minds are really good at spotting one or two differences when everything else is the same.

Like in this example, you can easily spot Waldo.


It's easy to spot Waldo surrounded by his arch nemesis, Odlaw.

Or in this example, right? This is not hard.

Zen Version of Where's Waldo, Dan Piraro
But obviously, this is not where Waldo typically hangs out! Where he goes, I can't find him at a glance, and I need to spend a lot of time and actual effort. Our experiences with Waldo are usually something more like this:


A few years ago a group of MIT researchers actually studied what happened when people saw a scene like this. They used eye tracking devices to look at how people go about finding Waldo. This is what happens on a typical search:

Statistical patterns of visual search for hidden objects, Scientific Reports
Those jagged lines are the path of the eye as it hunts for Waldo (ending in success at the red dot). As you can probably tell, the process is far from straightforward.

So, Waldo basically thwarts our preattentive processing. Instead, he forces us to use our attentive processing: the conscious, slow, sequential process that lets us focus on one thing at a time. This "spotlight" of attention might be good at letting us concentrate, but it makes us pretty bad at spotting Waldo. We have such a hard time seeing him (despite the fact that he's right there in plain sight) because he doesn’t stand out in any clear way, color or size or orientation.

And obviously there are reasons for why Waldo doesn't stand out – he is purposely hard to find because his surroundings were constructed to hide him. But in general, we don’t want our graphics or data visualizations to be this much work to understand. If someone had to search that hard to read the information in a chart or graphic, it would be a failure. So if you're in the business of displaying data, avoid the Waldo strategy.

Instead, take advantage of those preattentive features! In this graphic from ProPublica, the use of color draws your eyes to specific lines of red text.The grey lines are government claims about the succeses and results of the CIA's drone program. The red lines are the official statements that it doesn't exist (or rather, the government can neither confirm nor deny). The graphic uses the preattentive feature of color to call out these contradictions.

Stacking Up the Administration's Drone Claims, ProPublicaThe Credits Keep Going and Going, NY Times
This graphic from the New York Times uses size to highlight how much longer movie credits have gotten over the years.

Whether it's size, color, contrast, etc, it helps to have the point you want to get across encoded in one of these preattentive features..

Now the last two graphics I showed were also members of a special category of wee things I like to refer to as TinyText. This is exactly what it sounds like (you make the font size really small). Tiny words can help call attention to differences over time, like this piece comparing editions of the Origin of Species.

On the Origin of Species: The Preservation of Favoured Traces, Ben Fry
Or they can help us explore the terms used in Hong Kong policy addresses for the last few years, or see the rise and fall of Fortune 500 company rankings.


Behind the sound bite, South China Morning Post (L) and The Fortune 500, Fathom (R)

Show a Process

Small things can also help us show us a step-by-step process. Many examples of this sort of thing involve tiny people, like the following graphics that show figure skating spins, triple axels and toe loops, aerial skiing, and snowboarding tricks.

"""
print(summarize(text, .05))
