from util import http, hook


@hook.command(autohelp=False)
def dogecoin(inp, say=None):
    ".dogecoin -- gets current DOGE/BTC rate from craptsy"
    data = http.get_json("http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=132")
    data = data['return']['markets']
    ticker = {
        'last': data['DOGE']['lasttradeprice'],
        'vol': data['DOGE']['volume'],
    }
    say("Current: \x0307%(last)s\x0f satoshi - Volume: %(vol)s DOGE" % ticker)
