from time import sleep
import os, sys
import random
from colorama import init, Fore, Back, Style
from termcolor import colored
init(autoreset=True)


class Item:
    def __init__(self, name, description, worth):
        self.name = name
        self.description = description
        self.worth = worth
 
    def __str__(self):
        return "{}\n=====\n{}\nWert: {}\n".format(self.name, self.description, self.worth)

class Weapon(Item):
    def __init__(self, name, description, worth, damage):
        self.damage = damage
        super().__init__(name, description, worth)
 
    def __str__(self):
        return "{}\n=====\n{}\nWert: {}\nSchaden: {}".format(self.name, self.description, self.worth, self.damage)
 
class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Stein",
                         description="Ein faustgroßer Stein, besser als nichts.",
                         worth=0,
                         damage=5)
 
class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dolch",
                         description="Ein kleiner Dolch mit einer rostigen und stumpfen Klinge.",
                         worth=10,
                         damage=10)

class Potion(Item):
    def __init__(self, weight, worth):
        Item.__init__(self, weight, worth)

class HealthPotion(Potion):
    def __init__(self, weight, worth, regenerated_health):
        Potion.__init__(self, weight, worth)
        self.regenerated_health = regenerated_health

class Character:
    def __init__(self, hp, ad, name):
        self.hp = hp
        self.ad = ad
        self.name = name

    def get_hit(self, ad):
        self.hp = self.hp - ad
        if self.hp <= 0:
            self.die()

    def is_dead(self):
        return self.hp <= 0

    def die(self):
        print("[game] "+self.name+" wurde besiegt")

class BossLilith(Character):
    def __init__(self):
        Character.__init__(self, 100, 5, "(Boss) Daemon Lilith")

class BossDiablo(Character):
    def __init__(self):
        Character.__init__(self, 120, 6, "(Boss) Diablo")

class AncientDragon(Character):
    def __init__(self):
        Character.__init__(self, 75, 2, "Alter Drache")

class Nightshadow(Character):
    def __init__(self):
        Character.__init__(self, 70, 3, "Nachtschatten")

class Beast(Character):
    def __init__(self):
        Character.__init__(self, 50, 3, "Bestie")

class DarkWizzard(Character):
    def __init__(self):
        Character.__init__(self, 50, 3, "Dunkler Zauberer")
        
class DarkSepiroth(Character):
    def __init__(self):
        Character.__init__(self, 46, 4, "Dunkler Sepiroth")
        
class Cyclops(Character):
    def __init__(self):
        Character.__init__(self, 45, 3, "Zyklop")

class TheodoraTheWitch(Character):
    def __init__(self):
        Character.__init__(self, 30, 2, "Theodora Die Hexe")

class Harpy(Character):
    def __init__(self):
        Character.__init__(self, 30, 2, "Harpie")

class Ghost(Character):
    def __init__(self):
        Character.__init__(self, 15, 2, "Geist")

class PoisonedBat(Character):
    def __init__(self):
        Character.__init__(self, 5, 1, "Vergiftete Fledermaus")

class Snake(Character):
    def __init__(self):
        Character.__init__(self, 5, 1, "Schlange")

class Player(Character):
    def __init__(self, name, hp, ad):
        Character.__init__(self, hp, ad, name)
        self.max_hp = hp

    def die(self):
        exit("Du bist gestrorben. Versuche es nochmal.")

    def rest(self):
        self.hp = self.max_hp


class Field:
    def __init__(self, enemies):
        self.enemies = enemies
        self.loot = []

    def print_state(self):                                                  
        #print("["+str(p.hp)+" HP uebrig]")
        #print("[game] Du hast den naechsten Raum betreten. Du siehst ...")
        for i in self.enemies:
            print("[game] "+i.name)

    @staticmethod
    def gen_random():
        rand = random.randint(0,13)
        if rand == 0:
            return Field([])
        if rand == 1:
            return Field([DarkSepiroth()])
        if rand == 2:
            return Field([TheodoraTheWitch(), TheodoraTheWitch()])
        if rand == 3:
            return Field([Snake()])
        if rand == 4:
            return Field([PoisonedBat()])
        if rand == 5:
            return Field([Ghost()])
        if rand == 6:
            return Field([Harpy()])
        if rand == 7:
            return Field([Cyclops()])
        if rand == 8:
            return Field([Beast()])
        if rand == 9:
            return Field([Nightshadow()])
        if rand == 10:
            return Field([AncientDragon()])
        if rand == 11:
            return Field([BossDiablo()])
        if rand == 12:
            return Field([BossLilith()])
        if rand == 13:
            return Field([DarkWizzard()])

class Map:
    def __init__(self, width, height):
        self.state = []
        self.x = 0
        self.y = 0
        for i in range(width):
            fields = []
            for j in range(height):
                fields.append(Field.gen_random())
            self.state.append(fields)

    def print_state(self):
        self.state[self.x][self.y].print_state()

    def get_enemies(self):
        return self.state[self.x][self.y].enemies

    def forward(self):
        try:
            s = sys.winver
            os.system("cls")
        except:
            os.system("clear")
        print("[game] -----<"+Fore.RED +str(p.hp)+" HP"+Style.RESET_ALL+">-----")
        print("[game] Du laeufst geradeaus und betrittst den nächsten Raum. Du siehst ...")
        self.x = self.x + 1

    def backwards(self):
        try:
            s = sys.winver
            os.system("cls")
        except:
            os.system("clear")
        print("[game] -----<"+Fore.RED +str(p.hp)+" HP"+Style.RESET_ALL+">-----")
        print("[game] Du gehst zurück und betrittst den nächsten Raum. Du siehst ...")
        self.x - 1

    def right(self):
        try:
            s = sys.winver
            os.system("cls")
        except:
            os.system("clear")
        print("[game] -----<"+Fore.RED +str(p.hp)+" HP"+Style.RESET_ALL+">-----")
        print("[game] Du gehst nach rechts und betrittst den nächsten Raum. Du siehst ...")
        self.y = self.y + 1

    def left(self):
        try:
            s = sys.winver
            os.system("cls")
        except:
            os.system("clear")
        print("[game] -----<"+Fore.RED +str(p.hp)+" HP"+Style.RESET_ALL+">-----")
        print("[game] Du gehst nach links und betrittst den nächsten Raum. Du siehst ...")
        self.y = self.y - 1

def forward(p, m):
    m.forward()

def right(p, m):
    m.right()

def left(p, m):
    m.left()

def backwards(p, m):
    m.backwards()

def save():
    pass

def load():
    pass

def quit_game(p, m):
    print("[game] Du begehst Selbstmord und gibst auf.")
    exit(0)

def print_help(p, m):
    print(Commands.keys())

def pickup(p, m):
    pass

def fight(p, m):
    enemies = m.get_enemies()
    try:
        s = sys.winver
        os.system("cls")
    except:
        os.system("clear")
    while len(enemies) > 0:
        enemies[0].get_hit(p.ad)
        if enemies[0].is_dead():
            enemies.remove(enemies[0])
        for i in enemies:
            p.get_hit(i.ad)
    print("[game] Du bist verwundet und hast " + str(p.hp) + " HP übrig")

def rest(p, m):
    p.rest()

Commands = {
    'help': print_help,
    'quit': quit_game,
    'pickup': pickup,
    'forward': forward,
    'right': right,
    'left': left,
    'backwards': backwards,
    'fight': fight,
    'save': save,
    'load': load,
    'rest': rest
}

if __name__ == '__main__':
    print("[game] Willkommen zu Castle Knight")
    name = input("[game] Gib deinen Namen ein: ")
    sleep(1.5)
    abfrageprolog=input("[game] Möchtest du den ersten Teil des Prologs lesen? \n[game] Ja/Nein: ")
    if abfrageprolog=="Ja":
        sleep(1.5)
        try:
            s = sys.winver
            os.system("cls")
        except:
            os.system("clear")
        print(Fore.RED +"P", end="")
        sleep(0.25)
        print(Fore.GREEN +"R", end="")
        sleep(0.25) 
        print(Fore.BLUE +"O", end="")
        sleep(0.25)
        print(Fore.RED +"L", end="")
        sleep(0.25)
        print(Fore.GREEN +"O", end="")
        sleep(0.25)
        print(Fore.BLUE +"G", end="")
        sleep(4)
        try:
            s = sys.winver
            os.system("cls")
        except:
            os.system("clear")
        print("[game] Vor dir ragt eine große Burg auf, das Ziel deiner tagelangen")
        sleep(3.5)
        try:
            s = sys.winver
            os.system("cls")
        except:
            os.system("clear")
        print("[game] Reise durch die Wälder des Landes. Du bist der bekannte Dämonenjäger "+name+".")
        sleep(3.5)
        try:
            s = sys.winver
            os.system("cls")
        except:
            os.system("clear")
        print("[game] In einer heruntergekommenen Taverne hast du einen Auftrag angenommen")
        sleep(3.5)
        try:
            s = sys.winver
            os.system("cls")
        except:
            os.system("clear")
        print("[game] und dich für eine beträchtliche Menge Gold dafür bereiterklärt")
        sleep(3.5)
        try:
            s = sys.winver
            os.system("cls")
        except:
            os.system("clear")
        print("[game] eine verlassene Burg von ihren Dämonen zu befreien.")
        sleep(3.5)
        try:
            s = sys.winver
            os.system("cls")
        except:
            os.system("clear")
        print("[game] Über eine herabgelassene Zugbrücke und durch das Eingangstor")
        sleep(3.5)
        try:
            s = sys.winver
            os.system("cls")
        except:
            os.system("clear")
        print("[game] der Burg erreichst du den düsteren Burghof.")
        sleep(3.5)
        try:
            s = sys.winver
            os.system("cls")
        except:
            os.system("clear")
    else:
        try:
            s = sys.winver
            os.system("cls")
        except:
            os.system("clear")
        pass
    print("[game] LOADING")
    p = Player(name, 200, 5)
    map = Map(100,100)
    try:
        s = sys.winver
        os.system("cls")
    except:
        os.system("clear")
    print("[game] DONE")
    sleep(2)
    try:
        s = sys.winver
        os.system("cls")
    except:
        os.system("clear")
    abfrageprolog2=input("[game] Möchtest du den zweiten Teil des Prologs lesen? \n[game] Ja/Nein: ")
    if abfrageprolog2=="Ja":
        try:
            s = sys.winver
            os.system("cls")
        except:
            os.system("clear")
        print(Fore.RED +"P", end="")
        sleep(0.25)
        print(Fore.GREEN +"R", end="")
        sleep(0.25) 
        print(Fore.BLUE +"O", end="")
        sleep(0.25)
        print(Fore.RED +"L", end="")
        sleep(0.25)
        print(Fore.GREEN +"O", end="")
        sleep(0.25)
        print(Fore.BLUE +"G", end="")
        sleep(4)
        try:
            s = sys.winver
            os.system("cls")
        except:
            os.system("clear")
        sleep(5)     
        print("[game] Die hohen Burgmauern lassen nur wenig Licht")
        sleep(3.5)
        try:
            s = sys.winver
            os.system("cls")
        except:
            os.system("clear")
        print("[game] der untergehenden Sonne in den Burghof hinein.")
        sleep(3.5)
        try:
            s = sys.winver
            os.system("cls")
        except:
            os.system("clear")
        print("[game] Am anderen Ende des Burghofs erahnst du im schwachen")
        sleep(3.5)
        try:
            s = sys.winver
            os.system("cls")
        except:
            os.system("clear")
        print("[game] Schein des Lichts eine Tür zum inneren der Burg.")
        sleep(3.5)
        try:
            s = sys.winver
            os.system("cls")
        except:
            os.system("clear")
        print("[game] Du ziehst dein Schwert, öffnest vorsichtig die Tür und betrittst das Innere der Burg.")
        sleep(3.5)
        try:
            s = sys.winver
            os.system("cls")
        except:
            os.system("clear")
        print("[game] Um dich herum ist es dunkel, nur eine Fackel am Ende des Raumes spendet etwas Licht.")
        sleep(3.5)
        try:
            s = sys.winver
            os.system("cls")
        except:
            os.system("clear")
        print("[game] Doch was ist das?")
        sleep(3.5)
        try:
            s = sys.winver
            os.system("cls")
        except:
            os.system("clear")
        print("[game] Vor dir erscheint ein Gegner. Greife ihn an.")
        sleep(3.5)
    else:
        try:
            s = sys.winver
            os.system("cls")
        except:
            os.system("clear")
        print("[game] Vor dir erscheint ein Gegner. Greife ihn an.")
        sleep(3.5)
        pass
    print("[game] (Tippe <help> für eine Liste von Befehlen)")
    while True:
        command = input(">").lower().split(" ") #pickup
        if command[0] in Commands:
            Commands[command[0]](p, map)
        else:
            print("[game] Du läufst im Kreis und weißt nicht was du tun sollst.")
        map.print_state() 