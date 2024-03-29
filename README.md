Keylogger

Detailed Description:

The keylogger script provided here serves the purpose of silently capturing keystrokes made on the system it's installed on. It operates by intercepting keyboard input and logging it into a text file while also sending the captured keystrokes to a local http server. The server runs on the localhost IP address and utilizes port 80 for communication. (I need help because I am unable to connect to the HTTP server with other PCs on the same network.

Usage:

1) Installation:

Run the provided VBScript (start_all.vbs) to automatically install the necessary components and start all.
This script installs the required Python packages (keyboard, and other) for the keylogger to function properly.
this keyloger is full automaticly


2) Running the Keylogger:

Execute the keylogger script (keylogger.py) using Python.
The script will silently run in the background, capturing all keyboard input.


3) Accessing the Captured Keystrokes:

All captured keystrokes are logged into a text file (txt.txt).
The text file contains a chronological record of all keystrokes made while the keylogger is active.


4) Configuring Firewall:

If you encounter issues accessing the local http server from other devices on the network, it may be due to firewall restrictions.
You need to configure the firewall to allow incoming connections to the server port (port 80) to enable access from other devices.


5) Contributing:

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request on GitHub.


!!!Disclaimer:
This keylogger script is intended for educational and research purposes only. It should be used responsibly and ethically, and never for any illegal or malicious activities.


Author:
theBOST

Version:
V.1.0 (for github)

Date:
29.03.2024
