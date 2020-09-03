#Byrja á að stilla upp upphafsgildunum

dist_byrjun_m = 16637000000                                     #mílur frá sólu
hradi_solarhring = 38241*24                                     #mílur sem voyager 1 ferðast á sólarhring

#Hér fyrir neðan hefjast útreikningarnir

input = input('Number of days after 9/25/09: ')                 #input frá notanda um fjölda daga sem hann vill reikna   
dagar = int(input)                                              #breyti inputinu í integer tölu
dist_m = (dagar * hradi_solarhring) + dist_byrjun_m             #reikna út hvað hann fer langt á þeim dögum og bæti við upphafsfjarlægðina
dist_km = dist_m * 1.609344                                     #breyti í kílómetra
dist_AU = dist_m / 92955887.6                                   #breyti í AU
radio_time = dist_km / 1079252848.8                             #reikna út tímann sem samskipti taka með þvi að deila km fjólda á hraðann í km/klst
round_dist_km = round(dist_km)                                  #námunda fjarlægðina í km upp að næsta tug
round_dist_AU = round(dist_AU)                                  #námunda fjarlægðina í AU upp að næsta tug

#Prenta út öll gildin sem voru reiknuð hér að ofan

print("Miles from the sun:", dist_m)                            #Prenta út fjarlægð í mílum
print("Kilometers from the sun:", round_dist_km)                #Prenta út fjarlægð í kílómetrum
print("AU from the sun:", round_dist_AU)                        #Prenta út fjarlægð í AU
#print("Samskiptatími =", radio_time)                           #Prenta út tíma sem samskipti taka að fara fram og til baka