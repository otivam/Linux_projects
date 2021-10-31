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