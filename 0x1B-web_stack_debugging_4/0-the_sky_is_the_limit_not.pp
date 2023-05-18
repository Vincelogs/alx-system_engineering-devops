# reduce number of failed request

file { '/etc/nginx/nginx.conf':
  ensure  => present,
  content => inline_template('<%= File.read("/etc/nginx/nginx.conf").gsub(/worker_processes\s+\d+;/, "worker_processes 7;") %>'),
}
exec { 'restart-nginx':
  command => 'nginx restart',
  path    => ['/etc/init.d/'],
}
