// Opt-in Google Analytics 4 loader.
// Nothing is sent to Google (and no GA cookies are set) until the visitor clicks "Accept".
// The choice is stored in localStorage; "No thanks" or the footer toggle turns tracking off again.
(function () {
  var KEY = 'woikr-analytics-consent';
  var script = document.currentScript;
  var gaId = script && script.getAttribute('data-ga-id');
  if (!gaId) return;

  var banner = document.getElementById('analytics-consent');

  function getChoice() {
    try { return localStorage.getItem(KEY); } catch (e) { return null; }
  }
  function setChoice(value) {
    try { localStorage.setItem(KEY, value); } catch (e) { /* storage unavailable: choice lasts this page only */ }
  }

  function loadGA() {
    if (window.__woikrGaLoaded) return;
    window.__woikrGaLoaded = true;
    window['ga-disable-' + gaId] = false;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', gaId, { anonymize_ip: true });
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(gaId);
    document.head.appendChild(s);
  }

  function disableGA() {
    // GA4 honours this flag: no hits are sent for the rest of this page view.
    window['ga-disable-' + gaId] = true;
  }

  function apply(choice) {
    if (choice === 'granted') {
      loadGA();
    } else {
      disableGA();
    }
  }

  function showBanner() { if (banner) banner.hidden = false; }
  function hideBanner() { if (banner) banner.hidden = true; }

  function choose(value) {
    setChoice(value);
    apply(value);
    hideBanner();
  }

  if (banner) {
    banner.addEventListener('click', function (e) {
      var btn = e.target.closest('button[data-consent]');
      if (btn) choose(btn.getAttribute('data-consent'));
    });
  }

  // Footer link: reopens the banner so the visitor can change their mind.
  var settings = document.getElementById('analytics-settings');
  if (settings) {
    settings.addEventListener('click', function (e) {
      e.preventDefault();
      showBanner();
    });
  }

  var saved = getChoice();
  if (saved === 'granted' || saved === 'denied') {
    apply(saved);
    hideBanner();
  } else {
    // No decision yet: tracking stays off and the banner asks.
    disableGA();
    showBanner();
  }
})();
