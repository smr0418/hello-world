import requests
import re
import json
import time
import requests.exceptions as RequestException
#获取猫眼首页的排行信息，定义为函数
def get_one_page(url):
    try:
        headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Host': 'maoyan.com'
        }
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None
#正则匹配相关排行数据，函数
def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?<img data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?score.*?integer.*?>(.*?)<.*?fraction.*?>(.*?)<',re.S)
    items = re.findall(pattern,html)
    print(items)
#strip的作用 列表的操作
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2].strip(),
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score':item[5].strip() + item[6].strip()
        }
#写入文件
def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False) + '\n')


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    parse_one_page(html)
    for item in parse_one_page(html):
       write_to_file(item)
    '''print(html)'''

if __name__ == '__main__':
    for i in range(10):
        main(offset=i*10)
        time.sleep(1)
