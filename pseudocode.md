# Stock Market Simulator
    News_story():
        -The code begins buy calling the function news_storys().
        -News storys will randomly select a news story from 10 options.
        -All storys will be given a random value that is within a set domain.
        -This value will be stored as the return statement for news_storys().
    Set starting stocks:
        -The code will then set a random share price from within a domain to all 7 companies.
    Investment:
        -Now the user will buy their stocks using an input chain (each number corresponds to stock and takes you to that stocks page where you can buy however many shares you like.)
        -The stocks are then multiplied by the values produced by the news_story()
        -The profit for the round (net money in market-money speny) and money remaining(10000-money spent) are presented
        -Then the new cost for the stocks are presented
        -This proccess repeats 3 times using a while loop
    The Finishing Touches:
        -The code presents you total profit from the game.
