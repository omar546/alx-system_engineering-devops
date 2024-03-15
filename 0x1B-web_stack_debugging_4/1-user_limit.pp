# Fix user limits

exec { 'fix-config':
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command => "sed -ir 's/^holberton hard nofile 5$/holberton hard nofile 50000/g' /etc/security/limits.conf",
}

exec { 'fix-configII':
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command => "sed -ir 's/^holberton soft nofile 4$/holberton hard nofile 40000/g' /etc/security/limits.conf",
}
