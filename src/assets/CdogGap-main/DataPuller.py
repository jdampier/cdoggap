import requests

# get api key from file
# file = open("APIkey.txt", "r")
apiKey = "RGAPI-5781820a-dae7-41b8-9ec3-abf4a51173be"
# file.close()

# account info
cdogId = "R45ZfJH8CgTtBq2UiF6HVUkLZMoyOJDGfxXearmBVMwaavY"
cdogAccountId = "-POoaxXg349MtzOUMXKZu8Z-m12oBLltzsGbZl_KRSXqfyw"
cdogPuuid = "7m3_VhxqZzWasoxTfIEbXuejaNYp_v9RzsSYwjmGjrzn-bUM0zfKFNjsTDjptK_fmdBBer1N5VYPeA"

keetchieId = "1IQPDEfsHDgWepgSJQM9JMQyCklPvjrWe2dy3Onj8uGU8To"
keetchieAccountId = "m3fedHnpwrvS-GYnx8lyabcnMs8OhZII26BQVfG87YFXol0"
keetchiePuuid = "AFA5nVkG34uN4s3nVivgZ10myx4GzmMXZjeR93qjhhr90L0s_-rEeQ1a_3tFxq4ff-e5Ei4WyAM_OA"


def getRank():
    cdogRankResponse = requests.get("https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/R45ZfJH8CgTtBq2UiF6HVUkLZMoyOJDGfxXearmBVMwaavY?api_key=" + apiKey).json()
    keetchieRankResponse = requests.get("https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/1IQPDEfsHDgWepgSJQM9JMQyCklPvjrWe2dy3Onj8uGU8To?api_key=" + apiKey).json()

    try:
        cdogTier = cdogRankResponse[1]["tier"]
        cdogTierValue = -1
        cdogDiv = cdogRankResponse[1]["rank"]
        cdogDivValue = -1
        cdogLp = cdogRankResponse[1]["leaguePoints"]
    except:
        cdogTier = cdogRankResponse[0]["tier"]
        cdogTierValue = -1
        cdogDiv = cdogRankResponse[0]["rank"]
        cdogDivValue = -1
        cdogLp = cdogRankResponse[0]["leaguePoints"]

    keetchieTier = keetchieRankResponse[0]["tier"]
    keetchieTierValue = -1
    keetchieDiv = keetchieRankResponse[0]["rank"]
    keetchieDivValue = -1
    keetchieLp = keetchieRankResponse[0]["leaguePoints"]

    '''
    Tier Values
    Gold - 4
    Platinum - 5
    Diamond - 6
    Master - 7 '''
    if cdogTier == "GOLD":
        cdogTierValue = 4
    elif cdogTier == "PLATINUM":
        cdogTierValue = 5
    elif cdogTier == "DIAMOND":
        cdogTierValue = 6
    elif cdogTier == "MASTER":
        cdogTierValue = 7

    if keetchieTier == "GOLD":
        keetchieTierValue = 4
    elif keetchieTier == "PLATINUM":
        keetchieTierValue = 5
    elif keetchieTier == "DIAMOND":
        keetchieTierValue = 6
    elif keetchieTier == "MASTER":
        keetchieTierValue = 7

    if cdogDiv == "I":
        cdogDivValue = 1
    elif cdogDiv == "II":
        cdogDivValue = 2
    elif cdogDiv == "III":
        cdogDivValue = 3
    elif cdogDiv == "IV":
        cdogDivValue = 4

    if keetchieDiv == "I":
        keetchieDivValue = 1
    elif keetchieDiv == "II":
        keetchieDivValue = 2
    elif keetchieDiv == "III":
        keetchieDivValue = 3
    elif keetchieDiv == "IV":
        keetchieDivValue = 4

    return [[cdogTierValue, cdogDivValue, cdogLp], [keetchieTierValue, keetchieDivValue, keetchieLp]]


values = getRank()
totalLPDiff = -1

if values[0][0] != 7:
    # difference of tiers - hardcoded 7 for "masters" cutoff
    totalLPDiff = ((values[0][0]) - 7) * -400
    # add keetchie's LP
    totalLPDiff = totalLPDiff + values[1][2]
    # difference of divisions
    totalLPDiff = totalLPDiff - ((4 - values[0][1]) * 100)
    # caleb's current division LP
    totalLPDiff = totalLPDiff - values[0][2]
elif values[0][0] >= 7:
    totalLPDiff = values[1][1] - values[0][1]
    if totalLPDiff > 0:
        print("Cdog is masters, but still " + str(totalLPDiff) + "lp behind Keetchie")
    else:
        print("Cdog has passed Keetchie by " + str(totalLPDiff * -1) + "lp. God has left us.")
print("Cdog is " + str(totalLPDiff) + "lp behind Keetchie")
