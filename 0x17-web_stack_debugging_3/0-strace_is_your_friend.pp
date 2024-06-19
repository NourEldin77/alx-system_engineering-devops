# change the extention from phpp to php
$wp_settings_file = '/var/www/html/wp-settings.php'

# Ensure the file exists before attempting to modify it
file { $wp_settings_file:
  ensure => file,
}

exec { 'fix_phpp_extension':
  command => "sed -i 's/\\.phpp/\\.php/g' ${wp_settings_file}",
  onlyif  => "grep -q '\\.phpp' ${wp_settings_file}",
  path    => ['/bin', '/usr/bin'],
  require => File[$wp_settings_file],
}
