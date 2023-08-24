import json

login_credential = ""


def get_login_credentials():
    global login_credential

    def login_credentials():
        global login_credential
        print("---- Enter you Angel One login_credentials ---")
        # login_credential = {"api_key": str(input("Enter API Key :")),
        #                     "api_secret": str(input("Enter API Secret :"))
        #                     }

        login_credential = {"api_key": str(input("Enter API Key :")),
                            "clientId": str(input("Enter clientId :")),
                            "pwd": str(input("Enter pin :")),
                            "token": str(input("Enter token :"))
                            }
        if input("Press Y to save login_credential and any key to bypass : ").upper() == "Y":
            with open(f"login_credentials.txt", "w") as f:
                json.dump(login_credential, f)
            print("Data Saved. ..")
        else:
            print("Data save canceled!!!")

    while True:
        try:
            with open(f"login_credentials.txt", "r") as f:
                login_credential = json.load(f)
            break
        except:
            login_credentials()
    return login_credential
