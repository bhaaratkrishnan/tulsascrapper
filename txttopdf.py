def texttopdf(file):
    f=open(file, "r", encoding="unicode_escape")
    from fpdf import FPDF
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=11)
    for i in f:
        pdf.cell(200,10,txt=i, ln=1, align="L")
    pdf.output(file[:-4]+".pdf")
    f.close()

import os
main_dir="tulsa"
for i in os.listdir("tulsa"):
    year_dir=main_dir+"/"+i
    print(year_dir)
    for j in os.listdir(year_dir):
        file_dir=year_dir+"/"+j
        texttopdf(file_dir)