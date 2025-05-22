from pyrogram import Client
from pyrogram.types import ChatJoinRequest, InlineKeyboardMarkup, InlineKeyboardButton
import os

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
bot_token = os.environ["BOT_TOKEN"]

app = Client("luisvaz_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_chat_join_request()
async def aprovar(client, request: ChatJoinRequest):
    try:
        await client.approve_chat_join_request(request.chat.id, request.from_user.id)

        await client.send_message(
            chat_id=request.from_user.id,
            text="🤖 O que esse bot faz?\nTe mostra o caminho para mudar de vida com o Day Trade, copiando minhas operações passo a passo.\n\nClique abaixo para começar agora:",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("👉 Acessar Conteúdo Exclusivo", url="https://t.me/luisvazcap_bot?start=w39821122")]]
            )
        )
        print(f"✅ Aprovado e link do ManyChat enviado para: {request.from_user.first_name}")
    except Exception as e:
        print(f"❌ Erro: {e}")

app.run()
