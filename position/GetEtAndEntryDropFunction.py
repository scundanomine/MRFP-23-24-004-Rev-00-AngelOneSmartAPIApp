from entry.GetterDropAndSetterEntryList import getterDropAndSetterEntryList
from entry.GetterUpdateAndSetterECBList import getterUpdateAndSetterECBList
from entrytriggeredlist.GetterDropAndSetterEntryTriggeredList import getterDropAndSetterEntryTriggeredList
from entrytriggeredlist.GetterUpdateAndSetterBlackListET import getterUpdateAndSetterBlackListET


def getEtAndEntryDropFunction(lock, uid):
    with lock:
        # remove specific row from Entry list
        getterDropAndSetterEntryList(uid)
        # reset of black list
        getterUpdateAndSetterBlackListET(uid, 0)
        getterUpdateAndSetterECBList(uid, 0)
        # removal of specific row from ET list
        getterDropAndSetterEntryTriggeredList(uid)
