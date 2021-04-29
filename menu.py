from flask import Flask, render_template, request

# This program controls an interactive menu for ordering food.

app = Flask(__name__)


# This function takes the list of items ordered by the customer and converts the list to a string
# that can be displayed when they submit their order. It also adds commas and 'and' in the list.
def listToString(s): 
   # initialize an empty string
    str1 = '' 
    num_elements = len(s)
    # traverse in the string 
    word_count = 1
    for ele in s: 
        if num_elements > 1:
            if word_count < num_elements:
                if word_count < num_elements-1:
                    str1 += ele + ', '
                    word_count += 1 
                else:    
                    str1 += ele 
                    word_count += 1                    
            elif word_count == num_elements:
                str1 += ' and ' + ele 
        else: 
            str1 += ele
    return str1 

# This is the main part that handles the functionality of the webpage.

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        list_string = listToString(request.form.getlist('mycheckbox'))
        table_number = request.form
        print(table_number)
        if len(list_string) > 0:
            order_string = 'Your order of '+list_string+' has been submitted.我们接受你点的选择。'
        else:
            order_string = 'Please order at least one item on the menu.请点在菜单至少一种菜。'
        return order_string
    return render_template('index.html')