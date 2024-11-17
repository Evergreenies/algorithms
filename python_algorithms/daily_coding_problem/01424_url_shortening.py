"""
Implement a URL shortener with the following methods:

shorten(url), which shortens the url into a six-character alphanumeric string,
such as zLg6wl.
restore(short), which expands the shortened string into the original url. If no
such shortened string exists, return null.

Hint: What if we enter the same URL twice?
"""

import random
import string

from collections import defaultdict


class URLShortener:
    def __init__(self) -> None:
        self.url_to_short = defaultdict(str)
        self.short_to_url = defaultdict(str)
        self.base_url = "http://short.ly/"
        self.length = 6

    def shorten(self, url: str) -> str | None:
        if self.url_to_short.get(url):
            return self.base_url + self.url_to_short[url]

        short = self._generate_short_url()
        while short in self.short_to_url:
            short = self._generate_short_url()

        self.url_to_short[url] = short
        self.short_to_url[short] = url

        return self.base_url + short

    def restore(self, short: str) -> str | None:
        return self.short_to_url.get(short.replace(self.base_url, ""), None)

    def _generate_short_url(self) -> str:
        return "".join(
            random.choices(string.ascii_letters + string.digits, k=self.length)
        )


# Example usage:
shortener = URLShortener()

# Shorten a URL
short_url = shortener.shorten("https://www.example.com")
print("Shortened URL:", short_url)

# Restore the original URL
if short_url:
    original_url = shortener.restore(short_url)
    print("Original URL:", original_url)

# Shorten the same URL again
short_url_duplicate = shortener.shorten("https://www.example.com")
print("Shortened URL (duplicate):", short_url_duplicate)

# Restore an invalid shortened URL
invalid_restore = shortener.restore("http://short.ly/invalid")
print("Invalid Restore:", invalid_restore)
