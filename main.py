import re
from pprint import pprint


def main():
    log_file = "D:\\Programming\\access.log.txt"
    count=0

    with open(log_file, mode="r") as file:
        text = file.read()
        result1 = re.findall(r'\[23/Mar/2009:06:29:[1-9]\d \+0100] "GET /\w*[./]\w* \w*/\d\.\d" [^200]\w*', text)
        result2 = re.findall(r'\[23/Mar/2009:06:[3-5]\d:\d\d \+0100] "GET /\w*[./]\w* \w*/\d\.\d" [^200]\w*', text)
        result3 = re.findall(r'\[23/Mar/2009:07:\d\d:\d\d \+0100] "GET /\w*[./]\w* \w*/\d\.\d" [^200]\w*', text)
        result4 = re.findall(r'\[23/Mar/2009:08:[0-1][0-3]:[0-3][0-2] \+0100] \+0100] "GET /\w*[./]\w* \w*/\d\.\d" [^200]\w*', text)

        result5 = re.findall(r'\[23/Mar/2009:06:29:[1-9]\d \+0100] "GET / \w*/\d\.\d" [^200]\w*', text)
        result6 = re.findall(r'\[23/Mar/2009:06:[3-5]\d:\d\d \+0100] "GET / \w*/\d\.\d" [^200]\w*', text)
        result7 = re.findall(r'\[23/Mar/2009:07:\d\d:\d\d \+0100] "GET / \w*/\d\.\d" [^200]\w*', text)
        result8 = re.findall(r'\[23/Mar/2009:08:[0-1][0-3]:[0-3][0-2] \+0100] "GET / \w*/\d\.\d" [^200]\w*', text)
        
    result = []
    result.extend(result1)
    result.extend(result2)
    result.extend(result3)
    result.extend(result4)
    result.extend(result5)
    result.extend(result6)
    result.extend(result7)
    result.extend(result8)

    for item in result:
        count+=1
        result.sort()

    print(f"Unaccomplished GET requests: {count}")
    pprint(result)

if __name__ == '__main__':
    main()
