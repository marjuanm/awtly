# Awtly - php transpiller util
# Original file name: savetolog.py
# Copyright (c) 2026 Juan Manuel Mar Hdz.
# Licensed under GPL-3.0, see the license file on the root project structure for more information.

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
