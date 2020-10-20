import requests
from .. import loader, utils


def register(cb):
    cb(WeatherMod())
    
class WeatherMod(loader.Module):
    strings = {'name': 'Weather'}
    
    async def pwcmd(self, message):
        """"Кидает погоду картинкой.\nИспользование: .pw <город>; ничего."""
        await message.edit("Узнаем погоду...")
        city = utils.get_args_raw(message)
        msg = []
        for i in city:
            if city:
                city = f"https://wttr.in/{city}.png"
            else:
                city = "https://wttr.in/.png"
            msg.append(city)
            await message.client.send_file(message.to_id, ("".join(msg)))
            await message.delete()


    async def awcmd(self, message):
        """Кидает погоду ascii-артом.\nИспользование: .aw <город>; ничего."""
        await message.edit("Узнаем погоду...")
        city = utils.get_args_raw(message)
        msg = []
        for i in city:
            if city:
                r = requests.get(f"https://wttr.in/{city}?0?q?T")
            else:
                r = requests.get("https://wttr.in/?0?q?T")
            msg.append(r.text)
            await message.edit(f"<code>Город: {r.text}</code>")
            return