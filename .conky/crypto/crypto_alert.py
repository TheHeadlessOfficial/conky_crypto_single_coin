# Lock file to tell conky that the script is running
lock_file = "/tmp/script_crypto.lock"
# Check lock file
try:
    open(lock_file, 'w').close()
    import os, sys
    import signal
    import requests
    import subprocess
    ################################ get your HOME name automatically
    homepath = os.environ['HOME']
    homename = homepath
    homename = homename[6:]
    ################################ set the temporary paths
    home = '/home/'
    conky = '/.conky/'
    ptemp = 'crypto/'    
    ################################ paths
    pusertargets = home + homename + conky + ptemp + 'usertargets.txt'
    pconky = home + homename + conky + ptemp + 'conky.txt'
    sound = "${exec paplay " + home + homename + conky + ptemp + "complete.oga}"
    soundfake = ''
    pconky_user_data = home + homename + conky + ptemp + "_conky_user_data.flag"
    pscript_input_ready = home + homename + conky + ptemp + "script_input_ready.flag"
    ################################ variables
    news = ''
    row1 = '${color6}Target reached. ${color}'
    row2 = '${color}Target not reached. ${color}'
    ################################################################ flag file AREA
    flag_path = os.path.expanduser(pconky_user_data)
    data_path = os.path.expanduser(pusertargets)
    script_input_path = os.path.expanduser(pscript_input_ready)
    # final cleaning function
    def cleanup_and_exit(signum=None, frame=None):
        if os.path.exists(flag_path):
            os.remove(flag_path)
        if os.path.exists(script_input_path):
            os.remove(script_input_path)
        sys.exit(0)
    # Linking to exit signal
    signal.signal(signal.SIGINT, cleanup_and_exit)
    signal.signal(signal.SIGTERM, cleanup_and_exit)
    if not os.path.exists(flag_path):
        # bash script path
        bash_script = home + homename + conky + ptemp + 'script_input.sh'
        # q-terminal window
        process = subprocess.Popen(["gnome-terminal", "--", "bash", bash_script])
        # wait the end of the process
        process.wait()
    # COMMENT OR UNCOMMENT the following 2 rows based on how you prefer to use the two targets variables: vuserpriceUp and vuserpriceDown
    # If you want to use python variables, uncomment the two following rows and comment the two "with open" following blocks
    # vuserpriceUp = 113000.00
    # vuserpriceDown = 85000.00
    # COMMENT OR UNCOMMENT the following 5 rows based on how you prefer the two targets variables: vuserpriceUp and vuserpriceDown
    # If you want to read the two variables from file, uncomment the two following rows and comment the two variables above
    with open(pusertargets, "r") as f:
        vuserpriceUp = float(f.readline().strip())
    with open(pusertargets, "r") as f:
        f.readline()
        vuserpriceDown = float(f.readline().strip())
    ################################ my API url (REMEMBER TO CHANGE THE ID COIN VALUE BASED ON YOUR COIN)
    ID_COIN_VALUE = 90
    url1 = 'https://api.coinlore.net/api/ticker/?id=' + ID_COIN_VALUE
    res1 = requests.get(url1).json()
    data1 = res1
    ################################ write conky.txt file
    def fconky(fpath, fprice, fpriceUp, fpriceDown, frow, fnews, fsound, fvsymbol, fvname):
        fo = open(fpath, 'w')
        fo.write('${color2}' + fvsymbol + ' - ' + fvname.upper() + '${color}\n')
        fo.write('${color2}Actual price (USD): ${color}' + str(fprice) + '\n')
        fo.write('\n')
        fo.write('${color2}${ALIGNC}TARGETS\n')
        fo.write('${color2}Limit Up: ${color6}' + fpriceUp + '${color}')
        fo.write('${ALIGNR}${color2}Limit Down: ${color9}' + fpriceDown + '${color}\n')
        fo.write('\n')
        fo.write(frow + fnews + fsound + '\n')
        fo.close()
    ################################ API variables 
    vid = ""
    vsymbol = ""
    vname = ""
    vnameid = ""
    vrank = ""
    vprice_usd = ""
    vpercent_change_24h = ""
    vpercent_change_1h = ""
    vpercent_change_7d = ""
    vprice_btc = ""
    vmarket_cap_usd = ""
    vvolume24 = ""
    vvolume24a = ""
    vcsupply = ""
    vtsupply = ""
    vmsupply = ""
    ################################ swap "data" OWM
    data = data1
    ################################ get data
    vid = data[0]['id']
    vsymbol = data[0]['symbol']
    vname = data[0]['name']
    vnameid = data[0]['nameid']
    vrank = data[0]['rank']
    vprice_usd = data[0]['price_usd']
    vpercent_change_24h = data[0]['percent_change_24h']
    vpercent_change_1h = data[0]['percent_change_1h']
    vpercent_change_7d = data[0]['percent_change_7d']
    vprice_btc = data[0]['price_btc']
    vmarket_cap_usd = data[0]['market_cap_usd']
    vvolume24 = data[0]['volume24']
    vvolume24a = data[0]['volume24a']
    vcsupply = data[0]['csupply']
    vtsupply = data[0]['tsupply']
    vmsupply = data[0]['msupply']
    ################################ write raw data
    pbtc = home + homename + conky + ptemp + '-raw.txt'
    fo = open(pbtc, 'w')
    fo.write('id: {}\n'.format(vid))
    fo.write('symbol: {}\n'.format(vsymbol))
    fo.write('name: {}\n'.format(vname))
    fo.write('nameid: {}\n'.format(vnameid))
    fo.write('rank: {}\n'.format(vrank))
    fo.write('price_usd: {}\n'.format(vprice_usd))
    fo.write('percent_change_24h: {}\n'.format(vpercent_change_24h))
    fo.write('percent_change_1h: {}\n'.format(vpercent_change_1h))
    fo.write('percent_change_7d: {}\n'.format(vpercent_change_7d))
    fo.write('price_btc: {}\n'.format(vprice_btc))
    fo.write('market_cap_usd: {}\n'.format(vmarket_cap_usd))
    fo.write('volume24: {}\n'.format(vvolume24))
    fo.write('volume24a: {}\n'.format(vvolume24a))
    fo.write('csupply: {}\n'.format(vcsupply))
    fo.write('tsupply: {}\n'.format(vtsupply))
    fo.write('msupply: {}\n'.format(vmsupply))
    fo.close()
    ################################ write clean data
    pbtc = home + homename + conky + ptemp + 'clean.txt'
    fo = open(pbtc, 'w')
    fo.write('{}\n'.format(vid))
    fo.write('{}\n'.format(vsymbol))
    fo.write('{}\n'.format(vname))
    fo.write('{}\n'.format(vnameid))
    fo.write('{}\n'.format(vrank))
    fo.write('{}\n'.format(vprice_usd))
    fo.write('{}\n'.format(vpercent_change_24h))
    fo.write('{}\n'.format(vpercent_change_1h))
    fo.write('{}\n'.format(vpercent_change_7d))
    fo.write('{}\n'.format(vprice_btc))
    fo.write('{}\n'.format(vmarket_cap_usd))
    fo.write('{}\n'.format(vvolume24))
    fo.write('{}\n'.format(vvolume24a))
    fo.write('{}\n'.format(vcsupply))
    fo.write('{}\n'.format(vtsupply))
    fo.write('{}\n'.format(vmsupply))
    fo.close()
    ################################ write conky file
    # check for target UP
    if (float(vprice_usd) >= vuserpriceUp):
        tempprice = vuserpriceDown
        tempprice = '-'
        news = 'Actual price is above this value.'
        fconky(pconky, vprice_usd, str(vuserpriceUp), tempprice, row1, news, sound, vsymbol, vname)
    # check for target DOWN
    elif (float(vprice_usd) <= vuserpriceDown):
        tempprice = vuserpriceUp
        tempprice = '-'
        news = 'Actual price is under this value.'
        fconky(pconky, vprice_usd, tempprice, str(vuserpriceDown), row1, news, sound, vsymbol, vname)
    # check for between targets
    else:
        news = 'Actual price is between the targets.'
        fconky(pconky, vprice_usd, str(vuserpriceUp), str(vuserpriceDown), row2, news, soundfake, vsymbol, vname)
except Exception as e:
    # Manage exceptions (optional)
    filelockerror = (f"Error during script execution: {e}")
finally:
    # remove lock file
    try:
        os.remove(lock_file)
    except FileNotFoundError:
        pass  # file already removed