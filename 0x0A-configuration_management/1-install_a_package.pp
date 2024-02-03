#!/usr/bin/puppet
# installs Flask from pip
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
# Install Werkzeug as a requirement for Flask
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  => Package['Flask'],
}
