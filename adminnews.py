# 10/5/21 Justin Powell
#
# This app will allow you to access news and other information to start your day as a linux admin
# Most of the links are derived from UNIX and LINUX System Administrator Handbook 5e
# Hope you find this useful
#
# App uses kivy.app, webbrowser and datetime(only for the easter egg)
#
# To get kivy, (tested on kali), sudo apt install python3-kivy
#
# for use on linux:
# to make it executable: chmod +x adminnews.py
# to execute the script: ./adminnews.py
#
# ::Version Info::
# Kivy v2.0.0
# python v3.7.8
# adminnews v1.0 (initial release, 10-6-2021)
#
# ::Bug Tracking::
# Resolved assertionError with lambda f(x)
# not sure if this is the proper use of return
# novice programmer, use with caution.
#

# Libraries
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
import webbrowser
from datetime import datetime

# define URLs
dR = "https://darkreading.com"
redD = "https://www.reddit.com/r/Ubuntu/"
lin = "https://www.linux.com/topic/system-administration/"
linFou = "https://www.linuxfoundation.org/projects/news"
lwn = "https://www.lwn.net"
lxer = "https://www.lxer.com"
evSysAd = "https://www.everythingsysadmin.com"
sysAdv = "https://www.sysadvent.blogspot.com"
oreilly = "https://www.oreilly.com/topics"
schnei = "https://www.schneier.com"
adNews = "https://www.admin-magazine.com/News"


# obligatory Monty Python reference
def bunny(self):
    bunny = 'no ordinary rabbit'
    facts = 'I warned you'
    solution = 'Holy Hand Grenade'
    pass


# December "easter egg"
month = datetime.today().strftime('%m')
month = int(month)


class adminNews(App):
    def build(self):
        if month == 12:
            layout = GridLayout(cols=2)
            b1 = Button(text='Dark Reading (Security)')
            b1.bind(on_press=lambda x: self.darkRead())

            b2 = Button(text='Schneier (Security)')
            b2.bind(on_press=lambda x: self.schne())

            b3 = Button(text='Linux.org')
            b3.bind(on_press=lambda x: self.linO())

            b4 = Button(text='Linux Foundation')
            b4.bind(on_press=lambda x: self.linfo())

            b5 = Button(text='LWN (Linux and FOSS news)')
            b5.bind(on_press=lambda x: self.lWN())

            b6 = Button(text='LXer (Linux news)')
            b6.bind(on_press=lambda x: self.lXER())

            b7 = Button(text='EverythingSysAdmin')
            b7.bind(on_press=lambda x: self.etSA())

            b8 = Button(text='Oreilly Topics')
            b8.bind(on_press=lambda x: self.ooore())

            b9 = Button(text='Ubuntu (Reddit)')
            b9.bind(on_press=lambda x: self.reddit())

            b10 = Button(text='Admin Magazine')
            b10.bind(on_press=lambda x: self.adminN())

            b11 = Button(text='SysAdvent')
            b11.bind(on_press=lambda x: self.adva())

            layout.add_widget(b1)
            layout.add_widget(b2)
            layout.add_widget(b3)
            layout.add_widget(b4)
            layout.add_widget(b5)
            layout.add_widget(b6)
            layout.add_widget(b7)
            layout.add_widget(b8)
            layout.add_widget(b9)
            layout.add_widget(b10)
            layout.add_widget(b11)

            return layout

        else:
            layout = GridLayout(cols=2)
            b1 = Button(text='Dark Reading (Security)')
            b1.bind(on_press=lambda x: self.darkRead())

            b2 = Button(text='Schneier (Security)')
            b2.bind(on_press=lambda x: self.schne())

            b3 = Button(text='Linux.org')
            b3.bind(on_press=lambda x: self.linO())

            b4 = Button(text='Linux Foundation')
            b4.bind(on_press=lambda x: self.linfo())

            b5 = Button(text='LWN (Linux and FOSS news)')
            b5.bind(on_press=lambda x: self.lWN())

            b6 = Button(text='LXer (Linux news)')
            b6.bind(on_press=lambda x: self.lXER())

            b7 = Button(text='EverythingSysAdmin')
            b7.bind(on_press=lambda x: self.etSA())

            b8 = Button(text='Oreilly Topics')
            b8.bind(on_press=lambda x: self.ooore())

            b9 = Button(text='Ubuntu (Reddit)')
            b9.bind(on_press=lambda x: self.reddit())

            b10 = Button(text='Admin Magazine')
            b10.bind(on_press=lambda x: self.adminN())

            layout.add_widget(b1)
            layout.add_widget(b2)
            layout.add_widget(b3)
            layout.add_widget(b4)
            layout.add_widget(b5)
            layout.add_widget(b6)
            layout.add_widget(b7)
            layout.add_widget(b8)
            layout.add_widget(b9)
            layout.add_widget(b10)

        return layout

    def printTest(self):
        print('press')
        return

    def darkRead(self):
        webbrowser.open_new_tab(dR)
        return

    def reddit(self):
        webbrowser.open_new_tab(redD)
        return

    def linO(self):
        webbrowser.open_new_tab(lin)
        return

    def linfo(self):
        webbrowser.open_new_tab(linFou)
        return

    def lWN(self):
        webbrowser.open_new_tab(lwn)
        return

    def lXER(self):
        webbrowser.open_new_tab(lxer)
        return

    def etSA(self):
        webbrowser.open_new_tab(evSysAd)
        return

    def adva(self):
        webbrowser.open_new_tab(sysAdv)
        return

    def ooore(self):
        webbrowser.open_new_tab(oreilly)
        return

    def schne(self):
        webbrowser.open_new_tab(schnei)
        return

    def adminN(self):
        webbrowser.open_new_tab(adNews)
        return


adminNews().run()
