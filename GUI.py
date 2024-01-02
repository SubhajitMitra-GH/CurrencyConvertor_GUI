import tkinter as tk
from tkinter import ttk

contA = ["China", "Philippines", "Japan", "Vietnam", "Thailand", "Indonesia", "Malaysia", "South Korea", "Pakistan", "Bangladesh", "Nepal", "Sri Lanka", "Myanmar", "Cambodia", "Laos", "Mongolia", "Kazakhstan", "Uzbekistan", "Turkmenistan"]
contE = ["Albania", "Andorra", "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "United Kingdom", "Lithuania"]
contAf = ["Algeria", "Angola", "Benin", "Botswana", "Cameroon", "Chad", "Egypt", "Ethiopia", "Ghana", "Ivory Coast", "Kenya", "Libya", "Madagascar", "Morocco", "Nigeria", "Senegal", "South Africa", "Tanzania", "Uganda", "Zimbabwe"]
contN = ["United States", "Canada", "Mexico", "Guatemala", "Honduras", "El Salvador", "Nicaragua", "Costa Rica", "Panama", "Belize", "Jamaica", "Haiti", "Dominican Republic", "Cuba", "Trinidad and Tobago", "Barbados", "Bahamas", "Honduras", "Cayman Islands", "Puerto Rico"]
contS = ["Brazil", "Argentina", "Colombia", "Venezuela", "Aruba", "Caribbean Netherlands", "Chile", "Ecuador", "Bolivia", "Paraguay", "Uruguay", "Guyana", "Suriname", "French Guiana", "Falkland Islands", "Guyana", "Suriname", "French Guiana", "Falkland Islands", "Peru"]
contO = ["Australia", "New Zealand", "Papua New Guinea", "Fiji", "Solomon Islands", "Vanuatu", "New Caledonia", "French Polynesia", "Samoa", "American Samoa", "Tonga", "Tuvalu", "Kiribati", "Marshall Islands", "Nauru", "Palau", "Micronesia", "Federated States of Micronesia", "Guam", "Northern Mariana Islands"]
curA = [0.084, 0.67, 1.72, 325.42, 2.36, 188.27, 0.94, 10.68, 2.69, 1.27, 1.63, 2.69, 0.62, 50.96, 0.02, 0.21, 0.21, 0.02, 0.17]
curE = [0.087, 0.014, 0.014, 0.014, 0.032, 0.13, 0.014, 0.18, 0.11, 0.014, 0.014, 0.014, 0.014, 0.014, 0.056, 0.92, 0.014, 0.014, 0.011, 0.014]
curAf = [12.83, 11.40, 11.82, 11.02, 11.45, 11.09, 10.15, 11.88, 11.45, 11.45, 11.66, 11.41, 11.01, 11.01, 10.65, 11.09, 11.01, 10.91, 11.22, 10.75]
curN = [80.45, 74.17, 23.21, 11.82, 11.82, 11.82, 11.82, 11.82, 11.82, 11.82, 11.82, 11.82, 11.82, 11.82, 11.82, 11.82, 11.82, 11.82, 11.82, 11.82]
curS = [11.59, 11.84, 11.59, 11.59, 11.59, 11.59, 11.59, 11.59, 11.59, 11.59, 11.59, 11.59, 11.59, 11.59, 11.59, 11.59, 11.59, 11.59, 11.59, 11.59]
curO = [70.59, 73.54, 11.82, 11.82, 11.82, 11.82, 11.82, 11.82, 11.82, 11.82, 11.82, 11.82, 11.82, 11.82, 11.82, 11.82, 11.82, 11.82, 11.82, 11.82]
def convert_currency():
    try:
        amt = abs(float(entry_amount.get()))
        cont = var_continent.get()
        country = var_country.get()

        # Determine the conversion rate based on the selected continent and country
        if cont == "Asia":
            conversion_rate = curA[contA.index(country)]
        elif cont == "Africa":
            conversion_rate = curAf[contAf.index(country)]
        elif cont == "Europe":
            conversion_rate = curE[contE.index(country)]
        elif cont == "North America":
            conversion_rate = curN[contN.index(country)]
        elif cont == "South America":
            conversion_rate = curS[contS.index(country)]    
        elif cont == "Oceania":
            conversion_rate = curO[contO.index(country)]    
            
 
        converted_amount = amt * conversion_rate

        result_label.config(text=f"The amount in INR from {cont} - {country}'s currency would be {converted_amount:.2f}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Currency Converter")

# Create and place widgets
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label_amount = ttk.Label(frame, text="Enter the amount to be converted:")
label_amount.grid(row=0, column=0, sticky=tk.W, pady=5)

entry_amount = ttk.Entry(frame)
entry_amount.grid(row=0, column=1, pady=5)

label_continent = ttk.Label(frame, text="Select the continent:")
label_continent.grid(row=1, column=0, sticky=tk.W, pady=5)

var_continent = tk.StringVar()
combobox_continent = ttk.Combobox(frame, textvariable=var_continent, values=["Asia", "Africa", "Europe", "North America", "South America", "Oceania"])
combobox_continent.grid(row=1, column=1, pady=5)

label_country = ttk.Label(frame, text="Select the country:")
label_country.grid(row=2, column=0, sticky=tk.W, pady=5)

var_country = tk.StringVar()
# Set the initial values for the country based on the selected continent
combobox_country = ttk.Combobox(frame, textvariable=var_country, values=contA)
combobox_country.grid(row=2, column=1, pady=5)

button_convert = ttk.Button(frame, text="Convert", command=convert_currency)
button_convert.grid(row=3, column=0, columnspan=2, pady=10)

result_label = ttk.Label(frame, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=5)

# Event handling to update the country options based on the selected continent
def update_country_options(event):
    selected_continent = var_continent.get()
    if selected_continent == "Asia":
        combobox_country["values"] = contA
    elif selected_continent == "Africa":
        combobox_country["values"] = contAf
    elif selected_continent == "Europe":
        combobox_country["values"] = contE
    elif selected_continent == "North America":
        combobox_country["values"] = contN   
    elif selected_continent == "South America":
        combobox_country["values"] = contS
    elif selected_continent == "Oceania":
        combobox_country["values"] = contO    
# Bind the event handler to the continent selection
combobox_continent.bind("<<ComboboxSelected>>", update_country_options)

# Run the Tkinter event loop
root.mainloop()
