from neo_api_client import NeoAPI


def getKotakNeoApiAccessToken():
    def on_message(message):
        print(message)

    def on_error(error_message):
        print(error_message)

    # on_message, on_open, on_close and on_error is a call back function we will provide the response for the subscribe method.
    # access_token is an optional one. If you have barrier token then pass and consumer_key and consumer_secret will be optional.
    # environment by default uat you can pass prod to connect to live server
    client = NeoAPI(consumer_key="smVW_wd_DPf_XXERIrU27B7cZ8Aa", consumer_secret="D5pJF7s8Sg7_55nXutpQkOVttnwa",
                    environment='prod', on_message=on_message, on_error=on_error, on_close=None, on_open=None)

    # Initiate login by passing any of the combinations mobilenumber & password (or) pan & password (or) userid & password
    # Also this will generate the OTP to complete 2FA
    client.login(mobilenumber="+917982161429", password="System@2021")

    # Complete login and generate session token
    client.session_2fa(OTP="881340")

    # getting master list
    nseUrl = client.scrip_master(exchange_segment="NSE")
    print(nseUrl)

    # getting quote
    inst_tokens = [{"instrument_token": "11536", "exchange_segment": "nse_cm"},
                   {"instrument_token": "1594", "exchange_segment": "nse_cm"},
                   {"instrument_token": "11915", "exchange_segment": "nse_cm"},
                   {"instrument_token": "13245", "exchange_segment": "nse_cm"}]

    # try:
    #     # get LTP and Market Depth Data
    #     client.quotes(instrument_tokens=inst_tokens, quote_type="ltp", isIndex=False)
    # except Exception as e:
    #     print("Exception when calling get Quote api->quotes: %s\n" % e)

    try:
        # Get live feed data
        client.subscribe(instrument_tokens=inst_tokens)
    except Exception as e:
        print("Exception while connection to socket->socket: %s\n" % e)
    return client


getKotakNeoApiAccessToken()
