---
title: "Fix Boot Logo Loop Issue When Updating Firmware on a Samsung Smart TV"
date: 2012-03-14T10:00:43
url: /howto/fix-boot-logo-loop-issue-when-updating-firmware-on-a-samsung-smart-tv/
categories: ["How Tos", "Home Entertainment"]
tags: ["samsung smart TV", "samsung TV", "samsung boot logo repeat issue"]
aliases: ["/home-entertainment/fix-boot-logo-loop-issue-when-updating-firmware-on-a-samsung-smart-tv/"]
---
<p><img title="samsung smart tv logo.png" src="/wp/wp-content/uploads/2012/03/samsung-smart-tv-logo.png" alt="samsung smart tv logo" width="499" height="92" /></p>

<div>
<blockquote><em>This is a guest post by <a href="http://www.linkedin.com/profile/view?id=15139659">Rajnish Jain</a>. Rajnish is a product development enthusiast having around 12.5 years of experience. He enjoys solving complex technical problems and has worked on wide range of technologies including Open Source frameworks, Unix (shell scripting) &amp; embedded device programming.</em></blockquote>
</div>
<div>Recently I purchased Samsung UA40D5500RR. Using a USB Wi-Fi adapter (not the Samsung one which is very costly. See <a href="/?p=9009">this guide</a>), I got it to connect to the Internet and was prompted to update its software online. By pressing “MENU” -&gt; “System” -&gt; “Software Update” on the remote control, I could start the firmware upgrade. It started downloading the required software from the Internet and then started the upgrade process. At the end of it, the TV turned off automatically and came up by itself.</div>
<br />
<div>This is where the nightmare started. There was no LED indicator on the control panel of the TV. The “Samsung SMART TV” boot logo appeared which gave me a feel that the TV is about to start normally. But to my surprise, the screen went off for a while and then again the boot logo appeared. This process continued for a long time. The only way I could completely turn off the TV was cutting off the electricity supply since it wasn’t accepting the instructions from the remote control as well.</div>
On investigating a bit on the Internet, I could find some info which brought my TV back to normal. In fact, the software update wasn’t complete and the TV was waiting for user input to continue. This seemed a total non-sense as this process is nowhere documented by Samsung. This is what I did:
<blockquote><em><strong>DISCLAIMER</strong>: The author of this article &amp; woikr are not responsible for any damage/malfunction caused to the TV by following the instructions written below. Please continue at your own risk.</em></blockquote>
<ol>
	<li>Switched on the power supply to the TV.</li>
	<li>When the boot logo appeared and disappeared, I pressed <strong>“MUTE” “2” “5” “8” “EXIT”</strong> buttons (in sequence) on the remote.</li>
	<li>Finally, a screen appeared which said “Upgrading software”. Once this was complete, the TV automatically came into normal state.</li>
</ol>
