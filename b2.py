import re,requests,os

number=input("输入av号（例如：20035622）:")
# print(str(number))
# os.chdir("bilibili")
if os.path.lexists("bilibili"):
    os.chdir("bilibili")
else:
    os.mkdir("bilibili")
    os.chdir("bilibili")

def download(number):
    base_url="https://www.bilibili.com/video/av"
    base_http="http:"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"}
    url=base_url+str(number)
    # print(url)
    text=requests.get(url,headers=headers).text
    # print(text)
    pattern=re.compile(r'<img src="(.*?)" style="display:none;" class="cover_image"/>',re.S)
    picture=re.findall(pattern,text)
    if picture:#封面存在
        for i in picture:
            http=base_http+str(i)
            #print(http)#图片地址
            print('正在下载:av'+ number +'正在自动保存在当前页bilibili目录下')

            try:
                pic = requests.get(http, timeout=10)
            except requests.exceptions.ConnectionError:
                print('【错误】当前图片无法下载')
                continue

            f=open(str(number)+'.jpg','wb')
            f.write(pic.content)
            f.close()
    else:
        print("视频不存在！")


download(number)