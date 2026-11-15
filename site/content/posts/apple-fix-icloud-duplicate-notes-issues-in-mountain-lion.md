---
title: "Fix iCloud Duplicate Notes Issues in Mountain Lion"
date: 2012-10-27
url: /apple/fix-icloud-duplicate-notes-issues-in-mountain-lion/
author: ""
categories: ["Apple"]
tags: []
comments_count: 0
---
<p><strong>UPDATE:&nbsp;Please be very sure to backup the&nbsp;notes file before you do this and be sure this is only used on Mountain Lion.</strong></p>
<p>Ever since I upgraded to Mountain Lion, I’ve been facing an issue where in I see multiple copies of every single Note in Notes.app. Initially I thought it might be due to multiple Notes accounts being synced but turned out it was some bug in iCloud that creates multiple duplicate copies of the synced account.</p>
<p>Thankfully, this has a rather straightforward fix (Courtesy: <a href="http://nslog.com/2012/07/07/fixing_duplicate_icloud_accounts_in_notes">NSLog</a>).</p>
<ul>
<li>Open your favorite Terminal. (If that sounded weird, just open <code>/Applications/Utilities/Terminal.app</code>)</li>
<li>Quit Notes.app.</li>
<li>Enter ‘<code>rm -rf&nbsp;~/Library/Containers/com.apple.Notes</code>.’ without the quotes.</li>
<li>Done.</li>
</ul>
<p>This clears up the Notes synced to your Mac and on the next start Notes.app will download new copies with no duplicates!</p>
