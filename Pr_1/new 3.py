'''
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

from itertools import islice

sh_in = input()

if not "." in sh_in:
    sh_in = sh_in + '.txt'

line_1 = ''
line_2 = ''

with open(sh_in) as fin:
    for line in islice(fin, 0, 1):
        line_1 = line
        
with open(sh_in) as fin:
    for line in islice(fin, 1, 2):
        line_2 = line


def sh(num,txt):
    pr_nums_txt = ''
    non_pr_nums_txt = ''
    result = ''
    
    def pr_nums(x):
        num = x
        flag = False

        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    flag = True
                    break
        else:
            return False
            
        if flag:
            return False
        else:
            return True
    
    for x in range(int(num)):
        result = ''
        pr_nums_txt = ''
        non_pr_nums_txt  = ''

        for y in range(len(txt)):
            if pr_nums(int(y)+1):
                pr_nums_txt += (txt[y])
            else:
                non_pr_nums_txt += (txt[y])
         
        result = pr_nums_txt + non_pr_nums_txt  
        txt = result
        
    result_2 = result
    res_2_len = len(result_2)
    first_block = 0
    decode_1 = ''  
    sh_txt = []
    
    
    for x in range(res_2_len):
        sh_txt.append(0)
        if pr_nums(int(x)):
            first_block += 1
            
    for x in range(first_block):
        
        
    for x in range(first_block):
        for y in range(len(result_2)):
            if pr_nums(int(y)+1):
                sh_txt[int(y)] = result_2[int(x)]
                
                
                
    print(sh_txt)
        
    return result
    
print(sh(line_1,line_2))

'''


import new1

new1.test_f()
            
for i in range(10):
    print(i)
    
print(10/0)

        