import xmltodict
import requests


def download_file(url, save_path, chunk_size=128):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)

def main():
    url = "https://stepik.org/media/attachments/lesson/245681/map2.osm"
    save_path = "./files/map2.osm"
    # download_file(url, save_path)

    with open(save_path, 'r', encoding='utf8') as fd:
        xml = fd.read()

    mydict = xmltodict.parse(xml)

    # print(len(dict["osm"]["node"]))

    count_fuel = 0

    for i in mydict["osm"]["node"]:
        if "tag" in i:
            tags = i["tag"]
            if isinstance(tags, list):
                for tag in tags:
                    if "@v" in tag and tag["@v"] == "fuel" and len(i) > 1:
                        count_fuel += 1
            elif isinstance(tags, dict):
                if (tags['@v'])=='fuel':
                    count_fuel += 1

    print(count_fuel)

if __name__ == "__main__":
    main()