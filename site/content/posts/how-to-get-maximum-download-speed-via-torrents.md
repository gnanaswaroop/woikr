---
title: "How to get maximum download speed via torrents"
date: 2009-05-23T10:33:59
url: /howto/how-to-get-maximum-download-speed-via-torrents/
categories: ["How Tos"]
tags: ["utorrent", "torrents", "torrent", "maximum download speed", "max download speeds", "good download speed", "port forwarding", "router port forwarding", "broadband"]
image: "/wp/wp-content/uploads/2009/05/image.png"
author: "Setu"
authors: ["setu"]
---
<p><a href="/wp/wp-content/uploads/2009/05/image.png"><img title="image" src="/wp/wp-content/uploads/2009/05/image-thumb.png" alt="image" width="184" height="48" /></a></p>
<p>Most of us know that we can find almost anything on torrents these days. I remember not so long ago, <a href="http://en.wikipedia.org/wiki/Kazaa" target="_blank">KaZaa</a> revolutionized the way we downloaded and shared stuff. That place has now been taken by much faster and comparatively safer <a href="/tag/torrents">torrents</a> (or <a href="http://en.wikipedia.org/wiki/BitTorrent_(protocol)" target="_blank">bittorrents</a>).</p>
<p>The most popular torrent client is <a href="http://www.utorrent.com" target="_blank">uTorrent</a>. Owing to its extremely lightweight and awesome stability, it has become the client of choice for most people. However, its frustrating when you do not get good download speed even though you have a high speed broadband connection. The most probable reason behind this is that the port which uTorrent uses is blocked at your router/modem. To find out if that’s the case, perform the following steps:</p>

<ol>
	<li>
<div>Open uTorrent and go to Options –&gt; Speed Guide. Click on “Test if port is forwarded properly”. Make sure uTorrent is running while you do this. Also, note down the port number somewhere as you will need it in the steps later.<br>
<a href="/wp/wp-content/uploads/2009/05/utorrent-speed-guide.png"><img title="uTorrent_Speed_Guide" src="/wp/wp-content/uploads/2009/05/utorrent-speed-guide-thumb.png" alt="uTorrent_Speed_Guide" width="244" height="232" /></a></div></li>
	<li>
<div>A browser window will open and tell you the status of port forwarding on your router. If you get the OK screen like the one below, it means that port forwarding is properly set up on your router (or ports aren’t blocked) and the low speeds you get are due to crappy service from your ISP. Go thrash him.<br>
<a href="/wp/wp-content/uploads/2009/05/utorrent-speed-guide-ok.png"><img title="uTorrent_Speed_Guide_OK" src="/wp/wp-content/uploads/2009/05/utorrent-speed-guide-ok-thumb.png" alt="uTorrent_Speed_Guide_OK" width="504" height="143" /></a></div></li>
	<li>
<div>However, if you get an error screen like the one below, the port on your router is blocked. Proceed with this tutorial.<br>
<a href="/wp/wp-content/uploads/2009/05/utorrent-speed-guide-error.png"><img title="uTorrent_Speed_Guide_error" src="/wp/wp-content/uploads/2009/05/utorrent-speed-guide-error-thumb.png" alt="uTorrent_Speed_Guide_error" width="504" height="164" /></a></div></li>
</ol>
<p>The above error can be easily fixed using the steps below. We are using the screenshots of Netgear WGR614 wifi router here. If you have any other brand, don’t worry, just look for similar terms in the UI.</p>

<ol>
	<li>
<div>Open the web control panel of your router in a browser. Usually it located at http://192.168.1.1 unless you change it.</div></li>
	<li>
<div>The browser will ask for the admin username and password. If you do not know this, consult the manual which came with the router.</div></li>
	<li>
<div>Look for “Port Forwarding / Port Triggering” option in the menu. It should be somewhere under Advanced settings.<br>
<a href="/wp/wp-content/uploads/2009/05/image1.png"><img title="image" src="/wp/wp-content/uploads/2009/05/image-thumb1.png" alt="image" width="165" height="156" /></a></div></li>
	<li>
<div>On the port forwarding page, you will probably find presets for port forwarding for popular applications like AIM, NetMeeting etc. Since uTorrent is not there, click on “Add Custom Service”.<br>
<a href="/wp/wp-content/uploads/2009/05/image2.png"><img title="image" src="/wp/wp-content/uploads/2009/05/image-thumb2.png" alt="image" width="451" height="318" /></a></div></li>
	<li>
<div>On the Custom Services screen, enter the following details and click on Apply:<br>
<strong>Service Name</strong>: uTorrent (or whatever you might want to call it)<br>
<strong>Service Type</strong>: TCP/UDP<br>
<strong>Starting Port</strong>: &lt;The port number you  noted down above&gt;<br>
<strong>Ending Port</strong>: &lt;The same port number you  noted down above&gt;<br>
<strong>Server IP address</strong>: IP address allocated by your router to your computer. Run “ipconfig” command to find it out (“ifconfig” on Linux).<br>
<a href="/wp/wp-content/uploads/2009/05/image3.png"><img title="image" src="/wp/wp-content/uploads/2009/05/image-thumb3.png" alt="image" width="455" height="226" /></a></div></li>
	<li>Save the settings. Your router will be restarted.</li>
	<li>Perform the steps to check port forwarding again. You should get the success screen this time.</li>
</ol>
<p>Note that you should use the same port you forwarded above in uTorrent each time it starts. To ensure this, go to Preferences –&gt; Connection and uncheck the “Randomize port each start” option.</p>
<p>That’s it! You will get much faster download speeds in <a href="/tag/utorrent" target="_self">uTorrent</a> from now on. Of course it will depend on the seed/peer ratio. But if you are downloading a healthy torrent (seeds &gt; peer), you should get the maximum speed your connection supports.</p>
