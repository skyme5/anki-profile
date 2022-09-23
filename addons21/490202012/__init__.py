"""
Automatic Scoring
Defaults answer score based on time to answer

Copyright (c) 2019 Sicmha Rimler 
Based on Liam Cooke: https://github.com/araile/anki-quick-easy
Edited on August 2019 by Joseph Yasmeh to fix new cards being marked Easily with a lower threshold. And to import to Anki 2.1.
"""

# Edit this line to adjust how quickly you must reveal the answer. You can even use decimals (if you have OCD).
EASY_SECONDS = 1
GOOD_SECONDS = 2
HARD_SECONDS = 8

###########################################################
#This loads up the used resources.
import time
from anki.hooks import addHook
from aqt.reviewer import Reviewer

#The code works is by iterating "new_ease" by adding 1 each time a condition is met.
def my_defaultEase(self):
    ease = orig_defaultEase(self)
    new_ease = 1

#First statement below is for review cards. Says if there are 4 answer buttons (review), do this. 
    if self.mw.col.sched.answerButtons(self.card) == 4:
        if self.card.timeTaken() <  HARD_SECONDS * 1000:
           new_ease=new_ease+1
        if self.card.timeTaken() < GOOD_SECONDS * 1000:
           new_ease=new_ease+1
        if self.card.timeTaken() <  EASY_SECONDS * 1000:
            new_ease=new_ease+1

#"Else" means that if there aren't 4 answer buttons (new cards), do this. 
#Joseph added If and Else so new cards wouldn't get marked as easy with a lower threshold
#Because there is no Hard rating for new cards, Good has a longer interval.
#To make this tougher, replace "HARD" below with "GOOD" so that Again occurs earlier. 
    else:
        if self.card.timeTaken() < HARD_SECONDS * 1000:
           new_ease=new_ease+1
        if self.card.timeTaken() <  EASY_SECONDS * 1000:
            new_ease=new_ease+1

    max_ease = self.mw.col.sched.answerButtons(self.card)
    return min(new_ease, max_ease)

orig_defaultEase = Reviewer._defaultEase
Reviewer._defaultEase = my_defaultEase