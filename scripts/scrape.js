/*
 * Scraper for https://minecraftpocket-servers.com/ (full list of Bedrock servers).
 *
 * The site is protected by Cloudflare: curl/requests are blocked, so this must
 * run from a real browser:
 *   1. Open https://minecraftpocket-servers.com/ (pass the Cloudflare challenge)
 *   2. Open the developer tools console (F12) and paste this script
 *   3. Wait until the console prints "finished" (~10-15 min, requests are throttled)
 *   4. Export the result: copy(JSON.stringify(window.__job.data)) and paste it into raw.json
 *   5. python3 scripts/import_raw.py raw.json && python3 scripts/build.py
 *
 * Requests are deliberately slow (3 in parallel, with a pause between each).
 */
window.__job = { state: 'lists', done: 0, total: 0, errors: [], data: {} };
(async () => {
  const J = window.__job, sleep = ms => new Promise(r => setTimeout(r, ms)), P = new DOMParser();
  const get = async (u) => {
    for (let i = 0; i < 4; i++) {
      try {
        const r = await fetch(u, { credentials: 'include' });
        if (r.ok) return await r.text();
        if (r.status == 429 || r.status == 403 || r.status >= 500) await sleep(3000 * (i + 1)); else return null;
      } catch (e) { await sleep(2000); }
    }
    return null;
  };
  const ids = new Map();
  for (let p = 1; p <= 44; p++) {
    const h = await get(p == 1 ? '/' : '/servers/list/' + p + '/');
    if (!h) { J.errors.push('list ' + p); continue; }
    const d = P.parseFromString(h, 'text/html');
    d.querySelectorAll('table tbody tr').forEach(tr => {
      const a = tr.querySelector('a[href^="/server/"]'); if (!a) return;
      const m = a.getAttribute('href').match(/\/server\/(\d+)/); if (m) ids.set(m[1], 1);
    });
    await sleep(200);
  }
  const list = [...ids.keys()]; J.total = list.length; J.state = 'details';
  let idx = 0;
  const worker = async () => {
    while (idx < list.length) {
      const id = list[idx++];
      const h = await get('/server/' + id + '/'); if (!h) { J.errors.push('srv ' + id); J.done++; continue; }
      const d = P.parseFromString(h, 'text/html'); const info = {};
      d.querySelectorAll('table tr').forEach(tr => {
        const c = tr.children; if (c.length == 2) info[c[0].textContent.trim()] = c[1].textContent.trim().replace(/\s+/g, ' ');
      });
      const dc = d.querySelector('.card-text'); let desc = '';
      if (dc) {
        const c = dc.cloneNode(true);
        c.querySelectorAll('br').forEach(b => b.replaceWith('\n'));
        c.querySelectorAll('p,div,li').forEach(e => e.append('\n'));
        desc = c.textContent.replace(/[ \t]+/g, ' ').replace(/\n\s*\n\s*\n+/g, '\n\n').trim().slice(0, 2000);
      }
      const ban = [...d.querySelectorAll('img')].map(i => i.getAttribute('src') || '').find(s => s.includes('/server/' + id + '/'));
      const dis = [...d.querySelectorAll('a')].map(a => a.getAttribute('href') || '').find(s => /discord\.(gg|com)|discordapp\.com/.test(s));
      const tags = [...d.querySelectorAll('a[href^="/tag/"]')].map(a => a.textContent.trim()).filter((v, i, a) => v && a.indexOf(v) == i);
      J.data[id] = {
        id, address: info['Address'] || '', name: info['Hostname'] || '', country: info['Location'] || '',
        version: info['Version'] || '', website: info['Website'] || '', discord: dis || '', tags, description: desc,
        banner: ban ? new URL(ban, 'https://minecraftpocket-servers.com').href.split('?')[0] : '',
        registered: info['Registered since'] || '',
      };
      J.done++; await sleep(120);
    }
  };
  await Promise.all([worker(), worker(), worker()]);
  J.state = 'finished'; console.log('finished', J.done, 'serveurs,', J.errors.length, 'erreurs');
})();
