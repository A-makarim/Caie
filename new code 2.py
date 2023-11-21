import tkinter as tk
import webbrowser
import io
import requests
from pypdf import PdfReader
import time
prompt=""
import tkinter as tk
from tkinter import ttk



from typing import Dict, Union
from io import BytesIO

errorcode = ""

subjects = [
    {"name": "Physics", "code": "9702"},
    {"name": "Chemistry", "code": "9701"},
    {"name": "Mathematics - Further", "code": "9231"}
    # Add more subjects here
]

paperchar = ""
variantchar = ""
papernum = ""

url="no"
urlqp="qp"
urlms="ms"
urlgt="gt"

reportfound=False

prefix="20"
const="_er.pdf"
subcode=None

prompt = ""

selected_subject=""


def subject_selected(event):
    selected_subject = subject.get()
    subject_code = next((sub["code"] for sub in subjects if sub["name"] == selected_subject), "")
    print(f"Selected Subject: {selected_subject} (Code: {subject_code})")

def on_year_select(event):
    selected_year = year_combo.get()
    year.set(selected_year[-2:])
    print("Selected year:", year.get())

def toggle_feb_march():
    if feb_march_var.get() == 1:
        may_june_var.set(0) 
        oct_nov_var.set(0)
        month.set("m")
        print("Feb/March button ON")
    else:
        month.set("")
        print("Feb/March button OFF")

def toggle_may_june():
    if may_june_var.get() == 1:
        oct_nov_var.set(0)
        feb_march_var.set(0)
        month.set("s")
        print("May/June button ON")
    else:
        month.set("")
        print("May/June button OFF")

def toggle_oct_nov():
    if oct_nov_var.get() == 1:
        may_june_var.set(0)
        feb_march_var.set(0)
        month.set("w")
        print("Oct/Nov button ON")
    else:
        month.set("")
        print("Oct/Nov button OFF")

def toggle_paper1():
    global paperchar
    if paper1_var.get() == 1:
        paper2_var.set(0)
        paper3_var.set(0)
        paper4_var.set(0)
        paper5_var.set(0)
        print("Paper 1 button ON")
        paperchar= "1"
    else:
        print("Paper 1 button OFF")

def toggle_paper2():
    global paperchar
    if paper2_var.get() == 1:
        paper1_var.set(0)
        paper3_var.set(0)
        paper4_var.set(0)
        paper5_var.set(0)
        print("Paper 2 button ON")
        paperchar= "2"
    else:
        print("Paper 2 button OFF")

def toggle_paper3():
    global paperchar
    if paper3_var.get() == 1:
        paper1_var.set(0)
        paper2_var.set(0)
        paper4_var.set(0)
        paper5_var.set(0)
        print("Paper 3 button ON")
        paperchar= "3"
    else:
        print("Paper 3 button OFF")

def toggle_paper4():
    global paperchar
    if paper4_var.get() == 1:
        paper1_var.set(0)
        paper2_var.set(0)
        paper3_var.set(0)
        paper5_var.set(0)
        print("Paper 4 button ON")
        paperchar= "4"
    else:
        print("Paper 4 button OFF")

def toggle_paper5():
    global paperchar
    if paper5_var.get() == 1:
        paper1_var.set(0)
        paper2_var.set(0)
        paper3_var.set(0)
        paper4_var.set(0)
        print("Paper 5 button ON")
        paperchar= "5"
    else:
        print("Paper 5 button OFF")

def toggle_variant1():
    global variantchar
    if variant1_var.get() == 1:
        variant2_var.set(0)
        variant3_var.set(0)
        variant4_var.set(0)
        variant5_var.set(0)
        print("Variant 1 button ON")
        variantchar="1"
    else:
        print("Variant 1 button OFF")

def toggle_variant2():
    global variantchar
    if variant2_var.get() == 1:
        variant1_var.set(0)
        variant3_var.set(0)
        variant4_var.set(0)
        variant5_var.set(0)
        print("Variant 2 button ON")
        variantchar="2"
    else:
        print("Variant 2 button OFF")

def toggle_variant3():
    global variantchar
    if variant3_var.get() == 1:
        variant1_var.set(0)
        variant2_var.set(0)
        variant4_var.set(0)
        variant5_var.set(0)
        print("Variant 3 button ON")
        variantchar="3"
    else:
        print("Variant 3 button OFF")

def toggle_variant4():
    global variantchar
    if variant4_var.get() == 1:
        variant1_var.set(0)
        variant2_var.set(0)
        variant3_var.set(0)
        variant5_var.set(0)
        print("Variant 4 button ON")
        variantchar="4"
    else:
        print("Variant 4 button OFF")

def toggle_variant5():
    global variantchar
    if variant5_var.get() == 1:
        variant1_var.set(0)
        variant2_var.set(0)
        variant3_var.set(0)
        variant4_var.set(0)
        print("Variant 5 button ON")
        variantchar="5"
    else:
        print("Variant 5 button OFF")






def create_table(root, rows, cols):
    table_entries = []
    for i in range(rows):
        row_entries = []
        for j in range(cols):
            entry = ttk.Entry(table_frame, width=10)
            entry.grid(row=i+1, column=j+1, padx=2, pady=2)
            row_entries.append(entry)
        table_entries.append(row_entries)
    return table_entries


root = tk.Tk()

subject = tk.StringVar()
year = tk.StringVar()
month = tk.StringVar()

variant1_var = tk.IntVar()
variant2_var = tk.IntVar()
variant3_var = tk.IntVar()
variant4_var = tk.IntVar()
variant5_var = tk.IntVar()

paper1_var = tk.IntVar()
paper2_var = tk.IntVar()
paper3_var = tk.IntVar()
paper4_var = tk.IntVar()
paper5_var = tk.IntVar()





# Create a frame for the top row buttons (Physics and Chemistry)
subject_label = tk.Label(root, text="Subject:")
subject_label.pack()

subject_dropdown = ttk.Combobox(root, textvariable=subject, state="readonly")
subject_dropdown["values"] = [sub["name"] for sub in subjects]
subject_dropdown.bind("<<ComboboxSelected>>", subject_selected)
subject_dropdown.pack()

year_frame = ttk.Frame(root)
year_frame.pack(fill=tk.X)

year_instruction = tk.Label(year_frame, text="Enter year", fg='gray')
year_instruction.pack(side=tk.LEFT, padx=10, pady=5)

year_values = [str(year) for year in range(2005, 2024)]
year_combo = ttk.Combobox(year_frame, values=year_values, state="readonly")
year_combo.bind("<<ComboboxSelected>>", on_year_select)
year_combo.pack(fill=tk.X, padx=10, pady=5)

def on_year_select(event):
    selected_year = year_combo.get()
    year.set(selected_year[-2:])
    print("Selected year:", year.get())
    year_instruction.config(fg='black')

def on_year_focus_out(event):
    if year_combo.get() == '':
        year_instruction.config(fg='gray')

year_combo.bind('<FocusIn>', on_year_select)
year_combo.bind('<FocusOut>', on_year_focus_out)





month_frame = ttk.Frame(root)
month_frame.pack(fill=tk.X)

feb_march_var = tk.IntVar()
feb_march_button = tk.Checkbutton(month_frame, text="Feb/March", variable=feb_march_var, command=toggle_feb_march)
feb_march_button.pack(side=tk.LEFT, fill=tk.X, expand=True)

may_june_var = tk.IntVar()
may_june_button = tk.Checkbutton(month_frame, text="May/June", variable=may_june_var, command=toggle_may_june)
may_june_button.pack(side=tk.LEFT, fill=tk.X, expand=True)

oct_nov_var = tk.IntVar()
oct_nov_button = tk.Checkbutton(month_frame, text="Oct/Nov", variable=oct_nov_var, command=toggle_oct_nov)
oct_nov_button.pack(side=tk.LEFT, fill=tk.X, expand=True)

paper_frame = ttk.Frame(root)
paper_frame.pack(fill=tk.X)

paper1_var = tk.IntVar()
paper1_button = tk.Checkbutton(paper_frame, text="Paper 1", variable=paper1_var, command=toggle_paper1)
paper1_button.pack(side=tk.LEFT, fill=tk.X, expand=True)

paper2_var = tk.IntVar()
paper2_button = tk.Checkbutton(paper_frame, text="Paper 2", variable=paper2_var, command=toggle_paper2)
paper2_button.pack(side=tk.LEFT, fill=tk.X, expand=True)

paper3_var = tk.IntVar()
paper3_button = tk.Checkbutton(paper_frame, text="Paper 3", variable=paper3_var, command=toggle_paper3)
paper3_button.pack(side=tk.LEFT, fill=tk.X, expand=True)

paper4_var = tk.IntVar()
paper4_button = tk.Checkbutton(paper_frame, text="Paper 4", variable=paper4_var, command=toggle_paper4)
paper4_button.pack(side=tk.LEFT, fill=tk.X, expand=True)

paper5_var = tk.IntVar()
paper5_button = tk.Checkbutton(paper_frame, text="Paper 5", variable=paper5_var, command=toggle_paper5)
paper5_button.pack(side=tk.LEFT, fill=tk.X, expand=True)

variant_frame = ttk.Frame(root)
variant_frame.pack(fill=tk.X)

variant1_var = tk.IntVar()
variant1_button = tk.Checkbutton(variant_frame, text="Variant 1", variable=variant1_var, command=toggle_variant1)
variant1_button.pack(side=tk.LEFT, fill=tk.X, expand=True)

variant2_var = tk.IntVar()
variant2_button = tk.Checkbutton(variant_frame, text="Variant 2", variable=variant2_var, command=toggle_variant2)
variant2_button.pack(side=tk.LEFT, fill=tk.X, expand=True)

variant3_var = tk.IntVar()
variant3_button = tk.Checkbutton(variant_frame, text="Variant 3", variable=variant3_var, command=toggle_variant3)
variant3_button.pack(side=tk.LEFT, fill=tk.X, expand=True)

variant4_var = tk.IntVar()
variant4_button = tk.Checkbutton(variant_frame, text="Variant 4", variable=variant4_var, command=toggle_variant4)
variant4_button.pack(side=tk.LEFT, fill=tk.X, expand=True)

variant5_var = tk.IntVar()
variant5_button = tk.Checkbutton(variant_frame, text="Variant 5", variable=variant5_var, command=toggle_variant5)
variant5_button.pack(side=tk.LEFT, fill=tk.X, expand=True)

search_frame = ttk.Frame(root)
search_frame.pack(fill=tk.X)

search_entry = tk.Entry(search_frame, width=50, fg='gray')
search_entry.insert(0, 'Enter words here')
search_entry.bind('<FocusIn>', lambda event: on_search_focus_in())
search_entry.bind('<FocusOut>', lambda event: on_search_focus_out())
search_entry.pack(fill=tk.X, padx=10, pady=5)

def on_search_focus_in():
    if search_entry.get() == 'Enter words here':
        search_entry.delete(0, tk.END)
        search_entry.config(fg='black')

def on_search_focus_out():
    if search_entry.get() == '':
        search_entry.insert(0, 'Enter words here')
        search_entry.config(fg='gray')



def on_search_entry_changed(event):
    global prompt
    prompt = search_entry.get()

search_entry.bind('<KeyRelease>', on_search_entry_changed)




year_frame = ttk.Frame(root)
year_frame.pack(fill=tk.X)








questionum_frame = ttk.Frame(root)
questionum_frame.pack(fill=tk.X)

questionum_instruction = tk.Label(questionum_frame, text="Select question number", fg='gray')
questionum_instruction.pack(side=tk.LEFT, padx=10, pady=5)

questionum_values = [str(num) for num in range(1, 13)]
questionum_combo = ttk.Combobox(questionum_frame, values=questionum_values, state="readonly")
questionum_combo.pack(side=tk.LEFT, padx=10, pady=5)

# Define the questionum variable
questionum = tk.StringVar()

def on_questionum_select(event):
    selected_questionum = questionum_combo.get()
    questionum.set(selected_questionum)
    print("Selected question number:", questionum.get())
    questionum_instruction.config(fg='black')

def on_questionum_focus_out(event):
    if questionum_combo.get() == '':
        questionum_instruction.config(fg='gray')

questionum_combo.bind("<<ComboboxSelected>>", on_questionum_select)
questionum_combo.bind('<FocusIn>', on_questionum_select)
questionum_combo.bind('<FocusOut>', on_questionum_focus_out)

def on_submit():
    
    print("Submit button pressed!")
    print(questionum.get())
    
    r = requests.get(url)
    f = io.BytesIO(r.content)
    b=False
    b2=False


    if reportfound==True:
        reader = PdfReader(f)
        size=len(reader.pages)
        for i in range(size):
            content = reader.pages[i].extract_text().split("\n")
            size2=len(content)-1
            if b!=None:
                for j in range(size2):
                    line = content[j]

                    if b==True:
                        if line[:10] == "Paper "+str(subcode):
                            b=None
                            break
                        if line[:2] != "  "  and line[:9] != "Cambridge" and line[:9] != 'Principal' and line[:4] != str(subcode):
                            
                            
                            if b2==True:
                                if line[:8]=="Question":
                                    b2=None
                                    break
                                print(line)
                            if line[:10]== "Question "+str(questionum.get()) and b2==False:
                                print(line)
                                b2=True
                        
                    if line[:13] =="Paper "+str(subcode)+"/"+str(papernum) and b==False:
                        print(line)
                        b=True





    # Write your code here for the tasks you want to perform when the submit button is pressed

submit_button = ttk.Button(questionum_frame, text="Submit", command=on_submit)
submit_button.pack(side=tk.RIGHT, padx=10, pady=5)


def open_url_qp():
    # Code to open the question paper URL
    print("Opening Question Paper URL")
    webbrowser.open(urlqp)

def open_url_ms():
    # Code to open the marking scheme URL
    print("Opening Marking Scheme URL")
    webbrowser.open(urlms)

def open_url():
    # Code to open the examiner report URL
    print("Opening Examiner Report URL")
    webbrowser.open(url)

def open_url_gt():
    # Code to open the examiner report URL
    print("Opening Examiner Report URL (urlgt)")
    webbrowser.open(urlgt)


# Create a frame to hold the URL labels and buttons
url_frame = ttk.Frame(root)
url_frame.pack(fill=tk.X)

# Create the URL labels
urlqp_label = tk.Label(url_frame, text="Question Paper URL:")
urlqp_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)

urlms_label = tk.Label(url_frame, text="Marking Scheme URL:")
urlms_label.grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)

ur_label = tk.Label(url_frame, text="Examiner Report URL:")
ur_label.grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)

urlgt_label = tk.Label(url_frame, text="Grade Threshold URL:")
urlgt_label.grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)


# Create the open buttons
buttonurlqp = tk.Button(url_frame, text="Open", command=open_url_qp)
buttonurlqp.grid(row=0, column=1, sticky=tk.E, padx=10, pady=5)

buttonurlms = tk.Button(url_frame, text="Open", command=open_url_ms)
buttonurlms.grid(row=1, column=1, sticky=tk.E, padx=10, pady=5)

buttonurl = tk.Button(url_frame, text="Open", command=open_url)
buttonurl.grid(row=2, column=1, sticky=tk.E, padx=10, pady=5)

buttonurlgt = tk.Button(url_frame, text="Open", command=open_url_gt)
buttonurlgt.grid(row=3, column=1, sticky=tk.E, padx=10, pady=5)



line2=""

words=""
entered=False





def find_button_pressed():
    global variantchar, paperchar, papernum, urlqp, urlms, url,urlgt, subcode, reportfound, prompt, subject, month, yearstr, line2, words, entry
    print("Find button pressed")
    papernum = paperchar + variantchar
    
    
    # Add your custom code here to compute the values of urlqp, urlms, and ur
    print(selected_subject)
    if prompt=="":
        entered=False
        
        if subject.get()=="Chemistry":
            urlqp= "https://papers.gceguide.com/A%20Levels/Chemistry%20(9701)/20" + year.get() + "/9701_" + month.get() + year.get() + "_qp_" + papernum + ".pdf"
            urlms = "https://papers.gceguide.com/A%20Levels/Chemistry%20(9701)/20" + year.get() + "/9701_" + month.get() + year.get() + "_ms_" + papernum + ".pdf"
            url = "https://papers.gceguide.com/A%20Levels/Chemistry%20(9701)/" + prefix + year.get() + "/9701_" + month.get() + year.get() + const
            urlgt = "https://papers.gceguide.com/A%20Levels/Chemistry%20(9701)/20" + year.get() + "/9701_" + month.get() + year.get() + "_gt.pdf"  


            subcode=9701
            sub= "chem"
            reportfound=True
            print (urlqp)
            print (urlms)
            print (url)
            print(urlgt)

            # Update the labels to show the values
            urlqp_label.config(text="Question Paper URL: " + urlqp)
            urlms_label.config(text="Marking Scheme URL: " + urlms)
            ur_label.config(text="Examiner Report URL: " + url)
            urlgt_label.config(text="Grade Threshold URL: " + urlgt)
        elif subject.get()=="Physics":
            urlqp= "https://papers.gceguide.com/A%20Levels/Physics%20(9702)/20" + year.get() + "/9702_" + month.get() + year.get() + "_qp_" + papernum + ".pdf"
            urlms= "https://papers.gceguide.com/A%20Levels/Physics%20(9702)/20" + year.get() + "/9702_" + month.get() + year.get() + "_ms_" + papernum + ".pdf"
            url = "https://papers.gceguide.com/A%20Levels/Physics%20(9702)/" + prefix + year.get() + "/9702_" + month.get() + year.get() + const
            urlgt = "https://papers.gceguide.com/A%20Levels/Physics%20(9702)/20" + year.get() + "/9702_" + month.get() + year.get() + "_gt.pdf"
            subcode=9702
            sub = "phy"
            reportfound=True
            print (urlqp)
            print (urlms)
            print (url)
            print(urlgt)
                    # Update the labels to show the values
            urlqp_label.config(text="Question Paper URL: " + urlqp)
            urlms_label.config(text="Marking Scheme URL: " + urlms)
            ur_label.config(text="Examiner Report URL: " + url)
            urlgt_label.config(text="Grading Threshold URL: " + urlgt)

        elif subject.get()=="Mathematics - Further":
            urlqp= "https://papers.gceguide.com/A%20Levels/Mathematics - Further%20(9231)/20" + year.get() + "/9231_" + month.get() + year.get() + "_qp_" + papernum + ".pdf"
            urlms= "https://papers.gceguide.com/A%20Levels/Mathematics - Further%20(9231)/20" + year.get() + "/9231_" + month.get() + year.get() + "_ms_" + papernum + ".pdf"
            url = "https://papers.gceguide.com/A%20Levels/Mathematics - Further%20(9231)/" + prefix + year.get() + "/9231_" + month.get() + year.get() + const
            urlgt = "https://papers.gceguide.com/A%20Levels/Mathematics - Further%20(9231)/20" + year.get() + "/9231_" + month.get() + year.get() + "_gt.pdf"
            subcode=9702
            sub = "fmt"
            reportfound=True
            print (urlqp)
            print (urlms)
            print (url)
            print(urlgt)
                    # Update the labels to show the values
            urlqp_label.config(text="Question Paper URL: " + urlqp)
            urlms_label.config(text="Marking Scheme URL: " + urlms)
            ur_label.config(text="Examiner Report URL: " + url)
            urlgt_label.config(text="Grading Threshold URL: " + urlgt)

        else:
            print ("subject not compatible")
            reportfound=False

    

    

    





        


        



        

        if subject=="9702":
            
            urlgt = "https://papers.gceguide.com/A%20Levels/Physics%20(9702)/20" + yearstr + "/9702_" + month + yearstr + "_gt.pdf"
            sub = "phy"

            urlqp_label.config(text="Question Paper URL: " + urlqp)
            urlgt_label.config(text="Grading Threshold URL: " + urlgt)

     
    
    def bookmark_dict(
        bookmark_list, reader: PdfReader, use_labels: bool = False,
    ) -> Dict[Union[str, int], str]:
        global errorcode  # Declare errorcode as a global variable
        result = {}
        for item in bookmark_list:
            if isinstance(item, list):
                # Skip processing the sub-bookmarks
                continue
            else:
                page_index = reader.get_destination_page_number(item)
                page_label = reader.page_labels[page_index]
                if use_labels:
                    result[page_label] = item.title
                else:
                    result[page_index] = item.title
        return result

    def download_pdf_from_url(pdf_url: str) -> bytes:
        global errorcode  # Declare errorcode as a global variable
        response = requests.get(pdf_url)
        try:
            response.raise_for_status()
            return response.content
        except:
            errorcode = "PDF not found"
            print(errorcode)

    def bookmark_list_from_url(pdf_url: str, use_labels: bool = False) -> list:
        global errorcode  # Declare errorcode as a global variable
        pdf_content = download_pdf_from_url(pdf_url)
        with BytesIO(pdf_content) as pdf_buffer:
            try:
                reader = PdfReader(pdf_buffer)
                bms = bookmark_dict(reader.outline, reader, use_labels)
            except:
                return

        # Convert the dictionary to a list of lists
        result_list = [[int(page_nb), title] for page_nb, title in sorted(bms.items(), key=lambda n: int(n[0]) if isinstance(n[0], (int, str)) else n[0])]
        return result_list

    if __name__ == "__main__":
        pdf_url = url  # Replace with the actual URL
        bookmark_list = bookmark_list_from_url(pdf_url, use_labels=True)
        if errorcode == "":
            for page_info in bookmark_list:
                print(f"{page_info[0]:>3}: {page_info[1]}")




    def find_page_number(bookmark_list, target_text):
        for page_info in bookmark_list:
            if target_text.lower() in page_info[1].lower():
                return page_info[0]
        return None  # Return None if the text is not found in any bookmark

    if __name__ == "__main__":
        pdf_url = url  # Replace with the actual URL
        bookmark_list = bookmark_list_from_url(pdf_url, use_labels=True)

        target_text = papernum  # Replace with the text you're searching for
        page_number = find_page_number(bookmark_list, target_text)

        if page_number is not None:
            print(f"Page number for '{target_text}': {page_number}")
        else:
            print(f"'{target_text}' not found in bookmarks.")

        page_numberstr = str(page_number+3)

        url = url + "#page=" + page_numberstr
        ur_label.config(text="Examiner Report URL: " + url)





    if urlgt!="gt":
        r = requests.get(urlgt)
        f = io.BytesIO(r.content)
        b=False




        reader = PdfReader(f)
        size=len(reader.pages)
        for i in range(size):
            content = reader.pages[i].extract_text().split("\n")
            size2=len(content)-1
            #print(content)

            for j in range(size2):
                line = content[j]


                if line[:12] =="Component "+str(papernum) and b==False:
                    print(line)
                    print(line)
                    line2 = line[13:]
                    print(line2)


                    words = line2.split()
                    max= words[0]
                    grade_a = words[1]
                    grade_b = words[2]
                    grade_c = words[3]
                    grade_d = words[4]
                    grade_e = words[5]
                    print("max", max)
                    print("a:", grade_a)
                    print("b:", grade_b)
                    print("c:", grade_c)
                    print("d:", grade_d)
                    print("e:", grade_e)

                    
            

    
                    for i in range(5):
                        if table_entries[i][0].get() == "":
                            entry=i 



                            if entered!=True:

                                

                                table_entries[i][0].insert(0, sub + year.get() + month.get() + papernum )
                                table_entries[i][1].insert(0, max)
                                table_entries[i][2].insert(0, grade_a)
                                table_entries[i][3].insert(0, grade_b)
                                table_entries[i][4].insert(0, grade_c)
                                table_entries[i][5].insert(0, grade_d)
                                table_entries[i][6].insert(0, grade_e)

                            else:
                                table_entries[i][0].insert(0, sub + yearstr + month + papernum )
                                table_entries[i][1].insert(0, max)
                                table_entries[i][2].insert(0, grade_a)
                                table_entries[i][3].insert(0, grade_b)
                                table_entries[i][4].insert(0, grade_c)
                                table_entries[i][5].insert(0, grade_d)
                                table_entries[i][6].insert(0, grade_e)






                            b=True
                            break
        # Split the sentence into words
        
        

       

    else:
        print("error gt")  

find_button = ttk.Button(root, text="Find", command=find_button_pressed)


find_button.pack()

root.title("Table")

# Create table frame
table_frame = ttk.Frame(root)
table_frame.pack(anchor='w', padx=10, pady=10)

# Create labels A to E
label_a = ttk.Label(table_frame, text="A")
label_a.grid(row=0, column=3, padx=2, pady=2)
label_b = ttk.Label(table_frame, text="B")
label_b.grid(row=0, column=4, padx=2, pady=2)
label_c = ttk.Label(table_frame, text="C")
label_c.grid(row=0, column=5, padx=2, pady=2)
label_d = ttk.Label(table_frame, text="D")
label_d.grid(row=0, column=6, padx=2, pady=2)
label_e = ttk.Label(table_frame, text="E")
label_e.grid(row=0, column=7, padx=2, pady=2)

# Create table
table_entries = create_table(table_frame, 5, 7)









root.mainloop()




print("Prompt:", prompt)




print("Selected subject:", subject.get())
print(subject.get())
print("Selected year:", year.get())
print("Selected month:", month.get())
print(papernum)
print(paperchar)
print(variantchar)



#all reference parts output











