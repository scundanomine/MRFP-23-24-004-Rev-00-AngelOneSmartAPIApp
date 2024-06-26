from candlestickdata.GetterSpecificCandleData import getterSpecificCandleData


def queueOperation(sid, symbol, data):
    # get df (getter function)
    gdf = getterSpecificCandleData(sid, symbol)
    # queue operation
    gdf.drop(0, axis=0, inplace=True)
    gdf.index = list(range(9))
    gdf.loc[len(gdf.index)] = 0
    gdf.loc[9, 'bulRP'] = 'none'
    gdf.loc[9, 'berRP'] = 'none'
    lid = 9
    gdf.loc[lid, "time"] = data['0']
    gdf.loc[lid, "O"] = data['1']
    gdf.loc[lid, "H"] = data['2']
    gdf.loc[lid, "L"] = data['3']
    gdf.loc[lid, "C"] = data['4']
    gdf.loc[lid, "V"] = data['5']

    return gdf

# getCandlesticksProperties(1, "RELIANCE-EQ",
#                           {0: "2023-10-20T09:25:00+05:30", 1: 23010.65, 2: 2312.25, 3: 2309.75, 4: 2311.95, 5: 25800})
