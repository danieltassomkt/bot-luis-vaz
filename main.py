from pyrogram import Client
from pyrogram.types import ChatJoinRequest, InlineKeyboardMarkup, InlineKeyboardButton
import os

# Variáveis de ambiente (Pella)
api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
bot_token = os.environ["BOT_TOKEN"]

# Inicializar o bot
app = Client("luisvaz_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Evento: novo usuário solicita entrada no canal
@app.on_chat_join_request()
async def aprovar(client, request: ChatJoinRequest):
    try:
        # Aprovar a solicitação de entrada
        await client.approve_chat_join_request(request.chat.id, request.from_user.id)

        # Enviar a primeira mensagem com o botão e o nome do usuário
        await client.send_message(
            chat_id=request.from_user.id,
            text=f"👋 Olá {request.from_user.first_name}, seja bem-vindo(a) ao canal! 🚀",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("🔐 Acessar Conteúdo Exclusivo", url="https://t.me/luisvazcap_bot?start=w39821122")]]
            )
        )

        # (A segunda mensagem será enviada automaticamente pelo ManyChat ao clicar no botão)

        print(f"✅ Aprovado e mensagem de boas-vindas enviada para: {request.from_user.first_name}")

    except Exception as e:
        print(f"❌ Erro: {e}")

# Rodar o bot
app.run()
