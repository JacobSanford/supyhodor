import supybot.conf as conf
import supybot.registry as registry

def configure(advanced):
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('SupyHodor', True)

SupyHodor = conf.registerPlugin('SupyHodor')
conf.registerChannelValue(SupyHodor,'enable',registry.Boolean('False',"""Enable displaying messages from SupyHodor in channel?"""))
