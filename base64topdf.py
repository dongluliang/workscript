import argparse
import base64
import os

# 作者名称和版本号
author = "dongluliang"
version = "1.0"

def convert_base64_to_pdf(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            base64_data = file.read()

        decoded_data = base64.b64decode(base64_data)

        if not output_file:
            output_file = os.path.splitext(os.path.basename(input_file))[0] + ".pdf"

        with open(output_file, 'wb') as pdf_file:
            pdf_file.write(decoded_data)

        print(f"成功将 Base64 转换为 PDF 文件，保存为 '{output_file}'")
    except Exception as e:
        print(f"发生错误：{str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="将 Base64 转换为 PDF")
    parser.add_argument("-i", "--input", help="输入的 Base64 源码文本文件路径")
    parser.add_argument("-o", "--output", help="输出的 PDF 文件路径，默认为脚本同目录下")

    args = parser.parse_args()

    if not (args.input and args.output):
        print(f"作者: {author}")
        print(f"版本: {version}")
        parser.print_help()  # 显示参数帮助信息
    else:
        # 处理输入文件的相对路径
        input_file = os.path.abspath(args.input)

        if not args.output:
            # 处理默认输出文件的相对路径
            output_file = os.path.splitext(os.path.basename(input_file))[0] + ".pdf"
        else:
            # 处理输出文件的相对路径
            output_file = os.path.abspath(args.output)

        convert_base64_to_pdf(input_file, output_file)
