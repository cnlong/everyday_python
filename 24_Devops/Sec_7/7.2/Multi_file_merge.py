import os
import glob
import PyPDF2


def get_all_files(path):
    """
    通过glob匹配找到所有的PDF文件
    :param path: 目录
    :return: 找到的PDF文件列表
    """
    all_pdfs = glob.glob("{0}/*.pdf".format(path))
    all_pdfs.sort(key=str.lower)
    return all_pdfs


def main():
    all_pdfs = get_all_files(".")
    if not all_pdfs:
        raise SystemExit("No PDf file found!")

    merger = PyPDF2.PdfFileMerger
    # 打开第一个文件作为起始文件
    with open(all_pdfs[0], 'rb') as first_obj:
        reader = PyPDF2.PdfFileReader(first_obj)
        merger.append(fileobj=first_obj, pages=(0, reader.getNumPages()))

    for pdf in all_pdfs[1:]:
        with open(pdf, 'rb') as obj:
            reader = PyPDF2.PdfFileReader(obj)
            merger.append(fileobj=first_obj, pages=(1, reader.getNumPages()))

    with open('merge-pdf.pdf', 'wb') as f:
        merger.write(f)


if __name__ == '__main__':
    main()