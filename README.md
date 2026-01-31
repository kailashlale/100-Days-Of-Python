Welcome to my **#100DaysOfPython** journey!

I am a **Creative Designer with 8+ years of experience** in brand strategy, packaging, and UI/UX. This repository documents my transition from visual design to **Generative AI** technical implementation, exploring how Python can bridge the gap between conceptual thinking and practical application.

Here, you will find logic-based console applications and interactive web interfaces built with **Gradio** and deployed on **Hugging Face**.

---

### 🛠️ Tech Stack & Tools
- **Language:** Python 3.x
- **Interfaces:** Gradio (for web apps), Console (for logic)
- **Deployment:** Hugging Face Spaces
- **Design Philosophy:** Clean code, optimized flow, and user-centric functionality.

---

### 📂 Project Showcase

Below is a curated list of projects completed during this challenge. Click the **Live Demo** badges to try the apps instantly in your browser.

| Day | Project Name | Description | Source Code | Live Demo |
| :---: | :--- | :--- | :---: | :---: |
| 01 | **Number Guessing Game** | Classic game that generates a random number and counts your guess attempts till you find that number | [![Static Badge](https://img.shields.io/badge/Code-171717?logo=python&logoColor=21c063)](./Day01-Number-Guessing-Game/main.py) | [![Hugging Face](https://img.shields.io/badge/Gradio-171717?logo=gradio)](https://huggingface.co/spaces/kailashlale/Day01-Number-Guessing-Game) |
| 02 | **Rock Paper Scissors** | Interactive game where you compete against the computer using Rock, Paper, or Scissors | [![Static Badge](https://img.shields.io/badge/Code-171717?logo=python&logoColor=21c063)](./Day02-Rock-Paper-Scissor/main.py) | [![Hugging Face](https://img.shields.io/badge/Gradio-171717?logo=gradio)](https://huggingface.co/spaces/kailashlale/Day02-Rock-Paper-Scissors) |
| 03 | **Simple Calculator** | Basic calculator that performs addition, subtraction, multiplication, and division | [![Static Badge](https://img.shields.io/badge/Code-171717?logo=python&logoColor=21c063)](./Day03-Simple-Calculator/main.py) | [![Hugging Face](https://img.shields.io/badge/Gradio-171717?logo=gradio)](https://huggingface.co/spaces/kailashlale/Day03-Simple-Calculator) |



> **Note:** `app.py` contains the Gradio web interface code, while `main.py` contains the pure Python console logic.

---

## 🚀 How to Run Locally

If you want to run these projects on your own machine:

1. **Clone the repository**
   ```bash
   git clone https://github.com/kailashlale/100-Days-Of-Python.git
   ```

2. **Directly run the program in your console:**
   ```bash
   # Windows
   python {folderName}/main.py 
   # Example: python 001_Number-Guessing-Game/main.py

   # Mac/Linux
   python3 {folderName}/main.py 
   # Example: python3 001_Number-Guessing-Game/main.py
   ```

3. **For Gradio Interface:**

   First, ensure you have the library installed:
   ```bash
   pip install gradio
   ```

   Then run the app file:
   ```bash
   gradio {folderName}/app.py 
   # Example: gradio 001_Number-Guessing-Game/app.py
   ```
   *Click the local URL (usually http://127.0.0.1:7860) that appears in your terminal.*

