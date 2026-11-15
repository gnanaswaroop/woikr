---
title: "Custom Multi-touch firmware on your Samsung Galaxy Spica"
date: 2011-01-31T10:22:20
url: /howto/install-a-multi-touch-firmware-on-your-spica/
categories: ["How Tos", "Android"]
tags: ["Samsung Galaxy Spica", "Samsung Galaxy i5700", "Samsung Galaxy Spica Root", "Samsung Galaxy Spica Multitouch", "Samdroid Kitchen", "SamdroidMod Kitchen", "Custom Firmware on Spica", "Spica Multitouch", "Spica Root"]
---
<p>You <a href="/mobile-phones/root-your-samsung-galaxy-spica-i5700" target="_blank">successfully rooted your Samsung Galaxy Spica</a>. Now what? How to install a new custom firmware? How to enable Multi-touch? How to do that kitchen thingy? Here is the answer. This tutorial will make all these things clear so you can use your Spica like a pro!</p>

<h4>Backup/Disclaimer</h4>
<p>This process will erase everything from your device and make it shiny new (Not literally of course). I'd recommend you to back up your contacts, SMS and other important data. If you want to backup apps and related settings and data download and use <a href="http://matrixrewriter.com/android/index.html" target="_blank">Titanium Backup</a>. They have an <a href="http://matrixrewriter.com/wiki/tiki-index.php" target="_blank">excellent wiki</a> that you can go through for help. I personally didn't backup anything because it gives me the feeling of buying a new device. But that's me.</p>

<h4><strong>Requirements</strong></h4>
<ul>
	<li>A rooted Samsung Galaxy Spica i5700</li>
	<li>A memory card</li>
	<li>The firmware installation and patching procedure may look complex but it doesn't take much time or effort. You basically have to deal with 2 things: Recovery menu on your Phone and SamdroidMod Kitchen.</li>
</ul>
<h4>Recovery Menu</h4>
<p>Boot the phone into the Recovery Menu by pressing <strong>Volume Down</strong> + <strong>Call</strong> + <strong>Call End</strong> buttons at the same time. <strong>Trick:</strong> Keep the Volume Down and Call Button pressed and then pres the Call End button till the phone boots.</p>
<p>&nbsp;</p>
<p>It should look like the screen below or maybe slightly different based on your kernel version. While you may not use most of the options listed here, the things you should familiarize yourself with are these:</p>

<ul>
	<li>Apply from "SD Card/update.zip" and "SD Card/any ZIP" This option allows you to apply a patch or a whole firmware on your phone. I generally prefer to use the any ZIP option since that doesn't need me to modify the names on the file to update.zip every time.</li>
	<li>Partition Let's you partition and format your SD Card so you can use it to store apps using Apps2SD.</li>
	<li>Wipe Cache: Wipes the dalvik-cache that contains cache files created by Android OS and various installed apps. (Safe to clear) Data: Resets everything on your phone. (Not safe of course)</li>
</ul>
<p><a href="/wp/wp-content/uploads/2010/10/1.jpg"><img title="1" src="/wp/wp-content/uploads/2010/10/1-200x300.jpg" alt="" width="200" height="300" /></a></p>

<h4>SamdroidMod Kitchen</h4>
<p><a href="http://forum.samdroid.net/f9/samdroidmod-kitchen-v-2-all-one-samsung-spica-i5700-en-1901/" target="_blank">SamdroidMod Kitchen</a> is a web application created by <a href="http://forum.samdroid.net/f15/thanks-141/#post30659" target="_blank">LeshaK</a> that allows you to <em>cook</em> a custom firmware for your phone. Basically it means that you can design a firmware with the exact kernel you want, the languages, the themes and chosen applications as well.</p>

<h4>Procedure (Cook A Firmware)</h4>
<ol>
	<li>Go to the the <a href="http://forum.samdroid.net/f9/samdroidmod-kitchen-v-2-all-one-samsung-spica-i5700-en-1901/" target="_blank">Kitchen</a> and get ready to cook a Custom Firmware (also called ROM by some).</li>
	<li>
<div>Select a <strong>Base Package</strong>.</div>
<div>- "resigned"  is optimized and works faster than "deodexed". But you need "deodexed" for themes and other mods (camera-fix, rotary lockscreen etc.)</div>
<div>- Full Package means install a complete firmware; Light Package means install updates including kernel, software, patches to your existing firmware and Remove Package is to remove packages. I personally never used "Removed Package". Titanium Backup is good enough for that.</div></li>
	<li>
<div>Select a <strong>Kernel</strong>.</div>
<div>- "inc vol" will increase the volume of your phone by a notch.</div>
<div>- 1% or 5% battery will report battery levels in the said intervals.</div>
<div>- "undervolted" kernel runs the CPU slower and consumes lesser battery. It may be unstable and lag though.</div></li>
	<li>Select a Home application. You can install the one you want later but you have to select at least 1 for now.</li>
	<li>
<div>Similarly select the other applications you want from the other sections. Most of the apps listed have descriptions so you can understand what you are selecting. If there is an issue, you can always post a comment and ask me or ask in the Samdroid.net forums.</div>
<div>Note: Must haves in my opinions are: WiFi Tether, Gallery3D (without dynamic background) and Super Circle Battery.</div></li>
	<li>Don't select any experimental components. If you are not happy with the performance wait sometime for a Froyo (Androy 2.2) on Spica tutorial. This is for people who want features but value stability more than performance.</li>
	<li>Cook the firmware, download it and place it in the root (base) folder of your SD Card.
<strong>Note:</strong> The free members have a download limit of 100 MB a day</li>
</ol>
<h4>Procedure (Install the Firmware)</h4>
<ol>
	<li>Backup everything!</li>
	<li>Boot into the Recovery Menu (explained above).</li>
	<li>Wipe data and cache both.</li>
	<li>Select "Apply any ZIP from SD" and select the ZIP file that you just copied to the card.</li>
	<li>Follow the onscreen instructions and reboot your phone. Wait patiently for sometime. The first time may take as long as 15-20 minutes. If the phone is still stuck in the boot loop, just verify that you selected a Home Launcher app. Else just cook a ROM again with default options and try it. It should work.</li>
	<li>You are done!</li>
</ol>
<h4>Now what?</h4>
<p>Now just enjoy! Treat it as a brand new phone and have fun. Try the multi-touch (only 2 fingers are supported) in Maps and Browser app! Cook different ROMs and try them on if you are adventurous.</p>
<p>Thanks again to LeshaK, all the devs at <a href="http://forum.samdroid.net/">Samdroid.net</a> for the awesome work! Special thanks to <a href="http://twitter.com/munchy_cool">@munchy_cool</a> for being my 24x7 helpline for Spica related stuff and <a title="darth_llamah" href="http://forum.samdroid.net/members/darth_llamah/" target="_blank">darth_lammah</a> for the tips about this article :)</p>
