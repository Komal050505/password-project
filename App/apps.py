import PyPDF2
import logging

# Configure logging
logging.basicConfig(filename='main.log',
                    level=logging.DEBUG,
                    filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')


def add_password_to_pdf(input_pdf_path, output_pdf_path, password):
    """
    Adds a password to an existing PDF file and saves it as a new file.

    Args:
        input_pdf_path (str): The path to the input PDF file.
        output_pdf_path (str): The path where the password-protected PDF will be saved.
        password (str): The password to be set for the output PDF.

    Raises:
        FileNotFoundError: If the input PDF file is not found.
        Exception: For any general errors during PDF processing or writing.
    """
    try:
        # Open the input PDF file in read-binary mode
        with open(input_pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            # Create a PDF writer object
            pdf_writer = PyPDF2.PdfWriter()

            # Loop through each page and add it to the writer object
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)

            # Set a password for the PDF
            pdf_writer.encrypt(password)

            # Save the protected PDF to the output file
            with open(output_pdf_path, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)

        logging.info(f"PDF successfully protected with password and saved as '{output_pdf_path}'.")

    except FileNotFoundError as fnf_error:
        logging.error(f"File not found: '{input_pdf_path}'. Error: {fnf_error}")
        raise FileNotFoundError(f"Error: The file '{input_pdf_path}' was not found.") from fnf_error

    except Exception as e:
        logging.error(f"An error occurred while processing the PDF: {e}")
        raise Exception(f"An error occurred while processing the PDF: {e}") from e


if __name__ == "__main__":
    input_pdf_path = "C:/Users/lenovo/Downloads/gpCTVFVX7p.pdf"  # Replace with your input PDF file path
    output_pdf_path = "C:/Users/lenovo/Downloads/gpCTVFVX7p1.pdf"  # Replace with your desired output PDF file path
    password = "KATT0505"  # Replace with your desired password

    add_password_to_pdf(input_pdf_path, output_pdf_path, password)
