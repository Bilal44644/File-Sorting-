import os
import re
import shutil
from pathlib import Path
from typing import Dict
import PyPDF2

# Replace this with the path to your PDF files
PDF_DIRECTORY = r"C:\Users\Moe\Desktop\Bills 2023"
pdf_file = PDF_DIRECTORY




def extract_location_and_company(pdf_path: Path) -> Dict[str, str]:
    """Extracts the location and company from a PDF file.
    
    Args:
        pdf_path: Path to the PDF file.
        
    Returns:
        A dictionary with keys "location" and "company" and the corresponding values extracted from the PDF.
    """
    # Open the PDF file in read-only mode
    with open(pdf_path, "rb") as file:
       
        # Create a PDF object
        pdf = PyPDF2.PdfReader(file)
        
        read_pdf = PyPDF2.PdfReader(pdf_file)
        number_of_pages = read_pdf.getNumPages()
        page = read_pdf.pages[0]
        page_content = page.extractText()
        # Use regular expressions to extract the location and company
        location_pattern = r"([A-Z][a-z]+,? [A-Z]{2})"
        company_pattern = r"(Company: [\w\s]+)"
        
        location_match = re.search(location_pattern,text)
        company_match = re.search(company_pattern,text)
        
        location = location_match.group(1) if location_match else "Unknown"
        company = company_match.group(1).replace("Company: ", "") if company_match else "Unknown"
        
        return {"location": location, "company": company}

def sort_pdfs():
    """Sorts the PDF files in the PDF_DIRECTORY by location and company."""
    # Iterate over all PDF files in the directory
    for pdf_path in Path(PDF_DIRECTORY).glob("*.pdf"):
        # Extract the location and company from the PDF
        metadata = extract_location_and_company(pdf_path)
        location, company = metadata["location"], metadata["company"]
        
        # Create the target directory if it doesn't exist
        target_directory = Path(PDF_DIRECTORY) / location / company
        target_directory.mkdir(parents=True, exist_ok=True)
        
        # Move the PDF file to the target directory
        shutil.move(str(pdf_path), str(target_directory))

sort_pdfs()
