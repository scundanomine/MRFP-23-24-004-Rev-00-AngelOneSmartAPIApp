def getGainOrLoss(cc, pc):
    if cc == 0:
        gl = 0
    else:
        try:
            gl = (cc - pc)/pc * 100
        except Exception as e:
            print(f"exception while calculating gain or loss is {e}")
            gl = 0
    return gl
