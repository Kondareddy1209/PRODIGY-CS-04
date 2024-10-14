# Keylogger Program

## Overview

This is a **Keylogger Program** developed as part of my **internship at Prodigy** (Task 4). The program is intended for **educational and ethical purposes** only, capturing keystrokes on a device with explicit permission. The captured keystrokes are logged along with a timestamp and saved to a file.
I used for this execution in Vs code and python version is : 3.11.9.

**Important:** This project must only be used on devices where you have explicit permission to monitor the keystrokes. Unauthorized use is strictly prohibited.

---

## Features

- Logs keystrokes along with timestamps.
- Handles both regular characters and special keys (e.g., space, enter).
- Stores captured data in a plain text log file.
- Provides an ethical disclaimer before use.
- User-friendly interface with clear prompts for duration and consent.

---

## Installation

1. **Clone the repository** to your local machine:

    ```bash
    git clone https://github.com/your-username/keylogger-program.git
    ```

2. **Check if Python is installed**:

    Run the following command to check if Python is installed:

    ```bash
    python --version
    ```
    or
   ```bash
   py --version
   ```

    If Python is not installed, please download and install it from [python.org](https://www.python.org/downloads/).

4. **Navigate to the project directory**:

    ```bash
    cd keylogger-program
    ```

5. **Install the required Python libraries**:

    The project requires the `pynput` library to capture keyboard events. Install it using pip:

    ```bash
    pip install pynput
    ```

    Or, if you encounter issues, try:

    ```bash
    py -m pip install pynput
    ```

---

## Usage

1. **Run the keylogger script**:

    ```bash
    python keylogger.py
    ```

2. **Agree to the terms**:

    The program will display a disclaimer and ask for your agreement before proceeding.
   
3. **check the running status in keylogger_log.txt file**:

     If the program runs or execute correctly means it will show some keys 

5. **Enter the logging duration**:

    You will be prompted to input how long (in seconds) you want the program to run and capture keystrokes.

6. **View the log file**:

    Once the program finishes logging, the captured keystrokes will be saved in a text file called `keylogger_log.txt`. You can find this file in the project directory.

---

## Ethical Considerations

⚖️ **This keylogger is intended for educational purposes only. It should only be used on devices where you have explicit permission to monitor keystrokes.**

🚫 **Unauthorized use of this program is illegal and unethical.**

---

## Contribution

This project is intended for educational purposes. If you'd like to contribute to the project, feel free to create a pull request or report any issues via GitHub.

---

## License

This project is licensed under the **MIT License** - see the [LICENSE.md](LICENSE.md) file for details.

---

## Acknowledgments

- **Prodigy**: For the opportunity to work on this project during my internship.  
- **Python** and **pynput**: For the libraries that made the keylogging possible.

---

### THANK💚YOU
