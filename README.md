# RapidHub

## Description
RapidHub is a Python-based utility designed to secure file access on Windows systems by setting advanced permissions and access controls. It leverages the Windows API to manipulate file permissions, ensuring that only authorized users can access specific files.

## Features
- Set custom permissions for files on Windows systems.
- Log activities to a dedicated log file for audit and troubleshooting purposes.
- Interactive command-line interface for easy usage.

## Prerequisites
- Windows operating system.
- Python 3.x installed on your system.
- Administrative privileges to modify file permissions.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/rapidhub.git
   ```
2. Navigate to the project directory:
   ```bash
   cd rapidhub
   ```

## Usage
1. Ensure you have the necessary administrative privileges.
2. Run the script:
   ```bash
   python rapidhub.py
   ```
3. Follow the on-screen prompts to provide the file path, permissions, and username.

## Logging
RapidHub logs its operations to a file named `rapidhub.log` located in the same directory as the script. Review this log to audit changes and troubleshoot issues.

## Disclaimer
RapidHub modifies file permissions which can affect system security and file accessibility. Use with caution and ensure you have backups of important files.

## License
MIT License. See `LICENSE` for more details.

## Contributing
Contributions are welcome. Please fork the repository and submit a pull request for review.