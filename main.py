import requests
import random
import time
header = {
    'authorization': "NzE3MzAxNDM5ODg5OTMyMjg5.YH0s0Q.7hT6mQ3y5oxMuZCZ234dRWkZc48"
}

def postmessage():
    for i in range(1,1000000000):
        time.sleep(2)
        b = ["owo", "uwu", "p-p", "ewe", "+-+", "T-T", ";-;", "u.u", ".-.", "r-r", "g-g", "f-f", "q-q", ":)", ":))", ":((", "i like hentai but only if the story is good ", ":AP_what: :AP_what:", ":AP_claps: :AP_claps:", ":AP_drink~1: :AP_drink:", ":AP_fuall: :AP_fuall:", ":AP_smoke: :AP_smoke:", ":AP_truck: :AP_truck:", ":AP_cathit: :AP_cathit:", ":AP_daheck: :AP_daheck:", ":AP_notalk: :AP_notalk:", ":AP_runhug: :AP_runhug:"
 ,":AP_wiggle: :AP_wiggle:", ":AP_blobgun: :AP_blobgun:", ":AP_catpaws: :AP_catpaws:", ":AP_dogwave: :AP_dogwave:", ":AP_hugspin: :AP_hugspin:",  ":AP_pug: :AP_pug:", ":AP_birb: :AP_birb:", ":AP_kbye: :AP_kbye:", ":AP_milk: :AP_milk:", ":AP_rose: :AP_rose:", "i think i will make coffee", "ara ara",  "bitch", ":vibin:", "talk to me i am not a bot i swear uwu", "i Lie sometimes but i am a good boi ", "can't catch me ahahah", "fuck everyone who thinks i am a bot i am just automated text", ":AP_pepeicic:", ":AP_tech_angry:", ":BulbaWalk:", ":babydance:", ":AP_VentiCry:", ":AP_SCAREDLOOK:", "I am not dumb i am just not smart enough T^T", ":huhwhat:", ":AP_pepephone:", ":ricklepick:", ":AP_angrycry:", "w-w", "#-#",  ":confounded::confounded:",  "heya", "koya dance", "koya lewd", "koya bang", "!rank", "automated message here ewe", "pwease", "p-p","owo","=///=","i am fun", "sorry", "okey", "=-=", "r0r", ":blacksadge:", ":rolling_eyes:", ":kissing_closed_eyes: :kissing_closed_eyes:", ":sob:", ":AP_tech2:",":piss4::piss3:", ":AP_pepeverysus:",
 ":piss2::piss1:", "XD", "ahahahaahha", "Arigatou gozaimas", ":AP_stfuqt: ", "i know i am not a good guy but damn wtf is wrong with you","oh my god i hate the new members", "sad shit", "bitch ass nigga ", ":AP_whenlifegetsyou:", "damnn man", "that's sick", "oh nooooo"

             ]
        a = random.choice(b)
        payload = {
            'content': a
        }
        r = requests.post(" https://discord.com/api/v9/channels/874529359774494731/messages", data=payload, headers=header)
postmessage()
