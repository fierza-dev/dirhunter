# Dirhunter v2.3 (Release)

**Dirhunter** is a Python-based tool for discovering hidden directories (directory brute-forcing) on web servers using a wordlist. Dirhunter is designed to be **fast, efficient**, and **user-friendly**, supporting various search optimization methods.

![Dirhunter Logo](https://i.ibb.co.com/mV2gkfRt/Screenshot-From-2025-02-25-18-36-23.png)

## Key Features  
- 🔍 **Fast Search**: Optimized algorithms to accelerate directory searches.  
- 🧰 **Customization Support**: Use your preferred wordlist for more specific results.    
- 🌐 **HTTP/HTTPS Compatibility**: Automatically detects and handles protocols correctly.  
- 🛠️ **Stable Versions**: Enjoy features in the release version.
- 🔥 **Shebang Support**: Allows the tool to be executed directly as a script in Unix-like systems.

## 🚀 What's New?
- New Proxy Feature, New Scanning Modes, WAF Bypass via HTTP Smuggling, Etc
- Enhanced Scanning Speed for Faster Results
- Optimized Code for Better Performance
- Bug Fixes and General Improvements
- And More!

## Installation
1. Clone this repository:  
   ```bash
   git clone https://github.com/fierza-dev/dirhunter.git
   cd dirhunter
   (Optional) sudo chmod +x app.py
   ```
2. Install the required dependencies <br>
   ```bash
   pip install -r requirements.txt
    ```
4. Run the tool <br>
   ```bash
   python3 app.py -u <target-url> <br>
   Example : python3 app.py -u https://example.com/<br>
   ```
   ```bash
   ./app.py -u <target-url> <br>
   Example : ./app.py -u https://example.com/<br>
    ```
## Usage tutorial for the tools.
1.Basic
   ```bash
   python3 app.py -u <target-url> <br>
   ```
   ```bash
   ./app.py -u <target-url> <br>
   ```

 2.To get a list of all options and switches use:
   ```bash
   python3 app.py -h <br>
   ```
   ```bash
   ./app.py -h <br>
   ```

## License
This project is licensed under the AGPL-3.0 license.
