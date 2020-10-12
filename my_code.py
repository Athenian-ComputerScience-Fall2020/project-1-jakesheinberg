# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  
import random

print("Welcome to a stock market simulator!")
print("In this realistic simulation of the stock market you will be given news stories, relevant trends, and chances to commit insider trading or fraud, don't get caught!")
print("You will add to your investments every simulated week. It is important to note that money in the market cannot be recovered. You begin with a $10,000, you have 5 weeks to accumulate as much money as possible.")
print("Good luck!!")

def news_story():
    print("This weeks headlines: ")
    print(".")
    news_number=random.randint(1,11)
    news_number2=random.randint(1,11)
    if news_number==1:
        print(f"There is a hurricane coming! Get ready to stock up and stay at home!")
        hurricane=random.randint(95, 105)/100
        return hurricane
    elif news_number==2:
        print("Detroit to host Olympics! Expected Boom in economy!")
        olympics=random.randint(1010, 1015)/1000
        return olympics
    elif news_number==3:
        print("Social justice issues cause uprisings in urban cities!")
        uprising=random.randint(90, 95)/100
        return uprising
    elif news_number==4:
        print("Presidental election causes uncertainty in the market")
        election=random.randint(85,95)/100
        return election
    elif news_number==5:
        print("Water Bottle Companies Facing scrutinee for poisonous plastic")
        plastic=random.randint(60, 80)/100
        return plastic
    elif news_number==6:
        print("Oil found beneath california! Oils prices drop enourmously!")
        oil=random.randint(80,110)/100
        return oil
    elif news_number==7:
        print("Strict restrictions placed on gas cars all around the US")
        gas_car_restrictions=random.randint(80,120)/100
        return gas_car_restrictions
    elif news_number==8:
        print("Competing between social networks lead to a boom in social media use")
        social_use=random.randint(120, 140)/100
        return social_use
    elif news_number==9:
        print("Farmers all around the United States going bankrupt")
        farmer_bankrupcy=random.randint(60,90)/100
        return farmer_bankrupcy
    elif news_number==10:
        print("Schools have been shutdown due to a strike sparked by teachers!")
        school_cancelled=random.randint(900, 1001)/1000
        return school_cancelled




def starting_stocks():
    tesla=random.randint(100,115)
    print(f"1. a share of tesla cost {tesla}")
    papermate=random.randint(65, 80)
    print(f"2. a share of papermate cost {papermate}")
    safeway=random.randint(80,115)
    print(f"3. a share of safeway cost {safeway}")
    honda=random.randint(110, 130)
    print(f"4. a share of honda cost {honda}")
    chevron=random.randint(110,125)
    print(f"5. a share of chevron cost {chevron}")
    arrowhead=random.randint(80,90)
    print(f"6. a share of arrowhead cost {arrowhead}")
    lewies_burgers=random.randint(20,23)
    print(f"7. a share of Lewies Burgers cost {lewies_burgers}")
    news_story()
    total=10000
    x=0
    tesla_shares=0
    papermate_shares=0
    safeway_shares=0
    honda_shares=0
    chevron_shares=0
    arrowhead_shares=0
    lewies_burgers_shares=0
    spent=[]
    while x<7:
            investment=(input("Type the number of the stock to invest in it or type 'done' if you are finished investing: "))
            try:
                investment=int(investment)
                if investment!="done" and investment!="Done":
                    if investment==1:
                        how_much=int(input("How many shares of tesla would you like to buy: " ))
                        tesla_shares=tesla_shares+how_much
                        tesla_spent=tesla*how_much
                        spent.append(tesla_spent)
                    elif investment==2:
                        how_much=int(input("How many shares of papermate would you like to buy: " ))
                        papermate_shares=papermate_shares+how_much
                        papermate_spent=papermate*how_much
                        spent.append(papermate_spent)
                    elif investment==3:
                        how_much=int(input("How many shares of safeway would you like to buy: " ))
                        safeway_shares=safeway_shares+how_much
                        safeway_spent=safeway*how_much
                        spent.append(safeway_spent)
                    elif investment==4:
                        how_much=int(input("How many shares of honda would you like to buy: " ))
                        honda_shares=honda_shares+how_much
                        honda_spent=honda*how_much
                        spent.append(honda_spent)
                    elif investment==5:
                        how_much=int(input("How many shares of chevron would you like to buy: " ))
                        chevron_shares=chevron_shares+how_much
                        chevron_spent=chevron*how_much
                        spent.append(chevron_spent)
                    elif investment==6:
                        how_much=int(input("How many shares of arrowhead would you like to buy: " ))
                        arrowhead_shares=arrowhead_shares+how_much
                        arrowhead_spent=arrowhead*how_much
                        spent.append(arrowhead_spent)
                    elif investment==7:
                        how_much=int(input("How many shares of lewies_burgers would you like to buy: " ))
                        lewies_burgers_shares=lewies_burgers_shares+how_much
                        lewies_burgers_spent=lewies_burgers*how_much
                        spent.append(lewies_burgers_spent)
                total=total-sum(spent)
                print(f"you have {total} dollars left")
                x=x+1
            except:
                if investment=="done" or investment=="Done":
                    total=total-sum(spent)
                    print(f"you have {total} dollars left")
                    break
                else:
                    print("input is invalid")

        #def investment():
 #   round_num=0
  #  while round_num==0:
   #     starting_stocks()
    #    news_story()
     #   round_num=+1
#investment()



#def control_center():
    #print("Welcome to the market! You have 10,000 dollars to spend. Save it, spend it, risk it!")
    #nav=input("Type '1' to see weekly news storys, type '2' to see availible stocks and prices, and type 3 to insider trade! ")
    #if nav==1:
        #news_story()
    #if nav==2:
#
    

#control_center()



starting_stocks()