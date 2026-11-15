// Infinite scroll for the home card list. The page links stay in the HTML
// (for crawlers and no-JS visitors); this only appends the next page's cards.
(function () {
  var list = document.getElementById("cards");
  var pager = document.getElementById("pager");
  if (!list || !pager || !("IntersectionObserver" in window)) return;

  var status = document.getElementById("cards-status");
  var loading = false;

  function nextHref() {
    var a = pager.querySelector('a[aria-label="Next"][href]');
    return a ? a.getAttribute("href") : null;
  }

  function setStatus(msg) { if (status) status.textContent = msg || ""; }

  function loadMore() {
    var href = nextHref();
    if (loading || !href) return;
    loading = true;
    setStatus("Loading more…");
    fetch(href, { credentials: "same-origin" })
      .then(function (r) { if (!r.ok) throw new Error(r.status); return r.text(); })
      .then(function (html) {
        var doc = new DOMParser().parseFromString(html, "text/html");
        var cards = doc.querySelectorAll("#cards > article");
        cards.forEach(function (c) { list.appendChild(document.importNode(c, true)); });
        // Move the "next" pointer to the page we just loaded.
        var nextDoc = doc.querySelector('#pager a[aria-label="Next"][href]');
        var cur = pager.querySelector('a[aria-label="Next"]');
        if (nextDoc) {
          var newHref = new URL(nextDoc.getAttribute("href"), location.href).pathname;
          if (cur && cur.hasAttribute("href")) cur.setAttribute("href", newHref);
        } else if (cur) {
          cur.removeAttribute("href");
        }
        setStatus(nextHref() ? "" : "You have reached the end.");
        loading = false;
        if (!nextHref()) observer.disconnect();
      })
      .catch(function () {
        loading = false;
        setStatus("Could not load more posts. Scroll again to retry.");
      });
  }

  var observer = new IntersectionObserver(function (entries) {
    if (entries.some(function (e) { return e.isIntersecting; })) loadMore();
  }, { rootMargin: "600px 0px" });

  var sentinel = document.getElementById("cards-sentinel");
  if (nextHref()) {
    pager.classList.add("is-hidden-visually");
    observer.observe(sentinel);
  } else {
    setStatus("");
  }
})();
