#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests

def get_all_page_titles(wiki_url):
    all_titles = []
    apcontinue = None

    while True:
        params = {
            'action': 'query',
            'list': 'allpages',
            'format': 'json',
            'aplimit': 'max'
        }
        if apcontinue:
            params['apcontinue'] = apcontinue

        headers = {
            'User-Agent': 'Script/1.0 (email@example.com)'
        }
        response = requests.get(wiki_url, params=params, headers=headers)
        response.raise_for_status()  # 检查是否有错误
        data = response.json()

        for page in data['query']['allpages']:
            all_titles.append(page['title'])

        if 'continue' in data:
            apcontinue = data['continue']['apcontinue']
        else:
            break

    return all_titles

def save_titles(titles):
    with open("./moegirl-all-titles.txt", "wb") as f:
        f.write('\n'.join(titles).encode("utf-8"))

if __name__ == '__main__':
    wiki_url = 'https://mzh.moegirl.org.cn/api.php'
    titles = get_all_page_titles(wiki_url)
    print(titles)
    print(f"词条数量：{len(titles)}")
    save_titles(titles)