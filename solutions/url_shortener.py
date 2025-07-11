"""
URL Shortener Solution
Implements a simple URL shortening service that can convert between
long and short URLs.
"""
import hashlib

class URLShortener:
    def __init__(self):
        """Initialize the URL shortener with empty mappings."""
        self.url_map = {}  # short_url -> long_url
        self.long_url_map = {}  # long_url -> short_url (for deduplication)
        self.prefix = "https://short.url/"
    
    def shorten(self, long_url: str) -> str:
        """
        Convert a long URL to a short URL.
        
        Args:
            long_url (str): The original long URL to shorten
            
        Returns:
            str: The shortened URL
        """
        # Return existing short URL if we've seen this long URL before
        if long_url in self.long_url_map:
            return self.long_url_map[long_url]
        
        # Create a hash of the URL
        hash_object = hashlib.md5(long_url.encode())
        short_hash = hash_object.hexdigest()[:6]
        short_url = self.prefix + short_hash
        
        # Store the mapping in both directions
        self.url_map[short_url] = long_url
        self.long_url_map[long_url] = short_url
        
        return short_url
    
    def expand(self, short_url: str) -> str:
        """
        Convert a short URL back to the original long URL.
        
        Args:
            short_url (str): The shortened URL
            
        Returns:
            str: The original long URL, or an error message if not found
        """
        return self.url_map.get(short_url, "URL not found")


# Example usage
if __name__ == "__main__":
    shortener = URLShortener()
    
    # Test the URL shortener
    urls = [
        "https://www.example.com/very/long/url/with/many/parameters?query=test",
        "https://www.google.com/search?q=python+hackathon+questions",
        "https://www.example.com/very/long/url/with/many/parameters?query=test"  # Duplicate
    ]
    
    for url in urls:
        short_url = shortener.shorten(url)
        expanded = shortener.expand(short_url)
        print(f"Original: {url}")
        print(f"Short:    {short_url}")
        print(f"Expanded: {expanded}")
        print("-" * 50)
