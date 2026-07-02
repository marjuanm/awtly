# Awtly - php transpiller util
# Original file name: newprojectstructure.py
# Current file name: newproject.py
# Copyright (c) 2026 Juan Manuel Mar Hdz.
# Licensed under GPL-3.0, see the license file on the root project structure for more information.

# Purpose: New project structure
# Created date: 17/06/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 19/06/2026
# Last modified username: Juan Manuel Mar Hdz.
class NEWPROJECT:

    PROJECT = ''
    PROJECT += 'index="pages/index.awui"\n'
    PROJECT += 'assets="assets"\n'
    PROJECT += 'templates="templates"\n'
    PROJECT += 'compileextrastohtaccess=yes\n'
    PROJECT += 'compilesitemap=yes\n'
    PROJECT += 'compilerobots=yes\n'
    PROJECT += 'compileasresponsive=yes\n'
    PROJECT += 'outtologalways=yes\n'
    PROJECT += 'maxlogsize=10485760 #10 MB'

    DOCUMENT = ''
    DOCUMENT += '<document>\n'
    DOCUMENT += '  <content>\n'
    DOCUMENT += '    Hello world!\n'
    DOCUMENT += '  </content>\n'
    DOCUMENT += '</document>\n'
    
    DB = ''
    DB += 'dbconnection="mysql"\n'
    DB += 'dbhost="localhost"\n'
    DB += 'dbname=""\n'
    DB += 'dbusername=""\n'
    DB += 'dbpassword=""'

    CACHE = ''
    CACHE += 'images=30d'

    STYLES = ''
    STYLES += 'html, body\n'
    STYLES += '{\n'
    STYLES += '  font-family: "Ubuntu", Arial, Tahoma;\n'
    STYLES += '  font-size: 13.75px;\n'
    STYLES += '  color: #111;\n'
    STYLES += '  scroll-behavior: smooth;\n'
    STYLES += '}\n\n'

    STYLES += 'a:link\n'
    STYLES += '{\n'
    STYLES += '  text-decoration: none;\n'
    STYLES += '}\n\n'

    STYLES += 'a:active\n'
    STYLES += '{\n'
    STYLES += '  text-decoration: none;\n'
    STYLES += '}\n\n'

    STYLES += 'a:hover\n'
    STYLES += '{\n'
    STYLES += '  text-decoration: none;\n'
    STYLES += '}\n\n'

    STYLES += 'a:visited\n'
    STYLES += '{\n'
    STYLES += '  text-decoration: none;\n'
    STYLES += '}'
 