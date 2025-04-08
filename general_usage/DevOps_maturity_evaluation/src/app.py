from flask import Flask, render_template, request
app = Flask(__name__)


groups=[]
chapters=[]

def import_sills_enhanced():

    import csv
    with open("values.csv", "r") as csvfile:
        data= []
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            data.append(row)

    final_datas=[]

    for line in data:
    
        if not line['Group_id'] in groups:
           groups.append(line['Group_id']) 
           final_datas.append({'Group_id':line['Group_id'], 'Group_title': line['Group_title'],'chapters':[]}) 


    for row in final_datas:
        for line in data:
            if line['Group_id'] == row['Group_id']:
                if not line['Chapter_id'] in chapters:
                    chapters.append(line['Chapter_id']) 
                    row['chapters'].append({'Chapter_id':line['Chapter_id'], 'Chapter_title': line['Chapter_title'],'levels':[]}) 

    for row in final_datas:
        for row_chapter in row['chapters']:
            for line in data:
                if line['Group_id'] == row['Group_id']:
                    if line['Chapter_id'] == row_chapter['Chapter_id']:
                        row_chapter['levels'].append({'Level_id':line['Level_id'], 'Level_qualifier': line['Level_qualifier']}) 



        
    return final_datas
final_datas=import_sills_enhanced()



def parse_int(s, base=10, val=0)-> int:
 if s.isdigit():
  return int(s, base)
 else:
  return val


@app.route('/')
def index():
    return render_template('index.html', data = {'evaluate_data':final_datas})


@app.route('/calculate/', methods=('GET', 'POST'))
def calculate():
    if request.method == 'POST':
        cumul=[]
        fields=[]
        values=[]
        for group in final_datas:
            sum =0
            for chapter in group['chapters']:
                form_field=f'chapter_{chapter["Chapter_id"]}'
                value = request.form[form_field]
                result =parse_int(value)
                print(f'{form_field} : {value} - {result}')
                sum +=result
            cumul.append({"field":group["Group_title"],"value":sum})
            fields.append(group["Group_title"])
            values.append(sum)

    fields.append(fields[0])
    values.append(values[0])

    return render_template('calculate.html', data = {'fields':fields,'values':values})

