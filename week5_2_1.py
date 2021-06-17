hrs = input("Enter Hours:")
rate = input("Enter the Rate:")
h = float(hrs)
r = float(rate)
if h > 40 :
    reg = h*r
    opt = (h - 40.0) * (r * 1.25 )
    pay = reg + opt

else :
	pay= h*r

print(pay)
