"""Uso: python generar_datos.py archivo.xlsx (requiere openpyxl). No publica el Excel."""
import json, sys
from pathlib import Path
import openpyxl

w = openpyxl.load_workbook(sys.argv[1], data_only=True)
s, t = w['2026'], w['TMO TRACK-CISCO 2026']
months = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
records = []
month = None
for col in range(2, 117):
    v=s.cell(1,col).value
    if isinstance(v,str) and v.title() in months: month=months.index(v.title())
    course=s.cell(2,col).value
    if not course: continue
    value=s.cell(84,col).value
    if not isinstance(value,(int,float)): raise ValueError('Falta total numérico: '+str(col))
    records.append(dict(id='tmo-'+str(col),month=month,line='TMO',course=str(course).strip(),value=value))
for row in range(3,15):
    if all(t.cell(row,c).value is None for c in range(2,22)): continue
    for col in range(2,22):
        v=t.cell(row,col).value
        if v in (None,'-'): continue
        if not isinstance(v,(int,float)): raise ValueError('Valor no numérico')
        records.append(dict(id='auto-'+str(col),month=row-3,line='Cisco' if col<9 else 'TMO Track',course=' '.join(str(t.cell(2,col).value).split()),value=v))
for m in range(10):
    for line,col in [('TMO',2),('TMO Track',3),('Cisco',4)]:
        actual=sum(r['value'] for r in records if r['month']==m and r['line']==line)
        expected=t.cell(m+19,col).value
        assert actual==expected, (months[m],line,actual,expected)
data=dict(year=2026,source=Path(sys.argv[1]).name,months=months,records=records)
dest=Path(__file__).parent/'docs'/'index.html'
template=(Path(__file__).parent/'plantilla.html').read_text()
dest.parent.mkdir(exist_ok=True)
dest.write_text(template.replace('__DATA__',json.dumps(data,ensure_ascii=False).replace('</','<\\/')))
print('Validado:',sum(r['value'] for r in records),'inscripciones;',len(set(r['id'] for r in records)),'ofertas en el catálogo')
