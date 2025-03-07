from docxtpl import DocxTemplate

doc = DocxTemplate("invoice_template.docx")


invoice_list = [[2, "pen", 0.5, 1],
                [1,"paper", 5, 5],
                [2, "bag", 2, 4]]

doc.render({"name":"john",
            "phone": "555-5555",
             "invoice_list":invoice_list,
             "subtotal": 10,
             "salestax": "10%",
             "total":9
             })
doc.save("new_invoice.docx")