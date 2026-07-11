from PyPDF2 import PdfReader, PdfWriter


def write_metadata(input_pdf, output_pdf, secret):

    reader = PdfReader(input_pdf)

    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    metadata = {}

    if reader.metadata:
        for key, value in reader.metadata.items():
            metadata[key] = str(value)

    metadata["/HiddenMessage"] = secret

    writer.add_metadata(metadata)

    with open(output_pdf, "wb") as f:
        writer.write(f)


def read_metadata(pdf_file):

    reader = PdfReader(pdf_file)

    metadata = reader.metadata

    if metadata is None:
        return ""

    return metadata.get("/HiddenMessage", "")
