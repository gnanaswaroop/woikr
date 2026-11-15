---
title: "Using Non-Samsung Wi-Fi USB Adapter with Samsung Smart/Internet TV"
date: 2012-03-14T09:00:23
url: /howto/using-non-samsung-wi-fi-usb-adapter-with-samsung-smartinternet-tv/
categories: ["How Tos", "Home Entertainment"]
tags: ["samsung", "samsung TV", "samsung internet TV"]
aliases: ["/home-entertainment/using-non-samsung-wi-fi-usb-adapter-with-samsung-smartinternet-tv/"]
---
<p><img title="samsung smart tv logo.png" src="/wp/wp-content/uploads/2012/03/samsung-smart-tv-logo.png" alt="samsung smart tv logo" width="499" height="92" /></p>

<blockquote>
<p><em>This is a guest post by <a href="http://www.linkedin.com/profile/view?id=15139659">Rajnish Jain</a>. Rajnish is a product development enthusiast having around 12.5 years of experience. He enjoys solving complex technical problems and has worked on wide range of technologies including Open Source frameworks, Unix (shell scripting) &amp; embedded device programming.</em></p>
</blockquote>
<p>When you purchase a Samsung Smart TV (UA40D5500RR, for example), depending on the model, it may or may not support inbuilt Wi-Fi function. If it doesn’t, then Samsung recommends using WIS09ABGN USB WiFi adapter to let your TV connect to a Wireless router. Samsung has priced this USB adapter at a very huge cost (around INR 6,000) and any other adapter is not recognized by the TV. WTF?</p>
<p>I tried not to fall prey to this monopolistic approach by the company and put myself on work to find out a hack so that any Wi-Fi USB adapter is accepted by the TV. I found <a href="http://wiki.samygo.tv/index.php5/Using_NoN-Samsung_USB_WiFi_dongles_with_TV">this wonderful link</a> which helped a lot.</p>

<blockquote>
<p><em><strong>DISCLAIMER</strong>: The author of this article &amp; woikr are not responsible for any damage/malfunction caused to the TV by following the instructions written below. Please continue at your own risk.</em></p>
</blockquote>

<p>Few facts first:</p>

<ol>
	<li>WIS09ABGN uses a chipset which is RT2870. This manufacturer of this chipset is Ralink Technologies.</li>
	<li>The Samsung Smart TVs internally run Linux OS (which version, which variant is immaterial for this post here).</li>
	<li>
<div>Every USB device has these two properties (apart from many others):</div>
<ul>
	<li><strong>VID</strong> – vendor identification</li>
	<li><strong>PID</strong> – product identification</li>
	<li>Samsung TVs have built-in intelligence that if the Wi-Fi adapter that’s plugged in doesn’t have Samsung specific VID/PID values, the TV will reject it.</li>
</ul>
</li>
	<li>
<div>Samsung specific VID/PID values that the TV is expecting are:</div>
<ul>
	<li><strong>VID</strong>: 04E8</li>
	<li><strong>PID</strong>: 2018</li>
</ul>
</li>
	<li>I found this info (and the chipset info) <a href="http://wikidevi.com/wiki/Samsung_WIS09ABGN">here</a>.</li>
	<li>The same page (<a href="http://wikidevi.com/wiki/Samsung_WIS09ABGN">http://wikidevi.com/wiki/Samsung_WIS09ABGN</a>) tells us that the WIS09ABGN is running rt2870sta driver based on Linux.</li>
	<li>To be able to use any Wi-Fi USB adapter with Samsung TV, all you need to do is change that USB device’s VID/PID values to <strong>04E8 : 2018</strong> (Values assigned to Samsung Electronics Co.)</li>
</ol>
<p>So, to begin with, we need a USB adapter which is based on Ralink’s RT2870 chipset. A quick search on Google and Ifound this one: <a href="http://www.edimax.com/en/produce_detail.php?pd_id=223&amp;pl1_id=1&amp;pl2_id=44">Edimax EW-7718Un</a>. I could find this one on ebay.in for INR 999/- and quickly ordered it.</p>
<p>Upon receiving the Edimax dongle, I started towards modifying the required values. These values reside on EEPROM (e2p) of the chipset, so changing them means you need to issue commands that modify the values on e2p. However, e2p ioctl is generally not available by default, so you will need to modify the driver code, compile it, and then change the values. This is explained below.</p>
<p>We now already know that we need to deal with Linux OS. So, we need a Linux box wherein our USB adapter can be plugged in and its properties can be seen and modified.</p>
<p>For this, instead of looking for a Linux based box, or creating a new partition in my laptop’s hard drive, I chose to go in for USB flash drive based environment. That is, without changing any configuration of my Windows XP based laptop, I can get a new OS to play around with.</p>

<ol>
	<li>Start your Windows based computer.</li>
	<li>Plugin a USB flash drive into it.</li>
	<li>Follow the instructions at <a href="http://www.ubuntu.com/download/ubuntu/download">http://www.ubuntu.com/download/ubuntu/download</a> and make your USB drive bootable with ubuntu, <strong>preferably version 10.04</strong>.</li>
	<li>Once the flash drive is ready, restart your computer, change the boot sequence in BIOS so that it boots from the USB drive and you will get into a new world of ubuntu.</li>
	<li>
<div>Once the system comes up, plug in your USB adapter, open the command terminal and type:</div>
<ol type="a">
	<li># lsusb</li>
	<li>
<div>You should be able to figure out this string for your Edimax EW-7718Un adapter:</div>
<div><span><strong>7392:7718</strong></span></div></li>
	<li>These are the VID/PID values assigned to this USB device. And this is the task in hand – to replace these values with <strong>04E8:2018</strong>.</li>
</ol>
</li>
	<li>Plug out the adapter.</li>
	<li>
<div>Now is the time to first download the relevant driver. Open Mozilla Firefox browser (which comes installed by default with ubuntu), and download the driver from this location:</div>
<ol type="a">
	<li><a href="http://www.ralinktech.com/en/04_support/license.php?sn=5021">http://www.ralinktech.com/en/04_support/license.php?sn=5021</a></li>
	<li>
<div>You can enter any name and e-mail address in the boxes that appear on this link. Why are we downloading the driver? Because, to change the VID/PID values on EEPROM of the USB adapter, we will need to issue the following commands:</div>
<ul>
	<li># iwpriv ra0 e2p 208=04E8</li>
	<li># iwpriv ra0 e2p 20A=2018</li>
</ul>
</li>
	<li>
<div>But by default the e2p ioctl is missing for us. So, we will customize the driver code to introduce e2p ioctl and then the above command will do us the trick.</div>
<div><span><strong>NOTE</strong></span><span>: If the above sequence of commands (with USB adapter plugged-in) works for you then you are done.</span><span><strong> You don’t need to follow the rest of the tutorial</strong></span><span>.</span></div></li>
</ol>
</li>
	<li>
<div>Un-package the driver in a folder, say DRIVER_ROOT. Make the following changes to driver code:</div>
<ol type="a">
	<li>
<div># cd &lt;DRIVER_ROOT&gt;/os/linux and open config.mk file.</div>
<div>Make these changes:</div>
<div># Support ATE function</div>
<div>HAS_ATE=y</div>
<div># Support Wpa_Supplicant</div>
<div>HAS_WPA_SUPPLICANT=y</div>
<div># Support Native WpaSupplicant for Network Maganger</div>
<div>HAS_NATIVE_WPA_SUPPLICANT_SUPPORT=y</div>
</li>
	<li>
<div>While in the same folder, open usb_main_dev.c file and add this code:</div>
<div>MODULE_LICENSE("GPL”).<br>
It should now look like this:</div>
	MODULE_AUTHOR("Paul Lin &lt;paul_lin@ralinktech.com&gt;");<br>
	MODULE_DESCRIPTION("RT2870 Wireless Lan Linux Driver");<br>
	MODULE_LICENSE("GPL");<br>
	#ifdef CONFIG_STA_SUPPORT<br>
	#ifdef MODULE_VERSION<br>
	MODULE_VERSION(STA_DRIVER_VERSION);<br>
	#endif<br>
	#endif // CONFIG_STA_SUPPORT //
</li>
</ol>
</li>
	<li>
<div>Now we are ready to compile the driver code. You need the relevant compiler and helper tools and libraries for doing so. On the command terminal, issue these commands:</div>
<ul>
	<li># sudo apt-get update</li>
	<li># sudo apt-get upgrade</li>
	<li># sudo apt-get install build-essential</li>
	<li># sudo apt-get install linux-headers-$(uname -r)</li>
</ul>
</li>
	<li>
<div>While in DRIVER_ROOT, issue the following commands:</div>
<ul>
	<li># sudo make</li>
	<li># sudo make install</li>
	<li># sudo rmmod rt2870sta</li>
	<li># sudo rmmod rt2800usb</li>
	<li># sudo rmmod rt2x00usb</li>
	<li># sudo rmmod rt2800lib</li>
	<li>It may happen that the last 4 commands don’t do anything, or print a warning like “driver not found”. I don’t remember the exact warning message, but this means that we are trying to remove a module (rmmod) that doesn’t exist.  Double check that no ralink specific module is now in the memory:</li>
	<li># lsmod | grep rt</li>
	<li>You shouldn’t see any of the modules mentioned in the last 4 commands above.</li>
</ul>
</li>
	<li>
<div>Now, load your custom driver module in the kernel:</div>
<ul>
	<li># sudo su</li>
	<li># insmod &lt;DRIVER_ROOT&gt;/os/linux/rt3070sta.ko</li>
	<li>At this stage, if you insert your USB adapter and watch, the e2p specific ioctl will be listed.</li>
</ul>
</li>
	<li>
<div>Now, plugin your USB adapter (Edimax EW-7718Un, for example) and issue the following commands from the command terminal:</div>
<ul>
	<li># sudo su</li>
	<li># iwpriv ra0 e2p 208=04E8</li>
	<li># iwpriv ra0 e2p 20A=2018</li>
	<li>You may need to plug out and plug back in your adapter for the above commands to be successful.</li>
</ul>
</li>
	<li>We are now done. You can verify the modified values by using the lsusb command. Plugin your Wi-Fi adapter into your Samsung Smart TV and it will fool the  TV to think that a Samsung specific stick has been plugged in. Enjoy!</li>
</ol>
<p>Please note that the <strong>driver code doesn’t compile on version of ubuntu later than 10.04</strong>. If you have a reason to use a later version of ubuntu, you will need to make changes to some more .c files of the driver code because some of the libraries used have been renamed in the newer versions of ubuntu.</p>
