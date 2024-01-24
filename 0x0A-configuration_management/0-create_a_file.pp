# Using Puppet, create a file in /tmp.
file {'school':
  path    => '/tmp/school',
  content => 'I love puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
}
