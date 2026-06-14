def create_table(data):
    rows = data.split(";")          # split rows
    html = "<table border='1'>"

    # First row = headers
    headers = rows[0].split(",")

    html += "<tr>"
    for header in headers:
        html += f"<th>{header}</th>"
    html += "</tr>"

    # Remaining rows = table data
    for row in rows[1:]:
        cells = row.split(",")

        html += "<tr>"
        for cell in cells:
            html += f"<td>{cell}</td>"
        html += "</tr>"

    html += "</table>"

    return html


data = "Name,Age,Role;Bob,25,Developer;Alice,30,Designer"
print(create_table(data))