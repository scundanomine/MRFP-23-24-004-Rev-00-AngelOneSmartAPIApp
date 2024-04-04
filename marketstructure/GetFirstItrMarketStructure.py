from marketstructure.GetFirstItrEMAForNiftyIndex import getFirstItrEMAForNiftyIndex
from marketstructure.GetFirstItrMarketStrength import getFirstItrMarketStrength
from marketstructure.GetFirstItrMarketTimeOfTrend import getFirstItrMarketTimeOfTrend
from marketstructure.GetFirstItrMarketTrend import getFirstItrMarketTrend
from marketstructure.GetFirstItrThitaOneForNiftyIndex import getFirstItrThitaOneForNiftyIndex
from marketstructure.GetFirstItrThitaTwoForNiftyIndex import getFirstItrThitaTwoForNiftyIndex
from marketstructure.SetterPreMarketStructureDf import setterPreMarketStructureDf


def getFirstItrMarketStructure():
    setterPreMarketStructureDf()
    getFirstItrEMAForNiftyIndex()
    getFirstItrThitaOneForNiftyIndex()
    getFirstItrThitaTwoForNiftyIndex()
    getFirstItrMarketTrend()
    getFirstItrMarketStrength()
    getFirstItrMarketTimeOfTrend()
