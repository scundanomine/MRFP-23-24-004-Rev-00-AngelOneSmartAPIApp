import os
import time, json, datetime, sys
import xlwings as xw


def start_excel():
    # global kite, live_data
    print("Excel Starting...")
    if not os.path.exists("TA_Python.xlsm"):
        try:
            wb = xw.Book()
            wb.save('TA_Python.xlsm')
            wb.close()
        except Exception as e:
            print(f"Error : {e}")
            sys.exit()
    wb = xw.Book("TA_Python.xlsm")
    for i in ["MarketWatch", "Exchange", "OrderBook"]:
        try:
            wb.sheets(i)
        except:
            wb.sheets.add(i)
    dt = wb.sheets("MarketWatch")
    ex = wb.sheets("Exchange")
    ob = wb.sheets("OrderBook")
    ex.range("a:j").value = ob.range("a:h").value = dt.range("p:q").value = None
    dt.range(f"a1:t1").value = ["Sr No", "Symbol", "Open", "High", "Low", "LTP", "Volume", "Vwap", "Best Bid Price",
                                "Best Ask Price", "Close", "Product (MIS/NRML/CNC)", "Direction (Buy/Sell)", "Qty", "Trigger Price", "Limit Price",
                                "Place Order (Entry)", "Order (Modify/Cancel/Exit)", "Place Order INFO", "Order INFO"]


start_excel()
