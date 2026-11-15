---
title: "Make Your MacBook Hibernate Instead of Sleep [Lion/Snow Leopard]"
date: 2011-12-31T20:48:06
url: /mac/make-your-macbook-hibernate-instead-of-sleep-lionsnow-leopard/
categories: ["Mac"]
tags: ["Snow Leopard Hibernate mode", "Lion Hibernate mode", "Mac OS X hibernate mode", "Macbook Pro Hibernate"]
author: "Chirag"
authors: ["chirag"]
---
<a href="/wp/wp-content/uploads/2011/12/macbook_pro_sleep_light.jpg"><img title="macbook_pro_sleep_light" src="/wp/wp-content/uploads/2011/12/macbook_pro_sleep_light-300x200.jpg" alt="" width="300" height="200" /></a>
<p>By default, MacBooks are configured to sleep when you close the lids. This means it shuts down everything but provides little bit of power to the RAM so that the state is maintained as is. Once you open the lid, everything is restored as is. In case you leave your laptop for long and the battery runs out fully, the Macbook automagically stores all the state to the hard disk so that nothing gets lost. Even if you connect it to power after a week everything just works, including open windows, typed text and running processes.</p>
<p>While this works very well if you use your MacBook all the time and charge it regularly, it makes things difficult if you take it out only once in a while. The reason is that this eats battery . So imagine you use your laptop for 15 minutes and close the lid. But the next time you open it battery would have almost run down and you need to charge it again. If it instead had a Windows like hibernate mode, the battery life would be maintained despite the amount of gap between usages.</p>
<p>Thankfully, there is an easy solution that allows you to change the default lid closing behavior to Hibernate. I'll make it really simple. If you need more advanced options you can check the man page for "pmset" and figure it out.</p>

<ul>
	<li>Open Terminal.app.</li>
	<li>Enter the following: "sudo pmset -a hibernatemode 25"</li>
	<li>Enter you password when asked for.</li>
</ul>
<p>And you're done!</p>
<p>Now when you put the lid of your Macbook down, it will store the current state to the hard disk. The sleep light will indicate this process. Once the light is off, your Macbook has hibernated. When you open the lid and press the Power button, the stored state will be restored as is.</p>
<p>The only problem is that restoring from Hibernate takes much longer than waking up from sleep.</p>
<p>If you ever want to switch back to the old mode, all you need to do is run "sudo pmset -a hibernatemode 3" and the old Sleep style will be restored.</p>
<p>[Image Courtesy <a href="http://www.sampletheweb.com/2008/10/15/pictures-and-first-impressions-of-my-new-macbook/" target="_blank">SampleTheWeb</a>]</p>
