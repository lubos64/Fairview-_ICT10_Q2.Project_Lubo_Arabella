from pyscript import display, document

def gen_w_ave(e):
   fname = (document.getElementById("first_name").value)
   lname = (document.getElementById("last_name").value)
   eng = float(document.getElementById("eng").value)
   sci = float(document.getElementById("sci").value)
   ict = float(document.getElementById("ict").value)
   math = float(document.getElementById("mat").value)
   filipo = float(document.getElementById("fil").value)
   pe = float(document.getElementById("pe").value)

   
   w_sum = (eng * 5 + sci * 5 + ict * 2 + math * 5 + filipo * 3 + pe * 1)
   total_un = (5*3) + 3 + 2 + 1
   gwa = w_sum / total_un

   

   summery = f"""{subjects[0]}: {eng:.0f}
   {subjects[1]}: {sci:.0f}
   {subjects[2]}: {ict:.0f}
   {subjects[3]}: {math:.0f}
   {subjects[4]}: {filipo:.0f}
   """
   display(f'Name: {first_name}{last_name}', target = "student_info")
   display(summary, target = 'summary')
   display(f'Your General Weighted Average is {gwa:.2f}', target = 'output')

