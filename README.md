# 🚀 Disboard Auto-Bump

Automatically bump your Discord server on [Disboard.org](https://disboard.org) every 2 hours — no manual typing required.

![GitHub license](https://img.shields.io/github/license/shwt-dev/Disboard-auto-bump)
![GitHub stars](https://img.shields.io/github/stars/shwt-dev/Disboard-auto-bump?style=social)
![Maintained](https://img.shields.io/maintenance/yes/2025)

---

## 📌 About

Disboard helps Discord servers grow by listing them on a public server directory. However, it requires someone to manually run the `/bump` command every 2 hours to stay visible.

**Disboard Auto-Bump** automates this task — keeping your server at the top of the list without any manual effort.

---

## ⚙️ Features

- ✅ Automatically sends the `/bump` command every 2 hours
- ✅ Simple Node.js script
- ✅ Easy to configure
- ✅ Free and open source

---

## 🚀 Getting Started

```bash
git clone https://github.com/shwt-dev/Disboard-auto-bump.git
cd Disboard-auto-bump
npm install
npm start
```

---

## 🛠️ Configuration

```json
{
  "token": "YOUR_BOT_TOKEN",
  "guild_id": "YOUR_DISCORD_SERVER_ID",
  "channel_id": "DISBOARD_BUMP_CHANNEL_ID",
  "interval": 7200000
}
```

- `token`: Your bot token
- `guild_id`: Your Discord server ID
- `channel_id`: The channel where the `/bump` command is used
- `interval`: Time in milliseconds between bumps (default: 7200000 ms = 2 hours)

---

## ⚠️ Disclaimer

This project is for educational purposes only.  
Using selfbots or unauthorized automation may violate [Discord's Terms of Service](https://discord.com/terms).  
Use at your own risk.

---

## 🙌 Credits

Created by [shwt-dev](https://github.com/shwt-dev)  
Feel free to contribute or suggest improvements!

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
