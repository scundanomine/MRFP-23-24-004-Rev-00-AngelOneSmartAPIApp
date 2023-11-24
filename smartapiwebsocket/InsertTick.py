import sqlite3
import datetime


def insertTick(msg):
    db = sqlite3.connect('realtime.db', check_same_thread=False)
    c = db.cursor()
    # LIVE_FEED_JSON[message['token']] = {
    # 'time': datetime.datetime.fromtimestamp(message['exchange_timestamp']/1000).isoformat(),
    # 'token': message['token'],
    # 'ltp': message['last_traded_price'] / 100,
    # 'volume': message['volume_trade_for_the_day']}
    try:
        cT = datetime.datetime.now()
        time = datetime.datetime.fromtimestamp(msg['exchange_timestamp']/1000).isoformat()
        ltp = msg['last_traded_price'] / 100
        volume = msg['volume_trade_for_the_day']
        data = (time, cT, ltp, volume)
        token = msg['token']
        c.execute(f"INSERT INTO `{token}`(time, cT, ltp, volume) VALUES{data};")
        try:
            db.commit()
        except:
            db.rollback()
    except Exception as e:
        print(f"Exception while inserting tick data to db is {e}")
        pass

