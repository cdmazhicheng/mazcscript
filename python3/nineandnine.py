#!bin/python

import sys

class Nine_and_nine():

    def __init__(self):
        self.num_init = 10
        self.number = []

    def nineandnine(self):
        nine_list = list(range(self.num_init))
        need_list = nine_list[1:10]

        for i in range(len(need_list)):
            print()
            for j in range(need_list[i]):
                if need_list[i] * need_list[j] > 9:
                    sys.stdout.write('{}*{}='.format(need_list[i],need_list[j]) + str(need_list[i] * need_list[j])+"   ")
                else:
                    sys.stdout.write('{}*{}='.format(need_list[i], need_list[j]) + str(need_list[i] * need_list[j]) + "    ")

object_nie = Nine_and_nine()
object_nie.nineandnine()
