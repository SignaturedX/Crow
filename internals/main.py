import os

from dotenv import load_dotenv
from interactions import (
    Client,
    ClientPresence,
    PresenceActivity,
    PresenceActivityType,
    Intents,
)
from interactions.ext import wait_for


def main():
    # Loading environment variables
    load_dotenv("resources/.env")
    token = os.getenv("DISCORD_TOKEN")

    # Create presence for the bot
    presence = ClientPresence(
        activities=[
            PresenceActivity(
                type=PresenceActivityType.WATCHING, name="over the RPG World!"
            )
        ]
    )

    # Create client instance
    bot = Client(
        token=token,
        intents=Intents.DEFAULT | Intents.GUILD_MESSAGE_CONTENT,  # Intents will need privileges added at some point.
        presence=presence,
        default_scope=os.getenv("GUILD_ID"),
    )

    @bot.event
    async def on_ready():
        print("Bot has been launched successfully.")

    # Add wait_for and wait_for_component methods to bot
    wait_for.setup(bot, add_method=True)

    bot.start()


if __name__ == "__main__":
    main()

