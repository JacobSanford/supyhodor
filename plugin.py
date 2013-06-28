"""Supybot plugin for hodoring.

Listen for mentions of Hodor's name in channels and reply with a message.

Messages are pre-defined from a basic module import and classified by mood.

The 'mood' of reply is determined by comparing the content of the triggering
message against a library of words and human interpreted intent scoring. After
mood assignment, a message is chosen based on a dropo-type selection process
that allows for weighting of responses.
"""

import random
import re
import time
import supybot.callbacks as callbacks
import supybot.ircmsgs as ircmsgs
from supybot.commands import *
import hodorActions
import hodorMoodIndex

__author__ = "Jacob Sanford"
__copyright__ = "Copyright 2013"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Jacob Sanford"
__email__ = "jsanford@unb.ca"
__status__ = "Production"

class supyhodor(callbacks.Plugin) :
    threaded = True
    def doPrivmsg(self, irc, msg) :
        if(self.registryValue('enable', msg.args[0])):
            match = re.search(
                              'hodor',
                              msg.args[1],
                              re.IGNORECASE
                              )
            if match:
                hodor = Hodor(msg.args[1], )
                action_to_take = hodor.act()
                time.sleep(random.random() * 5)
                irc.queueMsg(
                             getattr(ircmsgs,action_to_take['type'])(
                                             msg.args[0],
                                             action_to_take['value']
                                             )
                             )

class Hodor(object):
    def __init__(self, message):
        self.message = message
        self.interpret_mood()
    def interpret_mood(self):
        mood_score = 0
        for curword in re.sub("[^\w]", " ",  self.message).split():
            try:
                mood_score += hodorMoodIndex.mood_index[curword]
            except:
                pass
        if mood_score >= 2:
            self.mood = 'happy'
        elif mood_score <= -2:
            self.mood = 'sad'
        else:
            self.mood = 'neutral'
    def act(self):
        action = HodorAction(self.mood)
        return action.get()

class HodorAction(object):
    def __init__(self, mood):
        self.possibleactions = []
        self.mood = mood
        self.total_weight = 0
        self.load()
    def add(self, action):
        self.total_weight += action['weight']
        self.possibleactions.append(action)
    def get(self):
        if self.total_weight is 0:
            return False
        winning_number = random.randint(0, self.total_weight)
        running_total = 0
        for cur_action in self.possibleactions:
            running_total += cur_action['weight']
            if running_total >= winning_number:
                return cur_action['action']
    def load(self):
        for mood, action_list in hodorActions.actions.iteritems():
            if mood is self.mood:
                for cur_action in action_list:
                    self.add(cur_action)

Class = supyhodor
