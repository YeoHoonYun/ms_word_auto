import json
from pathlib import Path
from docx import Document

base_path = "base/"
file_path = "result/"
my_file = Path(file_path)
with open("info_list.json","r", encoding="utf-8") as f:
    info_list = json.loads(f.read())
# document = Document()
# if not my_file.is_file():
#     document.save(file_path + 'base.docx')
for info in info_list:
    document = Document(base_path + 'work_doc.docx')
    for p in document.paragraphs:
        if "{{{name}}}" in p.text:
            p.text = p.text.replace("{{{name}}}", info.get("name"))
        elif "{{{num}}}" in p.text:
            p.text = p.text.replace("{{{num}}}", info.get("num"))
        elif "{{{sub}}}" in p.text:
            p.text = p.text.replace("{{{sub}}}", info.get("sub"))
        document.save(file_path + 'complete_%s.docx' % (info.get("num")))