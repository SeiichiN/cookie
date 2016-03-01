#!/usr/local/bin/ruby -Ku
# coding: utf-8

require('cgi')

cgi = CGI.new
count = cgi.params['ck'][0]

puts "Content-Type: text/html; charset=UTF-8"
puts

print Dir::pwd
print "<br>\n"
print "カウント無いし！<br>\n" if (count == nil || count == 0)
print "<br>\n"

print count
