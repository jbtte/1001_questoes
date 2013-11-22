from pdfminer.pdfparser import PDFDocument, PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter, process_pdf
from pdfminer.pdfdevice import PDFDevice, TagExtractor
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.cmapdb import CMapDB
from pdfminer.layout import LAParams
from cStringIO import StringIO
 
def scrap_pdf(path):
    """From http://stackoverflow.com/a/8325135/39040."""
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    process_pdf(rsrcmgr, device, fp)
    fp.close()
    device.close()
    str1 = retstr.getvalue()
    retstr.close()
    return str1



if __name__ == "__main__":

    path = "/Users/t316775/Downloads/Direito Processual Penal - CESPE.pdf"
    path1 = "/Users/t316775/Downloads/Direito Processo Penal - CESPE.txt"
    fp = open(path1, "w")
    str1 = scrap_pdf(path)
    fp.write(str1)

    fp.close()
        
    
