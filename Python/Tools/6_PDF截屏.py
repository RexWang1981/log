import fitz  # PyMuPDF
from PIL import Image
import io
import win32clipboard
import win32con

def pdf_page_to_clipboard(pdf_path, page_number):
    # 打开PDF文件
    document = fitz.open(pdf_path)

    # 检查页码范围
    if page_number < 0 or page_number >= document.page_count:
        raise ValueError(f"Page number {page_number} is out of range.")

    # 获取指定页
    page = document.load_page(page_number)

    # 获取页面的pixmap（即像素图像）
    pix = page.get_pixmap()

    # 将pixmap转换为Pillow的Image对象
    image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    # 将图像保存到字节流中
    output = io.BytesIO()
    image.save(output, format="BMP")
    bmp_data = output.getvalue()

    # 将BMP数据保存到剪贴板
    win32clipboard.OpenClipboard()
    try:
        win32clipboard.EmptyClipboard()
        # Set the clipboard data for BMP
        win32clipboard.SetClipboardData(win32con.CF_DIB, bmp_data[14:])
    finally:
        win32clipboard.CloseClipboard()

# 示例使用
pdf_path = "Decodifica ECM_Inglese 2 (1).pdf"
page_number = 0  # 从0开始，0表示第一页，6标识第7页

pdf_page_to_clipboard(pdf_path, page_number)