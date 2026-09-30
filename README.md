# 💬 Discord Message Automator

An automated Discord messaging tool written in Python for testing and scheduling channel messages. The tool sends randomized messages from a predefined library to a specified Discord channel at configurable intervals using direct HTTP requests.

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Requests](https://img.shields.io/badge/Requests-2.x-2CA5E0?style=for-the-badge)](https://requests.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

---

## ⚡ Features

- **Automated Messaging**: Delivers messages on a loop to a targeted Discord text channel.
- **Randomized Library**: Selects dynamically from an array of predefined text messages and emojis.
- **Direct REST API Calls**: Uses direct HTTP POST requests to the Discord API (`v9`) without heavy gateway dependencies.
- **Customizable Intervals**: Configurable delays between message dispatches to control transmission rate.

---

## 📁 Project Structure

```
discord-spammer/
├── LICENSE          # MIT License file
├── main.py          # Message loop script and API dispatcher
└── README.md        # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher installed on your system.
- A Discord account or bot token with access to post in the designated channel.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Joeljozzz/discord-spammer.git
   cd discord-spammer
   ```

2. **Install required dependencies:**
   ```bash
   pip install requests
   ```

---

## 🛠️ Usage

1. Open `main.py` in your preferred code editor.
2. Provide your authorization token in the `header` dictionary:
   ```python
   header = {
       'authorization': "YOUR_AUTHORIZATION_TOKEN"
   }
   ```
3. Set your target Discord channel ID in the `requests.post` URL inside the `postmessage()` function:
   ```python
   r = requests.post("https://discord.com/api/v9/channels/YOUR_CHANNEL_ID/messages", data=payload, headers=header)
   ```
4. Run the script:
   ```bash
   python main.py
   ```

> [!WARNING]
> **Terms of Service & Rate Limits**: Automating user accounts (self-botting) violates Discord's Terms of Service and can result in account suspension. Always adhere to Discord's API Guidelines and Developer Terms. Adjust request intervals appropriately to respect rate limits (`HTTP 429`).

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
