T1 = 200
T2 = 100
T3 = 1
To = 1
Me = 0
Ma = 120
Ba = 123
Ku = 333
Fl = 0
Gem = Ba + Ku + Fl
Ges = T1 + T2 + T3 + To + Me + Ma + Gem
print('Verbrauchseinheiten Gemeinschaft ' + str(Gem))
print("Verbrauchseinheiten Gesamt " + str(Ges)) 
print("Verbrauchseinheiten Tobi " + str(T1 + T2 + T3 + Gem/4))
print("Verbrauchseinheiten Tom " + str(To + Gem/4))
print("Verbrauchseinheiten Memo " + str(Me + Gem/4))
print("Verbrauchseinheiten Matthias " + str(Ma + Gem/4))

print To + Gem/4
print Me + Gem/4
print Ma + Gem/4