import jpype
import argparse

def hwp_extract(hwp_jar_path, file_path):

    ## jpype 시작
    jpype.startJVM(
        jpype.getDefaultJVMPath(),
        "-Djava.class.path={classpath}".format(classpath=hwp_jar_path),
        convertStrings=True,
        )

    ## java package 가져오기

    HWPReader_class = jpype.JPackage('kr.dogfoot.hwplib.reader')
    HWPFile_class = jpype.JPackage('kr.dogfoot.hwplib.object')
    TextExtrac_class = jpype.JPackage('kr.dogfoot.hwplib.tool.textextractor')
    HWPReader_ = HWPReader_class.HWPReader
    HWPFile_ = HWPFile_class.HWPFile
    TextExtractMethod_ = TextExtrac_class.TextExtractMethod
    TextExtractor_ = TextExtrac_class.TextExtractor

    # 한글 파일 읽기
    parser = HWPReader_.fromFile(file_path)

    # 한글 추출
    hwpText = TextExtractor_.extract(parser, TextExtractMethod_.InsertControlTextBetweenParagraphText)

    return hwpText


if __name__=="__main__":
    
    # 파라미터 파싱    
    parser = argparse.ArgumentParser(description='Hwp loader')
    parser.add_argument('--hwp_jar_path', type=str, default='./hwplib-1.1.6.jar', help='hwplib jar 위치')
    parser.add_argument('--file_path', type=str, default='./test.hwp', help='hwp 파일 경로')
    args = parser.parse_args()

    hwp_text = hwp_extract(args.hwp_jar_path, args.file_path)
    
    # print로 표준출력
    print(hwp_text)