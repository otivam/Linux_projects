class hero:
    def __init__(this, hero_class, hero_name):
        this.hero_class = hero_class
        this.hero_name = hero_name

game_on = False

while True:
    is_start = input("Please type \"start\" for new game: ")
    
    if is_start.lower() == "start":
        game_on = True
        break;
    else:
        print("Please try again!")



while game_on:
    hero_class = input("Chose hero class: ")
    
    if hero_class.lower() == "warrior":
        print("WARRIOR!")
        hero_name = input("Enter hero name: ")
        hero_name = hero("Warrior", hero_name)
        break;
    elif hero_class.lower() == "druid":
        print("DRUID!")
        hero_name = input("Enter hero name: ")
        hero_name = hero("Druid", hero_name)
        break;
    elif hero_class.lower() == "paladin":
        print("PALADIN!")
        hero_name - input("Enter hero name: ")
        hero_name = hero("Paladin", hero_name)
        break;
    else:
        print("Please select a valid class!")



print(hero_name.hero_name)
print(hero_name.hero_class)


