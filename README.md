# 🗳️ Election Management Software.

A lightweight **offline election management system** developed in **Python** for schools and organizations. The system allows voters to securely cast votes through a graphical interface while a local server receives and stores vote counts in real time.

Designed for **Local Area Networks (LAN)**, the application requires **no internet connection**, making it suitable for classrooms, schools, clubs, and institutional elections.

---

## ✨ Features

- 🖥️ Fullscreen graphical voting interface
- 🔒 Password protected voting access
- 🗳️ One vote per position
- 👤 Candidate photographs with selection highlighting
- ✅ Review page before final submission
- 📡 Real-time LAN communication using Python sockets
- 💾 Automatic vote counting and CSV storage
- 🚫 Prevents accidental closing (Alt + F4 & Close Button)
- ⚡ Lightweight and completely offline
- 🔄 Automatically resets after every successful vote

---

## 📦 Requirements

- Python 3.10+
- Pillow

Install dependencies

```bash
pip install pillow
```

---

# 📂 Project Structure

```text
ElectionSoftware/
│
├── client.py
├── svr.py
├── votes.csv
│
├── png/
│   ├── background/
│   └── Candidates/
│
└── README.md
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/soobruhdrip/election-software.git
cd election-software
```

Install dependencies

```bash
pip install pillow
```

---

# ⚙️ Configuration

## Configure the Server

The server listens on

```python
host = "0.0.0.0"
port = 65432
```

which accepts connections from every device on the same network.

---

## Configure the Client

Open **client.py**

Locate

```python
s.connect(("IPADDRESS",65432))
```

Replace `IPADDRESS` with your server computer's local IP.

Example

```python
s.connect(("192.168.1.25",65432))
```

---

## Configure Candidates

Candidate names are stored directly inside both the client and server.

Example

```python
"CAPTAIN BOYS": [
    "Candidate 1",
    "Candidate 2",
    "Candidate 3",
    "Candidate 4"
]
```

Replace these with your own candidates before running the election.

---

## Candidate Images

Candidate images should be placed inside

```text
png/Candidates/
```

Background images should be stored inside

```text
png/background/
```

---

# ▶️ Running the Software

## Start the Server

```cmd
python svr.py
```

Server Output

```text
Server listening on 0.0.0.0:65432
```

---

## Start the Client

```cmd
python client.py
```

---

# 🗳️ Voting Process

1. Launch the client application.
2. Enter the voting password.
3. Read the welcome screen.
4. Vote for:
   - Captain Boys
   - Captain Girls
   - Vice Captain Boys
   - Vice Captain Girls
5. Review your selections.
6. Confirm your votes.
7. Submit votes.
8. Votes are instantly transmitted to the server.
9. The application resets automatically for the next voter.

---

# 💾 Vote Storage

Votes are stored in

```text
votes.csv
```

Example

```csv
CAPTAIN BOYS

John Doe,14
Alex Smith,8
David Roy,21

CAPTAIN GIRLS

Jane Doe,18
Emily Rose,12
```

The server automatically

- Reads existing votes
- Updates counts
- Writes new totals
- Preserves previous results

---

# 📡 Network Architecture

```text
             ┌──────────────────┐
             │   Server (svr.py)│
             │   Port : 65432   │
             └────────┬─────────┘
                      │
        ──────────────┼──────────────
                      │
        ┌─────────────┴─────────────┐
        │                           │
 ┌──────────────┐           ┌──────────────┐
 │ Client PC 1  │           │ Client PC 2  │
 │  Tkinter UI  │           │  Tkinter UI  │
 └──────────────┘           └──────────────┘
```

---

# 🛠 Tech Stack

## Frontend

- Python
- Tkinter
- Pillow (PIL)

## Backend

- Python
- Socket Programming
- CSV File Storage
- Collections (defaultdict)

---

# 🔒 Security

- Password-protected login
- Offline operation
- LAN-only communication
- Vote confirmation screen
- Disabled window closing
- Prevents accidental Alt+F4

---

# 📸 Screenshots

## Login Screen

_Add screenshot here_

---

## Welcome Screen

_Add screenshot here_

---

## Voting Interface

_Add screenshot here_

---

## Review Page

_Add screenshot here_

---

# 📋 Current Election Positions

- Captain Boys
- Captain Girls
- Vice Captain Boys
- Vice Captain Girls

The software can easily be extended to include additional positions by adding another page and updating the server candidate lists.

---

# 🚧 Future Improvements

- SQLite database support
- Voter authentication using IDs
- Encrypted vote transmission
- Live results dashboard
- Administrator control panel
- Automatic candidate configuration
- Result export to Excel
- Portable executable (.exe)
- Relative file paths
- Multi-school support

---

# 📄 License

This project was developed as an offline election management system for educational and institutional use.
