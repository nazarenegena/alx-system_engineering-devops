# script describing kill process
# kill process pKill
exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
