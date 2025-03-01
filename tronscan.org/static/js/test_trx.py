
import requests

test_tx = "67f2cf1a63d9ac019066c94fcc9737d88411a0a595a50892937a36f8dc1f8374"
api_urls = [
    "https://api.trongrid.io",
    "https://nile.trongrid.io",
    "https://shasta.trongrid.io"
]

for api in api_urls:
    url = f"{api}/v1/transactions/{test_tx}"
    response = requests.get(url)
    print(f"🔎 Testing {api}...")
    print(f"🔹 Status: {response.status_code}")
    try:
        print(f"🔹 Response: {response.json()}\n")
    except:
        print("⚠️ Response is not JSON\n")
