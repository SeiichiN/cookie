# coding: utf-8
<%# coding: utf-8 %>
<%
require 'cgi'

cgi = CGI.new

# Cookie の受け取り
count1 = cgi.cookies['count1'].first
count2 = cgi.cookies['count2'].first

# 発行する Cookie の定義
expires = Time.now + 60*60*24*30
cookies = [
	# expires あり
	CGI::Cookie::new({
		"name" => 'count1',
		"value" => (count1.to_i + 1).to_s,
		'expires' => expires,
	}),
	# expires なし：ブラウザを閉じるまで
	CGI::Cookie::new({
		"name" => 'count2',
		"value" => (count2.to_i + 1).to_s,
	}),
]

cgi.out("cookie" => cookies) do
%>
	<html><body>Cookie test: count1='<%= #{count1} %>', count2='<%= #{count2} %>'</body></html>
<%
end
%>
