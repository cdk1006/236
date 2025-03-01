tax_rate = 0.06

def total_tax(total):
    return round(total * tax_rate, 2)

def after_tax_total(total):
    return round(total + total_tax(total), 2)