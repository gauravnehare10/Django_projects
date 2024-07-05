from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'app1/index.html')

def mobiles(request):
    mobiles_data = {'Oneplus Nord CE4': '₹24,999',
                    'Redmi 12 5G': '₹12,499',
                    'iQOO Z9x 5G': '₹12,999',
                    'realme GT 6T 5G': '₹32,999',
                    'Samsung Galaxy M14 5G': '₹9,990'}
    return render(request, 'app1/mobiles.html', context={"mobiles_data": mobiles_data})

def watches(request):
    watches_data = {'Fastrack Limitless Fs1+ Smartwatch': '₹1,499',
                    'Titan Smart 3 Premium Smart Watch': '₹4,980',
                    'Maxima Max Pro Sky 1.85" HD Smart Watch': '₹1,399',
                    'Fossil Flynn Analog Black Dial Mens Watch': '₹11,996',
                    'SKYLOFTS Stainless Steel Automatic Watch': '₹1,750'}
    return render(request, 'app1/watches.html', context={"watches_data": watches_data})

def tv(request):
    tv_data = {'Samsung 138 cm (55 Inches) Crystal Vision 4K Ultra HD Smart LED TV': '₹44,990',
               'Acer 127 cm (50 inches) Advanced I Series 4K Ultra HD Smart LED Google TV': '₹27,999',
               'Xiaomi 125 cm (50 inches) X 4K Dolby Vision Series Smart Google TV': '₹32,999',
               'LG 164 cm (65 inches) 4K Ultra HD Smart LED TV': '₹64,990',
               'Panasonic 108 cm (43 inches) 4K Ultra HD Smart LED Google TV': '₹29,990'}
    return render(request, 'app1/televisions.html', context={"tv_data": tv_data})

def laptops(request):
    laptops_data = {'HP Laptop 15s, 12th Gen Intel Core i5-1235U, 15.6-inch (39.6 cm), FHD, 16GB DDR4, 512GB SSD': '₹52,849',
                    'Dell 15 Thin & Light Laptop, 12th Gen Intel Core i5-1235U Processor, 8GB, 512GB SSD, 15.6"': '₹46,990',
                    'Apple MacBook Air Laptop M1 chip, 13.3-inch/33.74 cm Retina Display, 8GB RAM, 256GB SSD': '₹71,990',
                    'Lenovo IdeaPad Gaming 3 Laptop AMD Ryzen 5 5500H 15.6"':'₹45,990',
                    'ASUS Vivobook 16X (2022) Thin and Light Laptop,AMD Ryzen 5 5600H, 16.0-inch, (8GB RAM/512GB SSD': '₹46,990'}
    return render(request, 'app1/laptops.html', context={"laptops_data": laptops_data})
