from util import http, hook, timesince

expiration_period = 60  # 1 minute

# TODO use https://api.coindesk.com/v1/bpi/currentprice.json for btc rate
# TODO add conversion features
# TODO remember last rates so we can respond to any failed http queries
# TODO average rates for altcoins using multiple markets


@hook.command("doge", autohelp=False)
@hook.command(autohelp=False)
def dogecoin(inp, say=None):
    ".doge/.dogecoin -- gets current DOGE/BTC rate from craptsy"
    data = http.get_json("http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=132")
    data = data['return']['markets']
    ticker = {
        'last': data['DOGE']['lasttradeprice'],
        'volume': float(data['DOGE']['volume']),
    }
    say("DOGE/BTC: \x0307{last}\x0f BTC - Volume: {volume:.0f} DOGE".format(**ticker))


@hook.command("btc", autohelp=False)
@hook.command(autohelp=False)
def bitcoin(inp, say=None):
    ".btc/.bitcoin -- gets current exchange rate for bitcoins from BTC-e"
    data = http.get_json("https://btc-e.com/api/2/btc_usd/ticker")
    say("BTC/USD: \x0307${buy:.2f}\x0f - Volume: {vol_cur:.0f} BTC".format(**data['ticker']))