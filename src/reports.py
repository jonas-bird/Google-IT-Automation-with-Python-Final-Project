#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(content, heading, path_to_pdf):
    style = getSampleStyleSheet()
    report = SimpleDocTemplate(path_to_pdf)
    report_heading = Paragraph(heading, style['h1'])
    report_paragraphs = Paragraph(content, style['BodyText'])
    empty_line = Spacer(1,20)
    report.build([report_heading, empty_line, report_paragraphs, empty_line])
