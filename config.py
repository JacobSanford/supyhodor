import supybot.conf as conf
import supybot.registry as registry

def configure(advanced):
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('supyhodor', True)

supyhodor = conf.registerPlugin('supyhodor')
conf.registerChannelValue(supyhodor,'enable',registry.Boolean('False',"""Enable displaying messages from supyhodor in channel?"""))
