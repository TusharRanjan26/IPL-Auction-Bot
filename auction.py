import pandas as pd
import numpy as np
import random

batsmen = pd.read_csv("FINAL DATASET - Batsman.csv")
bowlers = pd.read_csv("FINAL DATASET - Bowlers.csv")
allRounders = pd.read_csv("FINAL DATASET - All Rounders.csv")
wicketKeepers = pd.read_csv("FINAL DATASET - Wicket Keepers.csv")

class team:
        Bat = []
        BatPrice = []
        Bowl = []
        BowlPrice = []
        allR = []
        allRPrice = []
        wk = []
        wkPrice = []
        purse = 40
        strength = 0
        foreign = 0

def batRating(avg, sr, age, matches, stars, base):
    avgRate = 2*(round(avg))
    srRate = round(sr-100)
    ageRate = 2*(-abs(age-30))
    matchesRate = 2 * round(matches/10)
    starsRate = 10*stars
    baseRate = 20*base
    return avgRate + srRate + ageRate + matchesRate + starsRate + baseRate

def wkBatRating(avg, sr, age, matches, stars, base , catches, stumpings):
    avgRate = 2*(round(avg))
    srRate = (round(sr-100))
    ageRate = 2*(-abs(age-30))
    matchesRate = 2 * round(matches/10)
    starsRate = 10*stars
    baseRate = 20*base
    catchRate = round(catches/10)
    stumpRate = round(stumpings/5)
    return avgRate + srRate + ageRate + matchesRate + starsRate + baseRate + catchRate + stumpRate

def bowlRating(bowlAvg, bowlSr, age, matches, stars, base):
    avgRate = -2*(round(bowlAvg))
    srRate = -(round(bowlSr-100))
    ageRate = -2*(age - 25)
    matchesRate = 2 * round(matches/10)
    starsRate = 10*stars
    baseRate = 20*base
    return avgRate + srRate + ageRate + matchesRate + starsRate + baseRate

def arRating(bowlAvg, bowlSr, batAvg, batSr, age, matches, stars, base):
    avgRate = -2*(round(bowlAvg))
    srRate = -(round(bowlSr-100))
    batAvgRate = 2*(round(batAvg))
    batSrRate = round(batSr-100)
    ageRate = -2*(age - 25)
    matchesRate = 2 * round(matches/10)
    starsRate = 10*stars
    baseRate = 20*base
    return avgRate + srRate + batAvgRate + batSrRate + ageRate + matchesRate + starsRate + baseRate


"""

batsmen.info() #41 max 286 min 110
bowlers.info() #31 max 185 min 49
allRounders.info() #17 max 318 min 96
wicketKeepers.info() #18 max 297 min 95 

for i in range(0,41):
    print(batRating(batsmen.iloc[i,9], batsmen.iloc[i,11], batsmen.iloc[i,3], batsmen.iloc[i,5], batsmen.iloc[i,1], batsmen.iloc[i,17]))
print("\n")
for i in range(0,31):
    print(bowlRating(bowlers.iloc[i,11], bowlers.iloc[i,13],bowlers.iloc[i,3], bowlers.iloc[i,5], bowlers.iloc[i,1], bowlers.iloc[i,16]))
print("\n")
for i in range(0,17):
    print(arRating(allRounders.iloc[i,22], allRounders.iloc[i,24], allRounders.iloc[i,9], allRounders.iloc[i,11], allRounders.iloc[i,3], allRounders.iloc[i,5], allRounders.iloc[i,1], allRounders.iloc[i,27]))
print("\n")
for i in range(0,18):
    print(wkBatRating(wicketKeepers.iloc[i,9], wicketKeepers.iloc[i,11], wicketKeepers.iloc[i,3], wicketKeepers.iloc[i,5], wicketKeepers.iloc[i,1], wicketKeepers.iloc[i,20], wicketKeepers.iloc[i,18], wicketKeepers.iloc[i,19]))
"""
def maxBatBid(rating):
    if rating < 200 :
        return 0
    else:
        return 2 + round((rating-200)/10)
    
def maxBowlBid(rating):
    if rating < 100 :
        return 0
    else:
        return 2 + round((rating-100)/10)
    
def maxArBid(rating):
    if rating < 200 :
        return 0
    else:
        return 2 + round((rating-220)/10)
    
def maxWkBid(rating):
    if rating < 200 :
        return 0
    else:
        return 2 + round((rating-220)/10)
"""    
for i in range(0,40):
    print(batsmen.iloc[i,0] , " ")
    print(maxBatBid(batRating(batsmen.iloc[i,9], batsmen.iloc[i,11], batsmen.iloc[i,3], batsmen.iloc[i,5], batsmen.iloc[i,1], batsmen.iloc[i,17])))
    print("\n") 
"""
# Batsman Auction
random_bat = random.sample(range(41),41)
for i in random_bat:
    print(batsmen.iloc[i,0] , " " , batsmen.iloc[i,17] , "\n")
    current_bid = batsmen.iloc[i,17]
    prompt= "start"
    if (len(team.Bat) == 3):
            break
    while (prompt != "out"):
        prompt = input("write bid to bid, out to end : ")
        bidAmount = input("Enter Bid Amount : ")

        #Price Logic

        if (len(team.BatPrice) == 1):
            if (team.BatPrice[0] + current_bid > 13):
                break

        if (len(team.BatPrice) == 2):
            if(team.BatPrice[0] + team.BatPrice[1] + current_bid > 16):
                break

        if (len(team.BatPrice) == 1):
            if (team.BatPrice[0] + maxBatBid(batRating(batsmen.iloc[i,9], batsmen.iloc[i,11], batsmen.iloc[i,3], batsmen.iloc[i,5], batsmen.iloc[i,1], batsmen.iloc[i,17])) < 8 ):
                break

        if (len(team.BatPrice) == 2):
            if(team.BatPrice[0] + team.BatPrice[1] + maxBatBid(batRating(batsmen.iloc[i,9], batsmen.iloc[i,11], batsmen.iloc[i,3], batsmen.iloc[i,5], batsmen.iloc[i,1], batsmen.iloc[i,17])) < 14 ):
                break

        if ((batsmen.iloc[i,2] == "F") and len(team.foreign == 2)):
            break
        if (prompt == "out"):
            final_bid = current_bid
            team.Bat.append(batsmen.iloc[i,0])
            team.BatPrice.append(final_bid)
            team.purse -= final_bid
            team.strength = team.strength + 1
            if (batsmen.iloc[i,2] == "F"):
                team.foreign = team.foreign + 1
            print("we have bought " , batsmen.iloc[i,0] , " for " , final_bid)
        else:
            current_bid += bidAmount
            print("current bid : " , current_bid)

        if (current_bid > maxBatBid(batRating(batsmen.iloc[i,9], batsmen.iloc[i,11], batsmen.iloc[i,3], batsmen.iloc[i,5], batsmen.iloc[i,1], batsmen.iloc[i,17]))):
            final_bid = 0
            break
        if (current_bid > team.purse):
            break
        if (team.purse - current_bid < 24):
            break
        if (len(team.Bat) == 3):
            break
        for j in range(len(team.Bat)):
            print("batsman : " , team.Bat[j])
        print("current purse : " , team.purse)

#Bowler Auction
random_bowl = random.sample(range(31),31)
for i in random_bowl:
    print(bowlers.iloc[i,0] , " " , bowlers.iloc[i,16] , "\n")
    current_bid = bowlers.iloc[i,16]
    prompt= "start"
    if (len(team.Bowl) == 2):
            break
    while (prompt != "out"):
        prompt = input("write bid to bid, out to end : ")
        bidAmount = input("Enter Bid Amount : ")

        #Price Logic

        if (len(team.BowlPrice) == 1):
            if (team.BowlPrice[0] + current_bid > 12):
                break

        if (len(team.BowlPrice) == 1):
            if (team.BatPrice[0] + maxBowlBid(bowlRating(bowlers.iloc[i,11], bowlers.iloc[i,13], bowlers.iloc[i,3], bowlers.iloc[i,5], bowlers.iloc[i,1], bowlers.iloc[i,16])) < 9 ):
                break

        if ((bowlers.iloc[i,2] == "F") and len(team.foreign == 3)):
            break
        if (prompt == "out"):
            final_bid = current_bid
            team.Bowl.append(bowlers.iloc[i,0])
            team.BatPrice.append(final_bid)
            team.purse -= final_bid
            team.strength = team.strength + 1
            if (bowlers.iloc[i,2] == "F"):
                team.foreign = team.foreign + 1
            print("we have bought " , bowlers.iloc[i,0] , " for " , final_bid)
        else:
            current_bid += bidAmount
            print("current bid : " , current_bid)

        if (current_bid > maxBowlBid(bowlRating(bowlers.iloc[i,11], bowlers.iloc[i,13], bowlers.iloc[i,3], bowlers.iloc[i,5], bowlers.iloc[i,1], bowlers.iloc[i,16]))):
            final_bid = 0
            break
        if (current_bid > team.purse):
            break
        if (team.purse - current_bid < 12):
            break
        if (len(team.Bowl) == 2):
            break
        for z in range(len(team.Bowl)):
            print("bowler : " , team.Bowl[z])
        print("current purse : " , team.purse)

#WicketKeeper Auction

random_wk = random.sample(range(18),18)
for i in random_wk:
    print(wicketKeepers.iloc[i,0] , " " , wicketKeepers.iloc[i,20] , "\n")
    current_bid = wicketKeepers.iloc[i,20]
    prompt= "start"
    if (len(team.wk) == 1):
            break
    while (prompt != "out"):
        prompt = input("write bid to bid, out to end : ")
        bidAmount = input("Enter Bid Amount : ")

        #Price Logic

        if (maxWkBid(wkBatRating(wicketKeepers.iloc[i,9], wicketKeepers.iloc[i,11], wicketKeepers.iloc[i,3], wicketKeepers.iloc[i,5], wicketKeepers.iloc[i,1], wicketKeepers.iloc[i,20], wicketKeepers.iloc[i,18], wicketKeepers.iloc[i,19]))):
            break

        if (current_bid > 6):
            break

        if ((wicketKeepers.iloc[i,2] == "F") and len(team.foreign == 3)):
            break
        if (prompt == "out"):
            final_bid = current_bid
            team.wk.append(wicketKeepers.iloc[i,0])
            team.wkPrice.append(final_bid)
            team.purse -= final_bid
            team.strength = team.strength + 1
            if (wicketKeepers.iloc[i,2] == "F"):
                team.foreign = team.foreign + 1
            print("we have bought " , wicketKeepers.iloc[i,0] , " for " , final_bid)
        else:
            current_bid += bidAmount
            print("current bid : " , current_bid)

        if (current_bid > maxWkBid(wkBatRating(wicketKeepers.iloc[i,9], wicketKeepers.iloc[i,11], wicketKeepers.iloc[i,3], wicketKeepers.iloc[i,5], wicketKeepers.iloc[i,1], wicketKeepers.iloc[i,20], wicketKeepers.iloc[i,18], wicketKeepers.iloc[i,19]))):
            final_bid = 0
            break
        if (current_bid > team.purse):
            break
        if (team.purse - current_bid < 6):
            break
        if (len(team.wk) == 1):
            break
        for z in range(len(team.wk)):
            print("wicket keeper : " , team.wk[z])
        print("current purse : " , team.purse)

#AllRounder Auction

random_allR = random.sample(range(17),17)
for i in random_allR:
    print(allRounders.iloc[i,0] , " " , allRounders.iloc[i,27] , "\n")
    current_bid = allRounders.iloc[i,27]
    prompt= "start"
    if (len(team.allR) == 1):
            break
    while (prompt != "out"):
        prompt = input("write bid to bid, out to end : ")
        bidAmount = input("Enter Bid Amount : ")

        #Price Logic

        if (maxArBid(arRating(allRounders.iloc[i,22], allRounders.iloc[i,24], allRounders.iloc[i,9], allRounders.iloc[i,11], allRounders.iloc[i,3], allRounders.iloc[i,5], allRounders.iloc[i,1], allRounders.iloc[i,27])) < 3):
            break

        if (current_bid > 6):
            break

        if ((allRounders.iloc[i,2] == "F") and len(team.foreign == 4)):
            break
        if (prompt == "out"):
            final_bid = current_bid
            team.allR.append(allRounders.iloc[i,0])
            team.allR.append(final_bid)
            team.purse -= final_bid
            team.strength = team.strength + 1
            if (allRounders.iloc[i,2] == "F"):
                team.foreign = team.foreign + 1
            print("we have bought " , allRounders.iloc[i,0] , " for " , final_bid)
        else:
            current_bid += bidAmount
            print("current bid : " , current_bid)

        if (current_bid > maxArBid(arRating(allRounders.iloc[i,22], allRounders.iloc[i,24], allRounders.iloc[i,9], allRounders.iloc[i,11], allRounders.iloc[i,3], allRounders.iloc[i,5], allRounders.iloc[i,1], allRounders.iloc[i,27]))):
            final_bid = 0
            break
        if (current_bid > team.purse):
            break
        if (team.purse - current_bid < 6):
            break
        if (len(team.allR) == 1):
            break
        for z in range(len(team.allR)):
            print("all rounder : " , team.wk[z])
        print("current purse : " , team.purse)

# Final Team 

for bt in range(0,2):
    print("Batsman: " , team.Bat[bt] , " Price: " , team.BatPrice[bt] ,  "Cr")
for bw in range(0,1):
    print("Bowler: " , team.Bowl[bw] , " Price: " , team.BowlPrice[bw] ,  "Cr")
for wck in range(0,0):
    print("Wicket Keeper: " , team.wk[wck] , " Price: " , team.wkPrice[wck] ,  "Cr")
for alR in range(0,0):
    print("All Rounder: " , team.allR[alR] , " Price: " , team.allRPrice[alR] ,  "Cr")
print(team.foreign , " Overseas Players")
print("Purse Remaining : " , team.purse)