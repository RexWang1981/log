import PyPDF2

def extract_pages(input_pdf, output_pdf, start_page, end_page):
    # 打开输入的PDF文件
    with open(input_pdf, "rb") as infile:
        reader = PyPDF2.PdfReader(infile)
        writer = PyPDF2.PdfWriter()

        # 提取指定页范围
        for i in range(start_page, end_page + 1):
            writer.add_page(reader.pages[i])

        # 保存为新的PDF文件
        with open(output_pdf, "wb") as outfile:
            writer.write(outfile)

# 示例使用
input_pdf = "CUSTOMER CONNECTORS DATASHEET.pdf"
output_pdf = "CUSTOMER CONNECTORS DATASHEET1.pdf"
start_page = 0  # 页码从0开始，所以这将提取第7页
end_page = 1    # 提取第7页

extract_pages(input_pdf, output_pdf, start_page, end_page)