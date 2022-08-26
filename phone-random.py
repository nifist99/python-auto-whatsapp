
import random
import string
import numpy as np
import pywhatkit
 

operator = {"0852","0853","0811","0812","0813","0821","0822","0851"
        "0857","0856","0896","0895","0897","0898","0899","0817",
        "0818","0819","0859","0877","0878","0813","0832","0833",
        "0838","0881","0882","0883","0884","0885","0886","0887",
        "0888","0889"
        }
        



def process():
    ran=random.randint(10000000, 99999999)
    op=random.sample(operator,1)
    result=" ".join(op)
    number =result+""+str(ran)
    print(number.replace("0","+62",1))
    pywhatkit.sendwhatmsg_instantly(number.replace("0","+62",1), "Hi", 10, tab_close=True)

def main():
    i=1
    while i<5:
        process()

if __name__ == "__main__":

      main()