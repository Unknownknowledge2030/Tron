
import re

# فایل‌هایی که می‌خوای بررسی کنی
js_files = ["main.35774be6.js", "8513.78b88a9f.js"]

# الگوهای جستجو برای پیدا کردن درخواست‌های API و توابع تراکنش
patterns = {
    "api_calls": r"(https?://[^\s\"']+)",  # پیدا کردن URL های API
    "transaction_functions": r"function\s+(\w+)\s*.*?\s*\{",  # توابع جاوااسکریپت
    "transfer_calls": r"(transfer|sendTransaction|submitTransaction)\s*.*?",  # متدهای مرتبط با انتقال
    "wallet_addresses": r"(T[a-zA-Z0-9]{33,})"  # پیدا کردن آدرس‌های TRX
}

# جستجو در هر فایل
for js_file in js_files:
    print(f"🔍 Analyzing: {js_file}\n" + "-"*50)

    try:
        with open(js_file, "r", encoding="utf-8") as f:
            content = f.read()

            for key, pattern in patterns.items():
                matches = re.findall(pattern, content)
                if matches:
                    print(f"📌 Found {key}:")
                    for match in set(matches):
                        print(f"   ➡ {match}")
                    print("-"*50)

    except Exception as e:
        print(f"❌ Error reading {js_file}: {e}")

print("✅ Analysis Complete!")
