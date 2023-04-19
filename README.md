# workscript
工作中常用的小脚本

<h2>udpscan.py</h2><br>
作用：读取CSV文件并验证其中IP对的应的UDP端口是否为开放。<br>
CSV文件内A列为ip，B列为port，验证完成后会输出ip_ports_result.csv报告。<br>
1、调用nmap模块批量验证udpport.csv内A列IP对应的B列端口是否开放。<br>
2、需要安装模块 pip install python-nmap<br>
<br>
<h2>对比ip和端口.py</h2><br>
作用：读取original.csv内A列ip B列port与nessus.csv的A列ip和B列port进行相互对比并输出存在差异数据到diff.csv。
