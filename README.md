# Unwanted App Uninstaller

This is a simple GUI application for removing unwanted applications from Kali Linux. It provides a user-friendly interface for selecting and uninstalling packages.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- List all installed applications
- Select multiple applications for removal
- User confirmation before removal
- Automatically clean up unused packages

## Requirements

- `Python 3`
- `tkinter` library
- `python3-apt` package

## Installation

Follow these steps to set up the application on your system:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/towsif-aktar/unwanted-app-uninstaller.git


2. **Change into the project directory:**

   `cd unwanted-app-uninstaller`

3. **Install the required packages:**

   `sudo apt install python3 python3-tk python3-apt`

4. **Run the application:**

   `python3 apps_uninstaller.py`


**Usage:**

1. Open the application.
2. Select the applications you want to remove from the list.
3. Click the "Remove Selected Apps" button.
4. Confirm your selection when prompted.
5. The selected applications will be removed.


**Contributing:**

This project is licensed under the MIT License - see the LICENSE file for details.



