import os

import jmcomic
from typing import *
from PIL import Image


class Translater():
    def __init__(self,basedir):
        self.basedir = basedir
        self.dir_list = os.listdir(self.basedir)
        if 'Download' not in self.dir_list:
            os.mkdir(self.basedir+'/Download')
            self.dir_list.append('Download')
        if 'PDF' not in self.dir_list:
            os.mkdir(self.basedir+'/PDF')
            self.dir_list.append('PDF')
        self.scan_path = os.path.join(self.basedir,'Download')
        self.pdf_path = os.path.join(self.basedir,'PDF')
    def translate_2_pdf(self):
        download_file_path = os.listdir(self.scan_path)
        translated_file_path = os.listdir(self.pdf_path)
        for file in download_file_path: # file is the comic name
            sources = []
            #which will stand for pdf tran name
            f_name = file.split('.')[0]+'.pdf'
            #check if translated
            if f_name in translated_file_path:
                print(f"pdf file{f_name} already translated")
                continue
            #translate into pdf
            for img_path in os.listdir(os.path.join(self.scan_path,file)):
                #open the image
                img_path = os.path.join(self.scan_path,file,img_path)
                img = Image.open(img_path)
                if img.mode == 'RGB':
                    img = img.convert('RGB')
                sources.append(img)

            #after the circulation we have sources as pdf
            out = sources[0]
            out.save(os.path.join(self.pdf_path,file.split('.')[0]+'.pdf'),'PDF',save_all=True,append_images=sources[1:])
            print(f"pdf file {file.split('.')[0]+'.pdf' } translated")

class Downloader():
    def __init__(self,basedir):
        self.basedir = basedir# base_dir to the directory you store your comic
        if 'Download' not in os.listdir(self.basedir):
            print("we hope to have a folder like this:\n"
                  "path/to/directory\n"
                  "|----> PDF 'where we will translate'\n"
                  "|----> Download 'where we will download'")
            print(f"the structure of the directory is wrong,automatically created 'Download' folder' in {self.basedir} directory")
            os.mkdir(self.basedir+'/Download')
        if 'PDF' not in os.listdir(self.basedir):
            print("we hope to have a folder like this:\n"
                  "path/to/directory\n"
                  "|----> PDF 'where we will translate'\n"
                  "|----> Download 'where we will download'")
            print(f"the structure of the directory is wrong,automatically created 'PDF' folder in {self.basedir} directory")
            os.mkdir(self.basedir+'/PDF')

    def download(self,jm_code:str|list,config:Optional[None] ) -> None:
        if isinstance(jm_code,list):
            for code in jm_code:
                jmcomic.download_album(code,config)
        else:
            jmcomic.download_album(jm_code,config)
        print("successfully downloaded")



if __name__ == '__main__':
    config = jmcomic.create_option_by_file('../config/jmconfig.yml')
    downloader = Downloader(basedir='S:/JMcomic')
    downloader.download('JM1091443',config)
    translator = Translater(basedir='S:/JMcomic')
    translator.translate_2_pdf()