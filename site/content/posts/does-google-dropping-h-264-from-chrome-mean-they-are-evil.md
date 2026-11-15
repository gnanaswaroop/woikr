---
title: "Does Google Dropping H.264 From Chrome Mean They Are Evil?"
date: 2011-01-12T22:56:09
url: /google/does-google-dropping-h-264-from-chrome-mean-they-are-evil/
categories: ["Google"]
tags: ["Google Drops H.264", "Google WebM", "adobe flash", "Video compression standard on the web"]
---
<p>By now everyone has arguably read that Google is dropping support for H.264 from the Chromium project. Since Chrome is based on the Chromium project, this change will come to Chrome in the next few months as per Google. While I don't claim any authority on this matter, I  want to simplify and explain what this actually means to you, the most important person on the Internet.</p>
<p><strong>What is H.264?</strong></p>
<p>H.264 is a standard for video compression that is widely accepted and free for consumers, but the broadcasters like YouTube who actually use the compression standard and display the videos have to pay a licensing fee to MPEG Licensing Association. At present pretty all the major websites like Netflix, Hulu, Vimeo and Google's own YouTube use H.264 to compress videos. Also, most of the consumer hardware devices including Computers, Mobile Phones and MP3 Players include support for optimal H.264 playback.</p>
<p><strong>Holy Smokes it looks important, why does Google want to drop support for it then?</strong></p>
<p>Google says that the web should be open and community driven. The H.264 codec is not. Moving to an open standard will offer the following benefits:</p>

<ul>
	<li>Rapid performance improvements in the video encoder and decoder thanks to contributions from dozens of developers across the community</li>
	<li>Broad adoption by browser, tools, and hardware vendors</li>
	<li>Independent (yet compatible) implementations that not only bring additional choice for users, publishers, and developers but also foster healthy competition and innovation</li>
</ul>
<p><strong>So what do they think should be used?</strong></p>
<p>Google has something of their own called <a href="http://www.webmproject.org/" target="_blank">WebM</a> which is an open, royalty-free, compression standard designed for the web. It is also supported by Mozilla, Opera and Adobe among others. Google will also support another open video compression standard called <a href="http://www.theora.org/" target="_blank">Theora</a>.</p>
<p><strong>What about the other browsers?</strong></p>
<p>Here is the list of the popular browsers and the codecs they support. (Thanks <a href="http://www.ghacks.net/2011/01/12/google-ditches-h-264-support-in-google-chrome/" target="_blank">GHacks</a>!)</p>

<ul>
	<li>Firefox: WebM and Theora</li>
	<li>Opera: WebM and Theora</li>
	<li>Internet Explorer 9: H.264</li>
	<li>Safari: H.264</li>
</ul>
<p><strong>Wait this is confusing; How do YouTube, Hulu etc work on Firefox now?</strong></p>
<p>Note that this support is only specific to native video playback in HTML5. Most of the video on the web now is displayed using Adobe Flash which supports H.264 playback. Since all the browsers support Flash, <em>you will actually be able to watch H.264 videos</em> like now.</p>
<p><strong>It all looks good, what is the problem here?</strong></p>
<p>There are multiple problems actually.</p>

<ul>
	<li>While the publishers will save on the licensing fees in the long-term, they'll have to re-encode their entire library into a new compression format to keep supporting Google Chrome. This will definitely be a major issues. Google themselves will have to face it but they probably already started working on it.</li>
	<li>What about all the hardware devices that support H.264? Not many devices in the market are optimized for WebM or Theora playback. It will easily take an year or more to include this support and many manufacturers may not even do it then. Does Google plan to keep multiple copies of videos on YouTube for specific devices?</li>
	<li>The above also includes Google's own Android devices. Will they drop support for H.264 too?</li>
	<li>It's a major kickback to HTML5 which is being called by many as the future of the web. This needs some explanation.
Since it's pretty much impossible to move everything to a new codec standard, the web will have multiple popular video compression standards supported by various groups. Apple and Microsoft support H.264 and Google supports WebM and Theora. Since most websites want to run on most web browsers, the only solution is Adobe Flash. And if Flash stays on, it means HTML 5's development will be slower. The publishers will have to choose between building in HTML and keeping multiple copies of video or building in Flash which will natively support playback of all video codecs.
The strange thing here is that Google itself is a major proponent of HTML5.</li>
	<li>As John Gruber <a href=" http://daringfireball.net/2011/01/simple_questions" target="_blank">pointed out</a>, if this is to support open innovation and leave behind proprietary, closed standards, why is Google Chrome supporting Adobe Flash? In fact they bundle Adobe Flash along with Chrome.</li>
	<li>The biggest problem is that does Google think they are allowed to take a decision on behalf on everyone on the Internet? As <a href="http://tech.slashdot.org/comments.pl?sid=1946532&amp;cid=34842344" target="_blank">znu points out on Slashdot</a>, WebM itself infringes many H.264 patents. How is that ok? This is Google manipulating the market entirely for their selfish advantage here, and it's all the worse because they're pretending otherwise. And it's going to be really frustrating watching people fall for it.</li>
</ul>
<p>It just doesn't feel like the good old times when Google was simpler. They are getting bigger. They have motives and long-term plans now. Maybe they finally figured out <a href="http://xkcd.com/792/" target="_blank">how to be evil</a>.</p>
<p>On a lighter note, you must <a href="http://blogs.msdn.com/b/tims/archive/2011/01/11/an-open-letter-from-the-president-of-the-united-states-of-google.aspx" target="_blank">read this funny take</a> on the Google announcement done by Time Sneath from Microsoft.</p>
<strong> </strong>
