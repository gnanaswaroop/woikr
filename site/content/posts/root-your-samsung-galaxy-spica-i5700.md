---
title: "Root your Samsung Galaxy Spica i5700"
date: 2010-08-29T20:26:34
url: /android/root-your-samsung-galaxy-spica-i5700/
categories: ["Android", "Mobile Phones"]
tags: ["Root Android", "root spica", "root samsung galaxy i5700", "samsung galaxy spica apps to sd", "samsung galaxy spica wifi tethering"]
author: "Chirag"
authors: ["chirag"]
---
<p>So you've been hearing that you need to root your Android phone for making the most out of it. In our opinion it depends on your usage and Phone model. If you have a Nexus One running the latest Froyo, there aren't as many benefits you get out of rooting. But for most other models you can get alternate firmwares which remove the bloatware loaded by Manufacturer/Carrier and provide lots of extra features.</p>
<p>Take Spica for example, without root it's an above average budget Android phone. But root it and it turns into an excellent Android phone. The amazing developers at <a href="http://forum.samdroid.net/" target="_blank">Samdroid</a> especially <a href="http://twitter.com/leshak" target="_blank">Leshak</a>, <a href="http://forum.samdroid.net/f9/samdroid-turbo-1301/" target="_blank">antibyte</a> and <a href="http://www.youtube.com/watch?v=RPyRhBtKIRk" target="_blank">Gabriel-LG</a> are totally pushing it's capabilities beyond limits.</p>
<p>&nbsp;</p>

<p><strong>Long Term Benefits</strong></p>

<ul>
	<li>More free Phone memory (Get rid of bloatware)</li>
	<li>Move Apps to SD card</li>
	<li>Special Apps
<ul>
	<li>Froyo's 3D Gallery</li>
	<li>WiFi Tethering</li>
	<li>Single click CacheCleaner</li>
	<li>Enhanced Phone.apk</li>
	<li>Titanium Backup for backing up all apps and settings</li>
</ul>
</li>
	<li>Multitouch!</li>
	<li>Visual Delight
<ul>
	<li>Themes</li>
	<li>Boot Animations</li>
	<li>More accurate battery indicator</li>
</ul>
</li>
	<li>Various Bug fixes and optimizations</li>
</ul>
<p><em>Rooting will just give you the ability to get the above benefits. We'll cover them all in a separate tutorial.</em></p>
<p><strong>Tools</strong></p>

<ul>
	<li>A Windows computer (Does NOT work on Virtual machines under MacOS or Linux)</li>
	<li>An officially unlocked Samsung Galaxy Spica (We had the latest ECLAIR.DDJC5 Indian firmware but any firmware will do)</li>
	<li><a href="http://forum.samdroid.net/f9/lk2-08-original-firmwares-root-new-superuser-wifi-tether-bb-12-07-2010-a-1193/" target="_blank">Leshak 2.08 kernel</a></li>
	<li>Odin Multi Downloader</li>
	<li>Samsung JC3 OPS file</li>
</ul>
<p>Here is a <a href="http://cid-f4c846b36719b2cc.office.live.com/self.aspx/woikr/SpicaRoot.zip">ZIP file</a> containing the last 3.</p>
<p><strong>Procedure</strong></p>
<p>Although the procedure doesn't erase any data whatsoever, we'd suggest you to backup important data. Also, we should pass along the statutory warning from the developers that the procedure has the potential to brick your phone, even though we have never faced it or seen anyone facing it.</p>

<ol>
	<li>Install the Samsung Utility from the CDROM that came along with your phone. This will also install the phone drivers.</li>
	<li>Unzip the downloaded ZIP file and keep all 3 files in the same folder.</li>
	<li>Turn off your phone and remove the SIM, leave the SD Card as it is.</li>
	<li>Open Odin Multi Downloader
<ul>
	<li>Make sure only "Reboot", "Protect OPS" and "Reset Time" are checked and "Reset Time" is set to 300.</li>
	<li>Select the OPS file from the ZIP in the "Select OPS" field.</li>
	<li>Select the tar file from the ZIP in the PDA field of "Select Images to Download".<br>
<a href="/wp/wp-content/uploads/2010/08/spica_root1.jpg"><img class="alignnone size-medium wp-image-4380" title="spica_root1" src="/wp/wp-content/uploads/2010/08/spica_root1-300x209.jpg" alt="" width="300" height="209" /></a></li>
</ul>
</li>
	<li>Hold Volume Down + Camera + End Call keys for some time till your Phone shows a "Downloading..." screen.</li>
	<li>Connect your phone to your computer using the supplied USB cable.
<ul>
	<li>Odin should detect your phone and show a COM port mapping.<br>
<a href="/wp/wp-content/uploads/2010/08/spica_root2.jpg"><img class="alignnone size-medium wp-image-4381" title="spica_root2" src="/wp/wp-content/uploads/2010/08/spica_root2-300x208.jpg" alt="" width="300" height="208" /></a></li>
	<li>If it doesn't work try a different USB port or reinstall the drivers and start from Step 4 again.</li>
</ul>
</li>
	<li>Press Start.
<ul>
	<li>You'll see a green progress bar and a timer. The display on the top will say RESET. The "Message" field in bottom left will display certain messages. You can ignore the messages and wait for the process to complete.<br>
<a href="/wp/wp-content/uploads/2010/08/spica_root3.jpg"><img class="alignnone size-medium wp-image-4382" title="spica_root3" src="/wp/wp-content/uploads/2010/08/spica_root3-300x208.jpg" alt="" width="300" height="208" /></a></li>
	<li>If timer starts but progress bar doesn't, close Odin and disconnect the  phone from the computer. Take out and re-insert the batter and move to  Step 5.</li>
	<li>After some time the RESET will change to a PASS. Wait for the timer to be over and display to change to a blue background saying PASS.Your phone will reboot during the process.<br>
<a href="/wp/wp-content/uploads/2010/08/spica_root4.jpg"><img class="alignnone size-medium wp-image-4383" title="spica_root4" src="/wp/wp-content/uploads/2010/08/spica_root4-300x208.jpg" alt="" width="300" height="208" /></a></li>
</ul>
</li>
	<li>If the phone booted into "System Recovery" mode, select the "Reboot system now" option.</li>
	<li>Once the phone boots normally, goto Settings/About Phone. You'll see Leshak's kernel and Samdroid.net build. Your phone has been rooted successfully!</li>
</ol>
<p><strong>New Stuff</strong></p>

<ul>
	<li>You can press Volume Down + Call + End Call keys while booting to enter the Recovery mode. This can be used to partition SD card, clear caches, make system backups and install updates and patches.</li>
	<li>You can find a new SuperUser app on your phone. This lets you use applications which run only on Rooted phones. We recommend installing the following two from the market for now:
<ul>
	<li>CacheCleaner<br>
Cleans up all the user/system app cache in a single click. No need to goto every app and remove the cache.</li>
	<li>TitaniumBackup<br>
Backups all your apps and settings and allows you to remove any protected app.</li>
</ul>
</li>
	<li>Apps2SD<br>
Everyone hates Android because of the limited App install memory. They fixed it in Froyo but Samsung has no plans to release it on Spica. So the only solution is to setup Apps2SD. The good news is that Apps2SD is included In the kernel you just installed. All you need to do is backup your SD card, make an ext2 partition on it using the Recovery console, and reboot. When the phone boots up all your Apps and cache would've been moved to the SD Card.<br>
<em>We personally recommend you to not move your Apps to SD Card unless you have a Class 6 SD Card. It will make your phone noticeably slow. </em></li>
	<li>Wifi Tethering<br>
The kernel includes a WiFi tethering app. You can use your Spica with EDGE/3G as a Wireless router.</li>
</ul>
<p><strong>Next?</strong></p>
<p>As we said before, rooting gives you loads of abilities. This article just covered some of the basic stuff that won't take much effort. In the future articles we will explain how to enable Multi Touch, install a custom firmware and more.<strong> </strong></p>
<strong>UPDATE:</strong> <a href="/howto/install-a-multi-touch-firmware-on-your-spica">Install a Custom Multi-touch firmware on your Spica</a>!
