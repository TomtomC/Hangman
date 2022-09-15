
import random as rand

def the_word():
    word_list = ["aardvark", "baboon", "camel"]
    ##listlen = len(word_list)-1
    ##randnum = rand.randint(0,listlen)
    ##t_word = word_list[randnum]
    t_word = rand.choice(word_list)
    return t_word