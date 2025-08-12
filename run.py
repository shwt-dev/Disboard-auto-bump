from bumpbot.main import create_bot

if __name__ == "__main__":
    client, token = create_bot()
    client.run(token)
