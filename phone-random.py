
import random
import string
import numpy as np
import pywhatkit
 

operator = {"0852","0853","0811","0812","0813","0821",
            "0822","0851","0857","0856","0896","0895",
            "0897","0898","0899","0817","0818","0819",
            "0859","0877","0878","0813","0832","0833",
            "0838","0881","0882","0883","0884","0885",
            "0886","0887","0888","0889"
        }

new_operator={"0811","0812","0813","0814","0815","0816",
              "0817","0818","0819","0821","0822","0823",
              "0828","0831","0838","0852","0853","0855",
              "0856","0857","0858","0859","08681","0877",
              "0878","0879","0881","0882","0883","0884",
              "0887","0888","0889","0896","0897","0898",
              "0899"}
        


# jumlah nomer 12
def process():
    ran=random.randint(10000000, 99999999)
    op=random.sample(new_operator,1)
    result=" ".join(op)
    number =result+""+str(ran)
    print(number.replace("0","+62",1))
    pywhatkit.sendwhatmsg_instantly(number.replace("0","+62",1), "Hi", 10, tab_close=True)

# jumlah nomer 11
def process2():
    ran=random.randint(1000000, 9999999)
    op=random.sample(new_operator,1)
    result=" ".join(op)
    number =result+""+str(ran)
    print(number.replace("0","+62",1))
    pywhatkit.sendwhatmsg_instantly(number.replace("0","+62",1), "Hi", 10, tab_close=True)

# jumlah nomer 10
def process3():
    ran=random.randint(100000, 999999)
    op=random.sample(new_operator,1)
    result=" ".join(op)
    number =result+""+str(ran)
    print(number.replace("0","+62",1))
    pywhatkit.sendwhatmsg_instantly(number.replace("0","+62",1), "Hi", 10, tab_close=True)

# jumlah nomer 10 - 12
def process4():
    ran=random.randint(100000, 99999999)
    op=random.sample(new_operator,1)
    result=" ".join(op)
    number =result+""+str(ran)
    print(number.replace("0","+62",1))
    pywhatkit.sendwhatmsg_instantly(number.replace("0","+62",1), "Hi", 10, tab_close=True)

def main():
    i=1
    while i<5:
        process()
        process2()
        process3()
        process4()

if __name__ == "__main__":
    main()