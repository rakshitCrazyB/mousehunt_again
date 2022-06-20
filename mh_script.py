import requests
import time
import random
from datetime import datetime
import sys
from pushbullet import PushBullet
import traceback


kingsReward = False
baseTime = 900 
pb_access_token = "o.rog2UWVKIxOH6GDZXDHAOvfuuWzsGo0f"
pb = PushBullet(pb_access_token)

def mhDebug(s):
    now = str(datetime.now())
    f = open("mhlog.txt", "a")
    f.write("MH LOG " + now +" : " +s)
    f.write("\n")
    f.write("\n")
    f.close()

def mhlog(s):
    now = str(datetime.now())
    print("MH LOG " + now +" : " +s)
    mhDebug(s)

def soundHorn():
    cookies = {
        'HG_TOKEN': 'AXC8u0J6rq6paN0J4nKyHR8IAO76LL0E6Dg2nns6Cn8u47k1ZfWSBvu3N0I6zgM2',
        '_gcl_au': '1.1.994906883.1654720969',
        '__utmc': '22815271',
        '__utmz': '22815271.1654720969.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
        'has_logged_in': 'true',
        '__utma': '22815271.1658349405.1654720969.1654720969.1654722882.2',
        '__utmb': '22815271.8.9.1654723841835',
        'hg_session[startTime]': '1654724160',
        'hg_session[sessionId]': '4iGbh6NML4SL7k64vK3y9344Re77CuoK',
        'hg_session[sessionNum]': '3',
    }

    headers = {
        # Requests sorts cookies= alphabetically
        # 'cookie': 'HG_TOKEN=AXC8u0J6rq6paN0J4nKyHR8IAO76LL0E6Dg2nns6Cn8u47k1ZfWSBvu3N0I6zgM2; _gcl_au=1.1.994906883.1654720969; __utmc=22815271; __utmz=22815271.1654720969.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); has_logged_in=true; __utma=22815271.1658349405.1654720969.1654720969.1654722882.2; __utmb=22815271.8.9.1654723841835; hg_session[startTime]=1654724160; hg_session[sessionId]=4iGbh6NML4SL7k64vK3y9344Re77CuoK; hg_session[sessionNum]=3',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'sn': 'Hitgrab',
        'hg_is_ajax': '1',
        'last_read_journal_entry_id': '6',
        'uh': '3k9XbE5U',
    }
    response = requests.post('https://www.mousehuntgame.com/managers/ajax/turns/activeturn.php', cookies=cookies, headers=headers, data=data)
    mhDebug(response.text)
    if "You must claim your King's Reward before continuing the hunt" in response.text:
        mhlog("Kings Reward Appeared")
        this.kingsReward = True
        pb.push_note("Kings Reward Appeared", "")
    else:
        mhlog("Sounded the horn")
        pb.push_note("Sounded the horn", "")

def checkIfKingsRewardSolved():
    mhlog("Checking if kings reward solved")
    cookies = {
        'HG_TOKEN': 'AXC8u0J6rq6paN0J4nKyHR8IAO76LL0E6Dg2nns6Cn8u47k1ZfWSBvu3N0I6zgM2',
        '_gcl_au': '1.1.994906883.1654720969',
        '__utmz': '22815271.1654720969.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
        'has_logged_in': 'true',
        'switch_to': 'standard',
        '__utmc': '22815271',
        'fbm_10337532241': 'base_domain=.mousehuntgame.com',
        'fbsr_10337532241': 'ayUEOnaeE75KWSyDO_b55AwGZHk43yp5jdcasD2iavM.eyJ1c2VyX2lkIjoiMTQ1MTg4MTgxNiIsImNvZGUiOiJBUUR4R3F4aTl1cm5wYWN0VWNyR09PVVZTYzZCOWtGcEVLTk9kWVRBdk5FMklqSnpSY1h1MVhOMG5NeWtjeUJZNktfQ19HUTRiWFViTlZTUEc5SG5KdFhESFh2bDluMEQzY3lQNTFqSUFfdDk3WF9FZUQzMnNkMlh1OWJ0LVdoQ2VVQlNzUW0wQUhzWG5XMTFuWS1uenFxNC1OMk5janBXOWpQWkhaMGpnVWVKLWJ3ZDFRV1VET0hhVnZwTUsyVDVIVno5R2VVcFNZNkplSlFaa1V2WUdIU3lPS3ZVRlIwd09EbzRfcDhJa0tWcEhhOFBYZTJtd1JYU1dMYUZyb05YQy1sODJVdGplcVhDd2ctSzM2S1JYUURtRTZ2emxmSnZyT0Jwd0VINmNzSEROaDFES05HcDE4MTFmMjBIN043VDhGbyIsIm9hdXRoX3Rva2VuIjoiRUFBQUFBbWdxT1ZFQkFHUFJqN25aQ3A1YTNDUllNY1pCaVZ3OHpScm13RlVET2dzdmtJWVFGeXVUMk81RUR5VFdWeUtJUzFOWGZpRE1IREc0VXRVWkJiSDhnUGZYUWpWTHMyTVRGM0pINDZuRHE4SEZnb2UyZXE0cE1DdnF6WGYzMXNBYjdSUXlGNGJaQ0kzVlJ1UHlkVlZOblBaQnpPN1R4cXo5UXVkRk1lZGVqSW9VVlE0UUciLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY1NDc3OTY5MX0',
        '__utma': '22815271.1658349405.1654720969.1654782605.1654793752.10',
        '__utmt': '1',
        '__utmb': '22815271.6.9.1654793803523',
        'HG_TOKEN': 'wP4lOwy0VU1427f3NtzFky4lerG5epT6YtEc912jSdehV1yC4Ov7Z1BQS9NcC5oE',
    }

    headers = {
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'HG_TOKEN=AXC8u0J6rq6paN0J4nKyHR8IAO76LL0E6Dg2nns6Cn8u47k1ZfWSBvu3N0I6zgM2; _gcl_au=1.1.994906883.1654720969; __utmz=22815271.1654720969.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); has_logged_in=true; switch_to=standard; __utmc=22815271; fbm_10337532241=base_domain=.mousehuntgame.com; fbsr_10337532241=ayUEOnaeE75KWSyDO_b55AwGZHk43yp5jdcasD2iavM.eyJ1c2VyX2lkIjoiMTQ1MTg4MTgxNiIsImNvZGUiOiJBUUR4R3F4aTl1cm5wYWN0VWNyR09PVVZTYzZCOWtGcEVLTk9kWVRBdk5FMklqSnpSY1h1MVhOMG5NeWtjeUJZNktfQ19HUTRiWFViTlZTUEc5SG5KdFhESFh2bDluMEQzY3lQNTFqSUFfdDk3WF9FZUQzMnNkMlh1OWJ0LVdoQ2VVQlNzUW0wQUhzWG5XMTFuWS1uenFxNC1OMk5janBXOWpQWkhaMGpnVWVKLWJ3ZDFRV1VET0hhVnZwTUsyVDVIVno5R2VVcFNZNkplSlFaa1V2WUdIU3lPS3ZVRlIwd09EbzRfcDhJa0tWcEhhOFBYZTJtd1JYU1dMYUZyb05YQy1sODJVdGplcVhDd2ctSzM2S1JYUURtRTZ2emxmSnZyT0Jwd0VINmNzSEROaDFES05HcDE4MTFmMjBIN043VDhGbyIsIm9hdXRoX3Rva2VuIjoiRUFBQUFBbWdxT1ZFQkFHUFJqN25aQ3A1YTNDUllNY1pCaVZ3OHpScm13RlVET2dzdmtJWVFGeXVUMk81RUR5VFdWeUtJUzFOWGZpRE1IREc0VXRVWkJiSDhnUGZYUWpWTHMyTVRGM0pINDZuRHE4SEZnb2UyZXE0cE1DdnF6WGYzMXNBYjdSUXlGNGJaQ0kzVlJ1UHlkVlZOblBaQnpPN1R4cXo5UXVkRk1lZGVqSW9VVlE0UUciLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY1NDc3OTY5MX0; __utma=22815271.1658349405.1654720969.1654782605.1654793752.10; __utmt=1; __utmb=22815271.6.9.1654793803523; HG_TOKEN=wP4lOwy0VU1427f3NtzFky4lerG5epT6YtEc912jSdehV1yC4Ov7Z1BQS9NcC5oE',
    }

    data = {
        'sn': 'Hitgrab',
        'hg_is_ajax': '1',
        'page_class': 'Camp',
        'last_read_journal_entry_id': '60',
        'uh': '3k9XbE5U',
    }

    response = requests.post('https://www.mousehuntgame.com/managers/ajax/pages/page.php', cookies=cookies, headers=headers, data=data)
    mhDebug(response.text)

    if "You must claim your King's Reward before continuing the hunt" not in response.text:
        this.kingsReward = False
        mhlog("Kings Reward not yet solved")
        pb.push_note("Kings Reward not yet solved", "")
    else :
        pb.push_note("Kings Reward Solved", "")
        mhlog("Kings Reward Solved")

while True:
    try:
        if kingsReward :
            checkIfKingsRewardSolved()
        
        if not kingsReward:
            soundHorn()
    except:
        mhlog("Something went wrong")
        mhlog(traceback.format_exc())
    time.sleep(baseTime + random.randint(10, 20))