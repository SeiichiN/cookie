#!/usr/local/bin/ruby -Ku

require('cgi')
cgi = CGI.new
s = CGI.escapeHTML(cgi['text1'])
expires = Time.now + 60 * 60 * 24 * 1
c = CGI::Cookie.new({'name'=>'name','path'=>'/cookie/','value'=>s,'expires'=>expires})
cgi.out({'cookie' => c, 'location' => '../cookie/hello.rhtml'}){''}
