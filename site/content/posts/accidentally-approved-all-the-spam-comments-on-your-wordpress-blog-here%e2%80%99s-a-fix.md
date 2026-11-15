---
title: "Accidentally Approved All The Spam Comments On Your Wordpress Blog? Here’s A Fix"
date: 2011-02-08T00:11:35
url: /howto/accidentally-approved-all-the-spam-comments-on-your-wordpress-blog-here%e2%80%99s-a-fix/
categories: ["How Tos", "Blogging"]
tags: ["wordpress tricks", "wordpress akismet fix", "how to re-check spam comments", "wordpress akismet approved comments", "wordpress akismet tables"]
author: "Swaroop"
authors: ["swaroop"]
aliases: ["/howto/accidentally-approved-all-the-spam-comments-on-your-wordpress-blog-here%e2%80%99s-a-fix"]
---
We recently had a mishap while trying out <a href="http://intensedebate.com/">IntenseDebate</a> integration on woikr.com. While importing all our existing comments, it marked all spam comments as approved. It left us with over 6000 comments out of which over 50% were spam and we had no way to separate them from the legitimate ones. It was a disaster.

We finally fixed the issue by using Akismet and some simple SQL scripts. If you have a similar issue, this is something that may help you.

<img title="image1" src="/wp/wp-content/uploads/2011/02/image1.png" alt="image1" width="240" height="52" />

Akismet is a great tool for blocking spam on your Wordpress blog, but what if you’re realized and installed it too late and you’ve already got thousands of comments?

When you go to the "Comments" section of Wordpress dashboard and click on "Check for spam", Akismet only "tags" any previous entries as possible and doesn't "mark as spam".
<div></div>
As long as they’re not marked as spam, they will continue to show up on the word press posts which isn't something you'd want. Follow these steps to fix this issue.
<h3>Use Akismet to verify the approved comments and tag as spam</h3>
Visit the word press Dashboard’s comments section and click on "All" and then “Check for spam”. This will tag them as spam comments but wouldn’t mark them as spam.

<img title="image2" src="/wp/wp-content/uploads/2011/02/image2.png" alt="image2" width="555" height="108" />
<h3>Backup your word press database</h3>
There are excellent plug-in to backup your database, one of which is "<a href="http://wordpress.org/extend/plugins/wp-db-backup/">WP Database Backup</a>". This is so that if you screwed up your database tables – you not loose all the "genuine" comments too.
<h3>Accessing phpMyAdmin/Wordpress database tables (Advanced)</h3>
Simpler approach - If you’ve got less comments that got approved "Spam", then you can manually visit each of the comment from the word press dashboard and mark them as "spam".

In case you’ve already got thousands of spam comments, then proceed further.<br>
Open phpMyAdmin or any other way to access the database tables/data for your word press Blog. If you’re on Dreamhost, it’s at <a href="https://panel.dreamhost.com">https://panel.dreamhost.com</a> -&gt; MySQL Databases (Tool Box section) -&gt; Click on the phpMyAdmin link against your database hostname.

<img title="image0" src="/wp/wp-content/uploads/2011/02/image0.png" alt="image0" width="513" height="323" />

Query to fetch all the "Approved but Tagged as spam" by Akismet
<blockquote><strong>SELECT</strong> *<br>
<strong>FROM</strong> wp_comments <strong>a</strong>, wp_commentmeta <strong>b</strong><br>
<strong>WHERE</strong><br>
<strong>a</strong>.comment_ID = <strong>b</strong>.comment_ID <strong>AND</strong><br>
<strong>a</strong>.comment_approved = '1' <strong>AND</strong><br>
<strong>b</strong>.meta_key = 'akismet_result' <strong>AND</strong><br>
<strong>b</strong>.meta_value = 'true';</blockquote>
Query to update all the Akismet tagged as “spam”.
<blockquote><strong>UPDATE</strong> wp_comments <strong>SET</strong> comment_approved = 'spam'<br>
<strong>WHERE</strong> comment_id in (<br>
<strong> SELECT</strong> distinct(<strong>b</strong>.comment_id)<br>
<strong>FROM</strong> wp_commentmeta <strong>b</strong><br>
<strong>WHERE</strong><br>
<strong>b</strong>.meta_key = 'akismet_result' <strong>AND</strong><br>
<strong>b</strong>.meta_value = 'true'<br>
);<br>
<strong>commit</strong>;</blockquote>
The update query should mark all the “Akismet tagged spam” to Wordpress Spam.
<h3>Verify your comments count</h3>
If your blog posts are still reflecting wrong comment count, then use the plug-in “<a href="http://wordpress.org/extend/plugins/web-ninja-comment-count-fixer/">Web Ninja Comment Count Fixer</a>“. It will recheck the comment count and update the database appropriately. It's pretty simple and straightforward.

Voila, you’re done marking all the spam comments in your approved queue. You can now verify that it’s been fixed and permanently out your “Spam Queue”.
