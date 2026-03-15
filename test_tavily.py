
import requests
import os
api_key = os.environ.get('TAVILY_API_KEY')
if not api_key:
    print('❌ TAVILY_API_KEY 未找到')
else:
    try:
        res = requests.post('https://api.tavily.com/search', json={
            'api_key': api_key,
            'query': '2026年创业热门方向',
            'max_results': 3,
            'include_answer': True
        })
        if res.status_code == 200:
            data = res.json()
            print('✅ Tavily 搜索配置成功！')
            print(f'摘要：{data["answer"]}')
            print('来源：')
            for item in data['results']:
                print(f'- {item["title"]}: {item["url"]}')
        else:
            print(f'❌ 请求失败，状态码：{res.status_code}，错误：{res.text}')
    except Exception as e:
        print(f'❌ 调用失败：{str(e)}')
