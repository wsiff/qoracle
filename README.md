# QOracle Discord Bot - stripped version

This is the script only version for bot that selects a verses from the big three Holy Books i.e. Bible, Quran, Torah, leveraging quantum-level randomness; using unpredictable decay of radioactive isotopes.

---

## Features
- Fetches random verses from the Quran.
- Utilizes the HotBits API for true randomness.
- Simple setup and execution.

---

## How to Use

### 1. Obtain API Keys
- **HotBits API Key**: Required for generating random numbers.
- **Discord Bot API Key**: Needed to authenticate your bot on Discord.

### 2. Setup Virtual Environment and Dependencies

To isolate dependencies, create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Add your API keys to the `Env.env` file. Ensure the file includes:
```
DISCORD_API_KEY=your_discord_api_key
HOTBITS_API_KEY=your_hotbits_api_key
```

### 4. Run the Application

Start the bot with:
```bash
python main.py
```

---

## Project Structure
```
QOracle Discord Bot/
├── main.py               # Main application entry point
├── requirements.txt      # List of dependencies
├── Env.env               # Environment variables file
├── README.md             # Project documentation
└── ...                   # Additional scripts and resources
```

---

## Dependencies
Ensure the following dependencies are installed (defined in `requirements.txt`):
- `discord.py`
- `requests`

---

## Notes
- The bot requires an active internet connection to access the APIs.
- Ensure your `Env.env` file is kept secure to protect your API keys.

---

## License
This project is licensed under the DWYW License. Go figure.

---

## Contribution
Feel free to fork this repository, submit issues, or make pull requests to contribute to the project.
