from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<head>
  <title>
    DEVICE DETAILS`
  </title>
</head>
<body bgcolor="#f8f8ff" >
  <h1 align="center"><b>M.K JEEVITH</b></h1><br>
  <h1 align="center"><b>26018300</b></h1>
  <h1><b>TOP 5 LAPTOPS TO BUY IN 2026</b></h1>
  <h1 align="center"><b>DEVICE SPECIFICATIONS</b></h1>
  <table border="1">
    <tr>
      <th>BRAND</th>
      <th>PRICE</th>
      <th>specifications</th>
      <th>order link</th>
    </tr>
    <tr>
      <td algin="center">LENOVO</td>
      <td algin="center">200000</td>
      <td algin="center">System Specs
      Processor

      AMD Ryzen AI 5 PRO 440 Processor (2.00 GHz up to 4.80 GHz)
      Operating System

      No Operating System
      Graphic Card

      Integrated Graphics
      Memory

      16 GB DDR5-5600 MT/s (SODIMM)
      Storage

      1 TB SSD M.2 2280 PCIe Gen4 TLC Opal
      Display

      35.56 cms (14) WUXGA (1920 x 1200), IPS, Anti-Glare, Non-Touch, 45%NTSC, 400 nits, 60 Hz
      AC Adapter / Power Supply
      65 W USB-C Slim GaN 90% PCC 3 pin AC Adapter - India
      Pointing Device
      Trackpad, No Fingerprint, No NFC, No WWAN, Black
      Keyboard
      Black - English (US)
      WIFI
      MediaTek Wi-Fi 7 MT7925 2 x 2 BE & Bluetooth 5.4
      Warranty
      3 Year On-site
      Color
      Black
      Brand
      ThinkPad P14s Gen 7 (AMD)
      Part Number: 21 X1CTO1WWIN2</td>
      <td algin="center"><a href="https://www.lenovo.com/in/en/p/laptops/thinkpad/thinkpadp/thinkpad-p14s-gen-7-14-inch-amd/21x1cto1wwin2?cid=in:sem:uksqym" title="lenovo laptop" target="_blank">buy here</a></td>
    </tr>
  <tr>
    <td algin="center">ACER</td>
    <td algin="center">200000</td>
    <td algin="center">Operating System: Windows 11 Home, 64-bit
      Processor: Intel Core i7-14650 HX processor
      Memory: 16 GB DDR5 RAM, Upgradable up to 32 GB
      Storage: 1 TB PCIe Gen 4 NVMe SSD,Upgradable up to 2 TB
      Graphics: NVIDIA GeForce RTX 5070 Laptop with 8 GB GDDR7 VRAM
      Display: 16.0-inch WQXGA (2560 x 1600) IPS Display, 180 Hz Refresh Rate, 3 ms Response Time, 100% sRGB.
      Battery: 92 Wh 4-cell Li-ion battery with up to 5 hours backup
      Color: Abyss Black</td>
      <td algin="center"><a href="https://store.acer.com/en-in/acer-predator-helios-neo-16-gaming-laptop-windows-11-home-ms-office-nvidia-geforce-rtx-5070-laptop-gpu-with-8gb-gddr7-vram-16gb-ram-1tb-ssd-16-0-40-64-cm-display-abyss-black-phn16-i31-2-5-kg-rgb-backlight-keyboard?utm_term=" title="acer laptop" target="_blank">buy here</a></td>
    </tr>
    <tr>
      <td algin="center">DELL</td>
      <td algin="center">200000</td>
      <td algin="center">Processor
      Intel Core Ultra 5 235 U, vPro (12 TOPS NPU, 12 cores, up to 4.9 GHz)
      Operating System
      Windows 11 Pro
      Graphics Card
      Integrated Intel graphics for Intel Core Ultra 5 235 U vPro processor
      Memory
      16 GB: 1 x 16 GB, DDR5, 5600 MT/s (5200 MT/s with Intel Core processors)
      Storage
      512 GB SSD
      Display
      16 , Non-Touch, FHD+, 300 nit, 45% NTSC, Anti-Glare, FHD+IR Cam
      Keyboard
      English International non-backlit Copilot key keyboard with numeric keypad</td>
      <td algin="center"><a href="https://www.dellstore.com/dell-pro-16-plus-laptop-bto102-pb16250-i3x.html?tfcid=30223580&gacd=10415953-1227-5761040-431855508-0&dgc=ST&SA360CID=23810231190&" title="dell laptop" target="_blank">buy here</a></td>
    </tr>
    <tr>
      <td algin="center">HP</td>
      <td algin="center">200000</td>
      <td algin="center">Operating systemWindows 11 Home Single Language
      ProcessorAMD Ryzen 9 - 9955 HX
      Memory16 GB RAM
      Storage1 TB SSD
      Display40.6 cm (16), 2 K (1920 x 1200), 165 Hz, 3 ms Response time
      GraphicsNVIDIA GeForce RTX 5060 (8 GB)</td>
      <td algin="center"><a href="https://www.hp.com/in-en/shop/products/laptops/hyperx-omen-16-inch-gaming-laptop-pc-16-ap1096ax-dq1j2pa-acj" title="hp laptop" target="_blank">buy here</a></td>
    </tr>
    <tr>
      <td algin="center">ASUS</td>
      <td algin="center">200000</td>
      <td algin="center">Processor: AMD Ryzen 7 260 Processor 3.8 GHz (24 MB Cache, up to 5.1 GHz, 8 cores, 16 Threads)
      Graphics: 8 GB GDDR7 NVIDIA GeForce RTX 5060 Laptop GPU || 1737 MHz* at 55 W (1687 MHz Boost Clock+50 MHz OC, up to 115 W Dynamic Boost)
      Display: 40.64 cms (16) FHD+ (1920 x 1200, WUXGA) Display having 16:10 Aspect Ratio || 144 Hz Refresh Rate || 300 nits Brightness
      Memory: 16 GB DDR5-5600 SO-DIMM RAM py --list up to 64 GB using 2 x SO-DIMM slots || the memory speed of the systems vary by CPU SPEC
      Storage: 512 GB PCIe 4.0 NVMe M.2 SSD + 100 GB Cloud Storage with Microsoft 365 Basic for 1 Year
      MS Office: Microsoft 365 Basic with 100 GB Cloud Storage for 1 Year + Office Home 2024 with lifetime validity
      Color: Jaeger Gray
      Operating System: Windows 11 Home - ASUS recommends Windows 11 Pro for business</td>
      <td algin="center"><a href="https://in.store.asus.com/gaming-laptop-asus-tuf-gaming-a16-fa608umi-tu288ws.html" title="asus laptop" target="_blank">buy here</a></td>
    </tr>
  </table>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()