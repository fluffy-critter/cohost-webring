---
layout: default
permalink: /redirect
---
<script>

const url = '{{ "list.json" | relative_url }}';

let req = new XMLHttpRequest();
req.open('GET', url, true);
req.responseType = 'json';

req.onload = function() {
  function fail(reason) {
    console.error('failure', reason);
    document.getElementById('message').innerHTML = 'There was a problem finding the next page. Redirecting to first page in the webring.';
  }

  if(req.status != 200) {
    fail('status');
    return;
  }

  if(!req.response) {
    fail('response');
    return;
  }

  const sites = req.response.sites;

  const queryString = window.location.search;
  const urlParams = new URLSearchParams(queryString);

  function normalize(hostname) {
    return hostname.replace(/^www\./, '');
  }

  let current;
  let from = new URL(urlParams.get('from'));
  for(let i = 0; i < sites.length; i++) {
    let test = new URL(sites[i].url);
    console.log(test);
    if (from && (normalize(from.hostname) == normalize(test.hostname) && from.pathname == test.pathname)) {
      console.log("found", from, test);
      current = i;
      break;
    }
  }

  if(typeof current === 'undefined') {
    fail('not-in-list');
    current = -1;
    console.log("not in list", from)
  }


  // We show the previous blog if they ask for it, otherwise assume we want the next one.
  let next = sites[((current + 1) % sites.length)];
  if(urlParams.get('dir') === 'prev') {
    next = sites[((current + sites.length - 1) % sites.length)];
  }

  if(next.url) {
    window.location.replace(next.url);
  }

}

req.send();

</script>

<p id="message">Redirecting...</p>