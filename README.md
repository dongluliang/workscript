# workscript
工作中常用的小脚本

udpscan.py
作用：读取CSV文件并验证其中IP对的应的UDP端口是否为开放。
CSV文件内A列为ip，B列为port，验证完成后会输出ip_ports_result.csv报告。
1、调用nmap模块批量验证udp-diff.csv内A列IP对应的B列端口是否开放。
2、需要安装模块 pip install python-nmap


对比ip和端口.py
读取original.csv内IP和nessus.csv内ip和端口，相互对比并输出存在差异数据。
