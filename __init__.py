"""Supybot plugin for hodoring.

Listen for mentions of Hodor's name in channels and reply with a message.

Messages are pre-defined from a basic module import and classified by mood.

The 'mood' of reply is determined by comparing the content of the triggering
message against a library of words and human interpreted intent scoring. After
mood assignment, a message is chosen based on a dropo-type selection process
that allows for weighting of responses.
"""

import supybot
import supybot.world as world

__version__ = "main"
__author__ = supybot.Author("Jacob Sanford","JS","jsanford@unb.ca")
__contributors__ = {}
__url__ = 'https://github.com/JacobSanford/SupyHodor'

import config
import plugin
reload(plugin)

if world.testing:
    import test

Class = plugin.Class
configure = config.configure
