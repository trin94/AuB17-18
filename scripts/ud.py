# -*- coding: UTF-8 -*-

import os
import sys
import glob
import shutil

DEBUG: bool = False


class File:
    def __init__(self, lec_nr: str, path_list):
        self.valid = True if path_list else False
        self.lec_nr = lec_nr
        self.path = path_list[0] if self.valid else ""
        self.file_name = os.path.basename(self.path) if self.valid else ""


class PdfFile(File):
    def __init__(self, lec_nr: str, path_list):
        super().__init__(lec_nr, path_list)

    def move(self):
        if self.valid:
            FileSystem.remove_existing_pdf(self.lec_nr)
            FileSystem.move_pdf(self.path)


class DviFile(File):
    def __init__(self, lec_nr: str, path_list):
        super().__init__(lec_nr, path_list)
        self.cmd_produce = "dvipdf {}"

    def to_pdf(self) -> PdfFile:
        if self.valid:
            FileSystem.create_dir_temp()
            os.system(self.cmd_produce.format(os.path.join(FileSystem.dir_tmp, self.file_name), self.path), )
        return FileSystem.get_pdf_file(self.lec_nr)


class TexFile(File):
    def __init__(self, lec_nr: str, path_list):
        super().__init__(lec_nr, path_list)
        self.cmd_produce = "latex -file-line-error -interaction=nonstopmode -synctex=1 -output-format=dvi " \
                           "-output-directory={} {}"

        if not self.valid:
            print("No file found for lecture {}".format(self.lec_nr))

    def to_dvi(self) -> DviFile:
        if self.valid:
            FileSystem.create_dir_temp()
            os.system(self.cmd_produce.format(FileSystem.dir_tmp, self.path), )
        return FileSystem.get_dvi_file(self.lec_nr)


class FileSystem:
    dir_src = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    dir_tex = os.path.join(dir_src, "lectures-tex")
    dir_pdf = os.path.join(dir_src, "lectures-pdf")
    dir_tmp = os.path.join(dir_src, "out")
    dir_scripts = os.path.join(dir_src, "scripts")

    @staticmethod
    def take_tex_file(lecture_nr: str) -> TexFile:
        file_path = os.path.join(FileSystem.dir_tex, ''.join(["lecture", lecture_nr.zfill(2), ".tex"]))
        return TexFile(lecture_nr, glob.glob(file_path))

    @staticmethod
    def get_dvi_file(lecture_nr: str) -> DviFile:
        file_path = os.path.join(FileSystem.dir_tmp, ''.join(["lecture", lecture_nr.zfill(2), ".dvi"]))
        return DviFile(lecture_nr, glob.glob(file_path))

    @staticmethod
    def get_pdf_file(lecture_nr: str) -> PdfFile:
        file_path = os.path.join(FileSystem.dir_scripts, ''.join(["lecture", lecture_nr.zfill(2), ".pdf"]))
        return PdfFile(lecture_nr, glob.glob(file_path))

    @staticmethod
    def create_dir_temp():
        if not os.path.exists(FileSystem.dir_tmp):
            os.makedirs(FileSystem.dir_tmp)

    @staticmethod
    def remove_existing_pdf(lecture_nr: str):
        files = glob.glob(os.path.join(FileSystem.dir_pdf, ''.join(["lecture", lecture_nr.zfill(2), ".pdf"])))
        for f in files:
            os.remove(f)

    @staticmethod
    def move_pdf(path: str):
        if os.path.exists(path):
            shutil.move(path, FileSystem.dir_pdf)

    @staticmethod
    def cleanup():
        if os.path.exists(FileSystem.dir_tmp):
            shutil.rmtree(FileSystem.dir_tmp)


def begin():
    args = sys.argv

    if len(args) == 2:
        arg_first = args[1]

        if not tools_available():
            print("Please try the \'updater.py\' script: python updater.py {}".format(arg_first))
            return

        if arg_first.isdigit():
            FileSystem.take_tex_file(arg_first).to_dvi().to_pdf().move()

            if not DEBUG:
                FileSystem.cleanup()

        elif arg_first == "all":
            print("Building all files is not supported currently.".format(arg_first))
        else:
            print("Use python ud.py <digit> to build a file.")


def tools_available() -> bool:
    tools = ["latex", "dvipdf"]
    passed: bool = True

    for tool in tools:
        if shutil.which(tool) is None:
            passed = False
            print("Tool \'{}\' is missing ...".format(tool))

    return passed


if __name__ == "__main__":
    begin()
