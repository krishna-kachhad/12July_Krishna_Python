#------------------------------ dictionary demo

cityCode={'Ahmedabad':79,'Mumbai':22,'Pune':20,'Delhi':11}

print(cityCode)

for key in cityCode:
    print(key," ",cityCode[key])

#-------------------------dictionary method

cityCode={'Ahmedabad':79,'Mumbai':22,'Pune':20,'Delhi':11}
cityFamousPlace={"Ahmedabad":"IIM","Delhi":"Metro","Mumbai":"Bollywood"}


cityFamousPlaceCopy = cityFamousPlace.copy()
print("CityFamousCopy",cityFamousPlaceCopy)


print("Before Update",cityCode)

cityCode.update(cityFamousPlace)
print("After Update",cityCode)