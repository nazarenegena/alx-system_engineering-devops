#!/usr/bin/env ruby
#three-reputation token matching method
pattern = /hbt+n/
if ARGV.any?
ARGV.first.scan(pattern) { |j| puts j }
end
