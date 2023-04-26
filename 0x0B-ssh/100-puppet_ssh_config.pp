#!/usr/bin/env bash
#make changes to configuration file
file_line { 'Use private key':
ensure => 'present',
path   => 'IdentityFile ~/.ssh/school'
}

file_line { 'Avoid password':
ensure => 'present',
path   => '/etc/ssh/ssh_config',
line   => 'PasswordAuthentification no'
}
