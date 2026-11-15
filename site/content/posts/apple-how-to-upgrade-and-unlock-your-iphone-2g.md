---
title: "How to: Upgrade and unlock your iPhone 2G to 2.0 in five steps"
date: 2008-08-20
url: /apple/how-to-upgrade-and-unlock-your-iphone-2g/
author: "Setu"
categories: ["Apple, iPhone"]
tags: []
comments_count: 117
---
<div></div>

        
            
            <div></div>

            <ul id="sharebar">
<li></li><li><a href="http://twitter.com/share" class="twitter-share-button" data-count="vertical" data-via="woikr">Tweet</a></li><li>

<g:plusone size="tall"></g:plusone></li><li></li></ul><ul id="sharebarx">
<li></li><li><a href="http://twitter.com/share" class="twitter-share-button" data-count="horizontal" data-via="woikr">Tweet</a></li><li>

<g:plusone size="medium"></g:plusone></li><li></li></ul><p><img loading="lazy" class="alignnone" src="/images/iphone-unlock_lead.JPG" alt="" width="593" height="225"></p>
<p><strong>DEPRECATED</strong>: This article is about an older version of the iPhone unlock software. Please use woikr’s <a href="/iphone/how-to-upgrade-and-unlock-your-iphone-2g-using-quickpwn" target="_self">new guide to upgrade your iPhone to 2.2 and unlock using QuickPwn</a>.</p>
<p><strong>Update Aug 30th 2008: <a href="http://www.winpwn.com/" target="_blank">WinPwn 2.5</a></strong> is released and can unlock and jailbreak firmware 2.0.2. <strong><a href="#2.0.2" target="_self">Click here</a></strong> for details</p>
<p>The iPhone 2.0 firmware was released in July. Since then, we have been hearing a lot of positive reviews about the <a href="http://www.apple.com/iphone/softwareupdate/" target="_blank">new features in 2.0</a> like <a href="http://www.apple.com/iphone/enterprise/" target="_blank">Push email</a>, <a href="http://www.apple.com/iphone/appstore/" target="_blank">App store</a> etc. If you have an iPhone 2G still running on firmware 1.1.4 or older, it is time to upgrade.</p>
<p>The following step by step guide will help you to upgrade your iPhone 2G running on previous firmwares to be upgraded to unlocked (read pwned) iPhone 2.0 firmware. This is achieved using pwnage tools created by the <a href="http://blog.iphone-dev.org/" target="_blank">iphone-dev team</a>. The whole process is broadly divided into the following 5 steps:</p>
<p>1. Download required software<br>
2. Sync your iPhone<br>
3. Create a custom pwned firmware using WinPwn<br>
4. Install the custom firmware created onto the iPhone<br>
5. Restore iPhone settings using the backup created in last sync</p>
<h4>DISCLAIMER:</h4>
<p>This guide is provided as is. The process worked well for all of us here at woikr and many of our friends. However, follow it at your own risk. Woikr will not be responsible in case anything goes wrong.</p>
<h3>System Requirements:</h3>
<p>– Minimum 512 MB RAM<br>
– Minimum 550 MB of free space on hard disk<br>
– Windows XP or Windows Vista<br>
– <a href="http://www.filehippo.com/download_itunes/" target="_blank">iTunes 7.6 or 7.7</a> (If you have a newer version, uninstall it completely and restart your system before installing the older one)<br>
– <a href="http://www.microsoft.com/downloads/en/details.aspx?familyid=0856eacb-4362-4b0d-8edd-aab15c5e04f5&amp;displaylang=en" target="_blank">.Net Framework 2.0</a></p>
<h3>1. Download required software</h3>
<p>For easy access, download the following in a single folder.</p>
<p>a. <a href="http://appldnld.apple.com.edgesuite.net/content.info.apple.com/iPhone/061-5135.20080729.Vfgtr/iPhone1,1_2.0.1_5B108_Restore.ipsw" target="_blank">iPhone firmware 2.0.1</a> – approx 242 MB<br>
b. <a href="http://rapidshare.com/files/136074645/winpwn_2.0.0.4_Setup.zip.html" target="_blank">WinPwn 2.0.0.4</a> (<a href="http://rapidshare.de/files/40196561/winpwn_2.0.0.4_Setup.zip.html" target="_blank">alternate link</a>) – approx 24 MB<br>
c. <a href="http://iphonefreakz.com/firmware/BL-39.bin" target="_blank">Bootloader version 3.9</a> – 128 KB<br>
d. <a href="http://iphonefreakz.com/firmware/BL-46.bin" target="_blank">Bootloader version 4.6</a> – 128 KB</p>
<h3>2. Sync your iPhone</h3>
<p>Sync your iPhone with iTunes. This step is needed so that a latest backup of your iPhone is created (automatically) in iTunes. We will use this backup to restore the settings (Contacts, SMS, Notes, Mail accounts etc.) after the upgrade is complete. Please note that the backup will NOT keep the media on your iPhone. You will have to add the media again after the upgrade.</p>
<h3>3. Create a custom pwned firmware using WinPwn 2.0.0.4</h3>
<p>a. Install WinPwn 2.0.0.4:</p>
<p>– Extract the file winpwn_2.0.0.4_Setup.zip downloaded in step 1b.<br>
– Run winpwn_2.0.0.4_Setup.exe from the extracted folder.<br>
– Follow the onscreen instructions. Do not alter any settings.</p>
<p>b. Double click on WinPwn icon on your desktop. This is the icon with a pineapple logo.</p>
<p>c. Click on “Browse .ipsw” button in the left pane.</p>
<p>d. Browse to the download location from step 1 and select the iPhone firmware 2.0 file downloaded in step 1a. WinPwn will be non responsive for a few seconds. Do not worry, it is just validating the firmware file. It will also display some text inside the text area.</p>
<p>e. Click on the “IPSW Builder” button in the left pane. This will launch the IPSW Builder window. Make sure to select exactly the following options in each of the tab:</p>
<p>– <strong>Applications Tab</strong>: Select Cydia, Installer 2.0 and Youtube activation fix.</p>
<p>– <strong>Custom Images Tab</strong>: Do nothing.</p>
<p>– <strong>Custom Payload Tab</strong>: Do nothing.</p>
<p>– <strong>Advanced Tab</strong>: Select Activate iPhone, Enable Baseband update, Neuter Bootloader 3.9/4.6, and Unlock Baseband. Click on “Bootloader 3.9 file …” button and select the “BL-39.bin” downloaded in step 1c. Click on “Bootloader 4.6 file …” button and select the “BL-46.bin” downloaded in step 1d.</p>
<p>– <strong>Partition Resizer Tab</strong>: Drag the slider to 512 MB. Please note that this is an <span>important step</span>.</p>
<p>f. Click on the “Build .ipsw” button located at the bottom left corner. It will ask you to specify a location to save the custom firmware file. Point it to the same folder where you downloaded the software&nbsp; in step 1and click “Save”.</p>
<p>g. The above process will take about 5 minutes to complete. During this time, you will see some text on the text area in the WinPwn window. Also, a progress bar at the bottom of the IPSW Builder window will show the progress of the process. Once the process is successfully completed, it will display a prompt. Click on the “OK” button.</p>
<p>h. Take a deep breath. And don’t get <a href="http://en.wikipedia.org/wiki/Goose_bumps" target="_blank">goose bumps</a> yet. There is still some work to do :).</p>
<h3>4. Install the custom firmware created onto the iPhone</h3>
<p>a. Click on the “iPwner”&nbsp; button in the WinPwn window. A Browse dialog box is displayed.</p>
<p>b. Browse to the location where you saved the custom firmware file in step 3f. Select the custom firmware file. It should have a name like “Custom-iPhone1,1_2.0.1_5B108_Restore.ipsw”.</p>
<p>c. Again, WinPwn will be non responsive for a few seconds. Also, iTunes will be automatically closed if it is open. Once the process is complete, you will be notified by a prompt. Click on the “OK” button.</p>
<p>d. Put the iPhone in DFU mode (Device Firmware Update) using the following steps:</p>
<p>– Connect the iPhone to your PC and start iTunes<br>
– Press and hold the sleep/wake button and home button simultaneously for 10 seconds<br>
– While keeping the home button pressed, release the sleep/wake button<br>
– Keep the home button pressed until you see an iPod cable icon pointing towards an iTunes icon on the iPhone screen<br>
– iTunes will prompt that it has detected an iPhone in recovery mode. Click on the “OK” button.</p>
<p>e. Hold the “Shift” key on the keyboard and click on the “Restore” button in iTunes. A Browse dialog is displayed.</p>
<p>f. Browse to the location where you saved the custom firmware file in step 3f. Select the custom firmware file. It should have a name like “Custom-iPhone1,1_2.0.1_5B108_Restore.ipsw”.</p>
<p>g. This process will take about 10 – 15 minutes to complete. Be patient. iTunes will display progress bars saying “Extracting iPhone software”, “Preparing iPhone for restore” etc</p>
<p>h. In case you get error 1604 in iTunes, restart your computer and start from step 4a. In case you still get the error, restart again and start from step 3b. <a href="#Error1604"><em>*UPDATE*</em></a></p>
<h3>5. Restore iPhone settings using the backup created in last sync</h3>
<p>Once the restore is complete, your iPhone will restart. Just after restarting, it will load BootNeuter and run some scripts. You will see a lot of stuff going on the iPhone screen. Do nothing. After all the scripts are executed, the iPhone will be restarted again and detected in iTunes.</p>
<p>Once the iPhone restarts, iTunes will detect it as a new phone and will ask you to restore from an old backup. This is the backup which we created in step 2. Select your iPhone’s name in the list and click on Continue. This process will take about 10 minutes to complete after which your iPhone will have the same settings it had before the upgrade.</p>
<p>Some users faced an issue with Mail app crashing after doing the settings restore. If you face the same issue take the following steps:</p>
<p>a. Click on Cydia icon on the home screen<br>
b. Install the essential software<br>
c. Click on “Search” and type “BossPrefs”<br>
d. Select BossPrefs from the search results and tap on Install<br>
e. Once the installation is complete, press the Home button to return to the home screen<br>
f. Tap on BossPrefs icon on the home screen<br>
g. Tap on “More” button on the top right<br>
h. Tap on “Fix User Fir Permissions”</p>
<p>This should fix your Mail app issue. Your iPhone is now upgraded and unlocked to 2.0 firmware. Congratulations !</p>
<p>If you do not already have an iTunes account, set it up by clicking on “iTunes Store” in the left panel in iTunes and clicking on the “Sign In” button on top right just below the search box. You can now use the App Store on the iPhone to install new apps on your iPhone.</p>
<p>Here are some free recommended apps for first time users:</p>
<p>– <strong>facebook</strong>: The social networking app<br>
– <strong>Remote</strong>: Remotely control your iTunes or Apple TV<br>
– <strong>Twitterriffic</strong>: Twitter client<br>
– <strong>AIM</strong>: The famous messenger</p>
<p>Enjoy !</p>
<p>[Thanks <a href="http://iclarified.com/entry/comments.php?enid=1572" target="_blank">iClarified</a> and <a href="/author/swaroop" target="_blank">Swaroop</a>]<a name="Error1604"><strong></strong></a></p>
<p><a name="Error1604"><strong>UPDATE:</strong></a></p>
<p>In case you continue to get Error 1601-1604 in Step 4h, try the following as well:</p>
<p>– Make sure you are in DFU mode. Your screen should show up as blank, as if the phone is switched off. The screen showing iTunes icon with cable is not DFU screen.<br>
– Change the USB port, make sure it’s not coming through an external hub.<br>
– Reinstall iTunes and all other related Apple software.<br>
<a name="2.0.2"></a></p>
<h3><strong>UPDATE: (For<strong> Updating 2G iPhone to unlocked </strong>2.0.2)</strong></h3>
<p>The new WinPwn 2.5 has much more cleaner interface. This time, we wouldn’t have to troubleshoot that much as we did for 2.0.1. Although WinPwn 2.5 is in beta this time, its still good to upgrade without any problems in the first time. For updating, you can refer to the pretty self explained article for experts at <a href="http://thebigboss.org/guides/winpwn-25-expert-guide/" target="_blank">BigBoss</a> and for beginners at <a href="http://www.iclarified.com/entry/index.php?enid=1755" target="_blank">iClarified</a>.</p>
<h3><strong>Note:</strong></h3>
<p>In case iTunes repeatedly asks to restore your iPhone from a backup even after you have restored it from a previous backup after the upgrade, do not panic. Just hit “Continue” again and immediately unplug your iPhone. iTunes will terminate the backup restore process. Now connected your iPhone again and iTunes will detect it as a restored phone and will not prompt you again to restore it.</p>

		
		<p>
		<em>Liked this article? Like us on Facebook!</em>
		<br>
				

		
		</p>

	    <hr id="before_comments_hr">

		

<a name="facebook-comments"></a>

<div id="fb-root"></div>

<div id="fbComments">
	<p>Comments</p>

	<fb:comments xid="D3r0bKBrWT986Sr_post338" url="/apple/how-to-upgrade-and-unlock-your-iphone-2g/" numposts="99" width="600" publish_feed="true" migrated="1"></fb:comments></div>

<div></div>
