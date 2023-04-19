import os
import re
import subprocess
from datetime import datetime

# 定义IP地址列表
ips = []

# 从ip.txt文件中读取IP地址
with open('ip.txt', 'r') as f:
    ips = f.read().splitlines()

# 初始化进度条
def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█', print_end="\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=print_end)
    if iteration == total:
        print()

# 打开或创建结果文件
if not os.path.exists('ping_results.csv'):
    with open('ping_results.csv', 'w') as f:
        f.write('IP,状态,丢包率,延时\n')

# 处理每个IP地址
for ip in ips:
    # 执行ping命令
    print(f'正在检测 {ip}...')
    cmd = ['ping', '-n', '20', '-w', '1000', ip]
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, universal_newlines=True)
    except subprocess.CalledProcessError as e:
        output = e.output
    except:
        output = None

    # 处理ping命令的输出
    if output:
        lost_rate = re.search(r'(\d+)% 丢失', output)
        if lost_rate:
            lost_rate = int(lost_rate.group(1))
        else:
            lost_rate = 100
        delay = re.search(r'最短 = (\d+)ms，最长 = (\d+)ms，平均 = (\d+)ms', output)
        if delay:
            delay = int(delay.group(3))
        else:
            delay = None
        if lost_rate < 10.73 and delay is not None and delay < 200:
            status = '正常'
        else:
            status = '不正常'
        result = f'{status}/丢包率{lost_rate}%/延时{delay}ms'
    else:
        result = '无法解析ping命令输出'

    # 将结果写入结果文件
    with open('ping_results.csv', 'a') as f:
        f.write(f'{ip},{result}\n')

    # 更新进度条
    current_progress = int((ips.index(ip) + 1) / len(ips) * 100)
    print_progress_bar(current_progress, 100, prefix='进度', suffix=f'{current_progress}%')

print('检测完成。')    
