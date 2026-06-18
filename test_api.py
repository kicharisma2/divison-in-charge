import requests
import urllib.parse
import re

API_KEY = "kicharisma"
mst = "2105167"
url = f"https://www.law.go.kr/DRF/lawService.do?OC={API_KEY}&target=ordin&type=XML&MST={mst}"
res = requests.get(url)

print("Response status:", res.status_code)
print("Length:", len(res.content))

for enc in ['utf-8', 'cp949', 'euc-kr']:
    try:
        decoded = res.content.decode(enc)
        kor = len(re.findall(r'[가-힣]', decoded))
        print(f"Decoding with {enc}: {kor} hangul chars")
        if "정보공개" in decoded:
            print("  FOUND '정보공개' in", enc)
    except Exception as e:
        print(f"Decoding with {enc} failed:", str(e))
