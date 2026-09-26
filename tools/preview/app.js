const $ = id => document.getElementById(id);
let network, current;
const escapeHTML = value => String(value).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const route = (path, fragment='') => '#/' + encodeURI(path) + (fragment ? '#' + encodeURIComponent(fragment) : '');
const title = path => network.docs.find(d => d.path === path)?.title || path;
const typeLabels = {concept:'Concept', proposal:'Proposal', person:'Contributor', source:'Source', guide:'Guide'};
const statusLabels = {draft:'Draft', provisional:'Draft senses', 'passages-inspected':'Cited passages consulted', 'navigation-entry':'Contributor entry', 'editorial-reconstruction':'Draft interpretation', 'editorial-mapping':'Draft link'};
const relationLabels = {'uses-sense':'Uses sense'};
const readable = (value, labels) => labels[value] || value.replace(/[-_]/g, ' ');
const anchorTitle = (path, fragment) => network.docs.find(d=>d.path===path)?.anchors?.[fragment] || fragment.replace(/[-_]/g, ' ');
function selection() {
  const [path, fragment=''] = location.hash.slice(2).split('#');
  try { return [decodeURIComponent(path || 'INDEX.md'), decodeURIComponent(fragment)]; }
  catch { return ['INDEX.md', '']; }
}
function browse() {
  if (!network) return;
  const query = $('search').value.toLowerCase().trim(), type = $('type').value;
  const matches = network.docs.filter(d => (!type || d.type === type) && (d.title + ' ' + d.text).toLowerCase().includes(query));
  $('count').textContent = `${matches.length} ${matches.length === 1 ? 'page' : 'pages'}`;
  $('results').innerHTML = matches.map(d => `<a href="${escapeHTML(route(d.path))}" ${d.path===current?'aria-current="page"':''}>${escapeHTML(d.title)}<small>${escapeHTML(readable(d.type,typeLabels))}</small></a>`).join('') || '<p>No matching pages. Try another term or page type.</p>';
}
function connections(edges, outgoing) {
  return edges.map(e => {
    const path = outgoing ? e.target : e.source;
    const description = e.type === 'link' ? 'Navigation link' : [readable(e.type,relationLabels),readable(e.status,statusLabels)].filter(Boolean).join(' · ');
    return `<div class="connection"><a href="${escapeHTML(route(path, outgoing ? e.fragment : ''))}">${escapeHTML(title(path))}</a><small>${escapeHTML(description)}${e.fragment ? ' · ' + escapeHTML(anchorTitle(e.target,e.fragment)) : ''}</small></div>`;
  }).join('') || '<p class="hint">None on this page.</p>';
}
function graph(edges) {
  const neighbors = [...new Set(edges.flatMap(e => [e.source,e.target]))].filter(p => p!==current);
  if (!neighbors.length) { $('graph').textContent = 'No connected pages.'; return; }
  const height = Math.max(100, neighbors.length*48), center = height/2;
  let svg = `<svg viewBox="0 0 300 ${height}" role="img" aria-label="Links between this page and connected pages"><defs><marker id="arrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto-start-reverse"><path d="M0 0L6 3L0 6" fill="none" stroke="#6681a1"/></marker></defs><circle cx="16" cy="${center}" r="8" fill="#1855a0"><title>${escapeHTML(title(current))}</title></circle>`;
  neighbors.forEach((path,i) => {
    const y = i*48+24, relevant = edges.filter(e => e.source===path || e.target===path);
    const outgoing = relevant.some(e=>e.source===current), incoming = relevant.some(e=>e.target===current);
    svg += `<path d="M27 ${center}L103 ${y}" fill="none" stroke="#6681a1" ${relevant.every(e=>e.type==='link')?'stroke-dasharray="4 3"':''} ${outgoing?'marker-end="url(#arrow)"':''} ${incoming?'marker-start="url(#arrow)"':''}/><a href="${escapeHTML(route(path))}"><title>${escapeHTML(title(path))}</title><rect x="110" y="${y-18}" width="188" height="36" rx="4" fill="#eaf0f8"/><text x="119" y="${y+5}">${escapeHTML(title(path).length>22?title(path).slice(0,21)+'…':title(path))}</text></a>`;
  });
  $('graph').innerHTML = svg + '</svg>';
}
function show(scroll=true) {
  const [path, fragment] = selection(); current = path;
  const doc = network.docs.find(d=>d.path===path);
  $('page').innerHTML = doc?.html || '<h1>Page not found</h1><p>Choose a page from the network browser.</p>';
  $('badges').innerHTML = doc ? [readable(doc.type,typeLabels),readable(doc.status,statusLabels),doc.error].filter(Boolean).map(v=>`<span>${escapeHTML(v)}</span>`).join('') : '';
  document.title = `${doc?.title || 'Page not found'} · Philosophy network`;
  const outgoing = network.edges.filter(e=>e.source===path), incoming = network.edges.filter(e=>e.target===path);
  $('outgoing').innerHTML = connections(outgoing,true); $('incoming').innerHTML = connections(incoming,false);
  graph([...outgoing,...incoming]); browse();
  if (scroll) {
    if (fragment) document.getElementById(fragment)?.scrollIntoView();
    else window.scrollTo(0,0);
  }
}
async function refresh() {
  try {
    const response = await fetch('/api/network');
    if (!response.ok) throw new Error('Network could not be read');
    const next = await response.json();
    if (next.version !== network?.version) {
      const first = !network, previousType = $('type').value;
      network = next;
      $('type').innerHTML = '<option value="">All page types</option>' + [...new Set(network.docs.map(d=>d.type))].sort((a,b)=>readable(a,typeLabels).localeCompare(readable(b,typeLabels))).map(t=>`<option value="${escapeHTML(t)}">${escapeHTML(readable(t,typeLabels))}</option>`).join('');
      $('type').value = previousType;
      show(first);
    }
    $('sync').textContent = 'Local preview · watching for edits';
  } catch {
    $('sync').textContent = 'Preview unavailable · retrying';
  } finally { setTimeout(refresh, 2000); }
}
$('search').addEventListener('input',browse); $('type').addEventListener('change',browse);
window.addEventListener('hashchange',()=>network && show());
refresh();
