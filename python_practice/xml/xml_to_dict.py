import xmltodict
import requests


def download_file(url, save_path, chunk_size=128):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)

def main():
	url = "https://stepik.org/media/attachments/lesson/245571/map1.osm"
	save_path = "./files/map1.osm"
	download_file(url, save_path)

	fin = open(save_path, 'r', encoding='utf8')
	xml = fin.read()
	fin.close()

	parsedxml = xmltodict.parse(xml)
	print(parsedxml['osm']['node'][100]['@id'])

if __name__ == "__main__":
	main()