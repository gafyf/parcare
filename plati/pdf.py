import io
from datetime import date 
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm, cm
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Frame
from reportlab.graphics.shapes import *
from django.http import FileResponse
import os
from django.conf import settings


image_path = os.path.join(settings.MEDIA_ROOT_LOGO, 'images', 'logo.jpg')

def factura_client_pdf(factura_client_dict):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4, bottomup=0)
    p.setTitle('Factura Fiscala')
    # p.rotate(45) p.rotate(-45)
    p.rotate(180)
    img = ImageReader(image_path)
    p.drawImage(img, -4*cm, -4*cm, width=30*mm, height=30*mm)
    p.rotate(-180)
    p.setFont('Helvetica', 16)
    p.setFillColor('red')
    p.drawString(7.5*cm, 2.5*cm, "FACTURA FISCALA")
    p.setStrokeColor(colors.red)
    p.line(7*cm, 2.6*cm, 13*cm, 2.6*cm) # linie orizontala 
    p.setFont('Helvetica', 11)
    p.drawString(9*cm, 3.5*cm, "Numar: " + str(factura_client_dict['numar']))
    p.setFillColorRGB(0,0,0)
    p.setFont('Helvetica', 12)
    dt_creare = date.today().strftime('%d-%m-%Y')
    p.drawString(17*cm, 4.5*cm, dt_creare)
    p.setStrokeColor(colors.black)
    p.line(1*cm, 5*cm, 20*cm, 5*cm)
    p.setFillColor('teal')
    p.drawString(2.5*cm, 5.8*cm, " Date Societate ")
    p.drawString(14*cm, 5.8*cm, ' Date Abonat')
    p.line(10*cm, 5.5*cm, 10*cm, 11*cm) # linie verticala
    p.setFillColor('black')
    p.setFont('Helvetica', 11)
    text_societate = p.beginText()
    text_societate.setTextOrigin(2.5*cm, 6.5*cm)
    text = [
        ' Parcare Zimbru',
        ' CIF: RO 948329843',
        ' Sediu: Iasi',
        ' Nr Reg Com: j46/87463/2020', 
        ' Cont: RO984BG7843786333',
        ' Banca: Transilvania',
        ' Capital Social: 8000', 
        ' Punct de lucru: Jud. Iasi, Iasi',
        ' Telefon: +40 232 735 983',
        ' Email: clienti@parcare.ro',
        ]
    for t in text:
        text_societate.textLine(t)
    p.drawText(text_societate)
    text_client = p.beginText()
    text_client.setTextOrigin(14*cm, 6.5*cm)
    text = [
        ' Nume: ' + str(factura_client_dict['nume']),
        ' Prenume: ' + str(factura_client_dict['prenume']),
        ' Cnp: ' + str(factura_client_dict['cnp']),
        ' Judet: ' + str(factura_client_dict['judet']), 
        ' Oras: ' + str(factura_client_dict['oras']),
        ' Adresa: ' + str(factura_client_dict['adresa']),
        ' Email: ' + str(factura_client_dict['email']), 
        ' Tel: ' + str(factura_client_dict['telefon']),
        ' Contract Nr: ' + str(factura_client_dict['contract_numar']),
        ]
    for t in text:
        text_client.textLine(t)
    p.drawText(text_client)
    st = []
    p.setFont('Helvetica', 12)
    p.setFillColor('black')
    p.drawString(2*cm, 12.6*cm, "CONTRACT ABONAMENT PARCARE" )
    if str(factura_client_dict['contract']) == 'public':
        abb = 500.00
    else:
        abb = 800.00
    p.drawString(17*cm, 12.6*cm, str(abb) + ' Lei')
    p.line(1*cm, 13*cm, 20*cm, 13*cm) # linie orizontala 
    p.drawString(2*cm, 26.5*cm, "PLATIT")
    p.line(1*cm, 25*cm, 20*cm, 25*cm) # linie orizontala 
    for s in st:
        p.beginText().textLine(s)
    f = Frame(1*cm, 12*cm, 19*cm, 16*cm, showBoundary=1)
    f.addFromList(st, p)
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, filename='factura.pdf')


def factura(factura_client_dict):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4, bottomup=0)
    p.setTitle('Factura Fiscala')
    # p.rotate(45) p.rotate(-45)
    p.rotate(180)
    img = ImageReader(image_path)
    p.drawImage(img, -4*cm, -4*cm, width=30*mm, height=30*mm)
    p.rotate(-180)
    p.setFont('Helvetica', 16)
    p.setFillColor('red')
    p.drawString(7.5*cm, 2.5*cm, "FACTURA FISCALA")
    p.setStrokeColor(colors.red)
    p.line(7*cm, 2.6*cm, 13*cm, 2.6*cm) # linie orizontala 
    p.setFont('Helvetica', 11)
    p.drawString(9*cm, 3.5*cm, "Numar: " + str(factura_client_dict['numar']))
    p.setFillColorRGB(0,0,0)
    p.setFont('Helvetica', 12)
    dt_creare = date.today().strftime("%d/%m/%Y")
    p.drawString(17*cm, 4.5*cm, dt_creare)
    p.setStrokeColor(colors.black)
    p.line(1*cm, 5*cm, 20*cm, 5*cm)
    p.setFillColor('teal')
    p.drawString(2.5*cm, 5.8*cm, " Date Societate ")
    p.drawString(14*cm, 5.8*cm, ' Date Abonat')
    p.line(10*cm, 5.5*cm, 10*cm, 11*cm) # linie verticala
    p.setFillColor('black')
    p.setFont('Helvetica', 11)
    text_societate = p.beginText()
    text_societate.setTextOrigin(2.5*cm, 6.5*cm)
    text = [
        ' Parcare Zimbru',
        ' CIF: RO 948329843',
        ' Sediu: Iasi',
        ' Nr Reg Com: j46/87463/2020', 
        ' Cont: RO984BG7843786333',
        ' Banca: Transilvania',
        ' Capital Social: 8000', 
        ' Punct de lucru: Jud. Iasi, Iasi',
        ' Telefon: +40 232 735 983',
        ' Email: clienti@parcare.ro',
        ]
    for t in text:
        text_societate.textLine(t)
    p.drawText(text_societate)
    text_client = p.beginText()
    text_client.setTextOrigin(14*cm, 6.5*cm)
    text = [
        ' Nume: ' + str(factura_client_dict['nume']),
        ' Prenume: ' + str(factura_client_dict['prenume']),
        ' Cnp: ' + str(factura_client_dict['cnp']),
        ' Judet: ' + str(factura_client_dict['judet']),
        ' Oras: ' + str(factura_client_dict['oras']),
        ' Adresa: ' + str(factura_client_dict['adresa']),
        ' Email: ' + str(factura_client_dict['email']),
        ' Tel: ' + str(factura_client_dict['telefon']),
        ' Contract Nr: ' + str(factura_client_dict['contract']).upper(),
        ]
    for t in text:
        text_client.textLine(t)
    p.drawText(text_client)
    st = []
    p.setFont('Helvetica', 12)
    p.setFillColor('black')
    p.drawString(2*cm, 12.6*cm, "CONTRACT ABONAMENT PARCARE" )
    if str(factura_client_dict['contract']) == 'public':
        abb = 500.00
    else:
        abb = 800.00
    p.drawString(17*cm, 12.6*cm, str(abb) + ' Lei')
    p.line(1*cm, 13*cm, 20*cm, 13*cm) # linie orizontala 
    p.drawString(2*cm, 26.5*cm, "PLATIT")
    p.line(1*cm, 25*cm, 20*cm, 25*cm) # linie orizontala 
    for s in st:
        p.beginText().textLine(s)
    f = Frame(1*cm, 12*cm, 19*cm, 16*cm, showBoundary=1)
    f.addFromList(st, p)
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, filename='factura.pdf')
