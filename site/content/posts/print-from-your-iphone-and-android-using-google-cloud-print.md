---
title: "Print From Your iPhone And Android Using Google Cloud Print"
date: 2011-01-26T16:50:14
url: /android/print-from-your-iphone-and-android-using-google-cloud-print/
categories: ["Android", "Google", "iPhone"]
tags: ["apple airprint", "apple printing", "iOS printing", "cloud printing", "airprint printers", "cloud enabled printing", "google cloud print", "printing iPhone", "printing images from iPhone", "printing documents from iPhone", "print from iPad", "CloudPrint API", "Integrate Cloud Print API", "CloudPrint"]
---
Apple’s <a href="http://www.apple.com/ipad/features/airprint.html" target="_blank">AirPrint</a> solved printing problems for Apple iOS (iOS4.2+) devices only like the iPhone, iPad and iPod Touch. It took a lot of criticism as it requires <a href="http://www.macworld.com/reviews/collection/5806/airprint.html" target="_blank">AirPrint enabled printers</a> (a <a href="http://jaxov.com/2010/11/how-to-enable-airprint-service-on-windows/" target="_blank">hack</a> for Non-AirPrint Printers) and wouldn’t work with older iPhone/iPod touch (stuck with older iOS firmware).

<a href="/wp/wp-content/uploads/2011/01/CloudPrint.jpg"><img title="CloudPrint" src="/wp/wp-content/uploads/2011/01/CloudPrint_thumb.jpg" alt="CloudPrint" width="305" height="194" /></a>

Google’s new solution (again cloud based) by the name of <a href="http://www.google.com/chrome/intl/en/p/cloudprint.html" target="_blank">Google Cloud Print</a> supports printing to 'Cloud-aware printers' and also to your personal/office's legacy printers from almost any mobile device (which has internet connectivity) – say your iPhone/iPad or Android mobile or even a blackberry phone (still obsolete the mobile phone?).



The support for legacy printers is done through a Google Chrome (experimental build) which acts as a proxy to receive the 'Print requests' spooled on the cloud. And yes, as expected if your proxy system or the printer is offline, the requests are queued online till the print requests are served. You can print anything off your phone now to your office printer which is buried deep in the office firewall too. (It's a backdoor here, yes if some one steals your password – they can issue huge number of print outs to a printer pre-configured). The proxy legacy printer support is only available for Windows PC's at the moment with Linux and Mac support coming out soon.

Google says that it’s currently supporting some of it’s products like GMail and Docs and has already integrated the 'Cloud Printing' support to the <a href="/google/what-is-google-chrome-os" target="_blank">Chrome OS</a> too.

<a href="/wp/wp-content/uploads/2011/01/GoogleCloudPrintingOverview.gif"><img title="Google-Cloud-Printing-Overview" src="/wp/wp-content/uploads/2011/01/GoogleCloudPrintingOverview_thumb.gif" alt="Google-Cloud-Printing-Overview" width="482" height="182" /></a>

Google also released a <a href="http://code.google.com/apis/cloudprint/docs/devguide.html" target="_blank">Cloud Print API</a> to enable 3rd party software developers to integrate this into their applications (Web and native). I foresee many Android applications having this integrated soon, although I don’t see iPhone native applications using this anytime soon (what with Apple being a P.I.A in approving competing technologies in AppStore).

<strong>Cons</strong> - The primary reason that many renowned people like Richard Stallman <a href="http://news.cnet.com/8301-1001_3-10054253-92.html" target="_blank">hate cloud computing</a> is that your private data can be read and modified by any one (say with evil intentions) and no one requires a key to your door to steal/go through your personal data.

Well, he's not completely wrong, but there's a level of trust that every one bestow upon Google (or Twitter or Facebook – I could go on) when using their services to manage email, likes, search &amp; shopping when you store your data with them. But deeply hidden in the "Privacy statement" are those regular statements that the company may access the data to improve the user (ex:- printing here) experience. This is the same as how Google’s automated programs figure out the best ads to show in GMail by studying the private email content.

One day far in the future, when <a href="http://www.wolframalpha.com/input/?i=are+you+skynet" target="_blank">Skynet</a> will be created it already knows a ton about us through your email, location, family and finances - We're doomed anyway.

Let it be a science fiction till then will you?
