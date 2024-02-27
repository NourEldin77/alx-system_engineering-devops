#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:([A-Za-z]+|\+?[0-9]{11,11})\] \[to:([A-Za-z]+|\+?[0-9]{11,11})\] \[flags:(-1:-?\d:-?\d:-?\d:-1)\]/).join(",")
