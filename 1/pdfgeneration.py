from fpdf import FPDF
pdf = FPDF ("P", 'cm', (10,15))
pdf.add_page()
pdf.set_font('courier', '' , size= 16)
pdf.set_text_color(0,255,0)
pdf.set_fill_color(150,10,140)
pdf.cell(10,5 ,txt='Hello!', align='C', border=1, fill=1)
pdf.image('images/skelet.png', h=0,w=10,x=0,y=5)
pdf.output('pdf/new_pdf.pdf')
pdf.add_action()