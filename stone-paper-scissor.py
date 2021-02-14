# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 14:37:41 2021

@author: Owner
"""


from random import randrange

def main(human_c):
    human_c = human_c.upper()
    pc_c = randrange(0,3)
    
    dictionary = {'STONE':0,'PAPER':1,'SCISSOR':2}
    lst = list(dictionary.keys())
    
    print("\t{}  Vs {}".format(human_c,lst[pc_c]))
    
    human_c = dictionary[human_c]
    
    if human_c==pc_c:
        print("\tTIE")
    elif (human_c==0 and pc_c==2) or (human_c==1 and pc_c==0) or (human_c==2 and pc_c==1):
        print("\tYOU WON")
    else:
        print("\tYOU LOSE")
        

if __name__ == '__main__':
    print()
    print("****WELCOME TO STONE,PAPER OR SCISSOR GAME****\n")
    x = "YES"
    while(x.upper()=="YES"):
        human_c = input("\tCHOOSE STONE,PAPER OR SCISSOR: ")
        main(human_c)
        x = input("\tSTILL WANT TO PLAY(YES/N0)?:")

        
    

    