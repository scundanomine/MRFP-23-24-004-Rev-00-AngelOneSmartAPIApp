from AngelOneSmartAPIApp.GetLiveData import *


def getAccessTokenOne(apiKey, clientIdOne, passW, tok):
    accessToken = []
    api_key = apiKey
    clientId = clientIdOne
    pwd = passW
    token = tok
    smartApi = SmartConnect(api_key)
    totp = pyotp.TOTP(token).now()
    correlation_id = "abc123"
    data = smartApi.generateSession(clientId, pwd, totp)
    while True:
        try:
            print("Trying Log In...")
            accessToken = {"authToken": data['data']['jwtToken'],
                           "refreshToken": data['data']['refreshToken'],
                           "feedToken": smartApi.getfeedToken(),
                           }
            break
        except:
            pass
    print("boom!!!!")
    return smartApi, accessToken
