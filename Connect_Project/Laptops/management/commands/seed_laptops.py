from django.core.management.base import BaseCommand
from laptops.models import Laptop
from decimal import Decimal

class Command(BaseCommand):
    help = "Seed database with sample laptops"

    def handle(self, *args, **kwargs):
        laptops = [
            {
                "name": "Dell XPS 13",
                "brand": "Dell",
                "processor": "Intel i7 11th Gen",
                "ram": 16,
                "ram_type": "DDR4",
                "storage": 512,
                "storage_type": "SSD",
                "gpu": "Intel Iris Xe",
                "display": "13.3-inch FHD",
                "price": Decimal("1200.00"),
                "description": "Ultra-thin laptop with excellent performance."
          },
            {
                "name": "HP Pavilion 15",
                "brand": "HP",
                "processor": "Intel i5 10th Gen",
                "ram": 8,
                "ram_type": "DDR4",
                "storage": 256,
                "storage_type": "SSD",
                "gpu": "Intel UHD Graphics",
                "display": "15.6-inch FHD",
                "price": Decimal("700.00"),
                "description": "Reliable laptop for students and professionals."
            },
            {
                "name": "Lenovo ThinkPad X1 Carbon",
                "brand": "Lenovo",
                "processor": "Intel i7 12th Gen",
                "ram": 16,
                "ram_type": "DDR5",
                "storage": 1024,
                "storage_type": "SSD",
                "gpu": "Intel Iris Xe",
                "display": "14-inch 2K",
                "price": Decimal("1500.00"),
                "description": "Business laptop with durability and performance."
            },
            {
                "name": "Apple MacBook Air M1",
                "brand": "Apple",
                "processor": "Apple M1",
                "ram": 8,
                "ram_type": "Unified",
                "storage": 256,
                "storage_type": "SSD",
                "gpu": "Apple 7-core GPU",
                "display": "13.3-inch Retina",
                "price": Decimal("999.00"),
                "description": "Lightweight MacBook with powerful M1 chip."
            },
            {
                "name": "Apple MacBook Pro M2",
                "brand": "Apple",
                "processor": "Apple M2",
                "ram": 16,
                "ram_type": "Unified",
                "storage": 512,
                "storage_type": "SSD",
                "gpu": "Apple 10-core GPU",
                "display": "14-inch Liquid Retina",
                "price": Decimal("1999.00"),
                "description": "High-performance MacBook for creators."
            },
            {
                "name": "Asus ZenBook 14",
                "brand": "Asus",
                "processor": "Intel i7 11th Gen",
                "ram": 16,
                "ram_type": "DDR4",
                "storage": 512,
                "storage_type": "SSD",
                "gpu": "NVIDIA MX450",
                "display": "14-inch OLED",
                "price": Decimal("1100.00"),
                "description": "Compact ultrabook with OLED display."
            },
            {
                "name": "Acer Aspire 5",
                "brand": "Acer",
                "processor": "Intel i5 10th Gen",
                "ram": 8,
                "ram_type": "DDR4",
                "storage": 256,
                "storage_type": "SSD",
                "gpu": "Intel UHD Graphics",
                "display": "15.6-inch FHD",
                "price": Decimal("600.00"),
                "description": "Affordable laptop with solid performance."
            },
            {
                "name": "MSI GF63 Thin",
                "brand": "MSI",
                "processor": "Intel i7 10th Gen",
                "ram": 16,
                "ram_type": "DDR4",
                "storage": 512,
                "storage_type": "SSD",
                "gpu": "NVIDIA GTX 1650",
                "display": "15.6-inch FHD 144Hz",
                "price": Decimal("1200.00"),
                "description": "Gaming laptop with sleek design."          
            },
            {
                "name": "Samsung Galaxy Book Pro",
                "brand": "Samsung",
                "processor": "Intel i5 11th Gen",
                "ram": 8,
                "ram_type": "DDR4",
                "storage": 256,
                "storage_type": "SSD",
                "gpu": "Intel Iris Xe",
                "display": "15.6-inch AMOLED",
                "price": Decimal("950.00"),
                "description": "Lightweight laptop with AMOLED display."
            },
            {
                "name": "Microsoft Surface Laptop 4",
                "brand": "Microsoft",
                "processor": "AMD Ryzen 5",
                "ram": 8,
                "ram_type": "DDR4",
                "storage": 512,
                "storage_type": "SSD",
                "gpu": "AMD Radeon Graphics",
                "display": "13.5-inch PixelSense",
                "price": Decimal("1300.00"),
                "description": "Premium laptop with excellent battery life."
            },
        ]

        for laptop_data in laptops:
            Laptop.objects.get_or_create(**laptop_data)

        self.stdout.write(self.style.SUCCESS("✅ Successfully seeded laptops!"))
