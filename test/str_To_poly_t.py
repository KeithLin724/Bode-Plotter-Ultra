import re
polys = ['8938']

out = []
for poly in polys:
    poly = re.sub(r"(E\+)$", '', poly)
    list_coef = re.split(r'x[\^\d]*', poly)

    list_coef = [float(elt) for elt in list_coef if elt]
    out.append(list_coef)
print(out)
