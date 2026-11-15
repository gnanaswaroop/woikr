---
title: "Apparently, there are some things you can't Google"
date: 2011-09-01T18:19:39
url: /google/apparently-there-are-some-things-you-cant-google/
categories: ["Google"]
tags: ["google banned queries", "google denial of service", "google range search", "weird google results"]
image: "/wp/wp-content/uploads/2011/09/google_error.png"
author: "Chirag"
authors: ["chirag"]
---
<p>Here something weird. Try <a href="http://www.google.com/search?q=9999999..99999999999999999999999" target="_blank">Googling</a> "9999999..99999999999999999999999". It tries to load for sometime and then redirects to this strange error page.</p>
<p><img title="google_error" src="/wp/wp-content/uploads/2011/09/google_error.png" alt="" width="439" height="207" /></p>
<p>From what I figured out from a discussion on <a href="http://news.ycombinator.com/item?id=2948873" target="_blank">Hacker News</a>, ".." is an operator that is used to denote a range. So if you Google "1..10", it searches for all the numbers from 1 to 10. As you keep increasing this range the query takes more time as the result set grows. After a certain range, it's so big that Google refuses to accept it, thinking you are trying to start a <a href="http://en.wikipedia.org/wiki/Denial-of-service_attack" target="_blank"><em>Denial of Service</em> attack</a>.</p>
<p>There also are certain range searches for e.g. credit card number range that are also not allowed.</p>
<p>If you find a different/better explanation, do leave a comment.</p>
