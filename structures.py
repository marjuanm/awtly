# Awtly - php transpiller util
# Original file name: newprojectstructure.py
# Current file name: structures.py
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
    
# Purpose: Save to log structure
# Created date: 19/06/2026
# Created by username: Juan Manuel Mar Hdz.
# Last modified date: 19/06/2026
# Last modified username: Juan Manuel Mar Hdz.
class SAVETOLOG:
    
    FUNCTIONS = r"""
   
function savetolog($message, $logfile = '', $maxsize = 10485760)
{

  if(trim($logfile) == '') $logfile = 'logs/defaultlog.log';
  if((double)$maxsize <= 0) $maxsize = 10485760; // 10 MB
  
  //if the log dir not exists, create then
  $dir = dirname($logfile);
  if(!is_dir($dir)) mkdir($dir, 0777, true);
  
  //if the file exists then split and keep the most recent half
  if(file_exists($logfile) && filesize($logfile) > $maxsize)
  {
    
    $content = file_get_contents($logfile);
    $middle = (int)(strlen($content) / 2);
    $newline = strpos($content, PHP_EOL, $middle);
    
    if($newline !== false)
      $content = substr($content, $newline + strlen(PHP_EOL));
    else
      $content = substr($content, $middle);
    
    file_put_contents($logfile, $content);

  }
  
  $date = date("Y-m-d H:i:s");
  $line = "[{$date}] {$message}\n";
  file_put_contents($logfile, $line, FILE_APPEND | LOCK_EX);

}
   
"""
