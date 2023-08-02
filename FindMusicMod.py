#Name: FindMusicMod
#Decsription: A module for searching music in @fmusbot
#Author: kayt3m
#Commands:
# .fm
# 
#     _  __     ____    __    __  ________    ____       __  __
#    | |/ /    / /\ \   \ \  / / |__    __|  /_/\ \     /  \/  \
#    |   /    / /__\ \   \ \/ /     |  |        / /    / /\__/\ \
#    |   \   / /____\ \   |  |      |  |     _  \ \   / /      \ \
#    |_|\_\ /_/      \_\  |__|      |__|     \_\/_/  /_/        \_\
#    
#
#
#     🔐  Licenced under the GNU AGPLv3
#                        https://www.gnu.org/licenses/aplg-3.0.html
#meta developer: @dev_n0
#
__version__ = (1, 0, 0)


from .. import loader, utils
import logging 

logger = logging.getLogger(__name__)

@loader.tds
class FindMusicMod(loader.Module):
    """
    Module FindMusicMod - search music.
    Works via @fmusbot bot.
    """

    strings = {"name": "FindMusicMod"}

    async def fmcmd(self, message):
        """use for searching music."""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if not args:
            return await message.edit("<b><emoji document_id=5260342697075416641>❌</emoji>No args!</b>")
        try:
            await message.edit("<b><emoji document_id=5309924890462134382>📀</emoji>Search...</b>")
            music = await message.client.inline_query("fmusbot", args)
            await message.delete()
            await message.client.send_file(
                message.to_id,
                music[0].result.document,
                reply_to=reply.id if reply else None,
            )
        except:
            return await message.client.send_message(
                message.chat_id,
                f"<b> Sorry, I couldn't find your track. <code>{args}</code> </b>",
            )
