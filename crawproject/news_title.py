import requests
# 1. 주소분석, 2. 알고리즘(for문 돌면서 다운받는), 3. text.html 이기 때문 파싱하는게 힘들다


# 신문사 이름을 크롤링 
# 목적 : oid 수집, 수집시간 대략 1~2분

start_oid = 1
# oid_list = []
oid_names = []

for num in range(0, 1000):
    start_oid_str = str(start_oid).zfill(3)
    uri = f"https://newsstand.naver.com/?list=&pcode={start_oid_str}"

    response = requests.get(uri)

    if(response.status_code == 200):
       # oid_list.append(start_oid_str)
       print(response.text)

    start_oid = start_oid + 1

#print(f"oid 총 개수 : {len(oid_list)}")
#print(oid_list)