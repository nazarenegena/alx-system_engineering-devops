# script describing kill process
# kill process pKill
exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/bin:/usr/bin',
  onlyif  => 'pgrep killmenow',
  refreshonly => true,
}
