import os
import sys
import img2pdf

def convert_folders_to_pdf():
    if getattr(sys, 'frozen', False):
        main_folder = os.path.dirname(sys.executable)
    else:
        main_folder = os.path.dirname(os.path.abspath(__file__))

    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.webp')

    for root, dirs, files in os.walk(main_folder):
        image_list = []
        
        for file_name in sorted(files):
            if file_name.lower().endswith(image_extensions):
                image_path = os.path.join(root, file_name)
                image_list.append(image_path)
                
        if image_list:
            folder_name = os.path.basename(root)
            if root != main_folder:
                pdf_filename = os.path.join(main_folder, f"{folder_name}.pdf")
                try:
                    with open(pdf_filename, "wb") as f:
                        f.write(img2pdf.convert(image_list))
                    print(f"ተሳክቷል: '{folder_name}' -> '{folder_name}.pdf'")
                except Exception as e:
                    print(f"ስህተት ተፈጥሯል በ '{folder_name}': {e}")

if __name__ == "__main__":
    convert_folders_to_pdf()
