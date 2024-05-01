from marketstructure.GetFirstItrEMAForNiftyIndex import getFirstItrEMAForNiftyIndex
from marketstructure.GetFirstItrMarketStrength import getFirstItrMarketStrength
from marketstructure.GetFirstItrMarketTimeOfTrend import getFirstItrMarketTimeOfTrend
from marketstructure.GetFirstItrMarketTrend import getFirstItrMarketTrend
from marketstructure.GetFirstItrThitaOneForNiftyIndex import getFirstItrThitaOneForNiftyIndex
from marketstructure.GetFirstItrThitaTwoForNiftyIndex import getFirstItrThitaTwoForNiftyIndex
from marketstructure.GetterMarketStructureDf import getterMarketStructureDf
from marketstructure.SetterPreMarketStructureDf import setterPreMarketStructureDf
from positionportfolioandmargindisplay.DisplayPastFiveMarketTrend import displayPastFiveMarketTrend


def getFirstItrMarketStructure():
    setterPreMarketStructureDf()
    getFirstItrEMAForNiftyIndex()
    getFirstItrThitaOneForNiftyIndex()
    getFirstItrThitaTwoForNiftyIndex()
    getFirstItrMarketTrend()
    getFirstItrMarketStrength()
    getFirstItrMarketTimeOfTrend()
    df = getterMarketStructureDf()
    displayPastFiveMarketTrend(df)
