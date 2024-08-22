# Change user and nginx fs descriptor limit

file { '/etc/default/nginx':
  ensure => file,
  owner  => 'root',
  group  => 'root',
  mode   => '0644',
}

exec { 'update_nginx_limits':
  command => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx && sudo service nginx restart',
  path    => ['/usr/bin', '/bin'],
  require => File['/etc/default/nginx'],
}

