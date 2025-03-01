
import requests
import random

# لیست APIهای پیدا شده از فایل JS
api_urls = [
    "https://api.trongrid.io",
    "https://apilist.tronscanapi.com",
    "https://assistapi.tronscan.org/api/account",
    "https://tronscan.org/users/getUserList",
    "https://nile.trongrid.io",
    "https://test.trongrid.io"
]

# هدرهای درخواست برای شبیه‌سازی یک کلاینت واقعی
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Content-Type": "application/json"
}

# تست APIها و چک کردن پاسخ
for url in api_urls:
    print(f"🔍 Testing API: {url}")
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            print(f"✅ API is active: {url}")
            print(f"📌 Response Sample: {response.text[:300]}")
        else:
            print(f"⚠️ API returned status: {response.status_code}")
    except Exception as e:
        print(f"❌ Error connecting to {url}: {e}")

print("\n✅ Testing complete!")
