<p align="center">
    <img src="https://www.busquedaweb.com/openprojects/awtly/pet.png?v=2" width="auto" height="331" alt="Awtly's pet"><br>
    <a href="https://github.com/marjuanm/awtly/blob/main/history.txt"><img src="https://www.busquedaweb.com/openprojects/awtly/release.png?v=11" height="20" alt="Release version"></a>
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

# 🚀 Updates for the latest version (0.2.3):

Awtly now has a repository on <b><a href="https://gitlab.com/marjuanm/awtly">GitLab</a></b>!; although GitHub will remain the primary repository, the two will be synchronized every few weeks.

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
