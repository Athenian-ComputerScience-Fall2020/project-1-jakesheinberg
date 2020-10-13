# Collaborators (including web sites where you got help: none
#  
import random

print("Welcome to a stock market simulator!")
print("You will be given an arbitrary news story. Invest accordingly. This simulation is meant to provide practice for real investing.")
print("You have $10,000 to spend")
def news_story():
    print("This weeks headlines: ")
    print(".")
    news_number=random.randint(1,10)
    if news_number==1:
        print(f"There is a hurricane coming! Get ready to stock up and stay at home!")
        hurricane=random.randint(95, 105)/100 #can be used for further developement
        news_value=hurricane
    elif news_number==2:
        print("Detroit to host Olympics! Expected Boom in economy!")
        olympics=random.randint(1010, 1015)/1000
        news_value=olympics
    elif news_number==3:
        print("Social justice issues cause uprisings in urban cities!")
        uprising=random.randint(90, 95)/100
        news_value=uprising
    elif news_number==4:
        print("Presidental election causes uncertainty in the market")
        election=random.randint(85,95)/100
        news_value=election
    elif news_number==5:
        print("Water Bottle Companies Facing scrutinee for poisonous plastic")
        plastic=random.randint(60, 80)/100
        news_value=plastic
    elif news_number==6:
        print("Oil found beneath california! Oils prices drop enourmously!")
        oil=random.randint(80,110)/100
        news_value=oil
    elif news_number==7:
        print("Strict restrictions placed on gas cars all around the US")
        gas_car_restrictions=random.randint(80,120)/100
        news_value=gas_car_restrictions
    elif news_number==8:
        print("Competing between social networks lead to a boom in social media use!")
        social_use=random.randint(120, 140)/100
        news_value=social_use
    elif news_number==9:
        print("Farmers all around the United States going bankrupt!")
        farmer_bankrupcy=random.randint(60,90)/100
        news_value=farmer_bankrupcy
    elif news_number==10:
        print("Schools have been shutdown due to a strike sparked by teachers!")
        school_cancelled=random.randint(900, 1001)/1000
        news_value=school_cancelled
    return news_value





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
total=10000
y=0
    #setting shares bought: 
tesla_shares=0
papermate_shares=0
safeway_shares=0
honda_shares=0
chevron_shares=0
arrowhead_shares=0
lewies_burgers_shares=0
spent=[]
spent2=[]#used for total in market calculation (values dont clear)
final_profit=10000#used to find the total profit if all rounds

while y<3:
        news=news_story()
        investment=(input("Type the number of the stock to invest in it or type 'done' if you are finished investing: "))
        try:
            investment=int(investment)
            if investment!="done" and investment!="Done":
                if investment==1:
                    how_much=int(input("How many shares of tesla would you like to buy: " ))
                    tesla_shares=tesla_shares+how_much
                    tesla_spent=tesla*how_much
                    spent.append(tesla_spent)
                    spent2.append(tesla_spent)
                elif investment==2:
                    how_much=int(input("How many shares of papermate would you like to buy: " ))
                    papermate_shares=papermate_shares+how_much
                    papermate_spent=papermate*how_much
                    spent.append(papermate_spent)
                    spent2.append(papermate_spent)                    
                elif investment==3:
                    how_much=int(input("How many shares of safeway would you like to buy: " ))
                    safeway_shares=safeway_shares+how_much
                    safeway_spent=safeway*how_much
                    spent.append(safeway_spent)
                    spent2.append(safeway_spent)
                elif investment==4:
                    how_much=int(input("How many shares of honda would you like to buy: " ))
                    honda_shares=honda_shares+how_much
                    honda_spent=honda*how_much
                    spent.append(honda_spent)
                    spent2.append(honda_spent)
                elif investment==5:
                    how_much=int(input("How many shares of chevron would you like to buy: " ))
                    chevron_shares=chevron_shares+how_much
                    chevron_spent=chevron*how_much
                    spent.append(chevron_spent)
                    spent2.append(chevron_spent)
                elif investment==6:
                    how_much=int(input("How many shares of arrowhead would you like to buy: " ))
                    arrowhead_shares=arrowhead_shares+how_much
                    arrowhead_spent=arrowhead*how_much
                    spent.append(arrowhead_spent)
                    spent2.append(arrowhead_spent)
                elif investment==7:
                    how_much=int(input("How many shares of lewies_burgers would you like to buy: " ))
                    lewies_burgers_shares=lewies_burgers_shares+how_much
                    lewies_burgers_spent=lewies_burgers*how_much
                    spent.append(lewies_burgers_spent)
                total=total-sum(spent)
                spent=[]
                print(f"you have {total} dollars left in the bank")
                totalInMarket=sum(spent2)
            stocksafterchange=[]
            stocks_changing=[tesla, papermate, safeway, honda, chevron, arrowhead, lewies_burgers]
            for x in stocks_changing:
                x=x*news
                stocksafterchange.append(x)
            profit=sum(stocksafterchange)-totalInMarket
            profit=round(profit, 2)
            if profit>0:
                print(f"You made {profit} dollars in profit this round")
            elif profit==0:
                print("you broke even this round")
            elif profit<0:
                print(f"you lost {profit} dollars this round")
            print("round completed")
            final_profit=final_profit+profit
            y=y+1
            tesla=tesla*news
            tesla=round(tesla,2)
            papermate=papermate*news
            papermate=round(papermate, 2)
            safeway=safeway*news
            safeway=round(safeway, 2)
            honda=honda*news
            honda=round(honda,2)
            chevron=chevron*news
            chevron=round(chevron, 2)
            arrowhead=arrowhead*news
            arrowhead=round(arrowhead,2)
            lewies_burgers=lewies_burgers*news
            lewies_burgers=round(lewies_burgers, 2)           
            print(f"1. a share of tesla cost {tesla}")
            print(f"2. a share of papermate cost {papermate}")
            print(f"3. a share of safeway cost {safeway}")
            print(f"4. a share of honda cost {honda}")
            print(f"5. a share of chevron cost {chevron}")
            print(f"6. a share of arrowhead cost {arrowhead}")
            print(f"7. a share of Lewies Burgers cost {lewies_burgers}")
        except:
            if investment=="done" or investment=="Done":
                print(f"you have {total} dollars left")
                print("round completed")
                y=y+1
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
