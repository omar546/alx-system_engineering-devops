# A puppet to fix server by altering a line

$wrongfile = '/var/www/html/wp-settings.php'

#replace "phpp" with "php"

exec { 'fix_line':
  command => "sed -i 's/phpp/php/g' ${wrongfile}",
  path    => ['/bin','/usr/bin']
}
