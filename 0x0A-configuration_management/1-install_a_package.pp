# to install Flask Version 2.1.0 using puppet and pip3

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
