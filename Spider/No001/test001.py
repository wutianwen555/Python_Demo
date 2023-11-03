"""
    10行代码集2000张美女图，Python爬虫120例，再上征途
    https://dream.blog.csdn.net/article/details/117024328
"""
import requests
import re
import time


# 请求函数
def request_get(url, ret_type="text", timeout=5, encoding="GBK"):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                      "Version/17.1 Safari/605.1.15"
    }
    res = requests.get(url=url, headers=headers, timeout=timeout)
    res.encoding = encoding
    if ret_type == "text":
        return res.text
    elif ret_type == "image":
        return res.content


# 抓取函数
def main():
    urls = [f"http://www.netbian.com/mei/index_{i}.htm" for i in range(2, 201)]
    url = "http://www.netbian.com/qiche/index.htm"
    urls.insert(0, url)
    for url in urls:
        print("抓取列表页地址为：", url)
        text = request_get(url)
        format(text)


# 解析函数
def analysis(text):
    origin_text = split_str(text, '<div class="list">', '<div class="page">')
    pattern = re.compile('href="(.*?)"')
    hrefs = pattern.findall(origin_text)
    hrefs = [i for i in hrefs if i.find("desk") > 0]
    for href in hrefs:
        url = f"http://www.netbian.com{href}"
        print(f"正在下载：{url}")
        text = request_get(url)
        format_detail(text)


def split_str(text, s_html, e_html):
    start = text.find(s_html) + len(e_html)
    end = text.find(e_html)
    origin_text = text[start:end]

    return origin_text


def format_detail(text):
    origin_text = split_str(text, '<div class="pic">', '<div class="pic-down">')
    pattern = re.compile('src="(.*?)"')
    image_src = pattern.search(origin_text).group(1)
    # 保存图片
    save_image(image_src)


# 存储函数
def save_image(image_src):
    content = request_get(image_src, "image")
    with open(f"./No001/{str(time.time())}.jpg", "wb") as f:
        f.write(content)
        print("图片保存成功")


if __name__ == '__main__':
    main()
