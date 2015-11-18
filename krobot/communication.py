from __future__ import print_function
from ircbot import IRCKrobot

class Communication(object):
    """
    communication class to chat with actual people. Right now, we use IRC.
    """
    def __init__(self, personList, ruList, channel="#CRIStALSigmaLunch", port="6667", nickname="krobot", server="irc.foonetic.net", medium="IRC"):
        super(Communication, self).__init__()
        self.medium = medium
        self.ruList = ruList
        self.personList = personList
        if medium == "IRC":
            self.bot = IRCKrobot(channel, nickname, server, port, personList, ruList)

    def checkWhoIsOnline():
        """
        make a list of persons online and store it in personList
        """
        return 0 # not implemented yet

    def printMenus(self):
        """
        make bot print menus
        """
        self.bot.printMenus()

    def fetchPreferences():
       """
       fetch individual preferences for RU and time slot
       """
       return 0
       #self.bot.fetchPreferences()








