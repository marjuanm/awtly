# Purpose: New project structure
# Created date: 17/06/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 17/06/2026
# Last modified username: Juan Manuel Mar Hdz.
class NPRJSTRUCT:

    PROJECT = ''
    PROJECT += 'assets="assets"\n'
    PROJECT += 'templates="templates"\n'
    PROJECT += 'compileextrastohtaccess=yes\n'
    PROJECT += 'compilesitemap=yes\n'
    PROJECT += 'compilerobots=yes\n'
    PROJECT += 'compileasresponsive=yes'

    DOCUMENT = ''
    DOCUMENT += '<document>\n'
    DOCUMENT += '  Hello world!\n'
    DOCUMENT += '</document>\n'
    
    DB = ''
    DB += 'DB_CONNECTION="mysql"\n'
    DB += 'DB_HOST="localhost"\n'
    DB += 'DB_DATABASE=""\n'
    DB += 'DB_USERNAME=""\n'
    DB += 'DB_PASSWORD=""'

    CACHE = ''
    CACHE += 'images=30d'

    STYLES = ''
    STYLES += 'html, body\n'
    STYLES += '{\n'
    STYLES += '  font-family: "Ubuntu", Arial, Tahoma;\n'
    STYLES += '  font-size: 13.75px;\n'
    STYLES += '  margin: 0;\n'
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
    STYLES += '}\n'
