# 🇳🇵 NATO Phonetic Alphabet Converter

A simple Python command-line program that converts user input into the **NATO phonetic alphabet** using data from a CSV file.

This project demonstrates:
- Reading data from a CSV file
- Dictionary comprehension
- Basic error handling
- Command-line input processing

---

## ✨ Features
- Converts any word into Nepali NATO phonetic code words
- Reads phonetic mappings from a `.csv` file
- Handles invalid input gracefully
- Simple and beginner-friendly Python project

---

## 🛠️ Technologies Used
- `Python`
- `Pandas`
- `CSV` file handling

---

## 📂 Project Structure
```bash
nepali-phonetic-converter/
│
├── main.py
├── nato_phonetic_alphabet.csv
└── README.md
```
---
## 📸 Example Output


---

## ▶️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/sudinkatuwal7/Nato-Over-And-Out.git
```
### 2. Install dependencies
```bash
pip install pandas
```
### 3. Run the program
```bash
python main.py
```

### 💻 Example Usage

Enter a word: `momo`

`['Momo', 'Oho', 'Momo', 'Oho']`

---

Enter a word: `SuDiN`

`['Samosa', 'Uff', 'Daal', 'Iku-Iku', 'Nepal']`

---

Enter a word: `aalu86`

`Please enter only letters A–Z.`

---

### 🧠 How It Works

The program reads phonetic data from `nato_phonetic_alphabet.csv`

It creates a dictionary like:

`{'A': 'Aama', 'B': 'Bhat', 'C': 'Chiya', ...}`

- It converts each letter of the input word into its phonetic equivalent

- Uses try/except to handle invalid characters

- Recursively calls the function if the user enters invalid input

---

### 🚧 Future Improvements

- Add support for both NATO and Nepali modes

- Create a graphical interface (GUI)

- Add pronunciation audio

- Support numbers and symbols

---

