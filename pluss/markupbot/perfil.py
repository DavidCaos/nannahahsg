from configs._def_main_ import *

@rexbt('perfil')
async def exit(client, msg):
    await msg.edit_message_text(perfil.format(id=msg.from_user.id,name=msg.from_user.first_name,username=msg.from_user.username),reply_markup=atras)