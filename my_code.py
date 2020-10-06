# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  
import random

print("Welcome to a stock market simulator!")
print("In this realistic simulation of the stock market you will be given news stories, relevant trends, and chances to commit insider trading or fraud, don't get caught!")
print("You will adjust or add to you investments every simulated week. You begin with a $1000, you have 15 weeks to accumulate as much money as possible.")
print("Good luck!!")

def news_story():
    news_number=random.randint(1,1)
    if news_number==1:
        hurricane_weeks=random.randint(1,3)
        story=f"There is a hurricane coming in {hurricane_weeks} week! Get ready to stock up and stay at home!"
        return story, hurricane_weeks
        

print(news_story())





