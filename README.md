# 🔍 Finding Waldo

> A fun **"Where’s Waldo"**-inspired game built with **Python and Pygame** — test your observation skills while managing limited lives and hints!

![Tech Stack](https://img.shields.io/badge/Built%20With-Python%20%7C%20Pygame-orange)

---

## 📘 Overview

**Finding Waldo** is a Python mini-game designed using **Pygame**. The player must find Waldo in a busy image within a limited number of attempts. With a clean interface and light animations, the game mixes logic and visual attention. It was created for a programming activity to explore game mechanics, GUI handling, and event-driven programming in Python.

---

## ⚙️ Features

- 🔍 Interactive search for Waldo in an image  
- ❤️ 5 Lives — each wrong click deducts one  
- 💡 3 Hints to assist you during the game  
- 🧠 Win by locating Waldo, lose when all lives are used  
- 🖥️ Clean splash screen, instructions panel, and end screen  
- 🐍 Developed entirely with Python using **Pygame**  

---

## 📸 Screenshots

| Splash Screen | Instructions |
|---------------|--------------|
| ![Splash Screen](https://framerusercontent.com/images/oIfQNnEeCpPYWRhVFQscigtAMkY.png) | ![Instructions](https://framerusercontent.com/images/VSULg5st4X8kwdf9izi2a8MCg.png) |

| Game Mechanics | Actual Game |
|----------------|-------------|
| ![Game Mechanics](https://framerusercontent.com/images/EExvyUtWMK4HcUfBTSZJKRPveQ.png) | ![Actual Game](https://framerusercontent.com/images/Lo2Zw2QrzRsPq8wi94HIhWjbA7E.png) |

---

## 🚀 Getting Started

To run the game locally:

```bash
# 1. Clone the repository
git clone https://github.com/ChristianDeoManlangit/Python-Finding-Waldo.git
cd Python-Finding-Waldo

# 2. Install pygame
pip install pygame

# 3. Launch the game
python Main.py
```

Make sure **Python 3.8+** is installed.

---

## 🛠️ Build as Executable (Optional)

If you'd like to turn the app into a standalone `.exe` file using **PyInstaller**:

```bash
# 1. Install pyinstaller
pip install pyinstaller

# 2. Build the app
pyinstaller --onefile --windowed --add-data "Assets;Assets" Main.py

```

The `.exe` file will be available inside the `dist/` folder.

---

## 📝 Notes

- Game only have one level for now
- Game supports mouse clicks only (no keyboard controls)  
- The hints appears at the console instead of the GUI  

---

## 🔗 Live Link

🚫 *This is a local Python game — no live demo available*

---

## 👤 Author

Made with ❤️ by **[Chai](https://github.com/ChristianDeoManlangit)**  

---
