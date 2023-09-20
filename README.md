# workscript
工作中常用的小脚本
<h2>base64topdf.py</h2>
作用:将base64的编码txt文件转换为.pdf文件。<br>
optional arguments:<br>
  -h, --help            show this help message and exit<br>
  -i INPUT, --input INPUT<br>
                        输入的 Base64 源码文本文件路径<br>
  -o OUTPUT, --output OUTPUT<br>
                        输出的 PDF 文件路径，默认为脚本同目录下<br>
<h2>udpscan.py</h2><br>
作用：读取CSV文件并验证其中IP对的应的UDP端口是否为开放。<br>
CSV文件内A列为ip，B列为port，验证完成后会输出ip_ports_result.csv报告。<br>
1、调用nmap模块批量验证udpport.csv内A列IP对应的B列端口是否开放。<br>
2、需要安装模块 pip install python-nmap<br>
<br>
<h2>对比ip和端口.py</h2><br>
作用：读取original.csv内A列ip B列port与nessus.csv的A列ip和B列port进行相互对比并输出存在差异数据到diff.csv。
<br>
<h2>ping.py</h2>
用于判断ip.txt文件（每行一个ip）的网络状态<br>
if lost_rate < 10.73 and delay is not None and delay < 200:如果小于10.73ms回包小于200ms则在报告中打印“正常”，否则为不正常。
