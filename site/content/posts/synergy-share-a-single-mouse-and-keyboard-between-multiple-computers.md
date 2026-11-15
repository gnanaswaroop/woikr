---
title: "Synergy: share a single mouse and keyboard between multiple computers"
date: 2008-12-17T18:17:50
url: /howto/synergy-share-a-single-mouse-and-keyboard-between-multiple-computers/
categories: ["How Tos"]
tags: ["synergy", "synergy2", "share single keyboard and mouse", "multiple computers on single desk", "screen sharing", "multiple screens", "single mouse multiple screens", "multiple desktops", "extended desktops"]
---
<p><a href="/wp/wp-content/uploads/2008/12/synergy_logo.png"><img class="alignnone size-full wp-image-1847" title="synergy_logo" src="/wp/wp-content/uploads/2008/12/synergy_logo.png" alt="" width="212" height="61" /></a></p>
<p>This article/tutorial is for those people who use more than one computer at their desk and have to juggle through the stack of mice and keyboards to find the correct one.</p>
<p>With Synergy, redirecting the mouse and keyboard is as simple as moving the mouse off the edge of your screen. Synergy also merges the clipboards of all the systems into one, allowing cut-and-paste between systems. Furthermore, it synchronizes screen savers so they all start and stop together and, if screen locking is enabled, only one screen requires a password to unlock them all.</p>

<h3>System Requirements</h3>
<ul>
	<li>Microsoft Windows 95, Windows 98, Windows Me (the Windows 95 family)</li>
	<li>Microsoft Windows NT, Windows 2000, Windows XP (the Windows NT family)</li>
	<li>Mac OS X 10.2 or higher</li>
	<li>Unix
<ul>
	<li>X Windows version 11 revision 4 or up</li>
	<li>XTEST extension (use "xdpyinfo | grep XTEST" to check for XTEST)</li>
</ul>
</li>
</ul>
<ul>
	<li>All systems must support TCP/IP networking.</li>
</ul>
<h3>Setup</h3>
<p>It is recommended to share the keyboard and mouse of the system whose display is in the middle of all the displays on your desk. That way, it is easier to move your mouse pointer around different screens. In a 2 system setup, use the keyboard and mouse of the system on the left. If you have a lot of monitors, you can also go vertically.</p>

<h3>Download</h3>
<p>Download Synergy from <a href="http://sourceforge.net/project/showfiles.php?group_id=59275&amp;package_id=58013&amp;release_id=406637" target="_blank">here</a> and install it on ALL the systems.</p>

<h3>Configure Synergy</h3>
<ol>
	<li>Start Synergy on the system whose mouse and keyboard you want to share.<br>
<a href="/wp/wp-content/uploads/2008/12/synergy_host_screen1.png"><img class="alignnone size-medium wp-image-1830" title="synergy_host_screen1" src="/wp/wp-content/uploads/2008/12/synergy_host_screen1-300x225.png" alt="" width="300" height="225" /></a></li>
	<li>Select "Share this computer's keyboard and mouse (server)" and click "Configure".<br>
<a href="/wp/wp-content/uploads/2008/12/synergy_host_screen2.png"><img class="alignnone size-medium wp-image-1831" title="synergy_host_screen2" src="/wp/wp-content/uploads/2008/12/synergy_host_screen2-300x206.png" alt="" width="300" height="206" /></a></li>
	<li>Now we need to add the host screen. Click on the "+" button under Screens.<br>
<a href="/wp/wp-content/uploads/2008/12/synergy_host_screen3.png"><img class="alignnone size-medium wp-image-1832" title="synergy_host_screen3" src="/wp/wp-content/uploads/2008/12/synergy_host_screen3-200x300.png" alt="" width="200" height="300" /></a></li>
	<li>Enter the computer's name (or IP address) under "Screen Name". Enter an alias. Note that these 2 fields cannot have the same value. It is also recommended to use computer name instead of IP address for better readability and management. Click "OK" when done.</li>
	<li>Click on the "+" button under Screens again and add client systems.<br>
<a href="/wp/wp-content/uploads/2008/12/synergy_host_screen4.png"><img class="alignnone size-medium wp-image-1833" title="synergy_host_screen4" src="/wp/wp-content/uploads/2008/12/synergy_host_screen4-200x300.png" alt="" width="200" height="300" /></a></li>
	<li>Repeat step 6 for all the client systems on your desk.</li>
	<li>Let's link the screens. Select [New Link] option under Links. Now specify the position of screens on your desk relative to one another. For example - if system1 is to the right of host, here is what the setting should look like:<br>
<a href="/wp/wp-content/uploads/2008/12/synergy_host_links1.png"><img class="alignnone size-medium wp-image-1835" title="synergy_host_links1" src="/wp/wp-content/uploads/2008/12/synergy_host_links1-300x206.png" alt="" width="300" height="206" /></a></li>
	<li>Note that it is important to specify the links both ways. So, if system1 is to the right of host, you also have to specify that host is to the left of system1:<br>
<a href="/wp/wp-content/uploads/2008/12/synergy_host_links2.png"><img class="alignnone size-medium wp-image-1836" title="synergy_host_links2" src="/wp/wp-content/uploads/2008/12/synergy_host_links2-300x206.png" alt="" width="300" height="206" /></a></li>
	<li>Repeat the above steps for all the screens.<br>
<a href="/wp/wp-content/uploads/2008/12/synergy_host_links3.png"><img class="alignnone size-medium wp-image-1837" title="synergy_host_links3" src="/wp/wp-content/uploads/2008/12/synergy_host_links3-300x205.png" alt="" width="300" height="205" /></a></li>
	<li>This will setup your host machine. To configure a client, you simply have to start Synergy on the client system and select the option "Use another computer's shared keyboard and mouse". Enter host computer's name or IP address.<br>
<a href="/wp/wp-content/uploads/2008/12/synergy_client_screen11.png"><img class="alignnone size-medium wp-image-1840" title="synergy_client_screen11" src="/wp/wp-content/uploads/2008/12/synergy_client_screen11-300x228.png" alt="" width="300" height="228" /></a></li>
	<li>Once you are done with configuration, you can test it out by clicking on the "Test" button on all the machines.</li>
	<li>Once you are satisfied with the testing, you can run the program by clicking on the "Start" button. The Synergy icon in the system tray will change showing that it is connected to the clients.</li>
	<li>You can configure Synergy to Auto Start during operating system. Click on Auto Start and choose to start it at windows logon or at system startup.<br>
<a href="/wp/wp-content/uploads/2008/12/synergy_auto_start.png"><img class="alignnone size-medium wp-image-1841" title="synergy_auto_start" src="/wp/wp-content/uploads/2008/12/synergy_auto_start-270x300.png" alt="" width="270" height="300" /></a></li>
</ol>
<p>That's it! You can now use a single keyboard and mouse across all the computers on your desk and get rid of all the cable clutter and juggling through the stack to find the right one.</p>
