# -*- coding: utf-8 -*-
import csv

# 读取上报的台账，第一列IP，第二列端口
reported = {}
with open('original.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # 跳过表头
    for row in reader:
        ip = row[0]
        port = row[1]
        if ip not in reported:
            reported[ip] = set()
        reported[ip].add(port)

# nessus实际扫描报告导出的台账，第一列IP，第二列端口
actual = {}
with open('nessus.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # 跳过表头
    for row in reader:
        ip = row[0]
        port = row[1]
        if ip not in actual:
            actual[ip] = set()
        actual[ip].add(port)

# 对比两个表格并把有差异的结果输出到diff.csv
with open('diff.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['IP', 'Port'])
    for ip, ports in actual.items():
        if ip in reported:
            diff = ports - reported[ip]
            if diff:
                for port in diff:
                    writer.writerow([ip, port])
        else:
            for port in ports:
                writer.writerow([ip, port])
