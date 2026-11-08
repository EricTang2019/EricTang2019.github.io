/* Count the canonical article URL, independently of browser referrer policies. */
(async function () {
  const counter = document.querySelector("[data-page-views]");
  const value = document.querySelector("[data-page-views-value]");
  const canonical = document.querySelector('link[rel="canonical"]');
  if (!counter || !value || !canonical) return;

  const pageUrl = new URL(canonical.href);
  pageUrl.search = "";
  pageUrl.hash = "";
  if (window.location.origin !== pageUrl.origin) return;

  const controller = new AbortController();
  const timeout = window.setTimeout(() => controller.abort(), 8000);
  try {
    const response = await fetch("https://events.vercount.one/api/v2/log", {
      method: "POST",
      credentials: "omit",
      referrerPolicy: "no-referrer",
      headers: { "Content-Type": "application/json" },
      // Only page views are used; no browser identity or visitor cookie is stored.
      body: JSON.stringify({ url: pageUrl.href, isNewUv: false }),
      signal: controller.signal,
    });
    if (!response.ok) return;

    const result = await response.json();
    const count = result.data?.page_pv;
    if (result.status !== "success" || !Number.isSafeInteger(count) || count < 0) return;

    value.textContent = count.toLocaleString(document.documentElement.lang || "en");
    counter.hidden = false;
  } catch {
    // Keep the counter hidden rather than showing an old, browser-local value.
  } finally {
    window.clearTimeout(timeout);
  }
})();
