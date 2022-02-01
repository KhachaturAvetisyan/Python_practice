import requests 
import zipfile
import io
import xlrd
import time


def download_file(url, save_path, chunk_size=128):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)

def download_zip(url, save_path):
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(save_path)

def main():
    url = "https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip"
    save_path = "./files/rogaikopyta"

    # download_zip(url, save_path)

    dict = {}

    for i in range(1, 1001):
        wb = xlrd.open_workbook(f"{save_path}/{i}.xlsx")
        sheet_names = wb.sheet_names()
        sh = wb.sheet_by_name(sheet_names[0])

        row = sh.row_values(1, 1, 4)
        fio = row[0]
        salary = int(row[-1])
        # print(fio, salary)

        dict[fio] = salary

    with open("./files/result.txt", "w") as fd:
        print("#Start writing to file.")
        count = 0
        for i in sorted(dict):
            # print(i, dict[i])
            fd.write(f"{i} {dict[i]}\n")
            count += 1
            print(f"#Written to file {count}/1000.")
            time.sleep(0.01)

        print("#Finish of writing to file.")

if __name__ == "__main__":
    main()