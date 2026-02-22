subjects = int(input("Enter number of subjects: "))
subject_data = []
for i in range(subjects):
   print(f"\nSubject {i+1}:")
   name = input("Enter subject name: ")
   lec_total = int(input("Enter total lectures: "))
   lec_attended = int(input("Enter attended lectures: "))
   lab_total = int(input("Enter total labs: "))
   lab_attended = int(input("Enter attended labs: "))
   subject_data.append({
      "name": name,
      "lec_total": lec_total,
      "lec_attended": lec_attended,
      "lab_total": lab_total,
      "lab_attended": lab_attended
   })
print("\n")
for subject in subject_data:
   name = subject["name"]
   lec_total = subject["lec_total"]
   lec_attended = subject["lec_attended"]
   lab_total = subject["lab_total"]
   lab_attended = subject["lab_attended"]
   
   print(f"\nsubject:-{name}")
   #Lec
   if lec_total>0:
      lec_percentage = round(((lec_attended / lec_total) * 100),2)
      print(f"{name}-lecture:{lec_percentage}%")
      if lec_percentage >= 75:
         x = 0
         while ((lec_attended / (lec_total + x)) * 100) >= 75:
            x += 1
         print(f"You can bunk {x-1} lectures in {name}.")
      else:
         x = 0
         while (((lec_attended + x) / (lec_total + x)) * 100) < 75:
            x += 1
         print(f"You need to attend {x} lectures in {name}.")
   else:
      print(f"no lecture component for subject {name}")

    #lab
   if lab_total>0:
      lab_percentage = round(((lab_attended / lab_total) * 100),2)   
      print(f"{name}-lab:{lab_percentage}%")   
      if lab_percentage >= 75:
         x = 0
         while ((lab_attended / (lab_total + x)) * 100) >= 75:
            x += 1
         print(f"You can bunk {x-1} labs in {name}.")
      else:
         x = 0
         while (((lab_attended + x) / (lab_total + x)) * 100) < 75:
            x += 1
         print(f"You need to attend {x} labs in {name}.")
   else:
      print(f"no lab component for subject {name}")