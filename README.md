# Bitcoin-tracker

Bitcoin-tracker is a Telegram bot that pulls the current price of Bitcoin from the Coinmarketcap Api
and sends a message to my personal Telegram chat every 30 minutes.

Been getting into Bitcoin recently and figured I would create a bot as a small side-project that would send me the time and price of Bitcoin instead of having to look it up all the time. 

# Setup
1. Install the packages: ```pip install -r requirements.txt```
2. Create a .env file and put in your own Api key, bot token and Telegram chat ID.
3. Run the script: ```python tracker.py```