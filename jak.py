#Created by clown :/
#pm - @guslslakkaakdkab
import telethon
from .. import loader, utils
import os
import requests
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import re
from telethon import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import io
from io import BytesIO
from textwrap import wrap
import random

def register(cb):
    cb(JaksMod())

class JaksMod(loader.Module):
    """Согласен"""
    strings = {'name': 'Жак ебаный'}

    def __init__(self):
        self.name = self.strings['name']
        self._me = None
        self._ratelimit = []

    async def client_ready(self, client, db):
        self._db = db
        self._client = client

    async def jakcmd(self, message):
        """.jak <реплай на изображение.>"""
        
        reply = await message.get_reply_message()
        txet = utils.get_args_raw(message)
        if not txet:
            if not reply:
                await message.edit("где реплай на медиа. или текст.")
            else:
                pic = await check_media(message, reply)
                if not pic:
                    await utils.answer(message, 'это не изображение лол.')
                    return
                what = haha(pic)
                await message.delete()
                await message.client.send_file(message.to_id, what)
        else:
            pic = requests.get("https://github.com/SpyderJabro/SpYD3R/blob/master/modul/photo_2020-09-02_13-18-13.jpg?raw=true")
            pic.raw.decode_content = True
            img = Image.open(io.BytesIO(pic.content)).convert("RGB")
            if len(txet) < 5:
                W, H = 900, 1050
            elif len(txet) < 10:
                W, H = 700, 1000
            elif len(txet) < 20:
                W, H = 500, 1000
            elif len(txet) < 30:
                W, H = 300, 1000
            elif len(txet) < 60:
                W, H = 300, 950
            elif len(txet) < 120:
                W, H = 300, 900
            else:
                W, H = 600, 700
            ufr = requests.get("https://github.com/LaciaMemeFrame/FTG-Modules/raw/master/zfont.ttf")
            f = ufr.content
            txt = utils.get_args_raw(message)
            txt = txt.replace("\n", "𓃐")
            text = "\n".join(wrap(txt, 30))
            t = text
            t = t.replace("𓃐", "\n")
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype(io.BytesIO(f), 72, encoding='UTF-8')
            w, h = draw.multiline_textsize(t, font=font)
            imtext = Image.new("RGBA", (w, h), (0, 0, 0, 0))
            draw = ImageDraw.Draw(imtext)
            draw.multiline_text((1, 1), t, (0, 0, 0), font=font, align='center')
            imtext.thumbnail((600, 300))
            w, h = 150, 300
            img.paste(imtext, ((W - w) // 3, (H - h) // 2), imtext)
            out = io.BytesIO()
            out.name = "out.jpg"
            img.save(out)
            out.seek(0)
            await message.client.send_file(message.to_id, out)
            await message.delete()

def lol(background, image, cords, size):
    overlay = Image.open(BytesIO(image))
    overlay = overlay.resize((size * 7, size * 4))
    background.paste(overlay, cords)


def haha(image):
    pics = requests.get("https://github.com/SpyderJabro/SpYD3R/blob/master/modul/photo_2020-09-02_13-18-13.jpg?raw=true")
    pics.raw.decode_content = True
    img = Image.open(io.BytesIO(pics.content)).convert("RGBA")
    lol(img, image, (30, 140), 90)
    out = io.BytesIO()
    out.name = "outsider.png"
    img.save(out)
    return out.getvalue()




async def check_media(message, reply):
    if reply and reply.media:
        if reply.photo:
            data = reply.photo
        elif reply.document:
            if reply.gif or reply.video or reply.audio or reply.voice:
                return None
            data = reply.media.document
        else:
            return None
    else:
        return None
    if not data or data is None:
        return None
    else:
        data = await message.client.download_media(data, bytes)
        try:
            Image.open(io.BytesIO(data))
            return data
        except:
            return None
