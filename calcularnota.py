def calcularnota(bachiller, general, optativa1, optativa2, m1, m2):
    notafinal=bachiller*0.6+general*0.4+optativa1*m1+optativa2*m2
    return notafinal

bachiller=float(input("nota de bachiller"))
general=float(input("nota general de selectividad"))
optativa1=float(input("nota de la primera optativa"))
optativa2=float(input("nota de la segunda optativa"))
m1=float(input("cuanto pondera la primera optativa"))
m2=float(input("cuanto pondera la segunda optativa"))

notafinal=float(calcularnota(bachiller, general, optativa1, optativa2, m1, m2))

print(f"Tu nota final para el acceso a la universidad es: {round(notafinal, 2)}")
