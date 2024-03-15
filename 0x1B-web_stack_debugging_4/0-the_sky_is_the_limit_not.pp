# Fix too much requests problem

exec { 'fix-uslimit':
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command => "sed -i 's/15/4096/g' /etc/default/nginx",
}

exec { 'nginx-restart':
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command => 'sudo service nginx restart',
}
