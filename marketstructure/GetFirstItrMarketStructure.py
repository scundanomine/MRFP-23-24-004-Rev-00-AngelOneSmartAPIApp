from marketstructure.GetFirstItrEMAForNiftyIndex import getFirstItrEMAForNiftyIndex
from marketstructure.GetFirstItrThitaOneForNiftyIndex import getFirstItrThitaOneForNiftyIndex
from marketstructure.GetFirstItrThitaTwoForNiftyIndex import getFirstItrThitaTwoForNiftyIndex
from marketstructure.SetterPreMarketStructureDf import setterPreMarketStructureDf


def getFirstItrMarketStructure():
    setterPreMarketStructureDf()
    getFirstItrEMAForNiftyIndex()
    getFirstItrThitaOneForNiftyIndex()
    getFirstItrThitaTwoForNiftyIndex()
