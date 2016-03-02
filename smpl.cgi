#!/usr/local/bin/ruby -Ku
# coding: utf-8

require('cgi')

cgi = CGI.new
count = cgi.params['ck'][0].to_i
count += 1

new_cookie = CGI::Cookie.new("name" => "ck1",
                             "value" => count.to_s,
                             "path" => "/cookie/",
                             "expires" => nil,
                             "secure" => false)

print cgi.header("type" => "text/plain", "cookie" => [new_cookie], "Location" => "../cookie/sample.rhtml")

puts "Content-Type: text/html; charset=UTF-8"
puts

# print cgi.header("type" => "text/plain", "cookie" => [new_cookie])
puts

# cgi.out({'cookie' => new_cookie, 'location' => '../cookie/sample.rhtml'}){''}
puts

