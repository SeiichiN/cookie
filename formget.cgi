#! /usr/local/bin/ruby -Ku
# coding: utf-8

require 'cgi'

cgi = CGI.new

str = cgi.params["ck"][0]

puts "Content-Type: text/html; charset=UTF-8"
puts

print "POST_DATA => #{str}<br>\n"
