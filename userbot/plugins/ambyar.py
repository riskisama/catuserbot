import asyncio
from collections import deque

from . import mention


@bot.on(admin_cmd(pattern=f"bitch$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"bitch$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "I'M A BROKENT HOME")
    await asyncio.sleep(2)
    await event.edit("🙂Tangisan hanya mengacaukan segalanya tapi senyuman membuat mereka yakin aku Tegar")
    await asyncio.sleep(5)
    await event.edit("☹️Setiap anak ingin keluarga yang sempurna\ntapi tidak semua anak memilikinya.")
    await asyncio.sleep(5)
    await event.edit("Sayangilah kedua orang tuamu dengan\nsepenuh hati selagi masih ada🙂")
    await asyncio.sleep(5)
    
    
@bot.on(admin_cmd(pattern=f"io$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"io$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "`ioo....`")
    await asyncio.sleep(3)
    await event.edit("`Muka gw Burik...`")
    await asyncio.sleep(3)
    await event.edit("`Kayak Jemboot`.")
    await asyncio.sleep(1)
    await event.edit("`Muka Gw Burik gak Kek Kalian`")
    
    
@bot.on(admin_cmd(pattern=f"ll$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"ll$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "`Lucinta luna berbatang....`")
    await asyncio.sleep(3)
    await event.edit("`Tapi gua suka...`")
    await asyncio.sleep(3)
    await event.edit("`punya tt gede`.")
    await asyncio.sleep(1)
    await event.edit("`I LOVE MEMEK RAKITAN`")
    
    
@bot.on(admin_cmd(pattern=f"oi$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"oi$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "`oii....`")
    await asyncio.sleep(3)
    await event.edit("`Muka kalian Burik...`")
    await asyncio.sleep(3)
    await event.edit("`Kayak Jemboot`.")
    await asyncio.sleep(1)
    await event.edit("`Muka Gw Gak Burik Kek Kalian`")
    
    
@bot.on(admin_cmd(pattern=f"oe$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"oe$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "`oee....`")
    await asyncio.sleep(3)
    await event.edit("`Muka kalian 8 bit...`")
    await asyncio.sleep(3)
    await event.edit("`Kayak Monyet`.")
    await asyncio.sleep(1)
    await event.edit("`Muka Gw Gak Burik Kek Kalian`")
    
    
    
@bot.on(admin_cmd(pattern=f"tidr$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"tidr$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "**Eh, beban keluarga tdr woi** ")
    await asyncio.sleep(2)
    await event.edit("**Sadar gadangnya bukan untukmu**")
    await asyncio.sleep(2)
    await event.edit("**Melainkan untuk dia di akun satu**")    
    await asyncio.sleep(2)
    

@bot.on(admin_cmd(pattern=f"pc$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"pc$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "**Eh, yaela pc mulu jadian kaga** ")
    await asyncio.sleep(2)
    await event.edit("**Percuma jadian  putus iya, ngewe kaga**")
    await asyncio.sleep(2)
    await event.edit("**Canda ngewe😅**")    
    await asyncio.sleep(2)
    await event.edit("**Awokawok Canda monyet😜😅**")    
    await asyncio.sleep(2)
    
    
@bot.on(admin_cmd(pattern=f"tbat$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"tbat$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "**Eh beban keluarga!!** ")
    await asyncio.sleep(2)
    await event.edit("**Bapak lu kerja keras nafkahin keluarga**")
    await asyncio.sleep(2)
    await event.edit("**Anaknya kelakuannya  kek Sempak dajjal!! **")    
    await asyncio.sleep(2)
    await event.edit("**Tobat sadar lu anak haram!!**")    
    await asyncio.sleep(2)
    
    
@bot.on(admin_cmd(pattern=f"gabut$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"gabut$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "**Nyanyi dikit bolehlah ya😁** ")
    await asyncio.sleep(2)
    await event.edit("**Du🤸‍♂️**")
    await asyncio.sleep(0.5)
    await event.edit("**Du du🤸‍♂️ **")
    await asyncio.sleep(0.5)
    await event.edit("**Du du du du🤸‍♂️**")
    await asyncio.sleep(0.5)
    await event.edit("**Blackpink🤸‍♂️**")
    await asyncio.sleep(2)
    await event.edit("**Du🤸‍♂️**")
    await asyncio.sleep(0.5)
    await event.edit("**Du du🤸‍♂️ **")
    await asyncio.sleep(0.5)
    await event.edit("**Du du du du🤸‍♂️**")
    await asyncio.sleep(0.5)
    await event.edit("**Aye aye kimochi🤸‍♂️**")
    await asyncio.sleep(2)
    await event.edit("Asw gabut gua😑!!")    
    await asyncio.sleep(2)
    
    
@bot.on(admin_cmd(pattern=f"skak$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"skak$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "**Hmmm, Gurih-Gurih nyoy"" ")
    await asyncio.sleep(2)
    await event.edit("**Enak kena skak?**")
    await asyncio.sleep(2)
    await event.edit("**Yahahahah mampus lu dajjal😂**")    
    await asyncio.sleep(2)
    
     
CMD_HELP.update(
    {
        "ambyar": "__**PLUGIN NAME :** ambyar__\
\n\n**📌 CMD ➥** `.bitch` | `.tidr` | `.skak` | `.pc` | `.tbat` | `.gabut` |`.oe` |`.oi`  ` | `.io `| `.ll  `. \
 `. \
\n\n**USAGE   ➥  **These are animation bruh..Try & check yourself\
"
    }
)
   
