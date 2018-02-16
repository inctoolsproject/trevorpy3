# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
import time, random, sys, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, urllib2, wikipedia,tempfile,glob,shutil,unicodedata,goslate
from gtts import gTTS

cl = LINETCR.LINE()
cl.login(token="Ep6PefKEFxvnj1ybFZ61.Oku9Ylp0lStrGqdMVJBWeq.3lVxBOvKzGKORE7LqCFRtrA6MbTAF5ZOb8dchFsog/E=")
cl.loginResult()

ki = kk = kc = cl

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage =""" - Astrobot
[😹 COMMAND FOR GROUP😹]
[😹]===========================[😹]
[😹]Mentionall➡️ Untuk tagsemua member
[😹]Cek➡️ Untuk cek sider
[😹] Creator ➡️ Cek My Creator/Pembuat BOT
[😹]Sider➡️ Untuk mengetahui sider luknut
[😹]Sp➡️ Cek Speed Astro
[😹]Lirik  ➡️ Mencari lirik lagu
[😹]/instagram 
[😹]/music [lagu yang diinginkan][😹]
[😹]/fb [nama fbnya]
[😹]/twitter [usernametwitter]
[😹]/google
[😹]/admin  ➡ Tentang Bot
[😹]/say-jp ➡  bahasa jepang
[😹]/say-en  ➡  Bahasa Inggris
[😹]/say   ➡   Say untuk Voice 
[😹]Translate-eng  ➡  Translate Ke Inggris
[😹]Translate-jp ➡  Translate ke Jepang
[😹]Translate-th ➡  Translate ke Thailand
[😹]Checkmid: ➡  Check Mid Kontak
[😹]Profileig ➡  Cek Profile Instagram
[😹]Kalender ➡  Kalender ajalah ribet
[😹]playstore  ➡  searching
[😹]Apakah ➡  Kerang ajaib
[😹]ytube: ➡ searching youtube
[😹]Image ➡  Lu cari gambar apa aja
[😹]/bye  ➡   Mengeluarkan bot
[😹]=============================[😹]
[😹]Created By:http://line.me/ti/p/%40qwh5784m[😹]"""

about ="""ASTROBOT PUBLIC
Support Team:
 ➡CREATOR ASTROBOT
 ➡TEAM JOKER BOT
Support By:
 ➡ line.me/ti/p/~michaelf05
 ➡ line.me/ti/p/~aandreaas
 ➡ line.me/ti/p/~mysthic21
Untuk kritik dan saran Hub :http://line.me/ti/p/%40qwh5784m
"""

siskacantik ="""
[❤] siska cantik1
[❤] siska cantik2
[❤] siska cantik3
[❤] siska cantik4
[❤] siska loli1
[❤] siska loli2
[❤] siska alay
[❤] siska muka ngantuk
"""

Setgroup ="""

[😹] Pq on/off
[😹]Cbroadcast
[😹]Spam:
[😹] Contact on/off
[😹] Cancl on/off
[😹] Kickjoin on/off
[😹] Sensi on/off
[😹] Friendlist
[😹] Memlist
[😹] Friendinfo:
[😹] Friendpict:
[😹] Friendlistmid
[😹] Blocklist
[😹] G:L
[😹] Gruplistmid
[😹] Grupimage:
[😹] InviteMeTo: """

KAC=[cl,ki,kk,kc]
DEF=[ki,kk,kc]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid,"ua6cc2bfe8e9808aabff052aaeb98d5cd","u2b002b6d9738337dfa382dcd0bd23be3","u0f70e6c3817faeee7eae008025c01535","ua87810961d8822889217ef0eb64262cf","ucd28972c661bc5bfe3b347ffbdb40181","ua2b63ed69d7869bd1a85f5154717db00"]
admin=["u907eaacfec22116ced9b20175b27a2ee","uecc0e521c7c6f1a7c9e09bc2bb019523","u7d656f93e05d3fe3ba5090940b634abe","ua839713afa40928bbac0f55df34b0825","u366eaabbae79e8127840ae67030bc5a8","u366eaabbae79e8127840ae67030bc5a8","ua6cc2bfe8e9808aabff052aaeb98d5cd","ue7b3b382c8b47cc4189f7f47d8b5cebd","u8c0c05e9782fbf6776eabd9b5deb3229","uee36a80053c5f5814787d2858422d479","ua87810961d8822889217ef0eb64262cf","ucd28972c661bc5bfe3b347ffbdb40181","u2b002b6d9738337dfa382dcd0bd23be3","u0f70e6c3817faeee7eae008025c01535","ua2b63ed69d7869bd1a85f5154717db00"]
admsa=["u907eaacfec22116ced9b20175b27a2ee","uecc0e521c7c6f1a7c9e09bc2bb019523","u7d656f93e05d3fe3ba5090940b634abe","ua839713afa40928bbac0f55df34b0825","u366eaabbae79e8127840ae67030bc5a8","ucd28972c661bc5bfe3b347ffbdb40181"]
owner=["u907eaacfec22116ced9b20175b27a2ee","uecc0e521c7c6f1a7c9e09bc2bb019523"]
trev = cl.getContact('uecc0e521c7c6f1a7c9e09bc2bb019523')

wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':False,
    'tag':False,
    'autoAdd':False,
    "stiker":False,
    'alwaysReadgc':False,
    'alwaysReadpc':False,
    'message':"Thanks for adding me\nFollow my instagram; instagram.com/michaelf.s",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"Astrobot Public",
    "cName2":"Astro 1",
    "cName3":"Astro 2",
    "cName4":"Astro 3",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Protectgr":False,
    "Protectjoin":False,
    "alwayReader":False,
    "Protectcancl":False,
    "protectionOn":False,
    "atjointicket":True,
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']

settings = {
    "simiSimi":{},
     }
     
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def yt(query):
	with requests.session() as s:
		isi = []
		if query == "":
			query = "S1B nrik"
        s.headers['user-agent'] = 'Mozilla/5.0'
					 
        url    = 'http://www.youtube.com/results'
        params = {'search_query': query}
					 
        r    = s.get(url, params=params)
        soup = BeautifulSoup(r.content, 'html5lib')
					 
        for a in soup.select('.yt-lockup-title > a[title]'):
            if '&List' not in a['href']:
				if 'watch?v' in a['href']:
					b = a['href'].replace('watch?v=','')
					isi += ['youtu.be' + b]
        return isi    
	
def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "\n・" + Name
        else:
            pass
    except:
        pass

def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.contentType == 0:
            try:
                if msg.to in wait['readPoint']:
                    if msg.from_ in wait["ROM"][msg.to]:
                        del wait["ROM"][msg.to][msg.from_]
                else:
                    pass
            except:
                pass
        else:
            pass
    except KeyboardInterrupt:
	       sys.exit(0)
    except Exception as error:
        print error
        print ("\n\nRECEIVE_MESSAGE\n\n")
        return

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib,request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items

def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
					
		if op.type == 32:
			if wait["Protectgr"] == True:
				if op.param2 not in Bots + admin:
					ki.findAndAddContactByMid(op.param3)
					ki.inviteIntoGroup(op.param1,[op.param3])
					ki.kickoutFromGroup(op.param1,[op.param2])
			else:
				pass
        if op.type == 15:
			group = cl.getGroup(op.param1)
			cb = Message()
			cb.to = op.param1
			cb.text = "Good bye " + cl.getContact(op.param2).displayName
			cl.sendMessage(cb)
			print op.param2 + "has left the group"
        #------Protect Group Kick start------#
        if op.type == 11:
            if wait["Protectgr"] == True:
                if ki.getGroup(op.param1).preventJoinByTicket == False:
                    if op.param2 in Bots:
                        pass
                    if op.param2 in admin:
                        pass
                    else:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
                        ki.reissueGroupTicket(op.param1)
                        X = ki.getGroup(op.param1)
                        X.preventJoinByTicket = True
                        ki.updateGroup(X)
                        print "Url Opened, Autokick on"
                else:
                    print "random group update"
            else:
                pass
        #------Protect Group Kick finish-----#
        if op.type == 26:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                cl.sendText(msg.to, data['result']['response'].encode('utf-8'))
        #------Cancel Invite User start------#
        if op.type == 26:
            msg = op.message
            if wait["alwaysReadgc"] == True:     
                if msg.toType == 0:
                    cl.sendChatChecked(msg.to,msg.id)
                else:
                    cl.sendChatChecked(msg.to,msg.id)
                    print "AUTO READ GROUP"
        if op.type == 26:
            msg = op.message
            if wait["alwaysReadpc"] == True:     
                if msg.toType == 0:
                    cl.sendChatChecked(msg.from_,msg.id)
                else:
                    cl.sendChatChecked(msg.from_,msg.id)
                    print "Auto Read Personal Chat"
        #------Cancel Invite User Finish------#
        #--------------------------------------#
	if op.type == 13:
			if wait["Protectcancl"] == True:
				try:
					X = ki.getGroup(op.param1)
					gInviMids = [contact.mid for contact in X.invitee]
					ki.cancelGroupInvitation(op.param1, gInviMids)
					print "invite canceled"
				except:
					try:
						print "Retry canceling invitation"
						X = kk.getGroup(op.param1)
						gInviMids = [contact.mid for contact in X.invitee]
						kk.cancelGroupInvitation(op.param1, gInviMids)
						print "invite canceled"
					except:
						print "Bot can't cancel the invitation"
		
        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    cl.acceptGroupInvitation(op.param1)
                    print "BOT 1 Joined"
                else:
                    print "autoJoin is Off"
            else:
				pass
		
        if op.type == 13:
            if op.param3 in mid:
                if op.param2 in Amid:
                    G = Amid.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    Amid.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    Amid.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)

            if op.param3 in Amid:
                if op.param2 in mid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)

            if op.param3 in Bmid:
                if op.param2 in Amid:
                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)

            if op.param3 in Cmid:
                if op.param2 in Bmid:
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                
            if op.param3 in Dmid:
                if op.param2 in Cmid:
                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ks.updateGroup(X)
                    Ti = ks.reissueGroupTicket(op.param1)
                
            if op.param3 in Emid:
                if op.param2 in Dmid:
                    X = ks.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ks.updateGroup(X)
                    Ti = ks.reissueGroupTicket(op.param1)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ka.updateGroup(X)
                    Ti = ka.reissueGroupTicket(op.param1)
                
            if op.param3 in Fmid:
                if op.param2 in Emid:
                    X = ka.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ka.updateGroup(X)
                    Ti = ka.reissueGroupTicket(op.param1)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kb.updateGroup(X)
                    Ti = kb.reissueGroupTicket(op.param1)
                
            if op.param3 in Gmid:
                if op.param2 in Fmid:
                    X = kb.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kb.updateGroup(X)
                    Ti = kb.reissueGroupTicket(op.param1)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ko.updateGroup(X)
                    Ti = ko.reissueGroupTicket(op.param1)
                
            if op.param3 in Hmid:
                if op.param2 in Gmid:
                    X = ko.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ko.updateGroup(X)
                    Ti = ko.reissueGroupTicket(op.param1)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ke.updateGroup(X)
                    Ti = ke.reissueGroupTicket(op.param1)
                    
            if op.param3 in Imid:
                if op.param2 in mid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)        
			   
        #------Joined User Kick start------#
		if op.type == 17:
			if op.param2 in wait["blacklist"]:
				try:
					ki.kickoutFromGroup(op.param1, op.param2)
				except:
					random.choice(KAC).kickoutFromGroup(op.param1, op.param2)

        if op.type == 17:
			if wait["Protectjoin"] == True:
				if op.param2 not in Bots:
					random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
        if op.type == 55:
			if wait["alwayReader"] == True:
				if op.param2 not in Bots:
					random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
        #------Joined User Kick start------#

        if op.type == 17:
            group = cl.getGroup(op.param1)
            cb = Message()
            cb.to = op.param1
            cb.text = "Hi " + cl.getContact(op.param2).displayName + ", welcome to " + group.name
            cl.sendMessage(cb)

        if op.type == 19:
			print "someone was kicked"
			if op.param2 in admin:
				print "Admin has been kicked"
				if op.param2 in Bots:
					pass
				if op.param2 in admsa:
					pass
				else:
					cl.kickoutFromGroup(op.param1,[op.param2])
					wait["blacklist"][op.param2] = True
					print "kicker kicked"
					try:
						cl.inviteIntoGroup(op.param1,[op.param3])
					except:
						cl.inviteIntoGroup(op.param1,[op.param3])
				print "Admin invited back"      

			if mid in op.param3:
				print "BOT1 has been kicked"
				if op.param2 in Bots:
					pass
				if op.param2 in admin:
					pass
				else:
					ki.kickoutFromGroup(op.param1,[op.param2])
					wait["blacklist"][op.param2] = True
					print "kicker kicked"
					G = random.choice(KAC).getGroup(op.param1)
					G.preventJoinByTicket = False
					ki.updateGroup(G)
					Ti = ki.reissueGroupTicket(op.param1)
					cl.acceptGroupInvitationByTicket(op.param1,Ti)
					X = ki.getGroup(op.param1)
					X.preventJoinByTicket = True
					ki.updateGroup(X)
					Ti = ki.reissueGroupTicket(op.param1)
					print "BOT1 Joined"
				
			if Amid in op.param3:
				print "BOT2 has been kicked"
				if op.param2 in Bots:
					pass
				if op.param2 in admin:
					pass
				else:
					cl.kickoutFromGroup(op.param1,[op.param2])
					wait["blacklist"][op.param2] = True
					print "kicker kicked"
					G = random.choice(KAC).getGroup(op.param1)
					G.preventJoinByTicket = False
					cl.updateGroup(G)
					Ti = cl.reissueGroupTicket(op.param1)
					ki.acceptGroupInvitationByTicket(op.param1,Ti)
					X = cl.getGroup(op.param1)
					X.preventJoinByTicket = True
					cl.updateGroup(X)
					Ti = cl.reissueGroupTicket(op.param1)
					print "BOT2 Joined"
				
			if Bmid in op.param3:
				print "BOT3 has been kicked"
				if op.param2 in Bots:
					pass
				if op.param2 in admin:
					pass
				else:
					cl.kickoutFromGroup(op.param1,[op.param2])
					wait["blacklist"][op.param2] = True
					print "kicker kicked"
					G = random.choice(KAC).getGroup(op.param1)
					G.preventJoinByTicket = False
					cl.updateGroup(G)
					Ti = cl.reissueGroupTicket(op.param1)
					kk.acceptGroupInvitationByTicket(op.param1,Ti)
					X = cl.getGroup(op.param1)
					X.preventJoinByTicket = True
					cl.updateGroup(X)
					Ti = cl.reissueGroupTicket(op.param1)
					print "BOT3 Joined"
				
			if Cmid in op.param3:
				print "BOT4 has been kicked"
				if op.param2 in Bots:
					pass
				if op.param2 in admin:
					pass
				else:
					cl.kickoutFromGroup(op.param1,[op.param2])
					wait["blacklist"][op.param2] = True
					print "kicker kicked"
					G = random.choice(KAC).getGroup(op.param1)
					G.preventJoinByTicket = False
					cl.updateGroup(G)
					Ti = cl.reissueGroupTicket(op.param1)
					kc.acceptGroupInvitationByTicket(op.param1,Ti)
					X = cl.getGroup(op.param1)
					X.preventJoinByTicket = True
					cl.updateGroup(X)
					Ti = cl.reissueGroupTicket(op.param1)
					print "BOT4 Joined"
				
			else:
				if wait["Protectgr"] == True:
					if op.param2 in Bots + admin:
						pass
					else:
						ki.kickoutFromGroup(op.param1,[op.param2])
						kk.kickoutFromGroup(op.param1,[op.param2])
						kc.kickoutFromGroup(op.param1,[op.param2])
						wait["blacklist"][op.param2] = True
						print "autokick executed"
                    
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "ue11fc7860247c63bd3da149613a793f6":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to,"error")
        if op.type == 26:
            msg = op.message
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"Already in blacklist")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"Decided not to comment.")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Removed from blacklist.")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"There's no target in blacklist.")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"Already in blacklist")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Added to blacklist.")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Removed from blacklist.")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"There's no target in blacklist.")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"display name : " + msg.contentMetadata["displayName"] + "\n\nmid : " + msg.contentMetadata["mid"] + "\n\nstatus message : " + contact.statusMessage + "\n\ndisplay picture : http://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\ncover URL : " + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"display name : " + msg.contentMetadata["displayName"] + "\n\nmid : " + msg.contentMetadata["mid"] + "\n\nstatus message : " + contact.statusMessage + "\n\ndisplay picture : http://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\ncover URL : " + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
					msg.contentType = 0
					msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
					cl.sendMessage(msg)
            elif msg.text is None:
                return
            elif msg.text.lower() == 'help':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif msg.text.lower() == '/admin':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,about)
                else:
                    cl.sendText(msg.to,helpt)
                    
            elif msg.text.lower() == 'set':
				if msg.from_ in admin:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,Setgroup)
					else:
						cl.sendText(msg.to,Sett)
				else:
					cl.sendText(msg.to,"Command denied.")
					cl.sendText(msg.to,"Admin permission required.")
            elif ("Gn " in msg.text):
	       if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Kick ","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Invite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "inv: " in msg.text:
              if msg.from_ in admin:
                gid = msg.text.replace("inv: ","")
                if gid == "":
                    cl.sendText(msg.to,"invalid group id.")
                else:
                    try:
						cl.findAndAddContactsByMid(msg.from_)
						cl.inviteIntoGroup(gid,[msg.from_])
						cl.sendText(msg.to,"invited.")
                    except:
						cl.sendText(msg.to,"you are has been invited.")
            elif "leave: " in msg.text:
              if msg.from_ in admin:
                gid = msg.text.replace("leave: ","")
                if gid == "":
                    cl.sendText(msg.to,"invalid group id.")
                else:
                    try:
						cl.leaveGroup(gid)
						cl.sendText(msg.to,"Bot leaving the group.")
                    except:
						cl.sendText(msg.to,"Bot has left the group.")
            elif msg.text in ["Bot?"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                kc.sendMessage(msg)
            elif msg.text in ["Creator","creator"]:
                msg.contentType = 13
                cl.sendText(msg.to, "Follow instagram.com/michaelf.s")
                msg.contentMetadata = {'mid': 'uecc0e521c7c6f1a7c9e09bc2bb019523'}
                cl.sendMessage(msg)
            elif msg.text in ["Me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                cl.sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Open url","open url"]:
                if msg.from_ in admin:
		   if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Invite by link open")
                    else:
                        cl.sendText(msg.to,"Already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Close url","close url"]:
			  if msg.from_ in admin:
				if msg.toType == 2:
					X = cl.getGroup(msg.to)
					X.preventJoinByTicket = True
					cl.updateGroup(X)
					if wait["lang"] == "JP":
						cl.sendText(msg.to,"Invite by link Close")
					else:
						cl.sendText(msg.to,"Already close")
				else:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,"Can not be used outside the group")
					else:
						cl.sendText(msg.to,"Not for use less than group")
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"group name :\n" + str(ginfo.name) + "\n\ngid :\n" + msg.to + "\n\ngroup creator :\n" + gCreator + "\n\nprofile status :\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nmembers : " + str(len(ginfo.members)) + " members\npending : " + sinvitee + " people\nQR/Link : " + u + " it is inside")
                    else:
                        cl.sendText(msg.to,"group name :\n" + str(ginfo.name) + "\n\ngid :\n" + msg.to + "\n\ngroup creator :\n" + gCreator + "\n\nprofile status :\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nmembers : " + str(len(ginfo.members)) + " members\npending : " + sinvitee + " people\nQR/Link : " + u + " it is inside")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text.lower() == "id group":
                cl.sendText(msg.to,msg.to)
            elif msg.text.lower() == "my mid":
                cl.sendText(msg.to, msg.from_)
            elif msg.text.lower() == "Mid all":
			  if msg.from_ in admin:
				cl.sendText(msg.to,mid)
				ki.sendText(msg.to,Amid)
				kk.sendText(msg.to,Bmid)
				kc.sendText(msg.to,Cmid)
            elif msg.text in ["Wkwkwk","Wkwk","Wk","wkwkwk","wkwk","wk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Hehehe","Hehe","He","hehehe","hehe","he"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Galau"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["You"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Please"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Haaa"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Lol"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hmmm","Hmm","Hm","hmmm","hmm","hm"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Welcome"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["TL: "]:
			  if msg.from_ in admin:	
				tl_text = msg.text.replace("TL: ","")
				cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Mc "]:
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text in ["Readgc:on","R:on"]:
               if msg.from_ in admin:
                   wait["alwaysReadgc"] = True
                   cl.sendText(msg.to,"Sudah Read Tuan")
               else:
                   cl.sendText(msg.to,"Already Trev")
            elif msg.text in ["Readgc:off","R:off"]:
               if msg.from_ in admin:
                   wait["alwaysReadgc"] = False
                   cl.sendText(msg.to,"Sudah off Read Tuan")
               else:
                   cl.sendText(msg.to,"Already Trev")
            elif msg.text in ["Readpc:on","Rpc:on"]:
               if msg.from_ in admin:
                   wait["alwaysReadpc"] = True
                   cl.sendText(msg.to,"Sudah off Read Tuan")
               else:
                   cl.sendText(msg.to,"Already Trev")  
            elif msg.text in ["Readpc:off","Rpc:off"]:
               if msg.from_ in admin:
                   wait["alwaysReadpc"] = False
                   cl.sendText(msg.to,"Sudah off Read Tuan")
               else:
                   cl.sendText(msg.to,"Already Trev")
            elif msg.text in ["Sensi on","S:on"]:
              if msg.from_ in admin:   
                 wait["alwayReader"] = True
                 cl.sendText(msg.to,"Sensi on Tuan")
              else:
                 cl.sendText(msg.to,"Sensi sudah on dari tadi Tuan")
            elif msg.text in ["C:on"]:
                 wait["stiker"] = True
                 cl.sendText(msg.to,"On Astro")
            elif msg.text in ["C:off"]:
                 wait["stiker"] = False
                 cl.sendText(msg.to,"Off Astro")
            elif msg.text in ["Sensi off","S:off"]:
              if msg.from_ in admin:
                 wait["alwayReader"] = False
                 cl.sendText(msg.to,"Sensi off Tuan")
              else:
                 cl.sendText(msg.to,"Sudah off dari tadi Tuan")
            elif msg.text in ["Simisimi on","Simisimi:on"]:
                settings["simiSimi"][msg.to] = True
                cl.sendText(msg.to,"Simi Simi on yuk curhat sama astro")
                
            elif msg.text in ["Simisimi off","Simisimi:off"]:
                settings["simiSimi"][msg.to] = False
                cl.sendText(msg.to,"Simi Off :(") 
                
            elif msg.text in ["Kickjoin on"]:
              if msg.from_ in admin:
                if wait["Protectjoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectjoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Kickjoin off"]:
              if msg.from_ in admin:
                if wait["Protectjoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectjoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancl on","cancl on"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancl off","cancl off"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Pq on","pq on"]:
              if msg.from_ in admin:
                if wait["Protectgr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group On")
                    else:
                        cl.sendText(msg.to,"done")
                        
            elif msg.text in ["Pq off","pq off"]:
              if msg.from_ in admin:
                if wait["Protectgr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact On","Contact on","contact on"]:
              if msg.from_ in admin:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact Off","Contact off","contact off"]:
              if msg.from_ in admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ³","Join on","Auto join:on","è‡ªå‹•å�ƒåŠ ï¼šé–‹"]:
				if msg.from_ in admin:	
					if wait["autoJoin"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoJoin"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ•","Join off","Auto join:off","è‡ªå‹•å���ƒåŠ ï¼šé—œ"]:
				if msg.from_ in admin:
					if wait["autoJoin"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoJoin"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
				if msg.from_ in admin:	
					if wait["timeline"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["timeline"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text.lower() == 'autoleave on':
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave room set to on")
                    else:
                        cl.sendText(msg.to,"Auto Leave room already on")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave room set to on")
                    else:
                        cl.sendText(msg.to,"Auto Leave room already on")
            elif msg.text.lower() == 'autoleave off':
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave room set to off")
                    else:
                        cl.sendText(msg.to,"Auto Leave room already off")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave room set to off")
                    else:
                        cl.sendText(msg.to,"Auto Leave room already off")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
				if msg.from_ in admin:
					if wait["timeline"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["timeline"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
#===================================================
#===================================================
            elif msg.text.lower() == 'status':
			  if msg.from_ in admin:	
				md = ""
				if wait["Protectjoin"] == True: md+="ôﾀﾔﾃôﾀﾆﾑlockôﾏ﾿﾿  Block Join\n"
				else: md+=" Block Join Off\n"
				if wait["Protectgr"] == True: md+="￼   Block Group\n"
				else: md+=" Block Group Off\n"
				if wait["alwayReader"] == True: md+="ôﾀﾔﾃôﾀﾆﾑlockôﾏ﾿﾿  KickReader\n"
				else: md+=" KickReader Off\n"
				if wait["Protectcancl"] == True: md+="ôﾀﾔﾃôﾀﾆﾑlockôﾏ﾿﾿ Cancel All Invited\n"
				else: md+=" Cancel All Invited Off\n"
				if wait["contact"] == True: md+=" Contact : on\n"
				else: md+=" Contact : off\n"
				if wait["autoJoin"] == True: md+=" Auto join : on\n"
				else: md +=" Auto join : off\n"
				if wait["autoCancel"]["on"] == True:md+=" Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
				else: md+= " Group cancel : off\n"
				if wait["leaveRoom"] == True: md+=" Auto leave : on\n"
				else: md+=" Auto leave : off\n"
				if wait["timeline"] == True: md+=" Share : on\n"
				else:md+=" Share : off\n"
				if wait["autoAdd"] == True: md+=" Auto add : on\n"
				else:md+=" Auto add : off\n"
				if wait["commentOn"] == True: md+=" Comment : on\n"
				else:md+=" Comment : off\n"
				cl.sendText(msg.to,md)
            elif msg.text.lower() in ["Group id"]:
			  if msg.from_ in admin:	
				gid = cl.getGroupIdsJoined()
				h = ""
				for i in gid:
					h += "[ %s ] :\n%s\n\n" % (cl.getGroup(i).name,i)
				cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
			  if msg.from_ in admin:
				gid = cl.getGroupIdsInvited()
				for i in gid:
					cl.rejectGroupInvitation(i)
				if wait["lang"] == "JP":
					cl.sendText(msg.to,"All invitations have been refused")
				else:
					cl.sendText(msg.to,"æ‹’ç»�äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif msg.text in ["Gurl"]:
			  if msg.from_ in admin:
				if msg.toType == 2:
					x = cl.getGroup(msg.to)
					if x.preventJoinByTicket == True:
						x.preventJoinByTicket = False
						cl.updateGroup(x)
					gurl = cl.reissueGroupTicket(msg.to)
					cl.sendText(msg.to,"line://ti/g/" + gurl)
				else:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,"Can't be used outside the group")
					else:
						cl.sendText(msg.to,"Not for use less than group")
            elif msg.text.lower() == 'cek':
                    cl.sendText(msg.to, "Set point.")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                           pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M')
                    wait2['ROM'][msg.to] = {}
                    print wait2
                    print "[Command Cek sider Excuted]"
        
            elif msg.text.lower() == 'sider':
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "Readers:\n%s\nDate and time:\n[%s]"  % (chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "Type 'cek' to set point.")
                        print "[Command Sider excuted]"
#-----------------------------------------------
            elif "playstore " in msg.text.lower():
                    tob = msg.text.lower().replace("playstore ","")
                    cl.sendText(msg.to,"Wait ya kak :)")
                    cl.sendText(msg.to,"Title : "+tob+"\nSource : Google Play\nLinknya : https://play.google.com/store/search?q=" + tob)
                    cl.sendText(msg.to,"Ketemu kak ^.^")
            elif "Cbroadcast: " in msg.text:
               if msg.from_ in owner:
                  bc = msg.text.replace("Cbroadcast: ","")
                  gid = cl.getAllContactIds()
                  for i in gid:
                      cl.sendText(i, bc)
            elif "Spam change: " in msg.text:
                wait["spam"] = msg.text.replace("Spam change: ","")
                cl.sendText(msg.to,"spam changed")

            elif "Spam add: " in msg.text:
                wait["spam"] = msg.text.replace("Spam add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"spam changed")
                else:
                    cl.sendText(msg.to,"Done")
         
            elif "Spam: " in msg.text:
                strnum = msg.text.replace("Spam: ","")
                num = int(strnum)
                for var in range(0,num):
                    cl.sendText(msg.to, wait["spam"])
            elif 'Youtubemp4 ' in msg.text:
                    try:
                        textToSearch = (msg.text).replace('Youtubemp4 ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                        ght = ('https://www.youtube.com' + results['href'])
                        cl.sendVideoWithURL(msg.to, ght)
                    except:
                        cl.sendText(msg.to, "Could not find it")          
#-----------------------------------------------
         #----------------Fungsi Join Group Start-----------------------#
            elif msg.text in ["Astrobot join"]:
              if msg.from_ in admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "Bot Complete"
                        G.preventJoinByTicket(G)
                        cl.updateGroup(G)

            elif msg.text in ["Astro join"]:
              if msg.form_ in admin:
                  x = ki.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  ki.updateGroup(x)
                  invsend = 0
                  Ti = ki.reissueGroupTicket(msg.to)
                  cl.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(msg.to)

            elif msg.text in ["Astro1 join"]:
              if msg.from_ in admin:
                  x = cl.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  cl.updateGroup(x)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)

            elif msg.text in ["Astro2 join"]:
              if msg.from_ in admin:
                  x = cl.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  cl.updateGroup(x)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
                  
            elif msg.text in ["Astro3 join"]:
              if msg.from_ in admin:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kc.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
    #----------------------Fungsi Join Group Finish---------------#

    #-------------Fungsi Leave Group Start---------------#
            elif msg.text in ["Bye astro"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = ki.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["/bye"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.sendText(msg.to,"Kakak jahat :(")
                        cl.leaveGroup(msg.to)
                    except:
                        pass
    #-------------Fungsi Leave Group Finish---------------#
    
    #-------------Fungsi Tag All Start---------------#
            elif msg.text in ["Mentionall","Tagall"]:
                if msg.toType == 2:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      cl.sendMessage(msg)
                  except Exception as error:
                      print error
    #-------------Fungsi Tag All Finish---------------#

         #----------------Fungsi Banned Kick Target Start-----------------------#
            elif msg.text in ["Kill "]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        kk.sendText(msg.to,"Good Bye")
                        return
                    for jj in matched_list:
                        try:
                            klist=[ki,kk,kc]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
         #----------------Fungsi Banned Kick Target Finish----------------------#                

            elif "Sweep this group" in msg.text.lower():
              if msg.from_ in admsa:
                if msg.toType == 2:
                    print "sweeping"
                    _name = msg.text.replace("Sweep this group","")
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    ki.sendText(msg.to,"maaf kalo gak sopan")
                    kk.sendText(msg.to,"makasih semuanya..")
                    kc.sendText(msg.to,"hehehhehe")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': 'ue11fc7860247c63bd3da149613a793f6'}
                    cl.sendMessage(msg)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                          if target not in Bots:
						   if target not in admin:
							try:
								klist=[cl,ki,kk,kc]
								kicker=random.choice(klist)
								kicker.kickoutFromGroup(msg.to,[target])
								print (msg.to,[g.mid])
							except:
								pass

        #----------------Fungsi Kick User Target Start----------------------#
            elif "Nk " in msg.text:
                if msg.from_ in admin:
                    nk0 = msg.text.replace("Nk ","")
                    nk1 = nk0.lstrip()
                    nk2 = nk1.replace("@","")
                    nk3 = nk2.rstrip()
                    _name = nk3
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                           targets.append(s.mid)
                    if targets == []:
                        cl.sendMessage(msg.to,"user does not exist")
                        pass
                    else:
                        for target in targets:
						  if targets not in Bots:
						    if targets not in admin:
								try:
									klist=[cl,ki,kk,kc]
									kicker=random.choice(klist)
									ki.sendText(msg.to, "Good bye.")
									kicker.kickoutFromGroup(msg.to,[target])
									print (msg.to,[g.mid])
								except:
									pass
        #----------------Fungsi Kick User Target Finish----------------------#      
            #elif "Blacklist @" in msg.text:
                #_name = msg.text.replace("Blacklist @","")
                #_kicktarget = _name.rstrip(' ')
                #gs = ki2.getGroup(msg.to)
                #targets = []
                #for g in gs.members:
                    #if _kicktarget == g.displayName:
                        #targets.append(g.mid)
                        #if targets == []:
                            #cl.sendText(msg.to,"Not found")
                        #else:
                            #for target in targets:
                                #try:
                                    #wait["blacklist"][target] = True
                                    #f=codecs.open('st2__b.json','w','utf-8')
                                    #json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    #k3.sendText(msg.to,"Target locked.")
                                #except:
                                    #ki.sendText(msg.to,"error")
            
            #----------------Fungsi Banned User Target Start-----------------------#
            elif "Ban @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Banned] executed"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets in Bots:
                        cl.sendText(msg.to,"Can't ban bot")
                    else:
                        for target in targets:
                            try:
								wait["blacklist"][target] = True
								f=codecs.open('st2__b.json','w','utf-8')
								json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
								cl.sendText(msg.to,"Target locked.")
								print "[Banned] success"
                            except:
                                ki.sendText(msg.to,"Target already in blacklist.")
            #----------------Fungsi Banned User Target Finish-----------------------# 
            
            #----------------Fungsi Unbanned User Target Start-----------------------#
            elif "Unban @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Unban] executed"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Target not found")
                    else:
                        for target in targets:
                            try:
								del wait["blacklist"][target]
								f=codecs.open('st2__b.json','w','utf-8')
								json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
								cl.sendText(msg.to,"Target cleaned.")
								print "[Unban] success"
                            except:
                                ki.sendText(msg.to,"There's no target in blacklist.")
           #----------------Fungsi Unbanned User Target Finish-----------------------#
           
        #-------------Fungsi Spam Start---------------------#
            elif '􀔃􀆶up􏿿' in msg.text.lower():
                         cl.sendText(msg.to,"􀔃􀆶up􏿿")
                         
        #-------------Fungsi Spam Finish---------------------#
        #-------------Fungsi Friend List---------------------#
            elif msg.text in ["Friendlist"]:
               if msg.from_ in owner:
                contactlist = cl.getAllContactIds()
                kontak = cl.getContacts(contactlist)
                num=1
                msgs="═════════List Friend═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
                
            elif msg.text in ["Memlist"]:
               if msg.from_ in owner:
                kontak = cl.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="═════════List Member═════════-"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(group)
                cl.sendText(msg.to, msgs)
                
            elif "Friendinfo: " in msg.text:
               if msg.from_ in owner:
                saya = msg.text.replace('Friendinfo: ','')
                gid = cl.getAllContactIds()
                for i in gid:
                    h = cl.getContact(i).displayName
                    contact = cl.getContact(i)
                    cu = cl.channel.getCover(i)
                    path = str(cu)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    if h == saya:
                        cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                        cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                        cl.sendImageWithURL(msg.to,image)
                        cl.sendText(msg.to,"Cover " + contact.displayName)
                        cl.sendImageWithURL(msg.to,path)
                
            elif "Friendpict: " in msg.text:
               if msg.from_ in owner:
                saya = msg.text.replace('Friendpict: ','')
                gid = cl.getAllContactIds()
                for i in gid:
                    h = cl.getContact(i).displayName
                    gna = cl.getContact(i)
                    if h == saya:
                        cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
            
            elif msg.text in ["Friendlistmid"]:
               if msg.from_ in owner:
                gruplist = cl.getAllContactIds()
                kontak = cl.getContacts(gruplist)
                num=1
                msgs="═════════List FriendMid═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.mid)
                    num=(num+1)
                msgs+="\n═════════List FriendMid═════════\n\nTotal Friend : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
            
            elif msg.text in ["Blocklist"]:
               if msg.from_ in owner:
                blockedlist = cl.getBlockedContactIds()
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="═════════List Blocked═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Blocked═════════\n\nTotal Blocked : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
                
            elif msg.text in ["G:L"]:  
                gruplist = cl.getGroupIdsJoined()
                kontak = cl.getGroups(gruplist)
                num=1
                msgs="═════════List Grup═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.name)
                    num=(num+1)
                msgs+="\n═════════List Grup═════════\n\nTotal Grup : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
            
            elif msg.text in ["Gruplistmid"]:
               if msg.from_ in admin:
                gruplist = cl.getGroupIdsJoined()
                kontak = cl.getGroups(gruplist)
                num=1
                msgs="═════════List GrupMid═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.id)
                    num=(num+1)
                msgs+="\n═════════List GrupMid═══════���═\n\nTotal Grup : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
                    
            elif "Grupimage: " in msg.text:
               if msg.from_ in owner:
                saya = msg.text.replace('Grupimage: ','')
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).name
                    gna = cl.getGroup(i)
                    if h == saya:
                        cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)    
        #-------------Fungsi Broadcast Start------------#
            elif 'list gambar' in msg.text.lower():
                cl.sendText(msg.to,siskacantik)
            elif "Bc " in msg.text:
			  if msg.from_ in admin:
				bctxt = msg.text.replace("Bc ","")
				n = cl.getGroupIdsJoined()
				for manusia in n:
					cl.sendText(manusia, (bctxt))
       #--------------Fungsi Broadcast Finish-----------#
            elif 'siska muka ngantuk' in msg.text.lower():
                    try:
                        cl.sendImageWithURL(msg.to, "http://oi67.tinypic.com/2vnowzr.jpg")
                    except Exception as e:
                        sendMessage(msg.to, str(e))
            elif 'siska alay' in msg.text.lower():
                cl.sendImageWithURL(msg.to,"http://oi68.tinypic.com/n2oowp.jpg")
            elif 'siska cantik1' in msg.text.lower():
                cl.sendImageWithURL(msg.to,"http://oi67.tinypic.com/20gbac7.jpg")
            elif 'siska cantik2' in msg.text.lower():
                cl.sendImageWithURL(msg.to,"http://oi68.tinypic.com/2il1pw8.jpg")
            elif 'siska cantik3' in msg.text.lower():
                cl.sendImageWithURL(msg.to,"http://oi65.tinypic.com/or4gb5.jpg")
            elif 'siska cantik4' in msg.text.lower():
                cl.sendImageWithURL(msg.to,"http://oi64.tinypic.com/10mpq54.jpg")
            elif 'siska loli' in msg.text.lower():
                cl.sendImageWithURL(msg.to, "http://oi66.tinypic.com/331lngy.jpg")
            elif 'siska loli2' in msg.text.lower():
                cl.sendImageWithURL(msg.to,"http://oi63.tinypic.com/11r9chl.jpg")
        #--------------Fungsi Broadcast Finish-----------#           
            elif "/say-jp " in msg.text:
                say = msg.text.replace("/say-jp ","")
                lang = 'jp'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")   
            
            elif "/say-en " in msg.text:
                say = msg.text.replace("/say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
            
            elif "/say " in msg.text:
                 psn = msg.text.replace("/say ","")
                 tts = gTTS(psn, lang='id', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3') 
            
            elif "Checkid: " in msg.text:
                saya = msg.text.replace("Checkid: ","")
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).id
                    group = cl.getGroup(i)
                    if h == saya:
                        try:
                            creator = group.creator.mid 
                            msg.contentType = 13
                            msg.contentMetadata = {'mid': creator}
                            md = "Nama Grup :\n" + group.name + "\n\nID Grup :\n" + group.id
                            if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                            else: md += "\n\nKode Url : Diblokir"
                            if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                            else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                            cl.sendText(msg.to,md)
                            cl.sendMessage(msg)
                            cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ group.pictureStatus)
                        except:
                            creator = "Error"
            
            elif "Checkmid: " in msg.text:
                saya = msg.text.replace("Checkmid: ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":saya}
                cl.sendMessage(msg)
                contact = cl.getContact(saya)
                cu = cl.channel.getCover(saya)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                    cl.sendImageWithURL(msg.to,image)
                    cl.sendText(msg.to,"Cover " + contact.displayName)
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass     
                
            elif "kedapkedip" in msg.text.lower():
                txt = msg.text.replace("kedapkedip ", "")
                t1 = "\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xa0\x81\xf4\x80\xa0\x81\xf4\x80\xa0\x81"
                t2 = "\xf4\x80\x82\xb3\xf4\x8f\xbf\xbf"
                cl.sendText(msg.to, t1 + txt + t2)     
            elif "astro kick: " in msg.text:
                if msg.from_ in admin:
                    aa = msg.text.replace("astro kick: ","")
                    ab = aa.split(' ')
                    gid = ab[0]
                    cid = ab[1]
                    bb = cl.getGroup(gid)
                    ba = cl.getContact(cid)
                    cl.sendText(msg.to,"Target -> " + ba.displayName + "\nfrom group : " + bb.name)
                    random.choice(KAC).kickoutFromGroup(gid,[cid])
                    cl.sendText(msg.to,"Target kicked.")
                    print "Success Kickout From Group"
            elif 'astro close url: ' in msg.text:
                if msg.from_ in admin:
                    aa = msg.text.replace("astro close url: ","")
                    ab = aa.split(' ')
                    gid = ab[0]
                    Trevor = cl.getGroup(gid)
                    Trevor.preventJoinByTicket = True
                    cl.sendText(msg.to,"Target group ->" + Trevor.name)
                    random.choice(KAC).updateGroup(Trevor)
                    cl.sendText(msg.to,"Close url group success!")
                    print "Success Close Url"
            elif 'astro buka qr digrup: ' in msg.text:
                if msg.from_ in admin:
                    aa = msg.text.replace("astro buka qr digrup: ","")
                    ab = aa.split(' ')
                    gid = ab[0]
                    Trevor = cl.getGroup(gid)
                    Trevor.preventJoinByTicket = False
                    cl.sendText(msg.to,"Target group ->" + Trevor.name)
                    random.choice(KAC).updateGroup(Trevor)
                    cl.sendText(msg.to,"Qr berhasil di buka")
                    print "Success"        
            elif 'astro cancel invitation group: ' in msg.text:
                if msg.from_ in admin:
                  if msg.toType == 2:
                    aa = msg.text.replace("astro cancel invitation group: "," ")
                    ab = aa.split(' ')
                    gid = ab[0]
                    Trevor = cl.getGroup(gid)
                    if Trevor.invitee is not None:
                        gInviMids = [contact.mid for contact in Trevor.invitee]
                        cl.sendText(msg.to,"Target group ->" + Trevor.invitee.name)
                        cl.cancelGroupInvitation(msg.to,gInviMids)
                        cl.sendText(msg.to,"Success cancel all invitation group" + Trevor.invitee.name)
            elif msg.text in ["Cv say hi"]:
                ki.sendText(msg.to,"Hi buddy ôﾀﾜﾁôﾀﾅﾔHar Harôﾏ﾿﾿")
                kk.sendText(msg.to,"Hi buddy ôﾀﾜﾁôﾀﾅﾔHar Harôﾏ﾿﾿")
                kc.sendText(msg.to,"Hi buddy ôﾀﾜﾁôﾀﾅﾔHar Harôﾏ﾿﾿")

#-----------------------------------------------
            elif msg.text in ["Up"]:
                cl.sendText(msg.to,"￼")
                cl.sendText(msg.to,"￼")
                cl.sendText(msg.to,"￼")
                cl.sendText(msg.to,"￼")
                cl.sendText(msg.to,"￼")
                cl.sendText(msg.to,"￼")
                cl.sendText(msg.to,"￼")
                cl.sendText(msg.to,"￼")
                cl.sendText(msg.to,"￼")
                cl.sendText(msg.to,"￼")
                cl.sendText(msg.to,"￼")
                cl.sendText(msg.to,"￼")
                cl.sendText(msg.to,"￼")
                cl.sendText(msg.to,"￼")
                cl.sendText(msg.to,"￼")
                cl.sendText(msg.to,"￼")
                cl.sendText(msg.to,"￼")
                cl.sendText(msg.to,"￼")
                cl.sendText(msg.to,"￼")
                cl.sendText(msg.to,"￼")
                cl.sendText(msg.to,"￼")
                cl.sendText(msg.to,"￼")
                cl.sendText(msg.to,"￼")
                cl.sendText(msg.to,"￼")
                

            elif msg.text in ["astro"]:
                cl.sendText(msg.to,"Ya,ada apa kak? ketik 'help' yuk kak untuk bantuan")
            
#-----------------------------------------------
            elif 'apakah' in msg.text.lower():
                 jawaban = ["iya","tidak","bisa jadi"]
                 isi = random.choice(jawaban)
                 cl.sendText(msg.to,isi)
             
            elif "Image " in msg.text:
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass
            elif "Checkdate " in msg.text:
                tanggal = msg.text.replace("Checkdate ","")
                r = requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data = r.text
                data = json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                cl.sendText(msg.to,"============ H A S I L ============\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n============ F I N I S H ============")
            elif msg.text in ["Kalender","Time","Waktu"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): blan = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                cl.sendText(msg.to, rst)
            
            elif "Profileig " in msg.text:
                    try:
                        instagram = msg.text.replace("Profileig ","")
                        response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                        data = response.json()
                        namaIG = str(data['user']['full_name'])
                        bioIG = str(data['user']['biography'])
                        mediaIG = str(data['user']['media']['count'])
                        verifIG = str(data['user']['is_verified'])
                        usernameIG = str(data['user']['username'])
                        followerIG = str(data['user']['followed_by']['count'])
                        profileIG = data['user']['profile_pic_url_hd']
                        privateIG = str(data['user']['is_private'])
                        followIG = str(data['user']['follows']['count'])
                        link = "LinkNya: " + "https://www.instagram.com/" + instagram
                        text = "Name : "+namaIG+"\nUsername : "+usernameIG+"\nBiography : "+bioIG+"\nFollowerNya : "+followerIG+"\nFollowingNya : "+followIG+"\nPost : "+mediaIG+"\nVerified : "+verifIG+"\nPrivate : "+privateIG+"" "\n" + link
                        cl.sendText(msg.to, str(text))
                    except Exception as e:
                        cl.sendText(msg.to, str(e))  
                        print "[Command Instagram excuted]"
            elif "Lirik " in msg.text:
                try:
                    songname = msg.text.lower().replace("Lirik ","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as wak:
                        cl.sendText(msg.to, str(wak))
                        print "[Command Lyric excuted]"
            elif '/fb ' in msg.text.lower():
                    a = msg.text.replace('/fb ','')
                    replace = urllib.quote(a)
                    cl.sendText(msg.to,"「 Searching 」\n" "Type:Search Info\nStatus: Processing")
                    cl.sendText(msg.to, "https://www.facebook.com/search/str/"+ replace + "/keywords_search")
                    cl.sendText(msg.to,"「 Searching 」\n" "Type:Search Info\nStatus: Success")    
            elif '/google ' in msg.text.lower():
                    a = msg.text.replace('/google ','')
                    b = urllib.quote(a)
                    cl.sendText(msg.to,"「 Searching 」\n" "Type:Search Info\nStatus: Processing")
                    cl.sendText(msg.to, "https://www.google.com" + b)
                    cl.sendText(msg.to,"「 Searching 」\n" "Type:Search Info\nStatus: Success")    
            elif msg.text.lower() == 'bot restart':
              if msg.from_ in admin:
                    print "[Command]Like executed"
                    try:
                        cl.sendText(msg.to,"Restarting...")
                        restart_program()
                    except:
                        cl.sendText(msg.to,"Please wait")
                        restart_program()
                        pass        
            elif "Translate-eng " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.replace("Translate-eng ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'en')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate EN'
                except Exception as error:
                    cl.sendText(msg.to,(error))
            elif "Translate-jp " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.replace("Translate-jp ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'jp')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate jp'
                except Exception as error:
                    cl.sendText(msg.to,(error))
            elif "Translate-th " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.replace("Translate-th ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'th')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate th'
                except Exception as error:
                    cl.sendText(msg.to,(error))
            elif "Translate-idn " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.replace("Translate-id ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'id')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate ID'
                except Exception as error: 
                    cl.sendText(msg.to,(error))          
        
            elif '/music ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('/music ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[4])
		except Exception as njer:
		                cl.sendText(msg.to, str(njer))
		                print "[Commmand Music Excuted]"
                
	    elif "/Xvideos: " in msg.text.lower():
                    a = msg.text.replace("/Xvideos: ","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to,"「 Searching 」\n" "Type:Search Xvideos\nStatus: Processing")
                    cl.sendText(msg.to, "•••••••<{ Xvideos search page }>•••••••\n\nTitle:  "+b+"\nSource : Xvideos\nhttp://xvideos.com/?k=" +b)
                    cl.sendText(msg.to,"「 Searching 」\nType:Search Info\nStatus: Success")	                
            
            elif "/twitter" in msg.text.lower():
                    a = msg.text.replace("/twiterr","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to,"「 Searching 」\n" "Type:Search Info\nStatus: Processing")
                    cl.sendText(msg.to, "https://www.twitter.com" + b)
                    cl.sendText(msg.to,"「 Searching 」\n" "Type:Search Info\nStatus: Success")
	    elif '/instagram ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("/instagram ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "========INSTAGRAM INFO USER========\n"
                    details = "\n========INSTAGRAM INFO USER========"
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))	
	    elif msg.text.lower() == 'ifconfig':
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text.lower() == 'system':
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() == 'cpu':
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
       #-------------Fungsi Invite admin ke Grup---------------------#
            if "ytube: " in msg.text.lower():
            	cl.sendText(msg.to,"「􏿿 Youtube 」\nWaiting For: Youtube")
		query = msg.text.split(":")
		try:
		    if len(query) == 3:
	  	        isi = yt(query[2])
		        hasil = isi[int(query[1])-1]
		        cl.sendText(msg.to, 'Total search = ' + str(len(isi)) + " ini adalah hasil pencarian ke [" + str(query[1]) + "]")
		        cl.sendText(msg.to,"「􏿿 Youtube 」\n\nWaiting For Search Youtube..")
		        cl.sendText(msg.to, hasil)
		    else:
	                isi = yt(query[1])				
                        cl.sendText(msg.to, "Total search = " + str(len(isi)))
		        cl.sendText(msg.to, isi[0])
		        cl.sendAudio(msg.to, isi[0])
	 	except Exception as e:
	            print(e)
            elif "invitemeto:" in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("invitemeto: ","")
                    if gid == "":
                        cl.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            cl.sendText(msg.to,"Please wait..")
                            cl.findAndAddContactsByMid(msg.from_)
                            cl.inviteIntoGroup(gid,[msg.from_])
                        except:
                            cl.sendText(msg.to,"Maybe i'm not in that group")   
            elif 'pagi astro' in msg.text.lower():
                cl.sendText(msg.to,"Pagi juga kak ￼")
            elif 'Selamat malam' in msg.text.lower():
                cl.sendText(msg.to,"malam juga  kak ￼ ")
       #-------------Fungsi Respon Start---------------------#                
            elif msg.text in ["Astrobot"]:
			  if msg.from_ in admin:
				cl.sendText(msg.to,"I'm ready, Mikey!")
      #-------------Fungsi Respon Finish---------------------#
            elif msg.text in ["Remove all chat"]:
               if msg.from_ in owner:
                cl.removeAllMessages(op.param2)
                ki.removeAllMessages(op.param2)
                kk.removeAllMessages(op.param2)
                kc.removeAllMessages(op.param2)
                cl.sendText(msg.to,"Removed all chat")
      #-------------Fungsi Balesan Respon Finish---------------------#
            elif "Grup cancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Grup cancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Itu off undangan ditolak??\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan")
                        else:
                            cl.sendText(msg.to,"Off undangan ditolak??Sebutkan jumlah terbuka ketika Anda ingin mengirim")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis")
                        else:
                            cl.sendText(msg.to,strnum + "The team declined to create the following automatic invitation")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Nilai tidak benar")
                    else:
                        cl.sendText(msg.to,"Weird value")      

       #-------------Fungsi Speedbot Start---------------------#
            elif msg.text in ["Sp","Speed"]:
                start = time.time()
                cl.sendText(msg.to, "please wait...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%ss" % (elapsed_time))
      #-------------Fungsi Speedbot Finish---------------------#

      #-------------Fungsi Banned Send Contact Start------------------#
            elif msg.text in ["Ban"]:
	          if msg.from_ in admin:
				wait["wblacklist"] = True
				cl.sendText(msg.to,"send contact")
            elif msg.text in ["Unban"]:
			  if msg.from_ in admin:
				wait["dblacklist"] = True
				cl.sendText(msg.to,"send contact")
      #-------------Fungsi Banned Send Contact Finish------------------#
            elif msg.text == "tag:on":
              if msg.from_ in admin:
                if wait['tag'] == True:
                    cl.sendText(msg.to,"Mention notification is already on.")
                else:
                    wait['tag'] = True
                    cl.sendText(msg.to,"Mention notification is on.")
            elif msg.text == "tag:off":
              if msg.from_ in admin:
                if wait['tag'] == False:
                    cl.sendText(msg.to,"Mention notification is already off.")
                else:
                    wait['tag'] = False
                    cl.sendText(msg.to,"Mention notification is off.")
            elif "@"+trev.displayName in msg.text:
             if msg.from_ in Bots:
                 pass
             else:
              if wait['tag'] == True:
                at = msg.text.replace(" @"+trev.displayName,"")
                aa = cl.getContact(msg.from_).displayName
                ab = cl.getGroup(msg.to).name
                atime = datetime.now().strftime('%I:%M:%S %p')
                cl.sendText(trev.mid,aa + " mentioned you in " + ab + "\n" + atime)
                cl.sendText(trev.mid,'"' + at + '"' + '\n- ' + aa)
                cl.sendText(msg.to,"Trevor lagi off, " + aa)
      #-------------Fungsi Bannlist Start------------------# 
            elif msg.text in ["Join to pending group"]:
               if msg.from_ in admin:
                  gid = cl.getGroupIdsInvited()
                  for i in gid:
                     cl.acceptGroupInvitation(i)
                     cl.sendText(msg.to,"Success Accept All Invitation Group")	
            elif msg.text in ["Banlist"]:
			  if msg.from_ in admin:
				if wait["blacklist"] == {}:
					cl.sendText(msg.to,"There's no banned user")
				else:
					ki.sendText(msg.to,"Blacklist user")
					mc = ""
					for mi_d in wait["blacklist"]:
						mc += "->" +cl.getContact(mi_d).displayName + "\n"
					cl.sendText(msg.to,mc)
      #-------------Fungsi Bannlist Finish------------------#  
      
            elif msg.text in ["Cek ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
			  if msg.from_ in admin:
				if msg.toType == 2:
					group = cl.getGroup(msg.to)
					gMembMids = [contact.mid for contact in group.members]
					matched_list = []
					for tag in wait["blacklist"]:
						matched_list+=filter(lambda str: str == tag, gMembMids)
					if matched_list == []:
						cl.sendText(msg.to,"There was no blacklist user")
						return
					for jj in matched_list:
						cl.sendText(msg.to,"Good bye.")
						cl.kickoutFromGroup(msg.to,[jj])
						ki.kickoutFromGroup(msg.to,[jj])
						kk.kickoutFromGroup(msg.to,[jj])
						kc.kickoutFromGroup(msg.to,[jj])
            elif msg.text in ["Clear"]:
			  if msg.from_ in admin:
				if msg.toType == 2:
					group = cl.getGroup(msg.to)
					gMembMids = [contact.mid for contact in group.invitee]
					for _mid in gMembMids:
						cl.cancelGroupInvitation(msg.to,[_mid])
						cl.sendText(msg.to,"I pretended to cancel and canceled.")

            elif msg.text in ["Bot Like", "Bot like"]:
                if msg.from_ in admin:
                    print "[Command]Like executed"
                    cl.sendText(msg.to,"Trying to Like post(s)")
                    try:
                        likePost()
                    except:
                        pass

            elif msg.text.lower() == 'astro out all':
			  if msg.from_ in admsa:
				gid = cl.getGroupIdsJoined()
				gid = ki.getGroupIdsJoined()
				gid = kk.getGroupIdsJoined()
				gid = kc.getGroupIdsJoined()
				for i in gid:
					cl.leaveGroup(i)
					ki.leaveGroup(i)
					kk.leaveGroup(i)
					kc.leaveGroup(i)
				if wait["lang"] == "JP":
					cl.sendText(msg.to,"Astro pamit dulu ya kakak")
				else:
					cl.sendText(msg.to,"Astro pamit dulu kakak byee")
            elif msg.text.lower() == 'out':
			  if msg.from_ in admin:
				gid = cl.getGroupIdsJoined()
				for i in gid:
					cl.leaveGroup(i)
				if wait["lang"] == "JP":
					cl.sendText(msg.to,"Astro pamit")
				else:
					cl.sendText(msg.to,"God Bye")

            elif "Group pict" in msg.text.lower():            
				print "[command]steal executing"
				group = cl.getGroup(msg.to)
				path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
				cl.sendImageWithURL(msg.to,path)
				print "[command]steal executed"

            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
						
            elif msg.text.lower() in ["List group"]:
              if msg.from_ in admin:
				gid = cl.getGroupIdsJoined()
				h = ""
				for i in gid:
					h += "%s\n" % (cl.getGroup(i).name +" → ["+str(len(cl.getGroup(i).members))+"]")
				cl.sendText(msg.to,"-- List Groups --\n\n"+ h +"\nTotal groups =" +" ["+str(len(gid))+"]")
												
            elif "Staff add @" in msg.text:
                if msg.from_ in admsa:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Staff add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                cl.sendText(msg.to,"Staff added")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "Staff remove @" in msg.text:
                if msg.from_ in admsa:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Staff remove @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.remove(target)
                                cl.sendText(msg.to,"Staff deleted")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif msg.text in ["Stafflist","stafflist"]:
                if admin == []:
                    cl.sendText(msg.to,"The stafflist is empty")
                else:
                    cl.sendText(msg.to,"please wait...")
                    mc = ""
                    for mi_d in admin:
                        mc += "\n- " + cl.getContact(mi_d).displayName
                    cl.sendText(msg.to, "Staff :\n" + mc)
                    print "[Command]Stafflist executed"
					
            elif msg.text in ["Kernel","kernel"]:
                 if msg.from_ in admin:
                     botKernel = subprocess.Popen(["uname","-svmo"], stdout=subprocess.PIPE).communicate()[0]
                     cl.sendText(msg.to, botKernel)
                     print "[Command]Kernel executed"
		
            elif "Apakah " in msg.text:
				tanya = msg.text.replace("Apakah ","")
				jawab = ("Ya","Tidak")
				jawaban = random.choice(jawab)
				cl.sendText(msg.to,jawaban)
				
        if op.type == 55:
            try:
				if op.param1 in wait2['readPoint']:
					Name = cl.getContact(op.param2).displayName
					if Name in wait2['readMember'][op.param1]:
						pass
					else:
						wait2['readMember'][op.param1] += "\n- " + Name
						wait2['ROM'][op.param1][op.param2] = "- " + Name
				else:
					cl.sendText
            except:
                pass

        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"]
                cl.updateProfile(profile)

                profile2 = ki.getProfile()
                profile2.displayName = wait["cName2"]
                ki.updateProfile(profile2)

                profile3 = kk.getProfile()
                profile3.displayName = wait["cName3"]
                kk.updateProfile(profile3)

                profile4 = kc.getProfile()
                profile4.displayName = wait["cName4"]
                kc.updateProfile(profile4)

                profile5 = ks.getProfile()
                profile5.displayName = wait["cName5"]
                ks.updateProfile(profile5a)

                profile6 = ka.getProfile()
                profile6.displayName = wait["cName6"]
                ka.updateProfile(profile6)

                profile7 = kb.getProfile()
                profile7.displayName = wait["cName7"]
                kb.updateProfile(profile7)

                profile8 = ko.getProfile()
                profile8.displayName = wait["cName8"]
                ko.updateProfile(profile8)
                
                profile9 = ke.getProfile()
                profile9.displayName = wait["cName9"]
                ke.updateProfile(profile9)
                
                profile10 = ku.getProfile()
                profile10.displayName = wait["cName10"]
                ku.updateProfile(profile10)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

def autolike():
     for zx in range(0,20):
        hasil = cl.activity(limit=400)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
          try:    
			cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1003)
			cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by\nline.me/ti/p/~mikefs05")
			print "Like"
          except:
            pass
        else:
            print "Already Liked"
     time.sleep(400)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
