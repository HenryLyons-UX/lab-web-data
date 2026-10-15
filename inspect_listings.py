def summarize(html):
    return {
    'listing count': count_matches(html, '.item'),
    'select text': select_texts(html, '.price'),
    'select attribute': select_attr(html, 'a[href]', 'href'),
    'extract title' : extract_titles(html),
    'extract prices' : extract_prices_cents(html),
    'count free shipping' : count_free_shipping(html),
    'first link': first_link(html),
    'extract listings' : extract_listings(html)
    }

