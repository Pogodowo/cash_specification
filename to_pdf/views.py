from django.shortcuts import render
from django.http import JsonResponse,response
from specification.calculation_dict_template import calculation_dict_template,calculation_dict,text_calc_dict,calculation
from specification.text_sum import text_sum
from .sumstr import sumstr,sumpdf
#================================================================================================================
import reportlab
import io
from django.http import FileResponse,response
from reportlab.pdfgen import canvas
#============================================================
from reportlab.platypus import SimpleDocTemplate,Table,TableStyle,Paragraph
from reportlab.lib.pagesizes import letter,A4
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import mm,cm
from django.conf import settings
#==================================

def to_pdf(request):
    test='-'
    if request.method == "POST":

        inputs={}
        calculations={}
        sum_all=0
        text_sum_all=''


        for key in calculation_dict_template:
             inputs[key]=request.POST.get(key)
        for key,value in calculation_dict.items():
            calculations[key]=calculation(request.POST.get(value),float(value[6:]))
            sum_all+=float(calculation(request.POST.get(value),float(value[6:])))
        for key,value in text_calc_dict.items():
            calculations[key]=text_sum(calculations[value])
        sum_all=round(sum_all,2)
        text_sum_all=text_sum(str(sum_all))
        t = [['nominał', 'ilość sztuk', 'suma zł', 'suma słownie'], ['500zł', request.POST.get("input-500"), calculations['sum-500'], calculations['sumtext-500']], ['200zł', request.POST.get("input-200"), calculations['sum-200'], calculations['sumtext-200']],
             ['100zł', request.POST.get("input-100"), calculations['sum-100'], calculations['sumtext-100']], ['50zł', request.POST.get("input-50"), calculations['sum-50'], calculations['sumtext-50']], ['20zł', request.POST.get("input-20"), calculations['sum-20'], calculations['sumtext-20']], ['10zł', request.POST.get("input-10"), calculations['sum-10'], calculations['sumtext-10']],
             ['5zł',request.POST.get("input-5"), calculations['sum-5'], calculations['sumtext-5']], ['2zł', request.POST.get("input-2"), calculations['sum-2'], calculations['sumtext-2']], ['1zł', request.POST.get("input-1"), calculations['sum-1'], calculations['sumtext-1']], ['0,5zł', request.POST.get("input-0.5"), calculations['sum-0.5'], calculations['sumtext-0.5']],
             ['0,2zł',request.POST.get("input-0.2"), calculations['sum-0.2'], calculations['sumtext-0.2']],
             ['0,1zł', request.POST.get("input-0.1"), calculations['sum-0.1'], calculations['sumtext-0.1']], ['0,05zł', request.POST.get("input-0.05"), calculations['sum-0.05'], calculations['sumtext-0.05']], ['0,02zł',request.POST.get("input-0.02"), calculations['sum-0.02'], calculations['sumtext-0.02']], ['0,01zł', request.POST.get("input-0.01"), calculations['sum-0.01'], calculations['sumtext-0.01']]]

        a = 0
        for i in t:
            a = a + i[3].count('\n')
        b = 390
        c = 370

        buffer = io.BytesIO()

        p = canvas.Canvas(buffer, pagesize=A4)

        reportlab.rl_config.TTFSearchPath.append(str(settings.BASE_DIR) + '/to_pdf')
        pdfmetrics.registerFont(TTFont('polishFont', 'AbhayaLibre-Regular.ttf'))
        # ======================================================================================
        p.setFont('polishFont', 32)
        p.drawString(130, 780, "Specyfikacja nominałowa")

        # =============================================rysowanie dat=========================================


        # ======================================tabela==============================================

        width = 500
        height = 500
        x = 30
        y = b - (a * 15)
        table = Table(t, colWidths=[25 * mm, 25 * mm, 30 * mm, 110 * mm])

        ts = TableStyle([('GRID', (0, 0), (-1, -1), 1, colors.black), ('FONT', (0, 0), (-1, -1), 'polishFont', 13),
                         ('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('VALIGN', (0, 0), (-1, -1), 'TOP')])
        table.setStyle(ts)

        table.wrapOn(p, width, height)
        table.drawOn(p, x, y)
        # ================suma==============================================================
        y = c - (a * 15)
        p.setFont('polishFont', 15)
        p.drawString(100, y, 'łącznie:  '+str(sum_all)+' zł.')
        z = p.beginText()
        z.setFont('polishFont', 14)
        z.setCharSpace(1)
        z.setTextOrigin(230, y)
        text_sum_all_brakelines = sumpdf(text_sum_all)
        z.textLines(  text_sum_all_brakelines)

        p.drawText(z)

        # ==========================================================================================
        p.showPage()
        p.save()
        buffer.seek(0)

        return FileResponse(buffer, as_attachment=True, filename='specyfikacja.pdf')










