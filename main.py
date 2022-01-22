# Write a Python program to print the sorted dictionary
color_dict = {'amearica':'washington',
            'japan':'seol',
            'india':'delhi',
             'vithura':'kalung'}

for key in sorted(color_dict):
    print("%s: %s" % (key, color_dict[key]))