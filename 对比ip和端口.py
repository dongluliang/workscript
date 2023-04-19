# -*- coding: utf-8 -*-
import csv

# ��ȡ�ϱ���̨�ˣ���һ��IP���ڶ��ж˿�
reported = {}
with open('original.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # ������ͷ
    for row in reader:
        ip = row[0]
        port = row[1]
        if ip not in reported:
            reported[ip] = set()
        reported[ip].add(port)

# nessusʵ��ɨ�豨�浼����̨�ˣ���һ��IP���ڶ��ж˿�
actual = {}
with open('nessus.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # ������ͷ
    for row in reader:
        ip = row[0]
        port = row[1]
        if ip not in actual:
            actual[ip] = set()
        actual[ip].add(port)

# �Ա�������񲢰��в���Ľ�������diff.csv
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
