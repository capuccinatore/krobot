#! /usr/bin/env python
#
# Modified from the TestBot example by
# Joel Rosdahl <joel@rosdahl.net>

"""A simple example bot.

This is an example bot that uses the SingleServerIRCBot class from
irc.bot.  The bot enters a channel and listens for commands in
private messages and channel traffic.  Commands in channel messages
are given by prefixing the text by the bot name followed by a colon.
It also responds to DCC CHAT invitations and echos data sent in such
sessions.

The known commands are:

    stats -- Prints some channel information.

    disconnect -- Disconnect the bot.  The bot will try to reconnect
                  after 60 seconds.

    die -- Let the bot cease to exist.

    dcc -- Let the bot invite you to a DCC CHAT connection.
"""

import irc.bot
import irc.strings
from irc.client import ip_numstr_to_quad, ip_quad_to_numstr
from data import RU, Person

class IRCKrobot(irc.bot.SingleServerIRCBot):
    """
    communication bot for krobot. It prints menus, and receives ru and time preferences from users.
    """
    def __init__(self, channel, nickname, server, port, personList, ruList):
        """
        ruList: list of RU instances, with name and menus filled.
        personList: list of persons present, initially empty
        """
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname)
        self.channel = channel
        self.ruList = ruList
        self.personList = []

    #def connect():
    #    """
    #    create chatroom
    #    """
    #    return 0 # not implemented yet

    def printMenus(self):
        c = self.connection
        c.notice(self.channel, "Hi everyone, today's menus are:")
        for ru in ruList:
            c.notice(self.channel, ru.name+": "+[item for item in ru.menu])

    def on_nicknameinuse(self, c, e):
        c.nick(c.get_nickname() + "_")

    def on_welcome(self, c, e):
        c.join(self.channel)

    def on_privmsg(self, c, e):
        self.do_command(e, e.arguments[0])

    def on_pubmsg(self, c, e):
        a = e.arguments[0].split(":", 1)
        if len(a) > 1 and irc.strings.lower(a[0]) == irc.strings.lower(self.connection.get_nickname()):
            self.do_command(e, a[1].strip())
        return

    def on_dccmsg(self, c, e):
        # non-chat DCC messages are raw bytes; decode as text
        text = e.arguments[0].decode('utf-8')
        c.privmsg("You said: " + text)

    def on_dccchat(self, c, e):
        if len(e.arguments) != 2:
            return
        args = e.arguments[1].split()
        if len(args) == 4:
            try:
                address = ip_numstr_to_quad(args[2])
                port = int(args[3])
            except ValueError:
                return
            self.dcc_connect(address, port)

    def do_command(self, e, cmd):
        nick = e.source.nick
        c = self.connection

        if cmd == "disconnect":
            self.disconnect()

        elif cmd == "die":
            self.die()

        elif cmd[:9] == "say hi to":
            nickToSayHiTo = cmd[10:]
            c.notice(nickToSayHiTo, "Hi, "+nickToSayHiTo)

        elif cmd == "stats":
            for chname, chobj in self.channels.items():
                c.notice(nick, "--- Channel statistics ---")
                c.notice(nick, "Channel: " + chname)
                users = sorted(chobj.users())
                c.notice(nick, "Users: " + ", ".join(users))
                opers = sorted(chobj.opers())
                c.notice(nick, "Opers: " + ", ".join(opers))
                voiced = sorted(chobj.voiced())
                c.notice(nick, "Voiced: " + ", ".join(voiced))

        elif cmd == "dcc":
            dcc = self.dcc_listen()
            c.ctcp("DCC", nick, "CHAT chat %s %d" % (
                ip_quad_to_numstr(dcc.localaddress),
                dcc.localport))

        elif cmd[:2] == "RU":
            user = nick
            preferredRU = cmd[:3]
            c.notice(nick, "I took note that "+nick+" prefers RU "+cmd[3:]+" today.")

        elif cmd[:2] == "TS":
            user = nick
            timeSlot = cmd[:3].split("-")
            if not (timeSlot[0] is int) or not (timeSlot[1] is int):
                c.notice(nick, "Please specify a time slot as in `TS 1230-1345`.")
            c.notice(nick, "I took note that "+nick+" prefers eating between "+timeSlot[0]+" and "+timeSlot[1]+" today.")
        else:
            c.notice(nick, nick+", I didn't understand: " + cmd)

def main():
    import sys
    if len(sys.argv) != 4:
        print("Usage: testbot <server[:port]> <channel> <nickname>")
        sys.exit(1)

    s = sys.argv[1].split(":", 1)
    server = s[0]
    if len(s) == 2:
        try:
            port = int(s[1])
        except ValueError:
            print("My error: Erroneous port.")
            sys.exit(1)
    else:
        port = 6667
    channel = sys.argv[2]
    nickname = sys.argv[3]

    bot = IRCKrobot(channel, nickname, server, port, [], [])
    bot.start()
    bot.printMenus()

if __name__ == "__main__":
    main()
