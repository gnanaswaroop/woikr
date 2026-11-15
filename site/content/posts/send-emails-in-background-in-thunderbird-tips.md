---
title: "Send emails in background in Thunderbird [Tips]"
date: 2009-10-05T00:17:49
url: /howto/send-emails-in-background-in-thunderbird-tips/
categories: ["How Tos"]
tags: ["thunderbird", "outbox", "background sending", "send in background", "outbox for thunderbird", "blunderdelay", "mozilla"]
---
<p><img title="image" src="/wp/wp-content/uploads/2009/10/image_thumb7.png" alt="image" width="320" height="91" /></p>
<p><a href="http://en.wikipedia.org/wiki/Mozilla_Thunderbird" target="_blank">Thunderbird</a> is an awesome open source email client. People switching from Outlook to Thunderbird find it annoying that it <span>does not have an Outbox folder and</span> opens a new dialog box (for a few seconds) while it sends emails.</p>
<p>Fortunately, there is a workaround for this problem. You will have to use a beta version though. Although this feature is not well publicized and buggy right now. If you're looking for an <a href="#novice-users">easier way</a>, look below.</p>
<p><span>For Advanced Users </span></p>

<ol>
	<li>
<div>Download Thunderbird 3.0 beta 4 preview from <a href="http://www.mozillamessaging.com/en-US/thunderbird/early_releases/downloads/" target="_blank">here</a>.</div></li>
	<li>
<div>Install Thunderbird and configure your mail account.</div></li>
	<li>
<div>Go to Tools –&gt; Options.</div></li>
	<li>
<div>Click on Config editor under Advanced –&gt; General
<a href="/wp/wp-content/uploads/2009/10/image8.png"><img title="image" src="/wp/wp-content/uploads/2009/10/image_thumb8.png" alt="image" width="504" height="431" />
</a></div></li>
	<li>
<div>Click on “I’ll be careful, I promise” to bypass the warning.</div></li>
	<li>
<div>In the config editor, type “background” to get a filtered list of config properties.</div></li>
	<li>
<div>Double click on “mailnews.sendInBackground” to set it to true. Close the config editor.
<a href="/wp/wp-content/uploads/2009/10/image9.png"><img class="alignnone" title="image" src="/wp/wp-content/uploads/2009/10/image_thumb9.png" alt="image" width="504" height="333" /></a></div></li>
	<li>That's it, whenever you click on 'Send' in your email client, it automatically tries to send the email in the background.</li>
</ol>
<p><a name="novice-users"></a><span>
Novice Users</span>
<ol>
	<li>
<div>You need to install the BlunderDelay add-on to send emails in background. If you are using a beta preview version of Thunderbird, the add-on won’t install unless you mod it. You can download a modded file from <a href="/downloads/blunderdelay-0.5.2-tb.xpi" target="_blank">here</a> (right click and Save as), or you can mod it yourself by following these steps:
<ul>
	<li> Download the plugin from <a href="https://addons.mozilla.org/en-US/thunderbird/addon/1814" target="_blank">here</a>.</li>
	<li>
<div>Change the file’s extension to .zip and open it using winrar or winzip.</div></li>
	<li>
<div>Open install.rdf in a text editor and change the “em:maxVersion” property to “4.0.0”.</div></li>
	<li>Save the zip and revert the .xpi extension of the file.</li>
</ul>
</div></li>
	<li>
<div>Click on Tools –&gt; Add-ons and click on the install button.
<a href="/wp/wp-content/uploads/2009/10/image10.png"><img title="image" src="/wp/wp-content/uploads/2009/10/image_thumb10.png" alt="image" width="504" height="369" /></a></div></li>
	<li>
<div>Browse and select the modded BlunderDelay xpi file and install the add on. Restart Thunderbird.</div></li>
	<li>
<div>Go to Tools –&gt; Add-ons –&gt; Extensions and click on the Options button under BlunderDelay.</div></li>
	<li>
<div>Set the frequency at which you want the add-on to check your outbox. The add-on will keep monitoring your Outbox folder at this frequency and will send any pending messages in it.
<a href="/wp/wp-content/uploads/2009/10/image11.png"><img title="image" src="/wp/wp-content/uploads/2009/10/image_thumb11.png" alt="image" width="504" height="369" /></a></div></li>
	<li>To send emails in the background use the Thunderbird's Save Later Shortcut key combination - Ctrl + Shift + Enter. This would send the email to the 'Outbox'/'Send Later' folder.</li>
	<li>
<div>Enjoy!</div></li>
</ol>
<p>Now when you send any message, it will not show the annoying dialog box. Instead, the message will go and sit in your Outbox quietly from where BlunderDelay will pick it up and send it across. This will also give you a buffer time to undo send in case you realize a mistake in your message after sending it.</p>
<p>This approach for  Novice users will work in the previous versions of Thunderbird too which has the Outbox/Send Later support.</p>
<p>Thanks to <a href="http://www.swaroop.in" target="_blank">Swaroop</a> for finding this process.</p>
