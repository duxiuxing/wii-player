# -- coding: UTF-8 --

import os
import shutil
import subprocess

from local_settings import LocalSettings
from lxml import etree


def save_id2name_dict_to_xml(id2name_dict, xml_file_path):
    game_list_elem = etree.Element("Game-List")

    for key, value in id2name_dict.items():
        attr_dict = {}
        attr_dict["id"] = key
        attr_dict["title"] = value

        game_elem = etree.SubElement(game_list_elem, "Game", attr_dict)

    doc = etree.ElementTree(game_list_elem)
    doc.write(xml_file_path, encoding="UTF-8",
              xml_declaration=True, pretty_print=True)


def convert_txt_to_xml(txt_file_path):
    txt_file = open(txt_file_path, 'r', encoding="UTF-8")

    txt_line = txt_file.readline()

    wii_id2name_dict = {}
    wiiware_id2name_dict = {}
    ngc_id2name_dict = {}
    is_ngc_game_id = False

    line_count = 0
    while txt_line:
        line_count = line_count + 1

        index = txt_line.find('=')
        if 7 == index:
            game_id = txt_line[:6]

            if game_id == "301E01":
                is_ngc_game_id = True

            if game_id != "TITLES":
                if is_ngc_game_id:
                    ngc_id2name_dict[game_id] = txt_line[9:-1]
                else:
                    wii_id2name_dict[game_id] = txt_line[9:-1]
        elif 5 == index:
            wiiware_id2name_dict[txt_line[:4]] = txt_line[7:-1]
        else:
            print(f"Skip ln {line_count}: {txt_line}")

        txt_line = txt_file.readline()

    txt_file.close()
    print(f"Total lines count: {line_count}")

    wii_xml_file_path = txt_file_path.replace("wiitdb.", "wii.")
    wii_xml_file_path = wii_xml_file_path.replace(".txt", ".xml")
    save_id2name_dict_to_xml(wii_id2name_dict, wii_xml_file_path)
    print(f"Total Wii games count: {len(wii_id2name_dict)}")

    wiiware_xml_file_path = txt_file_path.replace("wiitdb.", "wiiware.")
    wiiware_xml_file_path = wiiware_xml_file_path.replace(".txt", ".xml")
    save_id2name_dict_to_xml(wiiware_id2name_dict, wiiware_xml_file_path)
    print(f"Total WiiWare games count: {len(wiiware_id2name_dict)}")

    ngc_xml_file_path = txt_file_path.replace("wiitdb.", "ngc.")
    ngc_xml_file_path = ngc_xml_file_path.replace(".txt", ".xml")
    save_id2name_dict_to_xml(ngc_id2name_dict, ngc_xml_file_path)
    print(f"Total NGC games count: {len(ngc_id2name_dict)}")


convert_txt_to_xml(LocalSettings.wiitdb_en_txt)
convert_txt_to_xml(LocalSettings.wiitdb_zhcn_txt)
