import subprocess
import csv

input_file = 'ip.txt'
output_file = 'output.csv'

try:
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = infile.readlines()
        total_lines = len(reader)

        csv_writer = csv.writer(outfile)
        csv_writer.writerow(['IP', '归属地'])

        print("正在查询...")
        for i, line in enumerate(reader, start=1):
            ip = line.strip()
            process = subprocess.Popen(['nali', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, _ = process.communicate()
            result = stdout.decode().strip()
            csv_writer.writerow([ip, result])
            print(f"查询进度: {i}/{total_lines} ({(i / total_lines) * 100:.2f}%)", end='\r')

        print("\n查询完毕，结果已保存到", output_file)

except FileNotFoundError:
    print(f"输入文件 {input_file} 不存在.")
except Exception as e:
    print(f"发生错误: {e}")
input("按任意键退出...")
