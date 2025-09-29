edvs = []

contatos = [
    {
        "nome": "Lorenzo",
        "telefone": "19983659999",
        "edv": "1234",
        "email": "lorenzo@teste"
    },
    {
        "nome": "Wilson",
        "telefone": "1998070707",
        "edv": "9999",
        "email": "wilson@email"
    }
]

for i in contatos:
    edvs.append(i['edv'])

edv = input("edv: ")

index = edvs.index(edv)

print(contatos[index])


import reportlab.lib.pagesizes as pagesizes

from reportlab.pdfgen import canvas

page_size = pagesizes.letter

canvas = canvas.Canvas('example.pdf')

canvas.setPageSize(page_size)

text = str(contatos)

canvas.drawString(100, 750, text)

canvas.showPage()
canvas.save()