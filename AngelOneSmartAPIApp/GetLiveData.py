def get_live_data(instruments):
    global kite, live_data
    try:
        live_data
    except:
        live_data = {}
    try:
        live_data = kite.quote(instruments)
    except Exception as e:
        # print(f'Get live_data Failed {{{e}}}")
        pass
    return live_data