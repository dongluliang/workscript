import os
import re
import asyncio
import aiohttp
from tqdm import tqdm
import urllib.parse

# 定义异步函数下载图片
async def download_image(image_url, image_name):
    async with aiohttp.ClientSession() as session:
        async with session.get(image_url) as response:
            if response.status == 200:
                # 将图片保存到 'images' 文件夹中
                image_name = urllib.parse.quote(image_name, safe='')  # 将非法字符替换为合法字符
                with open(f'images/{image_name}', 'wb') as file:
                    file.write(await response.read())
                return f'images/{image_name}'
            return None

# 检查并创建 'images' 文件夹
if not os.path.exists('images'):
    os.makedirs('images')

# 遍历当前文件夹下的所有 .md 文件
for filename in os.listdir('.'):
    if filename.endswith('.md'):  # 只处理 .md 文件
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            # 使用正则表达式找到图片链接
            image_urls = re.findall(r'!\[.*?\]\((.*?)\)', content)
            
            tasks = []
            for image_url in image_urls:
                # 获取图片文件名
                image_name = image_url.split('/')[-1]
                task = download_image(image_url, image_name)
                tasks.append(task)
            
            # 启动异步任务并等待完成
            loop = asyncio.get_event_loop()
            downloaded_paths = loop.run_until_complete(asyncio.gather(*tasks))

            # 替换Markdown文件中的图片链接为本地相对路径
            for image_url, local_path in zip(image_urls, downloaded_paths):
                if local_path:
                    content = content.replace(image_url, local_path)
            
            # 将替换后的内容写回原文件
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(content)
                
            # 更新进度条显示当前处理的文件名
            tqdm.write(f"Processed: {filename}")
    else:
        tqdm.write(f"Skipped: {filename} (Not a .md file)")
