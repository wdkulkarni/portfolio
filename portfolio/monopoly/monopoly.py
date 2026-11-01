import random
import time
import socket
#used for going though turns
turn_thing=0
#creates classes to store information about players, title_deeds, etc.
class chests:
    def __init__(self, name, money, jail_card, place):
        self.name=name
        self.money=money
        self.jail_card=jail_card
        self.place=place
class chances:
    def __init__(self, name, money, jail_card, place):
        self.name=name
        self.money=money
        self.jail_card=jail_card
        self.place=place
class title_deeds:
    def __init__(self, place, buy, house_buy, hotel_buy, base_rent, rent_house, rent_house1, rent_house2, rent_house3, rent_hotel, color, num_houses, colorset, num_house, num_hotel, rent, mortgage):
        self.place=place
        self.buy=buy
        self.house_buy=house_buy
        self.hotel_buy=hotel_buy
        self.base_rent=base_rent
        self.rent_house=rent_house
        self.rent_house1=rent_house1
        self.rent_house2=rent_house2
        self.rent_house3=rent_house3
        self.rent_hotel=rent_hotel
        self.color=color
        self.num_houses=num_houses
        self.colorset=colorset
        self.num_house=num_house
        self.num_hotel=num_hotel
        self.rent=rent
        self.mortgage = mortgage
    #function to calculate rent
    def calc_rent(self):
        if self.num_hotel>0:
            self.rent=self.rent_hotel
        elif self.num_house==1:
            self.rent=self.rent_house
        elif self.num_house==2:
            self.rent=self.rent_house1
        elif self.num_house==3:
            self.rent=self.rent_house2
        elif self.num_house==4:
            self.rent=self.rent_house3
        else:
            self.rent=self.base_rent
        return self.rent
    #functiont to calculate selling price
    def calc_sell(self):
        sell=0
        sell+=self.buy/2
        sell+=self.num_house*(self.house_buy/2)
        sell+=self.num_hotel*(self.hotel_buy/2)
        return sell
class utilities:
    def __init__(self, name, buy, mortgage):
        self.name=name
        self.buy=buy
        self.mortgage=mortgage
class trains:
    def __init__(self, name, buy, mortgage):
        self.name=name
        self.buy=buy
        self.mortgage=mortgage
class specials:
    def __init__(self, name, money, jail):
        self.name=name
        self.money=money
        self.jail=jail
class players:
    def __init__(self, token, title_deeds, house, hotel, balance, position, jail_card, jail, ai, mortgaged_p, auction, time_in_jail):
        self.token=token
        self.title_deeds=title_deeds
        self.house=house
        self.hotel=hotel
        self.balance=balance
        self.position=position
        self.jail_card=jail_card
        self.jail=jail
        self.ai=ai
        self.mortgaged_p = mortgaged_p
        self.auction = auction
        self.time_in_jail = time_in_jail
    def append_title_deed(self, title_deed):
        self.title_deeds.append(title_deed)
#functions used to open and create save files
save_files = []
def save_file(file_name, classes):
    a = open(file_name, "w")
    b = str(classes)
    a.write(b)
    a.close()
    #print("saved")
def open_file(file_name, player_list):
    a = open(file_name, "r")
    c = eval(a.read())
    #Add code for extracting info from lists below and set equal to classes
    for i in range(len(player_list)):
        player_list[i].token = c[i][0]
        player_list[i].title_deeds = c[i][1]
        player_list[i].house = c[i][2]
        player_list[i].hotel = c[i][3]
        player_list[i].balance = c[i][4]
        player_list[i].position = c[i][5]
        player_list[i].jail_card = c[i][6]
        player_list[i].jail = c[i][7]
        player_list[i].ai = c[i][8]
    return player_list
#function that runs teh open and save files functions
def save(save_name):
    list_of_list_of_classes = []
    #makes a list and saves the list
    for i in range(len(player_list)):
        list_of_classes = []
        list_of_classes.append(player_list[i].token)
        list_of_classes.append(player_list[i].title_deeds)
        list_of_classes.append(player_list[i].house)
        list_of_classes.append(player_list[i].hotel)
        list_of_classes.append(player_list[i].balance)
        list_of_classes.append(player_list[i].position)
        list_of_classes.append(player_list[i].jail_card)
        list_of_classes.append(player_list[i].jail)
        list_of_classes.append(player_list[i].ai)
        list_of_list_of_classes.append(list_of_classes)
    save_file(save_name+"player_list.txt", list_of_list_of_classes)
#function to open up saves
def open_save(save_name, list_of_list_of_classes):
    list_of_list_of_classes = open_file(save_name+"player_list.txt", list_of_list_of_classes)
    return player_list
save_file_of_save_file_of_save_files = open("save_file_of_save_files.txt", "r")
save_files = eval(save_file_of_save_file_of_save_files.read())
#creates the players.
while True:
    player_num=int(input("How many players? 2-6: "))
    if player_num < 2 or player_num > 6:
        print("Choose a number from 2-6")
    else:
        break
player_list=[]
for i in range(player_num):
    token=input("Name of player "+str(i+1)+"?: ")
    is_ai=input("Is this player an ai(yes, no)?: ")
    if is_ai=="yes":
        ai=True
    else:
        ai=False
    player_list.append(players(token, [], 0, 0, 1500, 0, False, False, ai, [], True, 0))
#asks if they want to open up a previous save file
if input("Do you want to open up a save file(yes or no)(number of players listed above must be the same as the save file). ?: ")=="yes":
    print(save_files)
    open_save_file=input("What file do you want to open?: ")
    player_list=open_save(open_save_file, player_list)
#makes a list of classes for the title_deeds, cards, etc.
community_chest=[chests("Pay school tax", -50, False, ""),
                 chests("collect $50 from every player", 50*len(player_list), False, ""),
                 chests("You inherit $100", 100, False, ""),
                 chests("pay hospital $100", -100, False, ""),
                 chests("income tax refund", 50, False, ""),
                 chests("go to jail", 0, False, ""),
                 chests("get out of jail free card", 0, True, ""),
                 chests("second place prize in beauty contest, +$10", 10, False, ""),
                 chests("pay $40 per house and $115 for every hotel", -40*player_list[0].house+-115*player_list[0].hotel, False, ""),
                 chests("bank error, collect $200", 200, False, ""),
                 chests("Advance to go", 0, False, "Go"),
                 chests("IMA fund matures, collect $100", 100, False, ""),
                 chests("doctors fee of $50", -50, False, ""),
                 chests("sale of stock, $45", 45, False, ""),
                 chests("$25 for services", 25, False, ""),
                 chests("Life insurance matures, collect $100", 100, False, "")]
chance_card=[chances("Advance to St. Charles", 0, False, "St. Charles"),
             chances("Get out of jail free card", 0, True, ""),
             chances("Take a ride to a train station", 0, False, "Train Station"),
             chances("Advance to Illinois Ave", 0, False, "Illinois Ave"),
             chances("repairs, pay $25 per house and $100 per hotel", -35*player_list[0].house+-100*player_list[0].hotel, False, ""),
             chances("advance to go", 0, False, "Go"),
             chances("banks pays $50", 50, False, ""),
             chances("Pay poor tax of $15", -15, False, ""),
             chances("Advance to nearst Utility", 0, False, "Placeholder for nearest utility"),
             chances("Go to Jail", 0, False, "Jail"),
             chances("Elected chairman, pay $50 per player", -50*player_num, False, ""),
             chances("Advance to Boardwalk", 0, False, "Boardwalk"),
             chances("Go back 3 spaces", 0, False, "placeholder for player position minus 3 spaces"),
             chances("advance to nearest railroad", 0, False, "Placeholder for nearest railroad"),
             chances("Buildings and loan matures, collect $150", 150, False, "")]
title_deed=[title_deeds("Mediterranean Ave", 60, 50, 50, 2, 10, 30, 90, 160, 250, "brown", 0, False, 0, 0, 0, False),
            title_deeds("Baltic Ave", 60, 50, 50, 4, 20, 60, 180, 320, 450, "brown", 0, False, 0, 0, 0, False),
            title_deeds("Oriental Ave", 100, 50, 50, 6, 30, 90, 270, 400, 550, "light blue", 0, False, 0, 0, 0, False),
            title_deeds("Vermont Ave", 100, 50 ,50, 6, 30, 90, 270, 400, 550, "light blue", 0, False, 0, 0, 0, False),
            title_deeds("Connecticut Ave", 120, 50, 50, 8, 40, 100, 300, 450, 600, "light blue", 0, False, 0, 0, 0, False),
            title_deeds("St. Charles Place", 140, 100, 100, 10, 50, 150, 450, 625, 750, "pink", 0, False, 0, 0, 0, False),
            title_deeds("States Ave", 140, 100, 100, 10, 50, 150, 450, 625, 750, "pink", 0, False, 0, 0, 0, False),
            title_deeds("Virginia Ave", 160, 100, 100, 12, 60, 180, 500, 700, 900, "pink", 0, False, 0, 0, 0, False),
            title_deeds("St. James Place", 180, 100, 100, 14, 70, 200, 550, 750, 950, "orange", 0, False, 0, 0, 0, False),
            title_deeds("Tennessee Ave", 180, 100, 100, 14, 70, 200, 550, 750, 950, "orange", 0, False, 0, 0, 0, False),
            title_deeds("New York Ave", 200, 100, 100, 16, 80, 220, 600, 800, 1000, "orange", 0, False, 0, 0, 0, False),
            title_deeds("Kentucky Ave", 220, 150, 150, 18, 90, 250, 700, 875, 1050, "red", 0, False, 0, 0, 0, False),
            title_deeds("Indiana Ave", 220, 150, 150, 18, 90, 250, 700, 875, 1050, "red", 0, False, 0, 0, 0, False),
            title_deeds("Illinois Ave", 240, 150, 150, 20, 100, 300, 750, 925, 1100, "red", 0, False, 0, 0, 0, False),
            title_deeds("Atlantic Ave", 260, 150, 150, 22, 110, 330, 800, 975, 1150, "yellow", 0, False, 0, 0, 0, False),
            title_deeds("Ventnor Ave", 260, 150, 150, 22, 110, 330, 800, 975, 1150, "yellow", 0, False, 0, 0, 0, False),
            title_deeds("Marvin Gardens", 280, 150, 150, 24, 120, 360, 850, 1025, 1200, "yellow", 0, False, 0, 0, 0, False),
            title_deeds("Pacific Ave", 300, 200, 200, 26, 130, 390, 900, 1100, 1275, "green", 0, False, 0, 0, 0, False),
            title_deeds("North Carolina Ave", 300, 200, 200, 26, 130, 390, 900, 1100, 1275, "green", 0, False, 0, 0, 0, False),
            title_deeds("Pennsylvania Ave", 320, 200, 200, 28, 150, 450, 1000, 1200, 1400, "green", 0, False, 0, 0, 0, False),
            title_deeds("Park Place", 350, 200, 200, 35, 175, 500, 1100, 1300, 1500, "blue", 0, False, 0, 0, 0, False),
            title_deeds("Boardwalk", 400, 200, 200, 50, 200, 600, 1400, 1700, 2000, "blue", 0, False, 0, 0, 0, False)]
utility=[utilities("Electric Company", 150, False), utilities("Water Works", 150, False)]
train=[trains("Reading Railroad", 200, False), trains("Pennsylvania Railroad", 200, False), trains("B. & O. Railroad", 200, False), trains("Short Line", 200, False)]
special=[specials("Go", 200, False), specials("Jail", 0, True), specials("Free Parking", 0, False), specials("Go to jail", 0, False), specials("Income tax", -200, False), specials("Luxury tax", -100, False)]
#list used for seperating title_deeds into a list by color set for color set function
colorsets=[["Mediterranean Ave", "Baltic Ave"], ["Oriental Ave", "Vermont Ave", "Connecticut Ave"], ["St. Charles Place", "States Ave", "Virginia Ave"], ["St. James Place", "Tennessee Ave", "New York Ave"], ["Kentucky Ave", "Indiana Ave", "Illinois Ave"], ["Atlantic Ave", "Ventnor Ave", "Marvin Gardens"], ["Pacific Ave", "North Carolina Ave", "Pennsylvania Ave"], ["Park Place", "Boardwalk"]]
#function used for finding if a title_deed is in a colorset
def check_color_set(turn, ai = False):
    thing = True
    colorset = False
    #goes through owned title_deeds
    for i in range(len(player_list[turn].title_deeds)):
        #goes through each colorset
        for j in range(len(colorsets)):
            #goes through each owned title deed and match it to a colorset
            if player_list[turn].title_deeds[i] in colorsets[j]:
                #sees if the color set contains 2 or 3 properties
                if len(colorsets[j])==2:
                    #goes through each owned title deed
                    for k in range(len(player_list[turn].title_deeds)):
                        #finds teh colorset of the title deed
                        if player_list[turn].title_deeds[k]==colorsets[j][0]:
                            #goes through each title deed again
                            for l in range(len(player_list[turn].title_deeds)):
                                #sees if the title deed is in teh same color set
                                #The branch for 3 title deed does this step again
                                if player_list[turn].title_deeds[l]==colorsets[j][1]:
                                    #goes though each title deed
                                    for m in range(len(title_deed)):
                                        #matches teh title deed in a list to teh list of title deed classes
                                        if title_deed[m].place == player_list[turn].title_deeds[k]:
                                            if thing == True:
                                                print("You have a color set")
                                                thing = False
                                            if ai == True:
                                                colorset = True
                                            #makes the colorset value true
                                            title_deed[m].colorset=True
                                            title_deed[m+1].colorset=True
                if len(colorsets[j])==3:
                    for k in range(len(player_list[turn].title_deeds)):
                        if player_list[turn].title_deeds[k]==colorsets[j][0]:
                            for l in range(len(player_list[turn].title_deeds)):
                                if player_list[turn].title_deeds[l]==colorsets[j][1]:
                                    for m in range(len(player_list[turn].title_deeds)):
                                        if player_list[turn].title_deeds[m]==colorsets[j][2]:
                                            for n in range(len(title_deed)):
                                                if title_deed[m].place == player_list[turn].title_deeds[k]:
                                                    if thing == True:
                                                        print("You have a color set")
                                                        thing = False
                                                    if ai == True:
                                                        colorset = True
                                                    title_deed[m].colorset=True
                                                    title_deed[m+1].colorset=True
    if ai == False:
        return title_deed, player_list
    if ai == True:
        return colorset
#function that runs when someone goes broke, also used for trade
def broke(turn, reciver, player_list, negative):
    #moves ownership of title deeds
    def selling_td(sell_t, sell, player_list, td_index, turn = turn, reciver = reciver):
        player_list[turn].title_deeds.remove(sell_t)
        if sell=="trade":
            for i in range(len(player_list)):
                if player_list[i].token == reciver:
                    break
            player_list[i].title_deeds.append(sell_t)
        elif sell=="sell":
            player_list[turn].balance+=title_deed[td_index].calc_sell()
        else:
            for i in range(len(player_list)):
                if player_list[i].token == reciver:
                    break
            player_list[i].title_deeds.append(sell_t)
            player_list[turn].balance+=title_deed[td_index].calc_sell()
        time.sleep(3)
        return player_list
    #if the broke function is called for trade, reciver is a name
    #if the function is used for seeing if someone is broke, then the reciver is 1
    if reciver != 1:
        while True:
            if player_list[turn].ai == True:
                td_to_give = AI(player_list, "td_to_give", 0, 0, turn, reciver)
            else:
                td_to_give = input("What title deed do you want to give: ")
            list_of_td = [title_deed[i].place for i in range(len(title_deed))]
            list_of_rr = [train[i].name for i in range(len(train))]
            list_of_utility = ["Electric Company", "Water Works"]
            if td_to_give in list_of_td:
                index_of_td = list_of_td.index(td_to_give)
                if title_deed[index_of_td].colorset == True:
                    print("You cannot trade off a title deed in a colorset")
                    time.sleep(3)
                else:
                    break
            elif td_to_give in list_of_rr:
                index_of_td = list_of_rr.index(td_to_give)
                break
            elif td_to_give in list_of_utility:
                index_of_td = list_of_utility.index(td_to_give)
                break
            else:
                print("Please type a valid input")
                time.sleep(3)
        selling_td(td_to_give, "trade", player_list, index_of_td)
        for i in range(len(player_list)):
            if player_list[i].token == reciver:
                break
        if player_list[i].ai == True:
            td_to_recive = AI(player_list, "td_to_give", 0, 0, i, reciver)
        else:
            while True:
                td_to_recive = input("What title deed do you want to give(The player that recived): ")
                if td_to_recive in list_of_td or td_to_recive in list_of_rr or td_to_recive in list_of_utility:
                    break
                else:
                    print("Type in a valid input")
                    time.sleep(3)
        for i in range(len(title_deed)):
            if title_deed[i].place == td_to_recive:
                break
        for j in range(len(player_list)):
            if player_list[j].token == reciver:
                break
        selling_td(td_to_recive, "trade", player_list, i, j, player_list[turn].token)
    elif player_list[turn].balance<0 and negative == False:
        while True:
            #runs while player has title deeds
            if player_list[turn].title_deeds!=[]:
                print(player_list[turn].title_deeds)
                mos = 1
                #asks if they want to mortgage or sell a property
                if player_list[turn].ai == True:
                    sell_t = AI(player_list, "sell_t", 0, 0, turn)
                    mos = "mortgage"
                if player_list[turn].ai!=True:
                    while True:
                        sell_t=input(f"You have to sell one of your title deeds or mortgage it. Which one do you want to sell or mortgage(Type the title deed name EXACTLY `):\n{player_list[turn].title_deeds}")
                        list_of_td = [title_deed[i].place for i in range(len(title_deed))]
                        list_of_rr = [train[i].name for i in range(len(train))]
                        list_of_utility = ["Electric Company", "Water Works"]
                        if sell_t in list_of_td or sell_t in list_of_rr or sell_t in list_of_utility:
                            break
                        else:
                            print("Type a valid input")
                            time.sleep(3)
                    mos = input("mortgage or sell: ")
                if mos == "mortgage":
                    #turns the value for mortgage to true
                    for i in range(len(title_deed)):
                        if title_deed[i].place==sell_t:
                            td_index=i
                            title_deed[i].mortgage = True
                            player_list[turn].balance += title_deed[i].calc_sell()*0.5
                            break
                    for i in range(len(train)):
                        if train[i].name==sell_t:
                            td_index=i
                            train[i].mortgage = True
                            player_list[turn].balance+=100
                            break
                    for i in range(len(utility)):
                        if utility[i].name==sell_t:
                            td_index=i
                            utility[i].mortgage = True
                            player_list[turn].balance += 75
                            break
                    list_of_td = [title_deed[i].place for i in range(len(title_deed))]
                    player_list[turn].mortgaged_p.append(sell_t)
                    player_list[turn].title_deeds.remove(sell_t)
                    try:
                        if sell_t in list_of_td[:5]:
                            player_list[turn].balance += 50*title_deed[list_of_td.index(sell_t)].num_house
                            player_list[turn].balance += 50*title_deed[list_of_td.index(sell_t)].num_hotel
                        elif sell_t in list_of_td[5:11]:
                            player_list[turn].balance += 100*title_deed[list_of_td.index(sell_t)].num_house
                            player_list[turn].balance += 100*title_deed[list_of_td.index(sell_t)].num_hotel
                        elif sell_t in list_of_td[11:17]:
                            player_list[turn].balance += 150*title_deed[list_of_td.index(sell_t)].num_house
                            player_list[turn].balance += 150*title_deed[list_of_td.index(sell_t)].num_hotel
                        elif sell_t in list_of_td[17:]:
                            player_list[turn].balance += 200*title_deed[list_of_td.index(sell_t)].num_house
                            player_list[turn].balance += 200*title_deed[list_of_td.index(sell_t)].num_hotel
                        player_list[turn].house -= title_deed[list_of_td.index(sell_t)].num_house
                        player_list[turn].hotel -= title_deed[list_of_td.index(sell_t)].num_hotel
                        title_deed[list_of_td.index(sell_t)].num_house = 0
                        title_deed[list_of_td.index(sell_t)].num_hotel = 0
                    except ValueError:
                        None
                    print(f"{sell_t} has been mortgaged and all buildings have been sold")
                    time.sleep(3)
                else:
                    leave_loop=False
                    #The problem is that sometimes a rr or utility is chosen instead of a title deed
                    for i in range(len(title_deed)):
                        if title_deed[i].place==sell_t:
                            td_index=i
                            leave_loop=True
                            break
                    for i in range(len(train)):
                        if train[i].name==sell_t:
                            td_index=i
                            leave_loop=True
                            break
                    for i in range(len(utility)):
                        if utility[i].name==sell_t:
                            td_index=i
                            leave_loop=True
                            break
                    if leave_loop==True:
                        break
                    player_list=selling_td(sell_t, "give", player_list, td_index)
                if player_list[turn].balance >= 0:
                    return player_list
                else:
                    print("You still have a negative balance!")
                    time.sleep(3)
            else:
                #Runs if the person is still in debt and has no title deeds to sell or mortgage
                print("Game Over")
                print()
                time.sleep(3)
                list_winners=[]
                #sells teh property of all players to see who has the highest balance
                for i in range(len(player_list)):
                    for x in range(len(player_list[i].title_deeds)):
                        player_list[i].balance+=selling_td(player_list[i].title_deeds[x], "sell", player_list, td_index)
                        list_winners.append(player_list[i].balance)
                sorted(list_winners)
                #calculates the player with teh highest balance
                for i in range(len(player_list)):
                    next_player=False
                    if player_list[i].balance==list_winners[0]:
                        print("First,", player_list[i].name)
                        next_player=True
                    if player_list[i].balance==list_winners[1] and next_player==True:
                        print("Second,", player_list[i].name)
                raise ValueError("Game Over")
    return player_list
#function that runs teh auction
def auction(player_list, name):
    player_move = 0
    auction_price = 0
    must_win = 0
    print(f"Auction for {name} has started")
    time.sleep(3)
    for i in range(len(title_deed)):
        if title_deed[i].place == name:
            break
    while True:
        #if the value auction in teh player class is true it runs
        #if teh player ever says no in teh bid, it will not ask tehm again
        if player_list[player_move].auction == True:
            if player_list[player_move].ai == True:
                bid = AI(player_list, "bid", auction_price, i, turn)
                if bid == "no":
                    print("asdf")
                if must_win > 3:
                    bid = "yes"
                    must_win = 0
            else:
                bid = input(f"Do you want to place a bid, {player_list[player_move].token}?(yes or no)(one person must say yes per round): ")
            if bid == "yes":
                if auction_price > player_list[player_move].balance:
                    print("You don't have enough money to bid")
                    time.sleep(3)
                    bid = "no"
                else:
                    while True:
                        try:
                            if player_list[player_move].ai == True:
                                auction_bid = auction_price + 50
                            else:
                                auction_bid = int(input(f"How much do you want to bid?(current price - ${auction_price}): "))
                            break
                        except ValueError:
                            print("Enter a valid input")
                            time.sleep(3)
                    if auction_bid < auction_price:
                        print("You can't bid lower than the current price")
                        time.sleep(3)
                    else:
                        auction_price = auction_bid
                        print(f"The price is now ${auction_price}")
            elif bid == "no":
                player_list[player_move].auction = False
        player_move += 1
        time.sleep(3)
        #it resets player_move if it is to high
        if player_move >= len(player_list):
            player_move = 0
            players_auction = 0
            #adds one to players_auction for every player that is still bidding
            for i in range(len(player_list)):
                if player_list[i].auction == True:
                    players_auction += 1
            #if there is only one bidder left, it runs
            if players_auction == 1:
                player_move -= 1
                print(f"{player_list[player_move].token} has won!")
                time.sleep(3)
                #gives the player teh title deed and takes the money away
                player_list[player_move].title_deeds.append(name)
                player_list[player_move].balance -= auction_price
                #resets the auction value in teh class
                for i in range(len(player_list)):
                    player_list[i].auction = True
                break
            #if everyone says no, it restarts teh auction.
            elif players_auction == 0:
                print("Someone must win!")
                must_win += 1
                for i in range(len(player_list)):
                    player_list[i].auction = True
    return player_list
#code for the ai
def AI(player_list, action, price, location, turn, reciver = ""):
    '''
    this ai works by seeing what space it is on
    then the action parameter will tell it what action to do
    each input will have a seperate action
    teh action is kinda like a key, telling teh ai what input it is being asked
    it will take in its current position and others to find teh appropriate move
    if teh ai will have $10 left when buying a title deed, it wont buy it
    but if it will have $200 left over, then it will
    except if multiple players have title deeds with high rent
    then it will buy if it has $500 over
    '''
    colorsets=[["Mediterranean Ave", "Baltic Ave"], ["Oriental Ave", "Vermont Ave", "Connecticut Ave"], ["St. Charles Place", "States Ave", "Virginia Ave"], ["St. James Place", "Tennessee Ave", "New York Ave"], ["Kentucky Ave", "Indiana Ave", "Illinois Ave"], ["Atlantic Ave", "Ventnor Ave", "Marvin Gardens"], ["Pacific Ave", "North Carolina Ave", "Pennsylvania Ave"], ["Park Place", "Boardwalk"]]
    if action == "bid":
        player_list[turn].title_deeds.append(title_deed[location].place)
        colorset = check_color_set(turn, True)
        player_list[turn].title_deeds.remove(title_deed[location].place)
        if colorset == True:
            return "yes"
        else:
            if num_turn < len(player_list)*4:
                if location in [9, 10, 11, 12, 13, 14]:
                    if player_list[turn].balance - price > 100:
                        return "yes"
                    else:
                        return "no"
                else:
                    if player_list[turn].balance - price > 150:
                        return "yes"
                    else:
                        return "no"
            else:
                if location in [9, 10, 11, 12, 13, 14]:
                    if player_list[turn].balance - price > 200:
                        return "yes"
                    else:
                        return "no"
                else:
                    if player_list[turn].balance - price > 250:
                        return "yes"
                    else:
                        return "no"
    if action == "sell_t":
        aimort_td=[]
        aimort_td_num=[]
        aimort_td_value=[]
        for i in range(len(player_list[turn].title_deeds)):
            aimort_td_value.append(player_list[turn].title_deeds[i])
            aimort_td_value.append(title_deed[i].calc_sell())
            aimort_td_num.append(title_deed[i].calc_sell())
            aimort_td.append(aimort_td_value)
            aimort_td_value=[]
        sorted(aimort_td_num)
        for j in range(len(aimort_td_num)):
            if aimort_td_num[-1]==aimort_td[j][1]:
                sell_t=aimort_td[j][0]
                break
        return sell_t
    if action == "td_to_give":
        while True:
            #lopttd = list_of_possible_trade_td
            lopttd = [i for i in player_list[turn].title_deeds]
            ########
            ai_td=[]
            ai_td_num=[]
            ai_td_value=[]
            for i in range(len(lopttd)):
                ai_td_value.append(lopttd[i])
                ai_td_value.append(title_deed[i].calc_sell())
                ai_td_num.append(title_deed[i].calc_sell())
                ai_td.append(ai_td_value)
                ai_td_value=[]
            sorted(ai_td_num)
            for j in range(len(ai_td_num)):
                if ai_td_num[-1]==ai_td[j][1]:
                    trade_t=ai_td[j][0]
                    break
            ########
            for i in range(len(player_list)):
                if reciver == player_list[i].token:
                    break
            player_list[i].title_deeds.append(trade_t)
            colorset = check_color_set(i, True)
            player_list[i].title_deeds.remove(trade_t)
            if colorset == False:
                return trade_t
            else:
                lopttd.remove(trade_t)
    #on property
    if player_list[turn].position in [1, 3, 6, 8, 9, 11, 13, 14, 16, 18, 19, 21, 23, 24, 26, 27, 29, 31, 32, 34, 37, 39]:
        #branch runs if the input is asking to buy a house or hotel
        if action == "buyh":
            if num_turn < len(player_list)*3:
                return "yes"
            else:
                #if teh amount of turns is more than 25, then it will know it is probobly in endgame
                if num_turn > 25:
                    if (player_list[turn].balance - price) < 400:
                        for loop in range(3):
                            aimort_td=[]
                            aimort_td_num=[]
                            aimort_td_value=[]
                            for i in range(len(player_list[turn].title_deeds)):
                                aimort_td_value.append(player_list[turn].title_deeds[i])
                                aimort_td_value.append(title_deed[i].calc_sell())
                                aimort_td_num.append(title_deed[i].calc_sell())
                                aimort_td.append(aimort_td_value)
                                aimort_td_value=[]
                            sorted(aimort_td_num)
                            for j in range(len(aimort_td_num)):
                                if aimort_td_num[-1]==aimort_td[j][1]:
                                    sell_t=aimort_td[j][0]
                                    break
                            for i in range(len(title_deed)):
                                if title_deed[i].place==sell_t:
                                    title_deed[i].mortgage = True
                                    player_list[turn].balance += title_deed[i].calc_sell()*0.5
                                    break
                            for i in range(len(train)):
                                if train[i].name==sell_t:
                                    train[i].mortgage = True
                                    player_list[turn].balance+=100
                                    break
                            for i in range(len(utility)):
                                if utility[i].name==sell_t:
                                    utility[i].mortgage = True
                                    player_list[turn].balance += 75
                                    break
                            list_of_td = [title_deed[i].place for i in range(len(title_deed))]
                            player_list[turn].mortgaged_p.append(sell_t)
                            player_list[turn].title_deeds.remove(sell_t)
                            try:
                                if sell_t in list_of_td[:5]:
                                    player_list[turn].balance += 50*title_deed[list_of_td.index(sell_t)].num_house
                                    player_list[turn].balance += 50*title_deed[list_of_td.index(sell_t)].num_hotel
                                elif sell_t in list_of_td[5:11]:
                                    player_list[turn].balance += 100*title_deed[list_of_td.index(sell_t)].num_house
                                    player_list[turn].balance += 100*title_deed[list_of_td.index(sell_t)].num_hotel
                                elif sell_t in list_of_td[11:17]:
                                    player_list[turn].balance += 150*title_deed[list_of_td.index(sell_t)].num_house
                                    player_list[turn].balance += 150*title_deed[list_of_td.index(sell_t)].num_hotel
                                elif sell_t in list_of_td[17:]:
                                    player_list[turn].balance += 200*title_deed[list_of_td.index(sell_t)].num_house
                                    player_list[turn].balance += 200*title_deed[list_of_td.index(sell_t)].num_hotel
                                player_list[turn].house -= title_deed[list_of_td.index(sell_t)].num_house
                                player_list[turn].hotel -= title_deed[list_of_td.index(sell_t)].num_hotel
                                title_deed[list_of_td.index(sell_t)].num_house = 0
                                title_deed[list_of_td.index(sell_t)].num_hotel = 0
                            except ValueError:
                                pass
                            if player_list[turn].balance>250:
                                return "yes"
                            else:
                                if loop == 3:
                                    return "no"
                else:
                    return "yes"
        if action == "buyp":

            if num_turn < len(player_list)*3:
                return "yes"
            if (title_deed[location].place in colorsets[4]) or (title_deed[location].place in colorsets[5]):
                if num_turn<15:
                    if player_list[turn].balance - price > 50:
                        return "yes"
                    else:
                        return "no"
                else:
                    if player_list[turn].balance - price > 150:
                        return "yes"
                    else:
                        return "no"
            else:
                if num_turn<15:
                    if player_list[turn].balance - price > 10:
                        return "yes"
                    else:
                        return "no"
                else:
                    if player_list[turn].balance - price > 200:
                        return "yes"
                    else:
                        return "no"
    #on special place
    if player_list[turn].position in [0, 10, 20, 30, 4, 38]:
        if action == "payojfc":
            if num_turn > 20:
                if player_list[turn].time_in_jail == 3:
                    return "yes"
                else:
                    return "no"
            else:
                return "yes"
    #on railroad
    if player_list[turn].position in [5, 15, 25, 35]:
        if action == "buyrr":
            if num_turn<len(player_list)*3:
                return "yes"
            else:
                if player_list[turn].position == 25:
                    if player_list[turn].balance-price>100:
                        return "yes"
                else:
                    if player_list[turn].balance-price>150:
                        return "yes"
                return "no"
    #on utility
    if player_list[turn].position in [12, 28]:
        if action == "buyu":
            if num_turn<len(player_list)*3:
                return "yes"
            else:
                if player_list[turn].position == 28:
                    if player_list[turn].balance-price>100:
                        return "yes"
                else:
                    if player_list[turn].balance-price>150:
                        return "yes"
                return "no"
#Creates an 11 by 11 array
visual_board=[["[ ]" for i in range(11)] for i in range(11)]
#Function sets the visual board
def set_board():
    #used to assign each value in teh array
    vb=["[🔒 10]", "[C 11]", "[💡 12]", "[S 13]", "[V 14]", "[🚂 15]", "[J 16]", "[📦 17]", "[T 18]", "[N 19]", "[🚗 20]",
        "[C 9]", "                                                    ", " ", " ", " ", " ", " ", " ", " ", " ", "[K 21]",
        "[V 8]", "                                                   ", " ", " ", " ", " ", " ", " ", " ", " ", "[❓ 22]",
        "[❓ 7]", "                                                   ", " ", " ", " ", " ", " ", " ", " ", " ", "[I 23]",
        "[O 6]", "                                                    ", " ", " ", " ", " ", " ", " ", " ", " ", "[I 24]",
        "[🚂 5]", "                                                  ", " ", " ", " ", " ", " ", " ", " ", " ", "[🚂 25]",
        "[💰 4]", "                                                   ", " ", " ", " ", " ", " ", " ", " ", " ", "[A 26]",
        "[B 3]", "                                                    ", " ", " ", " ", " ", " ", " ", " ", " ", "[V 27]",
        "[📦 2]", "                                                  ", " ", " ", " ", " ", " ", " ", " ", " ", "[🚿 28]",
        "[M 1]", "                                                    ", " ", " ", " ", " ", " ", " ", " ", " ", "[M 29]",
        "[➢  0]", "[B 39]", "[💍 38]", "[P 37]", "[❓ 36]", "[🚂 35]", "[P 34]", "[📦 33]", "[N 32]", "[P 31]", "[🚓 30]",]
    a=0
    #sets the value in teh array
    for i in range(11):
        for j in range(11):
            visual_board[i][j]=vb[a]
            a+=1
set_board()
#prints the visual board
def print_board():
    for i in range(len(visual_board)):
        print("".join([str(x) for x in visual_board[i]]))
board=[]
#makes the board that is used by teh computer to calculate
def make_bts_board():
    #things chooses which title deed goes into the square1F512
    thing=0
    thing1=0
    thing2=0
    thing3=0
    thing4=0
    for i in range(40):
        #makes it so board doesnt go out of range
        board.append(i)
        #places the spot for title deeds
        if i in [1, 3, 6, 8, 9, 11, 13, 14, 16, 18, 19, 21, 23, 24, 26, 27, 29, 31, 32, 34, 37, 39]:
            board[i]=title_deed[thing].place
            thing+=1
        #places the utilities
        if i in [12, 28]:
            board[i]=utility[thing1].name
            thing1+=1
        #places the community chests
        if i in [2, 17, 33]:
            random.shuffle(community_chest)
            board[i]=community_chest[thing2].name
            thing2+=1
        #places chance cards
        if i in [7, 22, 36]:
            random.shuffle(chance_card)
            board[i]=chance_card[thing3].name
            thing3+=1
        #places Railroads
        if i in [5, 15, 25, 35]:
            board[i]=train[thing4].name
            thing4+=1
    #places all teh special places go, jail, etc.
    board[0]=special[0].name
    board[10]=special[1].name
    board[20]=special[2].name
    board[30]=special[3].name
    board[4]=special[4].name
    board[38]=special[5].name
    return board
#makes the moves
turn=1
def moves(turn_thing):

    #prints ten lines inbetween each turn
    for i in range(10):
        print("")
    #flips between players
    if turn_thing%player_num==0:
        turn=0
    elif turn_thing%player_num==1:
        turn=1
    elif turn_thing%player_num==2:
        turn=2
    elif turn_thing%player_num==3:
        turn=3
    elif turn_thing%player_num==4:
        turn=4
    else:
        turn=4
    turn_thing+=1
    ask_save="no"
    #prints necesarry information
    print(f"It is {player_list[turn].token}'s turn.")
    print(f"You have ${player_list[turn].balance}")
    print(f"You own {player_list[turn].title_deeds}\n")
    print_board()
    time.sleep(2)
    #asks if teh user wants to do an action and calls teh corresponding function
    if not player_list[turn].ai:
        make_action = input("\nDo you want to make an action(save, trade, unmortgage)(yes or no)?: ")
        if make_action == "yes":
            action_to_make = input("What action do you want to make(save, trade, unmortgage): ")
            if action_to_make == "save":
                ask_save=input("Do you want to save the game(yes or no) or delete a save file?(delete or no): ")
                if ask_save=="yes" and not player_list[turn].ai:
                    while True:
                        print(save_files)
                        save_name = input("What do you want to save it as or leave to leave?: ")
                        if save_name == "leave":
                            break
                        if save_name in save_files:
                            if input("You already have a save called that. Do you want to overwite save?: ") == "yes":
                                save(save_name)
                                break
                        else:
                            save(save_name)
                            save_files.append(save_name)
                            break
                if ask_save=="delete":
                    print(save_files)
                    remove_file = input("What file do you want to remove?: ")
                    save_files.remove(remove_file)
                    time.sleep(0)
            if action_to_make == "trade":
                list_of_players = []
                for i in range(len(player_list)):
                    list_of_players.append(player_list[i].token)
                while True:
                    list_of_tradable_players = []
                    for i in range(len(list_of_players)):
                        if player_list[i].token != player_list[turn].token:
                            list_of_tradable_players.append(player_list[i].token)
                    print(list_of_tradable_players)
                    trade_to = input("Who recives the card?: ")
                    if trade_to in list_of_players:
                        break
                    else:
                        print("Type a valid input")
                        time.sleep(3)
                broke(turn, trade_to, player_list, True)
            elif action_to_make == "unmortgage":
                unmort_p = []
                for i in range(len(player_list)):
                    if title_deed[i].mortgage == True:
                        unmort_p.append(title_deed[i])
                while True:
                    print(unmort_p)
                    unmort = input("What property do you want to unmortgage?: ")
                    try:
                        if unmort_p[unmort_p.index(unmort)].buy*0.1 > player_list[turn].balance:
                            print("You don't have enough money to unmortgage it")
                            time.sleep(3)
                        else:
                            title_deed[unmort_p.index(unmort)].mortgage = False
                            player_list[turn].title_deed.append(unmort)
                            player_list[turn].mortgaged_p.remove(unmort)
                            player_list[turn].balance -= unmort_p[unmort_p.index(unmort)].buy*0.1
                            time.sleep(3)
                        break
                    except IndexError:
                        print("Type a valid input")
                        time.sleep(3)
    save_file("save_file_of_save_files.txt", save_files)
    ##########
    player_list[turn].title_deeds=list(set(player_list[turn].title_deeds))
    #rolls dice
    #I need to dice because when leaving jail, both dice need ot be the same.
    dice1=random.randint(1, 6)
    dice2=random.randint(1, 6)
    dice=dice1+dice2
    if player_list[turn].jail!=True:
        #used to make the print statement grammaticly correct
        add_n=""
        if dice==8 or dice==11:
            add_n="n"
        print(f"The dice was a{add_n} {dice}")
        copyofpos=player_list[turn].position
        time.sleep(3)
        player_list[turn].position+=dice
        #used to move the corresponding moves if it passes go
        if player_list[turn].position>39:
            player_list[turn].position -= copyofpos
        print(f"You are on square {player_list[turn].position}")
        #sees if teh player passes go and gives $200
        if (copyofpos>27 and (player_list[turn].position>=0 and player_list[turn].position<12)) or player_list[turn].position == 0:
            print("You past Go. You got $200")
            player_list[turn].balance+=200
    check_color_set(turn)
    return player_list, turn, dice, dice1, dice2
#ilotd = if land on title deed
def ilotd():
    #function for possible actions when landing on a property
    def property_land(place, location, player_list, title_deed):
        location-=1
        if title_deed[location].mortgage != True:
            thing=True
            #makes a list of all owned title deeds
            list_of_owned_td = []
            for z in range(len(player_list)):
                for y in range(len(player_list[z].title_deeds)):
                    list_of_owned_td.append(player_list[z].title_deeds[y])
            if place in list_of_owned_td:
                #if teh property is owned but not by teh player whos turn it is
                if not (place in player_list[turn].title_deeds):
                    print(f"You must pay rent on {place}\nRent is ${title_deed[location].calc_rent()}.")
                    time.sleep(3)
                    rent_to_pay = title_deed[location].calc_rent()
                    #doubles rent if it is a colorset
                    if title_deed[location].colorset == True:
                        rent_to_pay = (title_deed[location].calc_rent()) * 2
                    player_list[turn].balance-=rent_to_pay
                    if player_list[turn].balance < 0:
                        player_list = broke(turn, 1, player_list, False)
                    #gives teh rent to teh person who owns teh title deed
                    for j in range(len(player_list)):
                        if place in list_of_owned_td and j != turn:
                            for x in range(len(player_list)):
                                if place in player_list[x].title_deeds:
                                    player_list[x].balance+=rent_to_pay

                    return player_list
                else:
                    #if teh player owns teh title deed, they can buy a house or hotel
                    buyh="no"

                    if player_list[turn].ai == True:
                        buyh = AI(player_list, "buyh", title_deed[location].house_buy, location, turn)
                    else:
                        buyh = input("Do you want to buy a house or a hotel(yes or no)?: ")
                    if title_deed[location].colorset==False:
                        print("You need to own the color set for this title deed before you can buy a house or a hotel")
                        time.sleep(3)
                        return player_list
                    if buyh=="yes":
                        if player_list[turn].balance<title_deed[location].house_buy:
                            print("You don't have enough money")
                            return player_list
                        hotel_or_house="no"
                        if player_list[turn].ai!=True:
                            hotel_or_house=input("Which one(house or hotel)?: ")
                        if hotel_or_house=="house" or (player_list[turn].ai==True):
                            #if teh player has 4 houses, it asks if they want a hotel instead
                            if title_deed[location].num_house==4:
                                if player_list[turn].ai!=True:
                                    buyh=input("You bought the maximum amount of house. Do you want to buy a hotel instead(yes or no)?: ")
                                if buyh=="yes":
                                    hotel_or_house="hotel"
                            else:
                                print("You bought a house")
                                #adds a house
                                title_deed[location].num_house+=1
                                player_list[turn].balance-=title_deed[location].house_buy
                                player_list[turn].house+=1
                        if hotel_or_house=="hotel":
                            if title_deed[location].num_house!=4:
                                print("You need four houses on the property until you can buy a hotel")
                            elif title_deed[location].num_hotel >= 1:
                                print("You already have a hotel at that location")
                            else:
                                print("You bought a hotel")
                                #gives them a hotel and removes the hosues
                                title_deed[location].num_hotel+=1
                                player_list[turn].balance-=title_deed[location-1].hotel_buy
                                player_list[turn].balance-=4
                                player_list[turn].hotel+=1
                return player_list
            else:
                #if teh title deed is not owned, they can buy it
                buyp="no"
                if player_list[turn].ai == True:
                    buyp = AI(player_list, "buyp", title_deed[location].buy, location, turn)
                if player_list[turn].ai!=True:
                    buyp=input(f"Do you want to buy {place}({title_deed[location].buy})(yes or no)?: ")
                if buyp=="yes":
                    if player_list[turn].balance<title_deed[location].buy:
                        print("You don't have enough money")
                    else:
                        print(f"You bought {place}")
                        player_list[turn].title_deeds.append(place)
                        player_list[turn].balance-=title_deed[location].buy
                else:
                    #auctions off teh title deed if tehy dont want it
                    print(f"{place} is being auctioned off")
                    time.sleep(3)
                    player_list = auction(player_list, place)
                #checks if they player has a colorset after buying the property
                title_deed, player_list=check_color_set(turn)
                return player_list
        else:
            print("You landed on a property that is mortgaged. Lucky you.")
            time.sleep(3)
        return player_list
    #it firsts looks what color the player is on and then the property
    #brown
    if player_list[turn].position in [1, 3]:
        if player_list[turn].position==1:
            property_land("Mediterranean Ave", 1, player_list, title_deed)
            return player_list
        if player_list[turn].position==3:
            property_land("Baltic Ave", 2, player_list, title_deed)
            return player_list
        return player_list
    #light blue
    if player_list[turn].position in [6, 8, 9]:
        if player_list[turn].position==6:
            property_land("Oriental Ave", 3, player_list, title_deed)
            return player_list
        if player_list[turn].position==8:
            property_land("Vermont Ave", 4, player_list, title_deed)
            return player_list
        if player_list[turn].position==9:
            property_land("Connecticut Ave", 5, player_list, title_deed)
            return player_list
        return player_list
    #pink
    if player_list[turn].position in [11, 13, 14]:
        if player_list[turn].position==11:
            property_land("St. Charles Place", 6, player_list, title_deed)
            return player_list
        if player_list[turn].position==13:
            property_land("States Ave", 7, player_list, title_deed)
            return player_list
        if player_list[turn].position==14:
            property_land("Virginia Ave", 8, player_list, title_deed)
            return player_list
        return player_list
    #orange
    if player_list[turn].position in [16, 18, 19]:
        if player_list[turn].position==16:
            property_land("St. James Place", 9, player_list, title_deed)
            return player_list
        if player_list[turn].position==18:
            property_land("Tennessee Ave", 10, player_list, title_deed)
            return player_list
        if player_list[turn].position==19:
            property_land("New York Ave", 11, player_list, title_deed)
            return player_list
        return player_list
    #red
    if player_list[turn].position in [21, 23, 24]:
        if player_list[turn].position==21:
            property_land("Kentucky Ave", 12, player_list, title_deed)
            return player_list
        if player_list[turn].position==23:
            property_land("Indiana Ave", 13, player_list, title_deed)
            return player_list
        if player_list[turn].position==24:
            property_land("Illinois Ave", 14, player_list, title_deed)
            return player_list
        return player_list
    #yellow
    if player_list[turn].position in [26, 27, 29]:
        if player_list[turn].position==26:
            property_land("Atlantic Ave", 15, player_list, title_deed)
            return player_list
        if player_list[turn].position==27:
            property_land("Ventnor Ave", 16, player_list, title_deed)
            return player_list
        if player_list[turn].position==29:
            property_land("Marvin Gardens", 17, player_list, title_deed)
            return player_list
        return player_list
    #green
    if player_list[turn].position in [31, 32, 34]:
        if player_list[turn].position==31:
            property_land("Pacific Ave", 18, player_list, title_deed)
            return player_list
        if player_list[turn].position==32:
            property_land("North Carolina Ave", 19, player_list, title_deed)
            return player_list
        if player_list[turn].position==34:
            property_land("Pennsylvania Ave", 20, player_list, title_deed)
            return player_list
        return player_list
    #blue
    if player_list[turn].position in [37, 39]:
        if player_list[turn].position==37:
            property_land("Park Place", 21, player_list, title_deed)
            return player_list
        if player_list[turn].position==39:
            property_land("Boardwalk", 22, player_list, title_deed)
            return player_list
        return player_list
#ilocc=if land on chance card/community chest
def ilocc():
    #see whether it is a chance or community chest
    #chest
    if player_list[turn].position in [2, 17, 33]:
        #picks a card if they land on a space with commynity chest
        print("You landed on community chest")
        chest_card=random.choice(community_chest)
        time.sleep(3)
        print(chest_card.name)
        #does special action if needed
        player_list[turn].balance+=chest_card.money
        if chest_card.jail_card==True:
            player_list[turn].jail_card=True
        if chest_card.place=="Go":
            player_list[turn].position=0
    #chance
    if player_list[turn].position in [7, 22, 36]:
        #same thing but with chance cards
        print("You landed on chance card")
        chance=random.choice(chance_card)
        time.sleep(3)
        print(chance.name)
        player_list[turn].balance+=chance.money
        if chance.jail_card==True:
            player_list[turn].jail_card=True
        #moves player if it tells tehm to move to a title deed
        if chance.place=="St. Charles": player_list[turn].position=11
        if chance.place=="Train Station": player_list[turn].position=15
        if chance.place=="Illinois Ave": player_list[turn].position=24
        if chance.place=="Go": player_list[turn].position=0
        if chance.place=="Placeholder for nearest utility":
            #moves player to nearest utility
            if player_list[turn].position==7:
                player_list[turn].position=12
            else:
                player_list[turn].position=28
        if chance.place=="Jail":
            player_list[turn].position=10
            player_list[turn].jail=True
        if chance.place=="Boardwalk": player_list[turn].position=39
        if chance.place=="placeholder for player position minus 3 spaces": player_list[turn].position=player_list[turn].position-3
        if chance.place=="Placeholder for nearest railroad":
            #same thing as utility but with railroads
            if player_list[turn].position==7:
                player_list[turn].position=5
            if player_list[turn].position==22:
                player_list[turn].position=25
            if player_list[turn].position==36:
                player_list[turn].position=35
    return player_list
#ilosp=if land on special place
#speacial place - jail, free parking, income and luxury tax
def ilosp(player_list):
    if player_list[turn].position==10:
        if player_list[turn].jail!=True:
            print("You are visiting jail")
        else:
            #runs if they are in jail
            print("You are in jail")
            time.sleep(3)
            jail_input = True
            if dice1==dice2:
                print("You rolled the same number on each dice!")
                time.sleep(3)
                player_list[turn].jail=False
                jail_input = False

            payojfc="no"
            #allows teh player to get out of jail
            if player_list[turn].ai == True and jail_input == True:
                payojfc = AI(player_list, "payojfc", 50, 0, turn)
            if player_list[turn].ai!=True and jail_input == True:
                payojfc=input("Do you want to use your get out of jail free card or pay $50(yes or no)?: ")
            if not ((payojfc=="yes" or player_list[turn].ai==True) and jail_input == True):
                if player_list[turn].time_in_jail == 3:
                    print("You have been in jail for too long. You must pay $50 for use your get out of jail free card")
                    time.sleep(3)
                    payojfc = "yes"
                else:
                    player_list[turn].time_in_jail +=1
            if (payojfc=="yes" or player_list[turn].ai==True) and jail_input == True:
                if player_list[turn].jail_card==False:
                    if player_list[turn].balance<50:
                        print("You don't have a get out of jail free card nor do you have enough money")
                    else:
                        print("You paid $50")
                        player_list[turn].jail=False
                        player_list[turn].balance-=50
                        player_list[turn].time_in_jail = 0
                else:
                    print("You used your get out of jail free card.")
                    player_list[turn].jail=False
                    player_list[turn].jail_card=False
                    player_list[turn].time_in_jail = 0
    #does teh action based on place that is landed
    if player_list[turn].position==20:
        print("You are in free parking")
    if player_list[turn].position==30:
        print("Go to jail")
        player_list[turn].jail=True
        player_list[turn].position=10
    if player_list[turn].position==4:
        print("Pay income tax of $200")
        player_list[turn].balance-=200
    if player_list[turn].position==38:
        print("Pay luxury tax of $100")
        player_list[turn].balance-=100
    while True:
        #checks to see if teh player is broke after paying the taxes
        player_list = broke(turn, 1, player_list, False)
        if player_list[turn].balance>=0:
            break
    return player_list
#ilorr=if land on railroad
def ilorr():
    def railroad_action(name, player_list):
        list_of_owned_rr = []
        list_of_trains = [train[i].name for i in range(4)]
        #checks to see if a rr is owned
        if train[list_of_trains.index(name)].mortgage == False:
            for z in range(len(player_list)):
                for y in range(len(player_list[z].title_deeds)):
                    list_of_owned_rr.append(player_list[z].title_deeds[y])
            if name in list_of_owned_rr:
                if name not in player_list[turn].title_deeds:
                    print("You must pay for train services")
                    time.sleep(3)
                    print("You pay $25 per train station owned")
                    time.sleep(3)
                    train_owned=0
                    #adds 1 per railroad owned
                    for i in range(len(player_list)):
                        if "Reading Railroad" in player_list[i].title_deeds: train_owned+=1
                        if "Pennsylvania Railroad" in player_list[i].title_deeds: train_owned+=1
                        if "B. & O. Railroad" in player_list[i].title_deeds: train_owned+=1
                        if "Short Line" in player_list[i].title_deeds: train_owned+=1
                    player_list[turn].balance-=25*train_owned
                    while True:
                        #checks to see if they are broke
                        player_list = broke(turn, 1, player_list, False)
                        if player_list[turn].balance>0:
                            break
                    for i in range(len(player_list)):
                        if name in player_list[i].title_deeds and i!=turn:
                            player_list[i].balance+=25*train_owned
                    return player_list
            else:
                #lets player buy a rr
                buyrr="no"
                if player_list[turn].ai == True:
                    buyrr = AI(player_list, "buyrr", 150, 0, turn)
                if player_list[turn].ai!=True:
                    buyrr=input(f"Do you want to buy {name}(yes or no)?: ")
                if buyrr=="yes" or (player_list[turn].ai==True and player_list[turn].balance-150>200):
                    if player_list[turn].balance<150:
                        print("You don't have enough money")
                        time.sleep(3)
                    else:
                        print(f"You bought {name} for $150")
                        player_list[turn].balance-=150
                        player_list[turn].title_deeds.append(name)
                    return player_list
            return player_list
        else:
            print("This railroad is mortgaged")
            time.sleep(3)

    if player_list[turn].position==5:
        railroad_action("Reading Railroad", player_list)
    if player_list[turn].position==15:
        railroad_action("Pennsylvania Railroad", player_list)
    if player_list[turn].position==25:
        railroad_action("B. & O. Railroad", player_list)
    if player_list[turn].position==35:
        railroad_action("Short Line", player_list)
    return player_list
#ilou=if land on utility
def ilou(dice):
    def utility_action(name, dice, player_list):
        list_of_owned_u = []
        list_of_utility = [utility[i].name for i in range(2)]
        if utility[list_of_utility.index(name)].mortgage == False:
            for z in range(len(player_list)):
                for y in range(len(player_list[z].title_deeds)):
                    list_of_owned_u.append(player_list[z].title_deeds[y])
            if name in list_of_owned_u:
                if name not in player_list[turn].title_deeds:
                    print("You must pay to utilities")
                    time.sleep(3)
                    print("You pay $4 per spaces moved")
                    time.sleep(3)
                    player_list[turn].balance-=4*dice
                    while True:
                        player_list = broke(turn, 1, player_list, False)
                        if player_list[turn].balance>0:
                            break
                    for i in range(len(player_list)):
                        if name in player_list[i].title_deeds and i!=turn:
                            player_list[i].balance+=4*dice
                    return player_list
            else:
                buyu="no"
                if player_list[turn].ai == True:
                    buyu = AI(player_list, "buyu", 150, 0, turn)
                if player_list[turn].ai!=True:
                    buyu=input(f"Do you want to buy {name}(yes or no)?: ")
                if buyu=="yes" or (player_list[turn].ai==True and player_list[turn].balance-150>200):
                    if player_list[turn].balance<150:
                        print("You don't have enough money")
                        time.sleep(3)
                    else:
                        print(f"You bought {name} for $150")
                        time.sleep(3)
                        player_list[turn].title_deeds.append(name)
                    return player_list
            return player_list
        else:
            print("This utility has been mortgaged")
            time.sleep(3)
    if player_list[turn].position==12:
        utility_action("Electric Company", dice, player_list)
    if player_list[turn].position==28:
        utility_action("Water Works", dice, player_list)
    return player_list
board=make_bts_board()
num_turn=0
while True:
    #runs the game
    depth = int(30/len(player_list))
    title_deed, player_list = check_color_set(turn)
    player_list, turn, dice, dice1, dice2=moves(turn_thing)
    turn_thing+=1
    #lands on chance or chest
    if player_list[turn].position in [2, 7, 17, 22, 33, 36]:
        player_list=ilocc()
    #lands on property
    if player_list[turn].position in [1, 3, 6, 8, 9, 11, 13, 14, 16, 18, 19, 21, 23, 24, 26, 27, 29, 31, 32, 34, 37, 39]:
        player_list=ilotd()
    #lands on special place
    if player_list[turn].position in [0, 10, 20, 30, 4, 38]:
        player_list=ilosp(player_list)
    #lands on railroad
    if player_list[turn].position in [5, 15, 25, 35]:
        player_list=ilorr()
    #land on utility
    if player_list[turn].position in [12, 28]:
        player_list=ilou(dice)
    if player_list[turn].balance < 0:
        player_list = broke(turn, 1, player_list, True)
    num_turn+=1
    print("Turns:", num_turn)
    time.sleep(2)