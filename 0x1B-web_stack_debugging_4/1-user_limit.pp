# change user limit 

file { '/etc/security/limits.conf':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "root soft nofile 100000\nroot hard nofile 100000\n* soft nofile 100000\n* hard nofile 100000\n",
}

