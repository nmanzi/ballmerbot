from util import http, hook

# http://itsthisforthat.com/api.php?json

@hook.command(autohelp=False)
def startup(inp, say=None):
    ".startup -- gives a shitty idea for a new business"
    data = http.get_json("http://itsthisforthat.com/api.php?json")
    say("so, basically, it's like a {this} for {that}.".format(**data))