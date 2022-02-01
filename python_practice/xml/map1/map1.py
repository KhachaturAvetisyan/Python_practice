import xmltodict
import requests


def download_file(url, save_path, chunk_size=128):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)

def main():
    url = "https://stepik.org/media/attachments/lesson/245571/map1.osm"
    save_path = "./files/map1_.osm"
    # download_file(url, save_path)

    with open(save_path, 'r', encoding='utf8') as fd:
        xml = fd.read()

    dict = xmltodict.parse(xml)

    count_node = len(dict["osm"]["node"])
    count_tag = 0

    for i in dict["osm"]["node"]:
        if "tag" in i:
            count_tag += 1
    print(count_tag, count_node - count_tag)

if __name__ == "__main__":
    main()