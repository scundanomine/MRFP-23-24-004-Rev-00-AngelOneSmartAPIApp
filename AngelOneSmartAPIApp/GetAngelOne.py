from GetAccessToken import *
from SmartApi import SmartConnect  # or from SmartApi.smartConnect import SmartConnect
from GetLoginCredential import *


def get_angel_one():
    smartApi = SmartConnect(get_login_credentials()["api_key"])
    try:
        res = smartApi.getProfile(get_access_token()["refreshToken"])
        # smartApi.generateToken(get_access_token()["refreshToken"])
        # res = res['data']['exchanges']
        print("rocks you have done it!!!!!!")
    except Exception as e:
        print(f"Error : {e}")
        os.remove(f"AccessToken/{datetime.datetime.now().date()}.json") if os.path.exists(
            f"AccessToken/{datetime.datetime.now().date()}.json") else None
        sys.exit()
