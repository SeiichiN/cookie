#!/usr/local/bin/ruby -Ku

require 'cgi'

cgi = CGI.new
count = cgi['ck']

print Dir::pwd
print "<br>\n"
print "カウント無いし！<br>\n" if (count == nil || count == 0)
print "<br>\n"

new_cookie = CGI::Cookie.new({'name' => 'ck1',
                             'value' => count.to_s,
                             'path' => '/cookie/',
                             'expires' => nil,
                             'secure' => false
                             })

# print cgi.header("type" => "text/plain", "cookie" => [new_cookie]) %>
cgi.out({"cookie" => [new_cookie], "location" => "../cookie/sample.rhtml"}){'OK'}
