# create a manifest that kills process

exec { 'killmenow':
  command  => 'pkill killmenow',
  provider => 'shell',
}
