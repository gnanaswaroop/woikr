---
title: "Setup a local PHP enabled Web Server on your Mac"
date: 2010-09-23T19:09:44
url: /mac/local-web-server-on-your-mac/
categories: ["Mac"]
tags: ["Mac Apache Web Server", "Snow Leopard PHP", "Mac PHP", "Snow leopard web server"]
---
<p>On Windows I've always used <a href="http://www.apachefriends.org/en/xampp.html" target="_blank">XAMPP</a> for all the small PHP scripts I used to write. I was about to download it's Mac version today but I thought, "Snow Leopard is basically *nix. I'm sure they have some PHP!". I was right.  The procedure to setup a basic web server with PHP support is something that Apple may not be proud of but it's fairly simple for someone who knows his way around a terminal. Read ahead for the steps.

 <strong>Apache</strong></p>

<ol>
	<li>Goto "System Preferences-&gt;Sharing" and enable Web Sharing. That's it! The URL is <em>http://localhost/~&lt;yourusername&gt;</em> or <em>http://&lt;Your IP Address&gt;/~&lt;yourusername&gt;</em> as shown in the Web Sharing info screen. This links to the files stored in <em>"Sites"</em> folder of your home directory (<em>"/Users/&lt;yourusername&gt;/Sites"</em>).</li>
</ol>
<p><strong>PHP</strong></p>

<ol>
	<li>Enable PHP Module loading. Open the Terminal, edit <code>"/private/etc/apache2/httpd.conf"</code> using your favorite editor using <em>sudo</em>. Look for the line <code>"#LoadModule php5_module  libexec/apache2/libphp5.so"</code> and un-comment it by removing the <em>#</em> from the beginning.</li>
	<li>Create a <em>php.ini</em> file. cd to <em>"/etc/"</em> in the Terminal and type <code>"sudo cp php.ini.default php.ini"</code>. This will create a <em>php.ini</em> based on the latest PHP 5.3. If you want to use 5.2 use <em>"php.ini.default-5.2-previous"</em> instead.</li>
	<li>Restart Web Server. Goto the "Web Sharing" preference, disable it and then re-enable it. Clearly, it  restarts the Apache Web Server to load the PHP module.</li>
	<li>Test your PHP script!</li>
</ol>
<p>If you have any simple questions, ask away! Complex questions, please Google.  Thanks to <a href="http://gabtechnews.wordpress.com/2009/09/29/using-apache-and-php-on-snow-leopard/" target="_blank">Caffeine Lack</a> for the tip!</p>
