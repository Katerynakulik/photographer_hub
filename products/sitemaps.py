from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from bookings.models import Photoshoot


class StaticViewSitemap(Sitemap):
    """
    Sitemap for static pages and main sections.
    This covers: Home, Contact and your Complete Gallery.
    """
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        # 'all_products' — це і є твоя сторінка з усіма фото
        return ['home', 'contact', 'all_products']

    def location(self, item):
        return reverse(item)


class SessionSitemap(Sitemap):
    """Sitemap for each individual photoshoot page"""

    priority = 0.9
    changefreq = 'daily'

    def items(self):
        return Photoshoot.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.created_at
