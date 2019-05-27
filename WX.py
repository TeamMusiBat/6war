#HIT TEAM PRO BOT
#VERSI        = WARBOT
#ASIST        = 5 ASIST
#CREATOR   = BINTANG
#=======================================#
import lineX
from lineX import *
from akad.ttypes import *
from thrift.Thrift import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
from multiprocessing import Pool, Process
from akad.ttypes import ContentType as Type
from akad.ttypes import ChatRoomAnnouncementContents
from akad.ttypes import Location
from akad.ttypes import ChatRoomAnnouncement
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess,asyncio
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse,youtube_dl,pafy,timeit,atexit,traceback,ffmpy,humanize
#=============================================================#

listApp = ["CHROMEOS", "DESKTOPWIN", "DESKTOPMAC", "IOSIPAD", "WIN10"]
print ("=============================================================\n                  HIT AUTO PROTECT BOT LINE\n                       CREATOR : DEDE\n                    HIT TEAM PRO BOTBOT\n=============================================================")
print ("===========[ HACKERS AUTO PROTECT BOT LOGIN START]===========")
ME = LINE('yauyilut@network-source.com','Lovers1978!')
H1 = LINE('atggnm@hostguru.info','Lovers1978!')
H2 = LINE('xkgxthhyr@dc-business.com','Lovers1978!')
H3 = LINE('zjdpfs@hostguru.info','Lovers1978!')
H4 = LINE('guzzqfxbf@hostguru.info','Lovers1978!')
H5 = LINE('nmgioywkj@hostguru.info','Lovers1978!')
print ("=============================================================")
print ("\n[ HIT AUTO PROTECT BOT START ]")
oepoll = OEPoll(ME)
myProfile = ME.getProfile()
mySettings = ME.getSettings()
mid = ME.profile.mid
meMID = ME.getProfile().mid
H1MID = H1.getProfile().mid
H2MID = H2.getProfile().mid
H3MID = H3.getProfile().mid
H4MID = H4.getProfile().mid
H5MID = H5.getProfile().mid
#==========================================================================================================================#

D_BOT = [meMID,H1MID,H2MID,H3MID,H4MID,H5MID]
D_WARS = [H1,H2,H3,H4,H5]
D_CREATOR = ["u38cbb60440251cd61c2e94efd715b181"]
D_WAR = ["u086c0c6fa344d081c99122c51a70e7a2","ufe656af28d2bb9195d150c4d2237f930","uc2db1af5451a43c7c7a5767e6ffe7ccc","u4ed6183c5c67c3346394b35ad18ff208","u7679b23cce711f7e51c63e06c1c7b0c7","u48b936605be834d195ae8e68fd1de51d"]
D_BOSS = ["u38cbb60440251cd61c2e94efd715b181","u086c0c6fa344d081c99122c51a70e7a2"]
D_LOVE = ["ud42687accb6906bcd14a826a29f16d9c","u3c3839c8e3f120f468bc2fec85d09204","uce37a6f47896e30e5287cbfd7e688f15"]
#==========================================================================================================================#

mulai = time.time()
tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)
msg_dict = {}
msg_dict1 = {}
D_NILLA = {
    "KUNCI": False,
    "PERINTAH": "",
    "SELFBOT": True,
    "WAR": False,
    "WAR_LINK": False,
    "WAR_JOIN": False,
    "WAR_INV": False,
    "PUBLIC": True,
    "ADDMESS": True,
    "VICTIM": {},
    "ADDVICTIM": False,
    "DELVICTIM": False,
    "JOINLINK": True,
    "IMAGE": False,
    "AGENT": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.200.32.99 Safari/537.36"
    ]
}
#=============================================================#

MESSAGE = """╭━━━━━━━━━━━━━━━━━━━╮
┃      HACKERS INC. TEAM BOT
┃                   SERVICE
┣•━━━━━━━━━━━━━━━━━━ 
┣•••[ AKTIVASI VIP SMULE ]•••
┃    •> PERORANGAN : 25K
┃    •> RESELLER        : 15 K
┃       ( S&K BERLAKU )
┃
┣•••[ HARGA LOGIN BOT ]•••
┃    •> SELFBOT ONLY :
┃         - REGULER   : 50K/BLN
┃         - PREMIUM1 : 100K/BLN
┃         - PREMIUM2 : 150K/BLN
┃         - ALWAYS ON 24 JAM
┃
┃    •> WAR BOT:
┃         - ROOM PROTECTION
┃         - ASIST 6   : 250K/BULAN
┃           > 1 Leader + 5 Asist
┃         - MEDIA COMMAND
┃         - REMOTE COMMAND***
┃         - ALWAYS ON 24 JAM
┃
┃    •> PROTECT BOT :
┃         - SBG OWNER BOT
┃         - ASIST 10  : 300K/BULAN
┃           > 7 asist + 3 Ghost/anti JS
┃         - ASIST 15  : 400K/BULAN
┃           > 12 asist + 3 Ghost/anti JS
┃         - ASIST 20 : 500K/BULAN
┃           > 17 asist + 3 Ghost/anti JS
┃         - FREE 4 ASIST ANTI JS
┃         - REMOTE COMMAND***
┃         - ALWAYS ON 24 JAM
┃
┣•••[ PROTECTION ]•••
┃    •> ROOM     : 300K/BULAN
┃    •> EVENT    : 400K/BULAN
┃         - START S/D SELESAI
┃    •> JUMLAH : 24 AUTO BOT
┃    •> REMOTE COMMAND***
┃         - ALWAYS ON 24 JAM
┃
┣•••[ N B ]•••
┃    •> ASIST BS KAMI SEDIAKAN
┣•━━━━━━━━━━━━━━━━━━━ 
┃ INFO LEBIH DETAIL,,SILAHKAN
┃ HUB. CONTACT DIBAWAH INI :
┃   •> OWNER : BINTANG
┃   •> line.me/ti/p/~__me___
┃   •> WA : +6281333833838
╰━━━━━━━━━━━━━━━━━━━╯"""
D_INFO = """╭━━━━━━━━━━━━━━━━━━╮
┃       🔰 DETAIL SISTEM 🔰
┣•━━━━━━━━━━━━━━━━━━
┣•🥇•  TYPE       : WAR BOT
┣•🥇•  ASIST      : 6 BOT
┣•🥇•  SISTEM    :  PYTHON 3
┣•🥇•  LOGIN       : VIA EMAIL                    
┣•🔰•  CREATOR : BINTANG
┣•📳•  ID LINE :
┃          line.me/ti/p/~__me___
┣•📳•  WHATSAPP :
┃          +6281333833838
┣•━━━━━━━━━━━━━━━━━━ 
┃     HACKERS INC. TEAM BOT
╰━━━━━━━━━━━━━━━━━━╯"""

D_MENU1 = """╭━━━━━━━━━━━━━━━━━╮
┃    HACKERS INC. TEAM BOT
┃        SISTEM : PYTHON3
┃      LOGIN : NO TOKEN/QR
┃ TYPE  : WARBOT 6 AUTO BOT
┣•━━━━━━━━━━━━━━━━━
┃    📳• MAIN COMMAND •📳
┣•━━━━━━━━━━━━━━━━━
┣•      📳•  Z MENU
┣•      📳•  Z ABOUT
┣•      📳•  Z RESET
┣•      📳•  Z RUN
┣•      📳•  Z SPEED
┣•      📳•  Z DC
┣•      📳•  Z REJECT
┣•      📳•  Z1-5 REJECT
┣•━━━━━━━━━━━━━━━━━
┃     ⚠️• WAR COMMAND •⚠️
┣•━━━━━━━━━━━━━━━━━
┣•      ⚠️•  Z JOIN
┣•      ⚠️•  Z GO
┣•      ⚠️•  Z BYE
┣•      ⚠️•  Z CON
┣•      ⚠️•  Z START / STOP
┣•      ⚠️•  Z KORBAN
┣•      ⚠️•  ZK ON / OFF
┣•      ⚠️•  ZDEL ON / OFF
┣•      ⚠️•  ZDELL ALL
┣•      ⚠️•  ZB *TAG
┣•      ⚠️•  ZBB *TAG
┣•      ⚠️•  Z CLEAN
┣•━━━━━━━━━━━━━━━━━
┃   •> CREATOR : BINTANG
┃   •> line.me/ti/p/~__me___
┃   •> WA : +6281333833838
╰━━━━━━━━━━━━━━━━━╯"""
D_MENU2 = """╭━━━━━━━━━━━━━━━━━╮
┃    HACKERS INC. TEAM BOT
┃        SISTEM : PYTHON3
┃      LOGIN : NO TOKEN/QR
┃ TYPE  : WARBOT 6 AUTO BOT
┣•━━━━━━━━━━━━━━━━━
┃  🆑• REMOTE COMMAND •🆑
┣•━━━━━━━━━━━━━━━━━
┣•      🆑•  Z GR
┣•      🆑•  Z GID
┣•      🆑•  ZGET (GID)
┣•      🆑•  ZINV (NO.GR)
┣•      🆑•  ZJOIN (NO.GR)
┣•      🆑•  ZLEAVE (NO.GR)
┣•      🆑•  ZMIDS (NO.GR)
┣•      🆑•  ZCL (NO.GR) (MID)
┣•      🆑•  ZPEND (NO.GR)
┣•      🆑•  ZCANCEL (NO.GR)
┣•      🆑•  ZNODES (NO.GR)
┣•━━━━━━━━━━━━━━━━━
┃    ▶️• MEDIA COMMAND •▶️
┣•━━━━━━━━━━━━━━━━━
┣•  ▶️•  Z TODAY
┣•  ▶️•  ZMP4 (SONG-SINGER)
┣•  ▶️•  ZMP3 (SONG-SINGER)
┣•  ▶️•  ZNEWS
┣•  ▶️•  ZBEJADD
┣•━━━━━━━━━━━━━━━━━
┃   •> CREATOR : BINTANG
┃   •> line.me/ti/p/~__me___
┃   •> WA : +6281333833838
╰━━━━━━━━━━━━━━━━━╯"""
#=============================================================#

def restartBot():
    print ("[ ] BOT RESTARTED")
    time.sleep(0.02)
    python = sys.executable
    os.execl(python, python, *sys.argv)
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
def logError(text):
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + " | " + inihari.strftime('%H:%M:%S')
    with open("serverBug.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def speedtest(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weaks, days = divmod(days,7)
    if days == 0:
        return '%02d' % (secs)
    elif days > 0 and weaks == 0:
        return '%02d' %(secs)
    elif days > 0 and weaks > 0:
        return '%02d' %(secs)
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]
def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
#=============================================================#

with open('blacklist.json', 'r') as fp:
    VICTIM = json.load(fp)
def addvictim():
    with open('blacklist.json', 'w') as fp:
        json.dump(VICTIM, fp, sort_keys=True, indent=4)
#=============================================================#
def command(text):
    pesan = text.lower()
    if D_NILLA["KUNCI"] == True:
        if pesan.startswith(D_NILLA["PERINTAH"]):
            D = pesan.replace(D_NILLA["PERINTAH"],"")
        else:
            D = "Undefined command"
    else:
        D = text.lower()
    return D
def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if D_NILLA["ADDMESS"] == True:
                ME.sendMessage(op.param1, str(MESSAGE))
                ME.sendContact(op.param1, "OWNER HACKERS INC. TEAM BOT")
                ME.sendContact(op.param1, "u38cbb60440251cd61c2e94efd715b181")
#===============================[ WAR BOT START ]=============================#
        
        if op.type == 19 or op.type == 32 or op.type == 13 or op.type == 11:
            if op.param2 not in D_BOT + D_BOSS:
                D_NILLA["WAR"] = True
                VICTIM["KICKS"][op.param2] = True
                addvictim()
                
        if op.type == 17:
            if D_NILLA["WAR"] == True:
                if op.param2 in VICTIM["KICKS"]:
                    random.choice(D_WARS).kickoutFromGroup(op.param1,[op.param2])
                    
        if op.type == 11:
            if D_NILLA["WAR"] == True:
                if op.param2 in VICTIM["KICKS"]:
                    random.choice(D_WARS).kickoutFromGroup(op.param1,[op.param2])
                    G = ME.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    ME.updateGroup(G)
                
        if op.type == 19 or op.type == 32:
            if op.param3 in D_BOSS:
                try:
                    if op.param2 not in D_BOT + D_BOSS:
                        H1.findAndAddContactsByMid(op.param3)
                        H1.kickoutFromGroup(op.param1,[op.param2])
                        H1.inviteIntoGroup(op.param1,[op.param3])
                except:
                    try:
                        if op.param2 not in D_BOT + D_BOSS:
                            H2.findAndAddContactsByMid(op.param3)
                            H2.kickoutFromGroup(op.param1,[op.param2])
                            H2.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            if op.param2 not in D_BOT + D_BOSS:
                                H3.findAndAddContactsByMid(op.param3)
                                H3.kickoutFromGroup(op.param1,[op.param2])
                                H3.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                if op.param2 not in D_BOT + D_BOSS:
                                    H4.findAndAddContactsByMid(op.param3)
                                    H4.kickoutFromGroup(op.param1,[op.param2])
                                    H4.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    if op.param2 not in D_BOT + D_BOSS:
                                        H5.findAndAddContactsByMid(op.param3)
                                        H5.kickoutFromGroup(op.param1,[op.param2])
                                        H5.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        if op.param2 not in D_BOT + D_BOSS:
                                            ME.findAndAddContactsByMid(op.param3)
                                            random.choice(D_WARS).kickoutFromGroup(op.param1,[op.param2])
                                            ME.inviteIntoGroup(op.param1,[op.param3])
                                    except: pass
                
        if op.type == 19 or op.type == 32:
            if op.param3 in H1MID:
                try:
                    if op.param2 not in D_BOT + D_BOSS:
                        H2.kickoutFromGroup(op.param1,[op.param2])
                        H2.inviteIntoGroup(op.param1,[op.param3])
                except:
                    try:
                        if op.param2 not in D_BOT + D_BOSS:
                            H3.kickoutFromGroup(op.param1,[op.param2])
                            H3.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            if op.param2 not in D_BOT + D_BOSS:
                                H4.kickoutFromGroup(op.param1,[op.param2])
                                H4.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                if op.param2 not in D_BOT + D_BOSS:
                                    H5.kickoutFromGroup(op.param1,[op.param2])
                                    H5.findAndAddContactsByMid("u086c0c6fa344d081c99122c51a70e7a2")
                                    H5.findAndAddContactsByMid("ufe656af28d2bb9195d150c4d2237f930")
                                    H5.findAndAddContactsByMid("uc2db1af5451a43c7c7a5767e6ffe7ccc")
                                    H5.findAndAddContactsByMid("u4ed6183c5c67c3346394b35ad18ff208")
                                    H5.findAndAddContactsByMid("u7679b23cce711f7e51c63e06c1c7b0c7")
                                    H5.inviteIntoGroup(op.param1,["u086c0c6fa344d081c99122c51a70e7a2"],["ufe656af28d2bb9195d150c4d2237f930"],["uc2db1af5451a43c7c7a5767e6ffe7ccc"],["u4ed6183c5c67c3346394b35ad18ff208"],["u7679b23cce711f7e51c63e06c1c7b0c7"])
                            except:
                                try:
                                    if op.param2 not in D_BOT + D_BOSS:
                                        G = ME.getGroup(op.param1)
                                        if G.preventedJoinByTicket == False:
                                            return
                                        else:
                                            G.preventedJoinByTicket = False
                                        ME.updateGroup(G)
                                        Ticket = ME.reissueGroupTicket(op.param1)
                                        for D_RAW in D_WARS:
                                            D_RAW.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        G.preventedJoinByTicket = True
                                        ME.updateGroup(G)
                                except: pass
        
        if op.type == 19 or op.type == 32:
            if op.param3 in H2MID:
                try:
                    if op.param2 not in D_BOT + D_BOSS:
                        H3.kickoutFromGroup(op.param1,[op.param2])
                        H3.inviteIntoGroup(op.param1,[op.param3])
                except:
                    try:
                        if op.param2 not in D_BOT + D_BOSS:
                            H4.kickoutFromGroup(op.param1,[op.param2])
                            H4.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            if op.param2 not in D_BOT + D_BOSS:
                                H5.kickoutFromGroup(op.param1,[op.param2])
                                H5.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                if op.param2 not in D_BOT + D_BOSS:
                                    H1.kickoutFromGroup(op.param1,[op.param2])
                                    H1.findAndAddContactsByMid("ufe656af28d2bb9195d150c4d2237f930")
                                    H1.findAndAddContactsByMid("uc2db1af5451a43c7c7a5767e6ffe7ccc")
                                    H1.findAndAddContactsByMid("u4ed6183c5c67c3346394b35ad18ff208")
                                    H1.findAndAddContactsByMid("u7679b23cce711f7e51c63e06c1c7b0c7")
                                    H1.findAndAddContactsByMid("u48b936605be834d195ae8e68fd1de51d")
                                    H1.inviteIntoGroup(op.param1,["u086c0c6fa344d081c99122c51a70e7a2"],["uc2db1af5451a43c7c7a5767e6ffe7ccc"],["u4ed6183c5c67c3346394b35ad18ff208"],["u7679b23cce711f7e51c63e06c1c7b0c7"],["u48b936605be834d195ae8e68fd1de51d"])
                            except:
                                try:
                                    if op.param2 not in D_BOT + D_BOSS:
                                        G = ME.getGroup(op.param1)
                                        if G.preventedJoinByTicket == False:
                                            return
                                        else:
                                            G.preventedJoinByTicket = False
                                        ME.updateGroup(G)
                                        Ticket = ME.reissueGroupTicket(op.param1)
                                        for D_RAW in D_WARS:
                                            D_RAW.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        G.preventedJoinByTicket = True
                                        ME.updateGroup(G)
                                except: pass
       
        if op.type == 19 or op.type == 32:
            if op.param3 in H3MID:
                try:
                    if op.param2 not in D_BOT + D_BOSS:
                        H4.kickoutFromGroup(op.param1,[op.param2])
                        H4.inviteIntoGroup(op.param1,[op.param3])
                except:
                    try:
                        if op.param2 not in D_BOT + D_BOSS:
                            H5.kickoutFromGroup(op.param1,[op.param2])
                            H5.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            if op.param2 not in D_BOT + D_BOSS:
                                H1.kickoutFromGroup(op.param1,[op.param2])
                                H1.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                if op.param2 not in D_BOT + D_BOSS:
                                    H2.kickoutFromGroup(op.param1,[op.param2])
                                    H2.findAndAddContactsByMid("u086c0c6fa344d081c99122c51a70e7a2")
                                    H2.findAndAddContactsByMid("uc2db1af5451a43c7c7a5767e6ffe7ccc")
                                    H2.findAndAddContactsByMid("u4ed6183c5c67c3346394b35ad18ff208")
                                    H2.findAndAddContactsByMid("u7679b23cce711f7e51c63e06c1c7b0c7")
                                    H2.findAndAddContactsByMid("u48b936605be834d195ae8e68fd1de51d")
                                    H2.inviteIntoGroup(op.param1,["u086c0c6fa344d081c99122c51a70e7a2"],["ufe656af28d2bb9195d150c4d2237f930"],["u4ed6183c5c67c3346394b35ad18ff208"],["u7679b23cce711f7e51c63e06c1c7b0c7"],["u48b936605be834d195ae8e68fd1de51d"])
                            except:
                                try:
                                    if op.param2 not in D_BOT + D_BOSS:
                                        G = ME.getGroup(op.param1)
                                        if G.preventedJoinByTicket == False:
                                            return
                                        else:
                                            G.preventedJoinByTicket = False
                                        ME.updateGroup(G)
                                        Ticket = ME.reissueGroupTicket(op.param1)
                                        for D_RAW in D_WARS:
                                            D_RAW.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        G.preventedJoinByTicket = True
                                        ME.updateGroup(G)
                                except: pass
       
        if op.type == 19 or op.type == 32:
            if op.param3 in H4MID:
                try:
                    if op.param2 not in D_BOT + D_BOSS:
                        H5.kickoutFromGroup(op.param1,[op.param2])
                        H5.inviteIntoGroup(op.param1,[op.param3])
                except:
                    try:
                        if op.param2 not in D_BOT + D_BOSS:
                            H1.kickoutFromGroup(op.param1,[op.param2])
                            H1.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            if op.param2 not in D_BOT + D_BOSS:
                                H2.kickoutFromGroup(op.param1,[op.param2])
                                H2.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                if op.param2 not in D_BOT + D_BOSS:
                                    H3.kickoutFromGroup(op.param1,[op.param2])
                                    H3.findAndAddContactsByMid("u086c0c6fa344d081c99122c51a70e7a2")
                                    H3.findAndAddContactsByMid("ufe656af28d2bb9195d150c4d2237f930")
                                    H3.findAndAddContactsByMid("u4ed6183c5c67c3346394b35ad18ff208")
                                    H3.findAndAddContactsByMid("u7679b23cce711f7e51c63e06c1c7b0c7")
                                    H3.findAndAddContactsByMid("u48b936605be834d195ae8e68fd1de51d")
                                    H3.inviteIntoGroup(op.param1,["u086c0c6fa344d081c99122c51a70e7a2"],["ufe656af28d2bb9195d150c4d2237f930"],["uc2db1af5451a43c7c7a5767e6ffe7ccc"],["u7679b23cce711f7e51c63e06c1c7b0c7"],["u48b936605be834d195ae8e68fd1de51d"])
                            except:
                                try:
                                    if op.param2 not in D_BOT + D_BOSS:
                                        G = ME.getGroup(op.param1)
                                        if G.preventedJoinByTicket == False:
                                            return
                                        else:
                                            G.preventedJoinByTicket = False
                                        ME.updateGroup(G)
                                        Ticket = ME.reissueGroupTicket(op.param1)
                                        for D_RAW in D_WARS:
                                            D_RAW.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        G.preventedJoinByTicket = True
                                        ME.updateGroup(G)
                                except: pass
       
        if op.type == 19 or op.type == 32:
            if op.param3 in H5MID:
                try:
                    if op.param2 not in D_BOT + D_BOSS:
                        H1.kickoutFromGroup(op.param1,[op.param2])
                        H1.inviteIntoGroup(op.param1,[op.param3])
                except:
                    try:
                        if op.param2 not in D_BOT + D_BOSS:
                            H2.kickoutFromGroup(op.param1,[op.param2])
                            H2.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            if op.param2 not in D_BOT + D_BOSS:
                                H3.kickoutFromGroup(op.param1,[op.param2])
                                H3.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                if op.param2 not in D_BOT + D_BOSS:
                                    H4.kickoutFromGroup(op.param1,[op.param2])
                                    H4.findAndAddContactsByMid("u086c0c6fa344d081c99122c51a70e7a2")
                                    H4.findAndAddContactsByMid("ufe656af28d2bb9195d150c4d2237f930")
                                    H4.findAndAddContactsByMid("uc2db1af5451a43c7c7a5767e6ffe7ccc")
                                    H4.findAndAddContactsByMid("u4ed6183c5c67c3346394b35ad18ff208")
                                    H4.findAndAddContactsByMid("u7679b23cce711f7e51c63e06c1c7b0c7")
                                    H4.findAndAddContactsByMid("u48b936605be834d195ae8e68fd1de51d")
                                    H4.inviteIntoGroup(op.param1,["u086c0c6fa344d081c99122c51a70e7a2"],["ufe656af28d2bb9195d150c4d2237f930"],["uc2db1af5451a43c7c7a5767e6ffe7ccc"],["u4ed6183c5c67c3346394b35ad18ff208"],["u48b936605be834d195ae8e68fd1de51d"])
                            except:
                                try:
                                    if op.param2 not in D_BOT + D_BOSS:
                                        G = ME.getGroup(op.param1)
                                        if G.preventedJoinByTicket == False:
                                            return
                                        else:
                                            G.preventedJoinByTicket = False
                                        ME.updateGroup(G)
                                        Ticket = ME.reissueGroupTicket(op.param1)
                                        for D_RAW in D_WARS:
                                            D_RAW.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        G.preventedJoinByTicket = True
                                        ME.updateGroup(G)
                                except: pass
                
        if op.type == 13:
            if meMID in op.param3:
                if op.param2 in D_BOSS:
                    ME.acceptGroupInvitation(op.param1)
                    G = ME.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    ME.updateGroup(G)
                    LINK = ME.reissueGroupTicket(op.param1)
                    for D_RAW in D_WARS:
                    	D_RAW.acceptGroupInvitationByTicket(op.param1,LINK)
                    G.preventedJoinByTicket = True
                    ME.updateGroup(G)
            if meMID in op.param3:
                if op.param2 in D_BOT:
                    ME.acceptGroupInvitation(op.param1)
            if H1MID in op.param3:
                if op.param2 in D_BOT:
                    H1.acceptGroupInvitation(op.param1)
            if H2MID in op.param3:
                if op.param2 in D_BOT:
                    H2.acceptGroupInvitation(op.param1)
            if H3MID in op.param3:
                if op.param2 in D_BOT:
                    H3.acceptGroupInvitation(op.param1)
            if H4MID in op.param3:
                if op.param2 in D_BOT:
                    H4.acceptGroupInvitation(op.param1)
            if H5MID in op.param3:
                if op.param2 in D_BOT:
                    H5.acceptGroupInvitation(op.param1)
            if D_NILLA["WAR"] == True:
                if op.param3 in VICTIM["KICKS"] + op.param2 not in D_BOT + D_BOSS:
                    random.choice(D_WARS).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(D_WARS).kickoutFromGroup(op.param1,[op.param2])
        
#==============================[ WAR BOT COMMAND ]==============================#
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            KUNCI = D_NILLA["PERINTAH"].title()
            if D_NILLA["KUNCI"] == False:
                 KUNCI = ''
            if msg.contentType == 13:
              if msg._from in D_BOSS:
                if D_NILLA["ADDVICTIM"] == True:
                    if msg.contentMetadata["mid"] in VICTIM["KICKS"]:
                        ME.sendMessage(msg.to,"__Already in Victim list__")
                        D_NILLA["ADDVICTIM"] = True
                    else:
                        VICTIM["KICKS"][msg.contentMetadata["mid"]] = True
                        D_NILLA["ADDVICTIM"] = True
                        addvictim()
                        ME.sendMessage(msg.to,"__Added to Victim list__")
                if D_NILLA["DELVICTIM"] == True:
                    if msg.contentMetadata["mid"] in VICTIM["KICKS"]:
                        del VICTIM["KICKS"][msg.contentMetadata["mid"]]
                        addvictim()
                        ME.sendMessage(msg.to,"__Not in Victim list__")
                        D_NILLA["DELVICTIM"] = True
                    else:
                        D_NILLA["DELVICTIM"] = True
                        ME.sendMessage(msg.to,"__Deleted from Victim list__")
            if msg.contentType == 1:
                 if msg._from in D_BOSS:
                   if D_NILLA["IMAGE"] == True:
                     path = ME.downloadObjectMsg(msg_id)
                     path1 = H1.downloadObjectMsg(msg_id)
                     path2 = H2.downloadObjectMsg(msg_id)
                     patH3 = H3.downloadObjectMsg(msg_id)
                     path4 = H4.downloadObjectMsg(msg_id)
                     path5 = H5.downloadObjectMsg(msg_id)
                     D_NILLA["IMAGE"] = False
                     ME.updateProfilePicture(path)
                     H1.updateProfilePicture(path1)
                     H2.updateProfilePicture(path2)
                     H3.updateProfilePicture(patH3)
                     H4.updateProfilePicture(path4)
                     H5.updateProfilePicture(path5)
                     ME.sendMessage(msg.to,"🗡️___Finish___")

#=========================================================================#        
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != ME.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 0:
                    if text is None:
                        return
                    else:
                        D = command(text)
                        if D == "z menu1" or D == "z help1":
                        	if msg._from in D_BOSS:
                        	    ME.sendMessage(msg.to, str(D_MENU1))
                        if D == "z menu2" or D == "z help2":
                        	if msg._from in D_BOSS:
                        	    ME.sendMessage(msg.to, str(D_MENU2))
                        if D == "z about":
                        	if msg._from in D_BOSS:
                        	    ME.sendMessage(msg.to, str(D_INFO))
                        elif D == "z reset":
                            if msg._from in D_BOSS:
                               ME.sendMessage(msg.to,"___Reset___")
                               restartBot()
                        elif D == "z dc":
                          if msg._from in D_BOSS:
                            ME.removeAllMessages(op.param2)
                            H1.removeAllMessages(op.param2)
                            H2.removeAllMessages(op.param2)
                            H3.removeAllMessages(op.param2)
                            H4.removeAllMessages(op.param2)
                            H5.removeAllMessages(op.param2)
                            ME.sendMessage(msg.to,"___Finish___")
                        elif D == "z run":
                            if msg._from in D_BOSS:
                               eltime = time.time() - mulai
                               bot = "🔰HIT PROTECT BOT ACTIVE TIME🔰\n===========================\n__Status : Active\n__Sistem : Running\n__Active Time :\n   " +waktu(eltime)+"\n==========================="
                               ME.sendMessage(msg.to,bot)
                        elif D == "z sp":
                          if msg._from in D_BOSS:
                            start = time.time()
                            elapsed_time = time.time() - start
                            ME.sendMessage(msg.to,"__Z__: \n\n   "+format(str(elapsed_time)))
                            elapsed_time = time.time() - start
                            H1.sendMessage(msg.to,"__Z_1__: \n\n   "+format(str(elapsed_time)))
                            elapsed_time = time.time() - start
                            H2.sendMessage(msg.to,"__Z_2__: \n\n   "+format(str(elapsed_time/10)))
                            elapsed_time = time.time() - start
                            H3.sendMessage(msg.to,"__Z_3__: \n\n   "+format(str(elapsed_time/10)))
                            elapsed_time = time.time() - start
                            H4.sendMessage(msg.to,"__Z_4__: \n\n   "+format(str(elapsed_time/10)))
                            elapsed_time = time.time() - start
                            H5.sendMessage(msg.to,"__Z_5__: \n\n   "+format(str(elapsed_time/100)))
                        elif D == "z mid":
                          if msg._from in D_BOSS:
                          	ME.sendMessage(msg.to,meMID)
                          H1.sendMessage(msg.to,H1MID)
                          H2.sendMessage(msg.to,H2MID)
                          H3.sendMessage(msg.to,H3MID)
                          H4.sendMessage(msg.to,H4MID)
                          H5.sendMessage(msg.to,H5MID)
                          
#============================[WAAAAAAARRRRRRRRRR]===============================#
                        elif D == "z join":
                          if msg._from in D_BOSS:
                            G = ME.getGroup(msg.to)
                            ginfo = ME.getGroup(msg.to)
                            G.preventedJoinByTicket = False
                            ME.updateGroup(G)
                            invsend = 0
                            Ticket = ME.reissueGroupTicket(msg.to)
                            H1.acceptGroupInvitationByTicket(msg.to,Ticket)
                            H2.acceptGroupInvitationByTicket(msg.to,Ticket)
                            H3.acceptGroupInvitationByTicket(msg.to,Ticket)
                            H4.acceptGroupInvitationByTicket(msg.to,Ticket)
                            H5.acceptGroupInvitationByTicket(msg.to,Ticket)
                            for ZJS in D_ZJS:
                            	ME.findAndAddContactsByMid(op.param3)
                            ME.inviteIntoGroup(msg.to,[op.param3])
                            ME.sendMessage(msg.to,"___READY___")
                            D_NILLA["WAR"] = True
                        elif D == "z bye":
                          if msg._from in D_BOSS:
                            H1.leaveGroup(msg.to)
                            H2.leaveGroup(msg.to)
                            H3.leaveGroup(msg.to)
                            H4.leaveGroup(msg.to)
                            H5.leaveGroup(msg.to)
                        elif D == "z go":
                          if msg._from in D_BOSS:
                          	ME.leaveGroup(msg.to)
                        if D == "z cek":
                            if msg._from in D_BOSS:
                               ME.sendMessage(msg.to, "___O_N ___")
                               H1.sendMessage(msg.to, "___O_N ___")
                               H2.sendMessage(msg.to, "___O_N ___")
                               H3.sendMessage(msg.to, "___O_N ___")
                               H4.sendMessage(msg.to, "___O_N ___")
                               H5.sendMessage(msg.to, "___O_N ___")
                               if D_NILLA["WAR"] == False:
                               	ME.sendMessage(msg.to,"___STOPPED___")
                               if D_NILLA["WAR"] == True:
                               	ME.sendMessage(msg.to,"___READY___")
                        elif D == "z start":
                          if msg._from in D_BOSS:
                              D_NILLA["WAR"] = True
                              ME.sendMessage(msg.to,"___READY___")
                        elif D == "z stop":
                          if msg._from in D_BOSS:
                              D_NILLA["WAR"] = False
                              ME.sendMessage(msg.to,"___STOPPED___")
                        elif D == "zk on":
                          if msg._from in D_BOSS:
                          	D_NILLA["ADDVICTIM"] = True
                          ME.sendMessage(msg.to,"__Adding Victim On__\n\n__Send Contact__")
                        elif D == "zk off":
                          if msg._from in D_BOSS:
                          	D_NILLA["ADDVICTIM"] = False
                          ME.sendMessage(msg.to,"__Adding Victim Off__")
                        elif D == "zdel on":
                          if msg._from in D_BOSS:
                          	D_NILLA["DELVICTIM"] = True
                          ME.sendMessage(msg.to,"__Deleting Victim On__\n\n__Send Contact__")
                        elif D == "zdel off" or D == "finish":
                          if msg._from in D_BOSS:
                          	D_NILLA["DELVICTIM"] = False
                          D_NILLA["WAR"] = False
                          ME.sendMessage(msg.to,"__Deleting Victim Off__")
                        elif D == "z korban":
                          if msg._from in D_BOSS:
                          	if VICTIM["KICKS"] == {}:
                          	    ME.sendMessage(msg.to,"__Victim Empty__")
                          for K in VICTIM["KICKS"]:
                          	ME.sendMessage(msg.to, None, contentMetadata={'mid': K}, contentType=13)
                        elif D == "zdel all" or D == "z dbl":
                          if msg._from in D_BOSS:
                              D_NILLA["WAR"] = False
                              D_NILLA["DELVICTIM"] = True
                          if VICTIM["KICKS"] == {}:
                          	ME.sendMessage(msg.to,"__Victim Empty__")
                          for K in VICTIM["KICKS"]:
                          	ME.sendMessage(msg.to, None, contentMetadata={'mid': K}, contentType=13)
                          ME.sendMessage(msg.to, "Finish")
                        elif D == "z con":
                            if msg._from in D_BOSS:
                               try:ME.inviteIntoGroup(to, [meMID]);has = "OK"
                               except:has = "NOT"
                               try:ME.kickoutFromGroup(to, [meMID]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "Ready..☑️"
                               else:sil = "Limit..🚫"
                               if has1 == "OK":sil1 = "Ready..☑️"
                               else:sil1 = "Limit..🚫"
                               ME.sendMessage(msg.to, "🔰Z*___CONDITION🔰\n==================\n__KICK     : {} \n__INVITE : {}".format(sil1,sil) + "\n==================")
                               try:H1.inviteIntoGroup(to, [H1MID]);has = "OK"
                               except:has = "NOT"
                               try:H1.kickoutFromGroup(to, [H1MID]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "Ready..☑️"
                               else:sil = "Limit..🚫"
                               if has1 == "OK":sil1 = "Ready..☑️"
                               else:sil1 = "Limit..🚫"
                               H1.sendMessage(msg.to, "🔰🔰\n==================\n__KICK     : {} \n__INVITE : {}".format(sil1,sil) + "\n==================")
                               try:H2.inviteIntoGroup(to, [H2MID]);has = "OK"
                               except:has = "NOT"
                               try:H2.kickoutFromGroup(to, [H2MID]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "Ready..☑️"
                               else:sil = "Limit..🚫"
                               if has1 == "OK":sil1 = "Ready..☑️"
                               else:sil1 = "Limit..🚫"
                               H2.sendMessage(msg.to, "🔰Z___CONDITION🔰\n==================\n__KICK     : {} \n__INVITE : {}".format(sil1,sil) + "\n==================")
                               try:H3.inviteIntoGroup(to, [H3MID]);has = "OK"
                               except:has = "NOT"
                               try:H3.kickoutFromGroup(to, [H3MID]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "Ready..☑️"
                               else:sil = "Limit..🚫"
                               if has1 == "OK":sil1 = "Ready..☑️"
                               else:sil1 = "Limit..🚫"
                               H3.sendMessage(msg.to, "🔰Z____CONDITION🔰\n==================\n__KICK     : {} \n__INVITE : {}".format(sil1,sil) + "\n==================")
                               try:H4.inviteIntoGroup(to, [H4MID]);has = "OK"
                               except:has = "NOT"
                               try:H4.kickoutFromGroup(to, [H4MID]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "Ready..☑️"
                               else:sil = "Limit..🚫"
                               if has1 == "OK":sil1 = "Ready..☑️"
                               else:sil1 = "Limit..🚫"
                               H4.sendMessage(msg.to, "🔰Z____CONDITION🔰\n==================\n__KICK     : {} \n__INVITE : {}".format(sil1,sil) + "\n==================")
                               try:H5.inviteIntoGroup(to, [H5MID]);has = "OK"
                               except:has = "NOT"
                               try:H5.kickoutFromGroup(to, [H5MID]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "Ready..☑️"
                               else:sil = "Limit..🚫"
                               if has1 == "OK":sil1 = "Ready..☑️"
                               else:sil1 = "Limit..🚫"
                               H5.sendMessage(msg.to, "🔰Z____CONDITION🔰\n==================\n__KICK     : {} \n__INVITE : {}".format(sil1,sil) + "\n==================")
                        
                        elif D.startswith("zb "):
                          if msg._from in D_BOSS:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                D_NILLA["WAR"] = True
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        random.choice(D_WARS).kickoutFromGroup(msg.to,[ls])
                                        for KR in VICTIM["KICKS"]:
                                        	random.choice(D_WARS).kickoutFromGroup(msg.to,[KR])
                                    except: pass
                                        
#============================[GANTI NAMA N FOTO PROFIL BOT]===============================#
                        elif D == "z up":
                            if msg._from in D_BOSS:
                                D_NILLA["IMAGE"] = True
                                ME.sendMessage(msg.to,"__KIRIM FOTONYA__") 

                        elif D.startswith("znm "):
                          if msg._from in D_BOSS:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ME.getProfile()
                                profile.displayName = string
                                ME.updateProfile(profile)
                                ME.sendMessage(msg.to,"__NAMA __W_Z DI GANTI :\n   " + string + "")
                        elif D.startswith("z1nm "):
                          if msg._from in D_BOSS:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = H1.getProfile()
                                profile.displayName = string
                                H1.updateProfile(profile)
                                H1.sendMessage(msg.to,"__NAMA __Z_1 DI GANTI :\n   " + string + "")
                        elif D.startswith("z2nm "):
                          if msg._from in D_BOSS:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = H2.getProfile()
                                profile.displayName = string
                                H2.updateProfile(profile)
                                H2.sendMessage(msg.to,"__NAMA __Z_2 DI GANTI :\n   " + string + "")
                        elif D.startswith("z3nm "):
                          if msg._from in D_BOSS:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = H3.getProfile()
                                profile.displayName = string
                                H3.updateProfile(profile)
                                H3.sendMessage(msg.to,"__NAMA __Z_3 DI GANTI :\n   " + string + "")
                        elif D.startswith("z4nm "):
                          if msg._from in D_BOSS:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = H4.getProfile()
                                profile.displayName = string
                                H4.updateProfile(profile)
                                H4.sendMessage(msg.to,"__NAMA __Z_4 DI GANTI :\n   " + string + "")
                        elif D.startswith("z5nm "):
                          if msg._from in D_BOSS:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = H5.getProfile()
                                profile.displayName = string
                                H5.updateProfile(profile)
                                H5.sendMessage(msg.to,"__NAMA __Z_5 DI GANTI :\n   " + string + "")
                        elif D.startswith("zanm "):
                          if msg._from in D_BOSS:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = H1.getProfile()
                                profile.displayName = string
                                H1.updateProfile(profile)
                                profile = H2.getProfile()
                                profile.displayName = string
                                H2.updateProfile(profile)
                                profile = H3.getProfile()
                                profile.displayName = string
                                H3.updateProfile(profile)
                                profile = H4.getProfile()
                                profile.displayName = string
                                H4.updateProfile(profile)
                                profile = H5.getProfile()
                                profile.displayName = string
                                H5.updateProfile(profile)
                                ME.sendMessage(msg.to," __D O N E__")
                        
#============[MEDIA MENU]==============#
                        elif D == "z news":
                            if msg._from in D_BOSS:
                            	r=requests.get("https://newsapi.org/v2/top-headlines?country=id&apiKey=1214d6480f6848e18e01ba6985e2008d")    
                            data=r.text
                            data=json.loads(data)
                            hasil = "🔰 NEWS UPDATE 🔰\n"
                            hasil += "\n========================================"
                            hasil += "\n💠 JUDUL  : " + str(data["articles"][0]["title"])
                            hasil += "\n💠 SOURCE  :"+ str(data["articles"][0]["source"]["name"])
                            hasil += "\n💠 PENULIS : " + str(data["articles"][0]["author"])
                            hasil += "\n💠 LINK         : " + str(data["articles"][0]["url"])
                            hasil += "\n========================================\n"
                            hasil += "\n========================================"
                            hasil += "\n💠 JUDUL  : " + str(data["articles"][1]["title"])                                   
                            hasil += "\n💠 SOURCE  :"+ str(data["articles"][1]["source"]["name"])
                            hasil += "\n💠 PENULIS : " + str(data["articles"][1]["author"])
                            hasil += "\n💠 LINK         : " + str(data["articles"][1]["url"])
                            hasil += "\n========================================\n"
                            hasil += "\n========================================"
                            hasil += "\n💠 JUDUL  : " + str(data["articles"][2]["title"])                                   
                            hasil += "\n💠 SOURCE  :"+ str(data["articles"][2]["source"]["name"])
                            hasil += "\n💠 PENULIS : " + str(data["articles"][2]["author"])
                            hasil += "\n💠 LINK         : " + str(data["articles"][2]["url"])
                            hasil += "\n========================================\n"
                            hasil += "\n========================================"
                            hasil += "\n💠 JUDUL  : " + str(data["articles"][3]["title"])                                   
                            hasil += "\n💠 SOURCE  :"+ str(data["articles"][3]["source"]["name"])
                            hasil += "\n💠 PENULIS : " + str(data["articles"][3]["author"])
                            hasil += "\n💠 LINK         : " + str(data["articles"][3]["url"])
                            hasil += "\n========================================\n"
                            hasil += "\n========================================"
                            hasil += "\n💠 JUDUL  : " + str(data["articles"][4]["title"])                                   
                            hasil += "\n💠 SOURCE  :"+ str(data["articles"][4]["source"]["name"])
                            hasil += "\n💠 PENULIS : " + str(data["articles"][4]["author"])
                            hasil += "\n💠 LINK         : " + str(data["articles"][4]["url"])
                            hasil += "\n========================================\n"
                            ME.sendMessage(msg.to, str(hasil))
                        elif D.startswith("zmp4 "):
                          if msg._from in D_BOSS:
                          	sep = msg.text.split(" ")
                          textToSearch = msg.text.replace(sep[0] + " ","")
                          query = urllib.parse.quote(textToSearch)
                          search_url="https://www.youtube.com/results?search_query="
                          mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                          sb_url = search_url + query
                          sb_get = requests.get(sb_url, headers = mozhdr)
                          soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                          yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                          x = (yt_links[1])
                          yt_href =  x.get("href")
                          yt_href = yt_href.replace("watch?v=", "")
                          qx = "https://youtu.be" + str(yt_href)
                          vid = pafy.new(qx)
                          stream = vid.streams
                          best = vid.getbest()
                          best.resolution, best.extension
                          for s in stream:
                          	me = best.url
                          vin = s.url
                          title = "             🔰 DETAIL VIDEO 🔰\n==========================\n💠 Judul :\n   " + vid.title
                          author = '\n💠 Author : ' + str(vid.author)
                          durasi = '\n\n💠 Duration : ' + str(vid.duration)
                          suka = '\n\n💠 Likes : ' + str(vid.likes)
                          dislike = '\n💠 Dislikes : ' + str(vid.dislikes)
                          rating = '\n💠 Rating : ' + str(vid.rating)
                          ME.sendMessage(msg.to,title+ author+ durasi+ suka+dislike+ rating+"\n💠 Source : Youtube\n==========================")
                          ME.sendMessage(msg.to, "⬇️ DOWNLOADING VIDEO....")
                          ME.sendVideoWithURL(msg.to, me)
                          ME.sendMessage(to, "🙏 ENJOY IT...")
                        elif D.startswith("zmp3 "):
                          if msg._from in D_BOSS:
                          	sep = msg.text.split(" ")
                          textToSearch = msg.text.replace(sep[0] + " ","")
                          query = urllib.parse.quote(textToSearch)
                          search_url="https://www.youtube.com/results?search_query="
                          mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                          sb_url = search_url + query
                          sb_get = requests.get(sb_url, headers = mozhdr)
                          soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                          yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                          x = (yt_links[1])
                          yt_href =  x.get("href")
                          yt_href = yt_href.replace("watch?v=", "")
                          qx = "https://youtu.be" + str(yt_href)
                          vid = pafy.new(qx)
                          stream = vid.streams
                          best = vid.getbest()
                          best.resolution, best.extension
                          for s in stream:
                          	me = best.url
                          vin = s.url
                          title = "      🔰 MUSIC RESULT 🔰\n======================\n 💠 Judul : \n\n   " + vid.title
                          durasi = '\n 💠 Duration : ' + str(vid.duration)
                          ME.sendMessage(msg.to,title + durasi +"\n======================")
                          ME.sendMessage(msg.to, "⬇️ DOWNLOADING AUDIO....")
                          ME.sendAudioWithURL(msg.to, me)
                          ME.sendMessage(to, "🙏 ENJOY IT...")
                        elif D == ".bejadd":
                          if msg._from in D_BOSS:
                          	bokep = "               WARNING....!!!!!!! \n📵 JANGAN DI KLIK LINK INI...!!! 📵\n===========================\n"
                          bokep += "     😜    nekopoi.host\n"
                          bokep += "     😜    sexvideobokep.com\n"
                          bokep += "     😜    memek.com\n"
                          bokep += "     😜    pornktube.com\n"
                          bokep += "     😜    faketaxi.com\n"
                          bokep += "     😜    videojorok.com\n"
                          bokep += "     😜    watchmygf.mobi\n"
                          bokep += "     😜    xnxx.com\n"
                          bokep += "     😜    pornhd.com\n"
                          bokep += "     😜    xvideos.com\n"
                          bokep += "     😜    vidz7.com\n"
                          bokep += "     😜    m.xhamster.com\n"
                          bokep += "     😜    xxmovies.pro\n"
                          bokep += "     😜    youporn.com\n"
                          bokep += "     😜    pornhub.com\n"
                          bokep += "     😜    anyporn.com\n"
                          bokep += "     😜    hdsexdino.com\n"
                          bokep += "     😜    rubyourdick.com\n"
                          bokep += "     😜    anybunny.mobi\n"
                          bokep += "     😜    cliphunter.com\n"
                          bokep += "     😜    sexloving.net\n"
                          bokep += "     😜    free.goshow.tv\n"
                          bokep += "     😜    eporner.com\n"
                          bokep += "     😜    Pornhd.josex.net\n"
                          bokep += "     😜    m.hqporner.com\n"
                          bokep += "     😜    m.spankbang.com\n"
                          bokep += "     😜    m.4tube.com\n"
                          bokep += "     😜    brazzers.com\n==========================="
                          ME.sendMessage(msg.to, str(bokep))
                          ME.sendMessage(msg.to,"📵 Hanya Orang bejad n suka mesum\n      yang nekad nge klik link di atas..!!!!\n      😜😜😜😜😜")
                        
                        elif D == "z today":
                          if D_NILLA["PUBLIC"] == True:
                          	tz = pytz.timezone("Asia/Jakarta")
                          timeNow = datetime.now(tz=tz)
                          day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                          hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                          bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                          hr = timeNow.strftime("%A")
                          bln = timeNow.strftime("%m")
                          for i in range(len(day)):
                          	if hr == day[i]: hasil = hari[i]
                          for k in range(0, len(bulan)):
                          	if bln == str(k): bln = bulan[k-1]
                          readTime = "  🔰 KALENDER HARI INI 🔰\n======================\n💠 Hari        : "+hasil + "\n💠 Tanggal : " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n💠 Jam        : " + timeNow.strftime('%H:%M:%S') + "\n======================"
                          ME.sendMessage(msg.to, readTime)

#===============================[REJECT SPAM UNDANGAN]==================================#
                        elif D == "z reject":
                          if D_NILLA["SELFBOT"] == True:
                            if msg._from in D_BOSS:
                              ginvited = ME.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      ME.rejectGroupInvitation(gid)
                                  ME.sendMessage(msg.to,"__Sukses menolak spam undangan : {}".format(str(len(ginvited))))
                              else:
                                  ME.sendMessage(msg.to,"__Spam Invite Kosong__")
                        elif D == "z1 reject":
                          if D_NILLA["SELFBOT"] == True:
                            if msg._from in D_BOSS:
                              ginvited = H1.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      H1.rejectGroupInvitation(gid)
                                  H1.sendMessage(msg.to,"__Sukses menolak spam undangan : {}".format(str(len(ginvited))))
                              else:
                                  H1.sendMessage(msg.to,"__Spam Invite Kosong__")
                        elif D == "z2 reject":
                          if D_NILLA["SELFBOT"] == True:
                            if msg._from in D_BOSS:
                              ginvited = H2.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      H2.rejectGroupInvitation(gid)
                                  H2.sendMessage(msg.to,"__Sukses menolak spam undangan : {}".format(str(len(ginvited))))
                              else:
                                  H2.sendMessage(msg.to,"__Spam Invite Kosong__")
                        elif D == "z3 reject":
                          if D_NILLA["SELFBOT"] == True:
                            if msg._from in D_BOSS:
                              ginvited = H3.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      H3.rejectGroupInvitation(gid)
                                  H3.sendMessage(msg.to,"__Sukses menolak spam undangan : {}".format(str(len(ginvited))))
                              else:
                                  H3.sendMessage(msg.to,"__Spam Invite Kosong__")
                        elif D == "z4 reject":
                          if D_NILLA["SELFBOT"] == True:
                            if msg._from in D_BOSS:
                              ginvited = H4.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      H4.rejectGroupInvitation(gid)
                                  H4.sendMessage(msg.to,"__Sukses menolak spam undangan : {}".format(str(len(ginvited))))
                              else:
                                  H4.sendMessage(msg.to,"__Spam Invite Kosong__")
                        elif D == "z5 reject":
                          if D_NILLA["SELFBOT"] == True:
                            if msg._from in D_BOSS:
                              ginvited = H5.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      H5.rejectGroupInvitation(gid)
                                  H5.sendMessage(msg.to,"__Sukses menolak spam undangan : {}".format(str(len(ginvited))))
                              else:
                                  H5.sendMessage(msg.to,"__Spam Invite Kosong__")

#=================================[REMOTE GROUP]==============================#
                        
                        elif D == "z gr":
                          if D_NILLA["SELFBOT"] == True:
                            if msg._from in D_BOSS:
                               ma = ""
                               a = 0
                               gid = ME.getGroupIdsJoined()
                               for i in gid:
                                   G = ME.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += " 🗡️  " + str(a) + ". " +G.name+ "\n"
                               ME.sendMessage(msg.to,"🔰 PRO GROUPS : "+str(len(gid))+"  🔰\n\n"+ma)
                        elif D == "z gid":
                          if msg._from in D_BOSS:
                            GR = ME.getGroupIdsJoined()
                            X = ""
                            for GID in GR:
                            	X += "🗡️  %s :\n%s\n\n" % (ME.getGroup(GID).name,GID)
                            ME.sendMessage(msg.to, X)
                        elif D.startswith("zgr "):
                          if msg._from in D_BOSS:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = ME.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = ME.getGroup(group)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(ME.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ME.sendMessage(msg.to, "           🔰 INFO DETAIL GROUP 🔰\n===============================\n💠 Nama Group : {}".format(G.name)+ "\n💠 ID Group : \n    {}".format(G.id)+ "\n💠 Pembuat : {}".format(G.creator.displayName)+ "\n💠 Waktu Dibuat : \n  {}".format(str(timeCreated))+ "\n💠 Jumlah Member : {}".format(str(len(G.members)))+ "\n💠 Jumlah Pending : {}".format(gPending)+ "\n💠 Group Qr : {}".format(gQr)+ "\n💠 Group Ticket : {}".format(gTicket)+"\n===============================")
                                ME.sendMessage(msg.to,"💠 Kontak Pembuat :")
                                ME.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                ME.sendMessage(msg.to,"💠 Goup Cover :")
                                ME.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except:
                                pass
                        elif D.startswith("zmids "):
                          if msg._from in D_BOSS:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = ME.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = ME.getGroup(group)
                                ret_ = "\n"
                                for mem in G.members:
                                    ret_ += "💠 "+ mem.displayName
                                    ret_ += "\n   "+ mem.mid + "\n"
                                ME.sendMessage(msg.to, "🔰 GROUP : "+ str(G.name) + "🔰\n==========================\n"+ str(ret_) + "\n==========================\n       🔰 TOTAL : %i  ORANG 🔰"% len(G.members))
                            except: 
                                pass

#=================================[REMOTE KICK]==============================#
                        elif D.startswith("zcl "): 
                          if msg._from in D_BOSS:
                            separate = msg.text.split(" ")
                            group = str(separate[1])
                            mids = str(separate[2])
                            name = text.replace("zcl " + str(group) + " ","")
                            groups = ME.getGroupIdsJoined()
                            target = ME.getContact(mids).displayName                            
                            try:
                                GS = groups[int(group)-1]
                                gs = ME.getGroup(GS)
                                _name = ME.getContact(name).displayName
                                target = ME.getContact(mids).displayName
                                ME.sendMessage(msg.to, "     🔰 REMOTE KICK MEMBER 🔰 \n===========================\n🗡️ Target Name :\n "+target+"\n🗡️ Target Group :\n "+str(gs.name)+"\n===========================")
                                korban = []
                                for s in gs.members:
                                	if _name in s.displayName:
                          	          korban.append(s.mid)
                                for _name in korban:
                                    if _name not in D_BOSS + D_LOVE:
                                    	random.choice(D_WARS).kickoutFromGroup(GS,[_name])
                                    ME.sendMessage(msg.to, "🗡️  Misi Sukses...")
                            except:
                            	pass
                       
#=========[REMOTE KELUAR MASUK BOT N INVITE OWNER]==================#
                        elif D.startswith("zget "):
                          if msg._from in D_BOSS:
                            separate = msg.text.split(" ")
                            group = str(separate[1])
                            mids = str(separate[2])
                            name = text.replace("zget " + str(group) + " ","")
                            groups = ME.getGroupIdsJoined()
                            target = ME.getContact(mids).displayName                            
                            try:
                                GS = groups[int(group)-1]
                                gs = ME.getGroup(GS)
                                ME.findAndAddContactsByMid(name)
                                ME.findAndAddContactsByMid(name)
                                H1.findAndAddContactsByMid(name)
                                H2.findAndAddContactsByMid(name)
                                H3.findAndAddContactsByMid(name)
                                H4.findAndAddContactsByMid(name)
                                target = ME.getContact(mids).displayName
                                ME.sendMessage(msg.to, "   🔰 REMOTE INVITE MEMBER 🔰\n===========================\n🗡️ Target Name :\n "+target+"\n🗡️ Target Group :\n "+str(gs.name)+"\n===========================")
                                if name not in gs.members:
                                    ME.sendMessage(msg.to,"__Target Sdh Ada Didalam Group")
                                if name not in gs.members:
                                    try:
                                        ME.inviteIntoGroup(GS,[name])
                                    except:
                                        try:
                                            ME.inviteIntoGroup(GS,[name])
                                        except:
                                            try:
                                                H1.inviteIntoGroup(GS,[name])
                                            except:
                                                try:
                                                    H2.inviteIntoGroup(GS,[name])
                                                except:
                                                    try:
                                                        H3.inviteIntoGroup(GS,[name])
                                                    except:
                                                        try:
                                                            H4.inviteIntoGroup(GS,[name])
                                                            ME.sendMessage(msg.to, "🗡️  Sukses invite : "+target+"\n\n🗡️ Ke Group :\n  "+str(gs.name))
                                                        except: pass
                                                            
                            except:
                            	pass
                        
                        elif D.startswith("zinv "):
                          if msg._from in D_BOSS:
                          	separate = msg.text.split(" ")
                          G = msg.text.replace(separate[0] + " ","")
                          gs = ME.getGroup(G)
                          if G == "":
                          	ME.sendMessage(msg.to,"__Invalid Group Id")
                          else:
                          	ME.findAndAddContactsByMid(sender)
                          ME.findAndAddContactsByMid(sender)
                          H1.findAndAddContactsByMid(sender)
                          H2.findAndAddContactsByMid(sender)
                          H3.findAndAddContactsByMid(sender)
                          H4.findAndAddContactsByMid(sender)
                          H5.findAndAddContactsByMid(sender)
                          try:
                              ME.inviteIntoGroup(G,[sender])
                          except:
                              try:
                                  ME.inviteIntoGroup(G,[sender])
                              except:
                                  try:
                                      H1.inviteIntoGroup(G,[sender])
                                  except:
                                      try:
                                          H2.inviteIntoGroup(G,[sender])
                                      except:
                                          try:
                                              H3.inviteIntoGroup(G,[sender])
                                          except:
                                              try:
                                                  H4.inviteIntoGroup(G,[sender])
                                              except:
                                                  try:
                                                      H5.inviteIntoGroup(G,[sender])
                                                      ME.sendMessage(msg.to,"__Sukses Inv Owner To Group: \n   " + str(gs.name))
                                                  except: pass
                        
                        elif D.startswith("zjointo "):
                          if msg._from in D_BOSS:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = ME.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                GS = groups[int(number)-1]
                                G = ME.getGroup(GS)
                                G.preventedJoinByTicket = False
                                ME.updateGroup(G)
                                invsend = 0
                                PLC = ME.reissueGroupTicket(GS)
                                H1.acceptGroupInvitationByTicket(GS,PLC)
                                H2.acceptGroupInvitationByTicket(GS,PLC)
                                H3.acceptGroupInvitationByTicket(GS,PLC)
                                H4.acceptGroupInvitationByTicket(GS,PLC)
                                H5.acceptGroupInvitationByTicket(GS,PLC)
                            except:
                            	pass
                        
                        elif D.startswith("zleave "):
                          if msg._from in D_BOSS:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = ME.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                H1.leaveGroup(group)
                                H2.leaveGroup(group)
                                H3.leaveGroup(group)
                                H4.leaveGroup(group)
                                H5.leaveGroup(group)
                                ME.leaveGroup(group)
                                ME.sendMessage(msg.to,"__Sukses keluar dari :\n   " + str(G.name))
                            except:
                                pass
                        
#======================[REMOTE CANCEL & RATAIN ROOM]========================#
                        elif D == 'c a' or D == 'canc a':
                          if msg._from in D_BOSS:
                          	GR = ME.getGroup(msg.to)
                          TRGT = [contact.mid for contact in GR.invitee]
                          for BL in TRGT:
                          	if BL not in D_BOSS:
                          	    random.choice(D_WARS).cancelGroupInvitation(msg.to,[BL])
                        elif D.startswith("zpend "):
                          if msg._from in D_BOSS:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = ME.getGroupIdsJoined()
                            try:
                                GS = groups[int(number)-1]
                                G = ME.getGroup(GS)
                                TRGT = [contact.mid for contact in G.invitee]
                                ret_ = "GROUP "+G.name
                                no = 0
                                if G.invitee is None or G.invitee == []:
                                	ME.sendMessage(msg.to,"__Tidak ada pendingan")
                                for pending in G.invitee:
                                	no += 1
                                ret_ += "\n__Total Pendingan  : {} orang".format(str(len(G.invitee)))
                                ME.sendMessage(to, str(ret_))
                            except:
                            	pass
                        elif D.startswith("zcancel "):
                          if msg._from in D_BOSS:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = ME.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                GS = groups[int(number)-1]
                                G = ME.getGroup(GS)
                                TRGT = [contact.mid for contact in G.invitee]
                                for BL in TRGT:
                                	if BL not in D_BOSS:
                                	    if BL not in D_LOVE:
                                	        random.choice(D_WARS).cancelGroupInvitation(GS,[BL])
                                ME.sendMessage(msg.to,"__Sukses Menghapus : " + str(len(TRGT)) + " Pending Invite\n\n__Group : " + str(G.name))
                            except:
                            	pass
                        
                        elif D.startswith("zclean "):
                            if msg._from in D_BOSS:
                                separate = msg.text.split(" ")
                                number = msg.text.replace(separate[0] + " ","")
                                GR = ME.getGroupIdsJoined()
                                GS = GR[int(number)-1]
                                G = ME.getGroup(GS)
                                KRBN = [contact.mid for contact in G.members]
                                for X in KRBN:
                                    if X not in D_BOT:
                                        if X not in D_BOSS:
                                            ZL = [H1,H2,H3,H4,H5]
                                            LZ = random.choice(LZ)
                                            LZ.kickoutFromGroup(GS,[X])
                        
                        elif D == "z nodes":
                            if msg._from in D_BOSS:
                                if msg.toType == 2:
                                    G = ME.getGroup(msg.to)
                                    KRBN = [contact.mid for contact in G.members]
                                    for X in KRBN:
                                        if X not in D_BOT:
                                            if X not in D_BOSS:
                                                ZL = [H1,H2,H3,H4,H5]
                                                LZ = random.choice(LZ)
                                                LZ.kickoutFromGroup(msg.to,[X])
                                	
#====================================================================================================# 

                    if "/ti/g/" in text.lower():
                     if msg._from in D_BOSS:
                        if D_NILLA["JOINLINK"] == True:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                    n_links.append(l)
                            for ticket_id in n_links:
                                group = ME.findGroupByTicket(ticket_id)
                                ME.acceptGroupInvitationByTicket(group.id,ticket_id)
                                ME.sendMessage(msg.to,"__Sukses Join...\n\n__Group : \n%s" % str(group.name))

#=========================================================================================================#
    except Exception as error:
        logError(error)
        if op.type == 59:
            print (op)
while True:
    try:
      ops=oepoll.singleTrace(count=50)
      if ops != None:
        for op in ops: 
          bot(op)
          oepoll.setRevision(op.revision)
    except:
    	pass
