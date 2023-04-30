#!/usr/bin/pup
#installing flask from pip3 using Puppet
package {'flask':
  ensure   => '2.5.0',
  provider => 'pip3'
}
