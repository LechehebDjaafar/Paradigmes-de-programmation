# ----------------Info Developer-------------
# -Last Name : Lecheheb
# -First Name : Djaafar
# -Country : Algeria
# -age : 26
# -Skills : Python - HTML - CSS - C
# -instagram : @ddos_attack_co
# ------------Fallowed Me for instagram-------

#استدعاء المكتبة 
from tkinter import *
from tkinter import messagebox
import re
def main():
    

    # تعريف دالة لمعالجة رسائل الخطأ وفحص الصيغة
    def error(bool1, text, bool2): 
        if not bool2:
            messagebox.showerror(r'Syntax Error', r'It appears you entered incorrect text << " " or  \' \' >>. Please retype it correctly.'.title())
        elif not bool1:
            # تعريف أنماط مختلفة لفحص أخطاء الصيغة
            Mistyped_variable = r'(?<!\w)\s*\d+[a-zA-Z_]+' 
            open_parentheses_pattern = r"\("
            close_parentheses_pattern = r"\)"
            open_parentheses_count = len(re.findall(open_parentheses_pattern, text))
            close_parentheses_count = len(re.findall(close_parentheses_pattern, text))
            Beyond_the_closed_arch = r"(\)(\w+))"
            error_sentext7 = r"\(\s*\w*\s*\)|\)\)\b|\(\s*\,"
            error_sentext8 = r"\b\d\("

            not_value_in_parenthese = r"\(\s*\)"
            error_sentext4 = r'(\w+\s+\w+)'
            if open_parentheses_count != close_parentheses_count:
                messagebox.showerror('Syntax Error', 'It appears you entered incorrect text << ( ) >>. Please retype it correctly.'.title())
            elif re.search(Mistyped_variable, text):
                messagebox.showerror('Syntax Error', f'It appears you entered incorrect text <<{re.findall(Mistyped_variable, text)[0]}>>. Please retype it correctly.'.title())
            elif re.search(Beyond_the_closed_arch, text):
                messagebox.showerror('Syntax Error', f'It appears you entered incorrect text <<{re.findall(Beyond_the_closed_arch, text)[0]}>>. Please retype it correctly.'.title())
            elif re.search(not_value_in_parenthese, text):
                messagebox.showerror('Syntax Error', f'It appears you entered incorrect text <<{re.findall(not_value_in_parenthese, text)[0]} is not a value here>>. Please retype it correctly.'.title())
            elif re.search(error_sentext4, text):
                messagebox.showerror('Syntax Error', f'It appears you entered incorrect text <<{re.findall(error_sentext4, text)[0]}>>. Please retype it correctly.'.title())
            elif re.search(error_sentext7,text):
                messagebox.showerror('Syntax Error', f'It appears you entered incorrect text n>1 value <<{re.findall(error_sentext7, text)[0]}>>. Please retype it correctly.'.title())
            elif re.search(error_sentext8,text):
                messagebox.showerror('Syntax Error', f'It appears you entered incorrect Number function value <<{re.findall(error_sentext8, text)[0]}>>. Please retype it correctly.'.title())
                
    # دالة لفحص الصيغة
    def Error_checking(term)->bool:
        Mistyped_variable = r'(?<!\w)\s*\d+[a-zA-Z_]+'
        open_parentheses_pattern = r"\("
        close_parentheses_pattern = r"\)"
        Beyond_the_closed_arch = r"\)(\w+)"
        error_sentext4 = r'\w+\s+\w+'
        error_sentext5 = r'\(\s*\"\w*\s*\"\)'
        error_sentext6 = r"\(\s*\'\w*\s*\'\)"
        error_sentext7 = r"\(\s*\w*\s*\)|\)\)\b|\(\s*\,"
        error_sentext8 = r"\b\d\("
        
        open_parentheses_count = len(re.findall(open_parentheses_pattern, term))
        close_parentheses_count = len(re.findall(close_parentheses_pattern, term))
        if not re.search(error_sentext5,input_textbox.get("1.0", "end-1c")) and not re.search(error_sentext6,input_textbox.get("1.0", "end-1c")):
            not_value_in_parenthese = r"\(\s*\)"
            term_pattern = fr'({Mistyped_variable}|{Beyond_the_closed_arch}|{not_value_in_parenthese}|{error_sentext4}|{error_sentext7}|{error_sentext8})'
        else:
            term_pattern = fr'({Mistyped_variable}|{Beyond_the_closed_arch}|{error_sentext4}|{error_sentext7}|{error_sentext8})'
            
        
        if re.search(term_pattern, term) or open_parentheses_count != close_parentheses_count:
            return False
        else:
            return True

    # دالة لإزالة كلمات من النص
    def remove_words(text, word_list)->str:
        if len(word_list) > 0:
            for word in word_list:
                text = re.sub(re.escape(word), '', text)
            return text
        else:
            return text

    # دالة للبحث عن سلاسل النص المتواجدة بين علامات التنصيص
    def find_quoted_strings(text)->list:
        list_strings = []
        if text.count('"') > 0:
            if text.count('"') % 2 == 0:
                start = text.index('"')
                nexts = text.index('"', start + 1)
                for i in range(text.count('"') // 2):
                    list_strings.append(text[start:nexts + 1])
                    try:
                        start = text.index('"', nexts + 1)
                        nexts = text.index('"', start + 1)
                    except:
                        continue
            else:
                return 1
        if text.count("'") > 0:
            if text.count("'") % 2 == 0:
                start = text.index("'")
                nexts = text.index("'", start + 1)
                for i in range(text.count("'") // 2):
                    list_strings.append(text[start:nexts + 1])
                    try:
                        start = text.index("'", nexts + 1)
                        nexts = text.index("'", start + 1)
                    except:
                        continue
            else:
                return 1
        return list_strings

    # دالة لاسترجاع الثوابت والمتغيرات من النص
    def return_variables(constants)->list:
        y = []
        for match in constants:
            for group in match:
                if group:
                    y.append(group)
        return y

    # اضافة رمز # في بداية
    def Add_code_at_the_beginning(lits)->list:
        new_list = []
        for i in lits:
            new_list.append(f'#{i}')
        return new_list
    # دالة لاستخراج الوظائف والمتغيرات
    def extract_functions_and_variables():
        input_text = input_textbox.get("1.0", "end-1c").strip()
        list_constants = find_quoted_strings(input_text)
        if list_constants != 1:
            input_text = remove_words(input_text, list_constants)
        if Error_checking(input_text) and find_quoted_strings(input_text) != 1:
            functions = re.findall(r'([A-Za-z0-9]+\s*)\(', input_text)
            variables = re.findall(r'\b(\w+)\b(?!\s*\()', input_text)
            constants = re.findall(r"(['\"])(.*?)\1|\b(\d+\.\d+|\d+)\b", input_text)

            unique_constants = return_variables(constants)

            constants_filtered = [constant for constant in unique_constants if constant not in functions]
            variables_filtered = [variable for variable in variables if variable not in functions and variable not in unique_constants]

            print_function = "\n".join(Add_code_at_the_beginning(list(set(functions))))
            print_constants = "\n".join(Add_code_at_the_beginning(list(set(constants_filtered + list_constants))))
            print_variables = "\n".join(Add_code_at_the_beginning(list(set(variables_filtered))))
            label_functions.config(text=f'functions:\n{print_function}')
            label_variable.config(text=f'variable:\n{print_variables}')
            label_constants.config(text=f'constants:\n{print_constants}')
        else:
            error(Error_checking(input_text), input_text, find_quoted_strings(input_text) != 1)

    # دالة لحذف النص
    def delete_text():
        input_textbox.delete(1.0, END)
        activate_analyze_delete(None)

    # دالة لتنشيط زر "تحليل" و"حذف"
    def activate_analyze_delete(event):
        if len(input_textbox.get("1.0", "end-1c")) > 0 and not re.search(r'^\s*$', input_textbox.get("1.0", "end-1c")):
            button_delete.config(state=NORMAL, bg='Yellow', fg='White')
            button_analyze.config(state=NORMAL, bg='green', fg='White')
        else:
            button_delete.config(state=DISABLED, bg='grey', fg='White')
            button_analyze.config(state=DISABLED, bg='grey', fg='White')
            label_functions.config(text=f'functions:')
            label_variable.config(text=f'variable:')
            label_constants.config(text=f'constants:')

    # دالة للتفعيل عند تغيير النص
    def on_text_change(event):
        activate_analyze_delete(None)


    #الواجهة الروسومية للعمل التطبيقي
    root = Tk()
    root.title('TP1: Imperative style')

    title = Label(root, text='Enter a term'.title(), font=("Arial", 16))
    title.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    input_textbox = Text(root, height=10, width=40, border=5)
    input_textbox.grid(row=1, column=1, padx=10, pady=10)
    input_textbox.bind("<KeyRelease>", on_text_change)

    button_exit = Button(root, text='Exit', padx=80, pady=5, font=("Arial", 12), bg='Red', fg='White', bd=7, command=root.quit)
    button_exit.grid(row=2, column=0, padx=10, pady=10)

    button_delete = Button(root, text='Delete', padx=80, pady=5, bg='grey', fg='White', font=("Arial", 12), bd=7,
                        command=delete_text, state=DISABLED)
    button_delete.grid(row=2, column=1, padx=10, pady=10)

    button_analyze = Button(root, text='Analysis', padx=80, pady=5, bg='grey', fg='White', font=("Arial", 12), bd=7,
                            command=extract_functions_and_variables, state=DISABLED)
    button_analyze.grid(row=2, column=2, padx=10, pady=10)

    label_functions = Label(root, text='Functions', relief=RIDGE, font=("Arial", 12))
    label_functions.grid(row=3, column=0, padx=10, pady=10)
    label_constants = Label(root, text='Constants', relief=RIDGE, font=("Arial", 12))
    label_constants.grid(row=3, column=2, padx=10, pady=10)
    label_variable = Label(root, text='Variable', relief=RIDGE, font=("Arial", 12))
    label_variable.grid(row=3, column=1, padx=10, pady=10)

    root.mainloop()

main()
############### Any inquiries, contact me #################################################################
