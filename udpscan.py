import nmap
import csv

nm = nmap.PortScanner()

# 读取CSV文件并验证IP地址和UDP端口
with open('udpport.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # 跳过标题行
    with open('ip_ports_result.csv', mode='w', newline='') as result_file:
        csv_writer = csv.writer(result_file)
        csv_writer.writerow(["IP", "Port", "Status"])
        for row in csv_reader:
            ip = row[0]
            try:
                port = int(row[1])
            except ValueError:
                print(f"Invalid port value for IP {ip}")
                continue
            result = nm.scan(hosts=ip, arguments=f"-sU -p {port}")
            if result["scan"][ip]["udp"][port]["state"] == "open":
                print(f"{ip}:{port} is open")
                csv_writer.writerow([ip, port, "open"])
            else:
                print(f"{ip}:{port} is closed")
                csv_writer.writerow([ip, port, "closed"])
                
