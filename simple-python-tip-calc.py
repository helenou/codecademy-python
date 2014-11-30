# Simple calculateur de pourboire

repas = 44.50
taxe = 0.0675
pourboire = 0.15

repas = repas + repas * taxe
total = repas + repas*pourboire

print("%.2f" % total)
