#!/usr/local/bin/ruby -Ku
# coding: utf-8
require 'cgi'

cgi = CGI.new
cookie = cgi.cookies
count = cookie["ck1"][0].to_i + 1
new_cookie = CGI::Cookie.new("name" => "ck1",
                             "value" => count.to_s,
                             "path" => "/",
                             "expires" => nil,
                             "secure" => false)

print cgi.header("type" => "text/plain", "cookie" => [new_cookie])
puts count

