from fpdf import FPDF
import pandas


data  = pandas.read_csv("topics.csv",sep=",")
print(data)
pdf = FPDF(orientation="P",unit="mm",format="A4")
pdf.set_auto_page_break(False,0)

for columns, rows in data.iterrows():
    pdf.add_page()
    pdf.set_font(family="times", style="B", size=24)
    pdf.set_text_color(100,100,100) #RGB
    pdf.cell(w=0, h=12, txt=f"{rows['Topic']}", align="L", ln=1)
    pdf.line(10,22,200,22)

    pdf.ln(260)
    pdf.set_font(family="times", style="B", size=8)
    pdf.set_text_color(100, 100, 100)  # RGB
    pdf.cell(w=0, h=8, txt=f"{rows['Topic']}", align="R", ln=1)

    pages = int(rows["Pages"])
    for i in range(pages-1):
        pdf.add_page()
        pdf.ln(272)
        pdf.set_font(family="times", style="B", size=8)
        pdf.set_text_color(100, 100, 100)  # RGB
        pdf.cell(w=0, h=8, txt=f"{rows['Topic']}", align="R", ln=1)


pdf.output("output.pdf")