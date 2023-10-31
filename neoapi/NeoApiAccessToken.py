from neo_api_client import NeoAPI


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
client.session_2fa(OTP=input("Enter otp:"))

# getting master list
nseUrl = client.scrip_master(exchange_segment="NSE")
print(nseUrl)
