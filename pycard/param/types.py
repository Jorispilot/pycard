from .base import Param


__all__ = [
	"GIFParam",
	"CGMParam",
	"WMFParam",
	"BMPParam",
	"METParam",
	"PMGParam",
	"DIBParam",
	"PICTParam",
	"TIFFParam",
	"PSParam",
	"PDFParam",
	"JPEGParam",
	"MPEGParam",
	"MPEG2Param",
	"AVIParam",
	"QTIMEParam",
]


class TypeParam(Param):

    def __init__(self, valu):
        super().__init__("TYPE", value)


GIFParam   = TypeParam("GIF")
CGMParam   = TypeParam("CGM")
WMFParam   = TypeParam("WMF")
BMPParam   = TypeParam("BMP")
METParam   = TypeParam("MET")
PMGParam   = TypeParam("PMG")
DIBParam   = TypeParam("DIB")
PICTParam  = TypeParam("PICT")
TIFFParam  = TypeParam("TIFF")
PSParam    = TypeParam("PS")
PDFParam   = TypeParam("PDF")
JPEGParam  = TypeParam("JPEG")
MPEGParam  = TypeParam("MPEG")
MPEG2Param = TypeParam("MPEG2")
AVIParam   = TypeParam("AVI")
QTIMEParam = TypeParam("QTIME")

