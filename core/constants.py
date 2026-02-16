from cachetools import TTLCache


CAPTCHA_CACHE = TTLCache(maxsize=1000, ttl=300)
captcha_cache = CAPTCHA_CACHE