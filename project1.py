class Character:
    def __init__(self, role, region, element, main_stat):
        self.role = role
        self.region = region
        self.element = element
        self.main_stat = main_stat

    def sett_atk(self):      #если главный стат персонажа атака -- смотрим роль подбираем сеты
        if (self.main_stat == "ATK") and (self.role == "support"):
            print("Use artifact sets «Gladiator's Finale», «Shimenawa's Reminiscence»")
        elif (self.main_stat == "ATK") and (self.role == "dps"):
            print("Use artifact sets «Gladiator's Finale» and «Vermillion Hereafter»")
        elif (self.main_stat == "ATK") and (self.role == "sup dps"):
            print("Use artifact sets «Marechaussee Hunter», «Shimenawa's Reminiscence»")

    def sett_hp(self):    #смотрим роль персов, играющихся от хп
        if (self.main_stat == "HP") and (self.role == "support"):
            print("Use artifact sets «Tenacity of the Millelith» and «Ocean-Hued Clam»")
        elif (self.main_stat == "HP") and (self.role == "dps"):
            print("Use artifact sets «Tenacity of the Millelith» and «Vourukasha's Glow»")
        elif (self.main_stat == "HP") and (self.role == "sup dps"):
            print("Use artifact sets «Vourukasha's Glow», «Marechaussee Hunter»")

    def sett_def(self):     #смотрим роль персов, играющихся от защиты (в основном щитовики)
        if (self.main_stat == "DEF") and (self.role == "support"):
            print("Use artifact sets «Husk of Opulent Dreams» and «Retracing Bolide»")
        elif (self.main_stat == "DEF") and (self.role == "sup dps"):
            print("Use artifact sets «Husk of Opulent Dreams», «Defender's Will»")

Sayu = Character(region="Inazuma", element="anemo", role="support", main_stat="ATK")
Razor = Character(region="Mondstadt", element="electro", role="dps", main_stat="ATK")
Kokomi = Character(region="Inazuma", element="hydro", role="support", main_stat="HP")
Elan = Character(region="Liue", element="hydro", role="sup dps", main_stat="ATK")
Noelle = Character(region="Mondstadt", element="geo", role="support", main_stat="DEF")
Xiangling = Character(region="Liue", element="pyro", role="sup dps", main_stat="ATK")
Mona = Character(region="Mondstadt", element="hydro", role="support", main_stat="HP")
Thoma = Character(region="Inazuma", element="pyro", role="support", main_stat="DEF")


region_input = input("Choose region: ")
element_input = input("Choose element: ")
role_input = input("Choose character's role: ")

list1 = [Sayu, Razor, Kokomi, Elan, Noelle, Xiangling, Mona, Thoma]
list2 = [i for i in list1 if i.region == region_input]
list3 = [i for i in list2 if i.element == element_input]
list4 = [i for i in list3 if i.role == role_input]

for character in list4:
    if character.main_stat == "ATK":
        character.sett_atk()
    elif character.main_stat == "HP":
        character.sett_hp()
    elif character.main_stat == "DEF":
        character.sett_def()