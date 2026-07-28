<p align="center">
    <img src="https://www.busquedaweb.com/openprojects/awtly/pet.png?v=2" width="auto" height="331" alt="Awtly's pet"><br>
    <a href="https://github.com/marjuanm/awtly/blob/main/history.txt"><img src="https://www.busquedaweb.com/openprojects/awtly/release.png?v=14" height="20" alt="Release version"></a>
    <a href="https://github.com/marjuanm/awtly/archive/refs/heads/main.zip"><img src="https://www.busquedaweb.com/openprojects/awtly/download.png" height="20" alt="Download current version"></a>
    <a href="https://github.com/marjuanm/awtly/blob/main/LICENSE"><img src="https://www.busquedaweb.com/openprojects/awtly/license.png" height="20" alt="Project's license"></a>
</p>

# What is Awtly?
Awtly is an ongoing project still in a very preliminary version, the goal is create a programming language that is very easy to learn, inspired by <a href="https://en.wikipedia.org/wiki/Python_(programming_language)" target="_blank">Python</a>, <a href="https://en.wikipedia.org/wiki/Lua" target="_blank">Lua</a>, and others, which will allow creating PHP projects from simple to complex with instructions and methodologies that are easy to understand.

The goal is someday to be able create complex applications for PHP, perhaps competing with what is seen in Laravel but without its complexity, through a language that is easy to maintain. I don't know if I will achieve this or not, but I will try.

# 🗺️ Development Roadmap

- [x] 🐺 Visual identity and core concept
- [ ] ⚙️ Lexical Analyzer (Lexer) core
- [ ] 🧠 Final syntax definition (Python/Lua hybrid)
- [ ] 🔄 Native PHP code generator
- [ ] 📦 Support for external libraries and other add-ons.

# 🚀 Updates for the latest version (0.2.6):

The initial steps have been taken to implement the "build" command; for now, it simply checks for the presence of the configuration file for the project to be transpiled. If found, it extracts the contents of the "index" and "assets" variables, which will serve as the basis for understanding the project's structure.

# 📋 License:

Awtly is released under GPL-3 license, but is provided "as is". The compiler may contain bugs that could generate incorrect source code, corrupted output files, or unexpected behavior. The author is not responsible for accidental deletion of files or information profiles; we will be regularly updating the project to correct errors and thereby minimize the possibility of data loss.

Always keep backups of your projects and important information.

# 💻 Prerequisites

| Enviroment / Software | Minimum Requirement | Configuration Notes |
| :--- | :---: | :--- |
| **Python** | `3.14+` | Required for the compiler engine. |
| **Operating System** | Windows / Linux | Fully functional on both platforms. |
| **Environment Variables** | `python` / `pyhon3` / `py` | Must be mapped in the system PATH. |

# ⚙️ Installation & Setup

If you don't yet have Python installed, follow the instructions below to install it.

<b>Windows:</b><br>
Download and install from <a href="https://www.python.org/downloads/" target="_blank">Python official downloads page</a> the desired version.

<b>Linux (Lubuntu version):</b><br>
Open your command console and type `"sudo apt update && sudo apt install -y python3 python3-pip python3-venv"`, then press ENTER key and put administrator password. Enter it and wait for Python to finish installing.

If you have Synaptic installed, open it, search for "python3" and mark all the dependencies that appear, including the "python3-pip" and "python3-venv" packages if you need the package manager and virtual environments. Install everything and wait for Synaptic to complete the process.

Download and unzip the project file, since the project is constantly changing due to ongoing development, it's recommended delete any existing folders and run the application from a clean project folder and not unzipping into a folder containing a previously tested version.

# 🛠️ Usage (Command Line Interface)

Open your console / command window, navigate to the Awtly folder and run the command `python awtly.py` (Windows) or `python3 awtly.py` (Linux). If we don't specify any parameter, we will get the following message: "Invalid number of parameters." Possible parameters (this may change in the future):

* `python awtly.py new projectname`<br>
Create a new Awtly project in the current folder or another.

* `python awtly.py addpage projectname pagetoadd`<br>
Add a new page structure to the project folder.

* `python awtly.py delete projectname`<br>
Delete an Awtly project in the current folder or another. Use with caution.

* `python awtly.py build projectname`<br>
It will convert an Awtly project in the current folder or anothers to its PHP equivalent, allowing with a simple language to create websites and applications without getting into many complications of some PHP frameworks. For now we will only receive the message "I will convert the project 'projectname' into its PHP equivalent".

* `python awtly.py help` ("/?" and "-h" are possible variations)<br>
This will display specific help if you type the name of a command after the command "help" or "-h" (for example, "awtly help new" or "awtly -h new"). If you only type "help", "/?", or just "-h", it will display general help for all commands supported by Awtly.

* `python awtly.py` -v<br>
This will display information about the current version of the Awtly IDE.

# 🌟 Milestones:

<a href="https://github.com/marjuanm/awtly/releases/tag/v0.2.5">0.2.5</a> Awtly now works correctly with all basic commands (except `build`), displaying status and error messages in the various languages ​​for which translations are available.

# ❤️ Donations

Awtly is a free project licensed under the GPL-3; anyone can download the source code and run the transpiler, provided they meet the necessary requirements. This is not a commercial project and is sustained through voluntary donations; if you wish to donate and support this project, you can do so via the following platforms.

* ⭐ <a href="https://github.com/sponsors/marjuanm?frequency=recurring" target="_blank">GitHub Sponsors</a>
* ☕ <a href="https://ko-fi.com/msproys" target="_blank">Ko-fi</a>
* 💳 <a href="https://www.paypal.com/donate/?business=73JT73SJF2HXY&no_recurring=0&item_name=Thank+you+for+donating+and+supporting+my+projects.+If+you+don%27t+need+a+commercial+license%2C+any+donation+helps.+Many+thanks%21&currency_code=MXN" target="_blank">PayPal</a>

# 🤝 Community Support

* Awtly is an open-source project developed and maintained in my spare time. While I strive to continuously improve the project, the time I can dedicate to it is limited.
* Bug reports, feature requests, and suggestions for improvement are always welcome. All requests will be reviewed based on available time, project priorities, and implementation feasibility.
* Currently, there is no Service Level Agreement (SLA) or guaranteed technical support for users who are not project sponsors. This means I cannot guarantee response times or specific dates for bug fixes or the implementation of new features.
* Sponsors help fund the ongoing development of Awtly. As a token of appreciation, their bug reports, feature requests, and support inquiries may receive higher priority during the review and handling process.
* If you are a sponsor and wish for your request to be considered with such priority (this feature is not yet enabled in this repository), please include a reference that identifies your sponsorship or donation, such as a link to your GitHub Sponsors profile or proof of a donation made via another method.
* All bug fixes, improvements, and new features will be published in the official Awtly repositories. Prioritizing a request does not mean the improvements are exclusive to sponsors; once implemented, they will be available to the entire community in accordance with the project's license.
* Pull requests are always welcome. Contributions that are high-quality, properly documented, include tests where possible, and adhere to the project's development style are more likely to be accepted.
