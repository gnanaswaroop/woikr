---
title: "Fix VLC skipping problem on your Mac"
date: 2009-10-02T05:37:46
url: /mac/fix-vlc-skipping-problem-on-your-mac/
categories: ["Mac"]
tags: ["switch to a mac", "window to mac", "VideoLan Client on Mac", "VLC on Mac", "VLC skipping problem"]
author: "Chirag"
authors: ["chirag"]
---
<p>I love VLC. The simple reason: it comes in a package. No clumsy codec downloads or crappy, hard to update codec packs. So when I thought of switching to Mac (will talk about that during the coming weeks), I was happy to see that VLC was there.</p>
<p>But VLC on Mac comes packed with a huge problem. All your movies, TV Shows skip randomly and the whole  experience is not perfect at all. It feels like playing from a badly scratched DVD. The surprising thing is that the same videos work flawlessly in QuickTime + Perian, which by the way is way better than any windows-based codec pack.</p>

<p>The good news is that after Googling and fiddling around with VLC Preferences, I've finally found a simple solution. Turns out, the problem is not with VLC but with the default settings that it comes with. Here is what you need to do to fix it.<br>

<ul>
	<li>Open VLC and goto VLC-&gt;Preferences from the Menu Bar on the top.<br>
<a href="/wp/wp-content/uploads/2009/10/vlc_mac_1.png"><img src="/wp/wp-content/uploads/2009/10/vlc_mac_1.png" alt="" width="400" /></a></li>
	<li>Select <span>All</span> instead of <span>Basic</span> to open the Advanced Preferences interface.</li>
	<li>Expand <span>Access Modules</span> and select <span>File</span>.<br>
<a href="/wp/wp-content/uploads/2009/10/vlc_mac_2.png"><img src="/wp/wp-content/uploads/2009/10/vlc_mac_2.png" alt="" width="400" /></a></li>
	<li>Change the <span>Caching Value</span> from default 300 to 1000 (Or higher if the problem persists).</li>
</ul>
So that's it. VLC on Mac plays videos perfectly as it should.
