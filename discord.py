from discord_webhook import DiscordWebhook
import os
Webhook = os.getenv("DISCORD_WEBHOOK_API")
def send(payload):
    DiscordWebhook(Webhook, content=content)