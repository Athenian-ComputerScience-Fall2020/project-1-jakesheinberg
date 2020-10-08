# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  
import random

print("Welcome to a stock market simulator!")
print("In this realistic simulation of the stock market you will be given news stories, relevant trends, and chances to commit insider trading or fraud, don't get caught!")
print("You will adjust or add to you investments every simulated week. You begin with a $10,000, you have 5 weeks to accumulate as much money as possible.")
print("Good luck!!")
z=0
while z<5:
    print(".")
    z=z+1

def news_story():
    news_number=random.randint(1,11)
    news_number2=random.randint(1,11)
    if news_number==1 or news_number2==1:
        print(f"There is a hurricane coming! Get ready to stock up and stay at home!")
        hurricane=True
    elif news_number==2 or news_number2==2:
        print("Detroit to host Olympics! Expected Boom in economy!")
        olympics=True
    elif news_number==3 or news_number2==3:
        print("Social justice issues cause uprisings in urban cities!")
        uprising=True
    elif news_number==4 or news_number2==4:
        print("Presidental election causes uncertainty in the market")
        election=True
    elif news_number==5 or news_number2==5:
        print("Water Bottle Companies Facing scrutinee for poisonous plastic")
        plastic=True
    elif news_number==6 or news_number2==6:
        print("Oil found beneath california! Oils prices drop enourmously!")
        oil=True
    elif news_number==7 or news_number2==7:
        print("Strict restrictions placed on gas cars all around the US")
        gas_car_restrictions=True
    elif news_number==8 or news_number2==8:
        print("Competing between social networks lead to a boom in social media use")
        social_use=True
    elif news_number==9 or news_number2==9:
        print("Farmers all around the United States going bankrupt")
        farmer_bankrupcy=True
    elif news_number==10 or news_number2==10:
        print("Schools have been shutdown due to a strike sparked by teachers!")
        school_cancelled:True



        

def investments():
    print("Welcome to the market! You have 10,000 dollars to spend. Save it, spend it, risk it!")
    control_center=input("Type '1' to see weekly news storys, type '2' to see availible stocks and prices, and type 3 to insider trade!")
    if x==1:
        news_story



