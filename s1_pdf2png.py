from pdf2image import convert_from_path
from tqdm import tqdm
import os

import toml

config = toml.load("./config.toml")


# 轉換 PDF 為 PNG 圖片
def pdf_to_png(pdf_path, output_folder, start_page=1, end_page=None, dpi=600):
    try:
        print("讀取 PDF 文件中，請稍等…")
        # 轉換 PDF 頁面為圖片
        images = convert_from_path(
            pdf_path,
            dpi=dpi,
            first_page=start_page,
            last_page=end_page,
        )

        # 進度條顯示
        for i, img in tqdm(enumerate(images, start=start_page), total=len(images), desc="轉換進度"):
            img.save(os.path.join(output_folder, f"{i}.png"), "PNG")

        print(f"轉換完成！圖片存儲於：{output_folder}")

    except Exceptiona as e:
        print(f"發生錯誤：{e}")

# 使用者輸入
pdf_path = config['src']['file_name'].strip()
output_folder = config['path']['page_png'].strip()
start_page = config['src']['starting_page']
end_page = config['src']['ending_page']

assert os.path.exists(pdf_path), "src.file_name is not found!"
assert start_page <= end_page, "src.starting_page is not <= src.ending_page"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

pdf_to_png(pdf_path, output_folder, start_page, end_page)
