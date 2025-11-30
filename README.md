# Band Name Generator 🎸

A whimsical command-line interface (CLI) tool that generates unique and cool band names based on your city and pet's name. Built with Python and styled using the `rich` library for a premium terminal experience.

## ✨ Features

- **Interactive CLI**: Colorful and engaging prompts.
- **Randomized Elements**: Adds random adjectives and music genres (Rock, Synthwave, Lo-Fi, etc.) to spice up the names.
- **"Senior-Dev" Vibe**: Includes developer-inspired humor and aesthetics.

## 🛠️ Prerequisites

- Python 3.11 or higher
- [Rich](https://github.com/Textualize/rich) library

## 🚀 Installation

1. **Navigate to the project directory**:
   ```bash
   cd python/BandGenerator
   ```

2. **Install dependencies**:
   It is recommended to use a virtual environment.
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Usage

Run the main script to start the generator:

```bash
python main.py
```

Follow the on-screen prompts to enter the city you grew up in and your pet's name. The tool will combine them with a random genre and adjective to create your new band name!

## 🐳 Docker Support

You can also run this application in a Docker container.

1. **Build the image**:
   ```bash
   docker build -t band-generator .
   ```

2. **Run the container**:
   Note: Use the `-it` flags to enable interactive mode so you can provide input.
   ```bash
   docker run -it band-generator
   ```
