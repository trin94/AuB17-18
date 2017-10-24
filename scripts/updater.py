# -*- coding: UTF-8 -*-

import os
import sys
import glob
import shutil


class Updater:
    def __init__(self, cleanup_after=True, dir_src_tex="lectures-tex", dir_src_pdf="lectures-pdf"):
        self.dir_src = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        self.dir_tex = os.path.join(self.dir_src, dir_src_tex)
        self.dir_pdf = os.path.join(self.dir_src, dir_src_pdf)
        self.dir_tmp = os.path.join(self.dir_src, "out")

        self.cmd_produce_pdf = "pdflatex -file-line-error -interaction=nonstopmode -synctex=1 -output-format=pdf " \
                               "-output-directory={} {}"

        self.clean_after = cleanup_after

    def take_lecture_tex(self, pattern="*.tex"):
        return glob.glob(os.path.join(self.dir_tex, pattern))

    def take_lecture_pdf(self, pattern="*.pdf"):
        return glob.glob(os.path.join(self.dir_tmp, pattern))

    def __create_dir_temp(self):
        if not os.path.exists(self.dir_tmp):
            os.makedirs(self.dir_tmp)

    def remove_dir_temp(self):
        if os.path.exists(self.dir_tmp):
            shutil.rmtree(self.dir_tmp)

    def remove_existing_pdf(self, pattern="*.pdf"):
        files = glob.glob(os.path.join(self.dir_pdf, pattern))
        for f in files:
            os.remove(f)

    def produce_pdf(self, tex_source_list):
        self.__create_dir_temp()

        for lecture_tex in tex_source_list:
            os.system(self.cmd_produce_pdf.format(self.dir_tmp, lecture_tex), )

    def move_pdf(self, pdf_list):
        for pdf in pdf_list:
            shutil.move(pdf, self.dir_pdf)


def begin():
    args = sys.argv

    if len(args) == 2:
        arg_first = args[1]
        updater = Updater()

        if arg_first == "all":
            updater.remove_existing_pdf()
            updater.produce_pdf(updater.take_lecture_tex())
            updater.move_pdf(updater.take_lecture_pdf())
        elif arg_first.isdigit():
            lead_zero_arg = arg_first.zfill(2)
            name_pdf = "lecture" + lead_zero_arg + ".pdf"
            name_tex = "lecture" + lead_zero_arg + ".tex"

            updater.remove_existing_pdf(name_pdf)
            updater.produce_pdf(updater.take_lecture_tex(name_tex))
            updater.move_pdf(updater.take_lecture_pdf(name_pdf))

        updater.remove_dir_temp()


if __name__ == "__main__":
    begin()
