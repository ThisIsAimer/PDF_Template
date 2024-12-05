from fpdf import FPDF

pdf = FPDF(orientation="L",unit="mm",format="A4")



pdf.add_page()
pdf.set_font(family="times",style="B",size=12)
#txt is written as text in actual fpdf documentation but doesn't work for some reason
pdf.cell(w=0,h=12,txt="hello there!",align="L",ln=1,border=1)

pdf.set_font(family="times",style="B",size=10)
pdf.cell(w=0,h=12,txt="hi there",align="R",ln=1)

pdf.add_page()
pdf.set_font(family="times",style="B",size=12)

pdf.cell(w=0,h=12,txt="next page!",align="L",ln=0,border=1)

pdf.set_font(family="times",style="B",size=10)
pdf.cell(w=0,h=12,txt="hi there",align="R",ln=1)
pdf.output("learn.pdf")