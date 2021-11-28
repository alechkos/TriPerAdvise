import firebase as fb
import places
import hotels

# hotels
"""
fb.db.child("Cities").child("Jerusalem").child('Hotels').update(hotels.jerusalem)
fb.db.child("Cities").child("Tel Aviv").child('Hotels').update(hotels.tel_aviv)
fb.db.child("Cities").child("Ashdod").child('Hotels').update(hotels.ashdod)
fb.db.child("Cities").child("Netanya").child('Hotels').update(hotels.netanya)
fb.db.child("Cities").child("Tveria").child('Hotels').update(hotels.tveria)
fb.db.child("Cities").child("Beer Sheva").child('Hotels').update(hotels.beer_sheva)
fb.db.child("Cities").child("Ramat Gan").child('Hotels').update(hotels.ramat_gan)
fb.db.child("Cities").child("Tsfat").child('Hotels').update(hotels.tsfat)
fb.db.child("Cities").child("Netivot").child('Hotels').update(hotels.netivot)
fb.db.child("Cities").child("Arad").child('Hotels').update(hotels.arad)
fb.db.child("Cities").child("Bat Yam").child('Hotels').update(hotels.bat_yam)
fb.db.child("Cities").child("Eilat").child('Hotels').update(hotels.eilat)
fb.db.child("Cities").child("Haifa").child('Hotels').update(hotels.haifa)
"""

# places

fb.db.child('Cities').child('Ashdod').child('Places').update(places.ashdod)
fb.db.child("Cities").child("Arad").child('Hotels').update(places.arad)
fb.db.child('Cities').child('Bat Yam').child('Places').update(places.bat_yam)
fb.db.child('Cities').child('Beer Sheva').child('Places').update(places.beer_sheva)
fb.db.child('Cities').child('Eilat').child('Places').update(places.eilat)
fb.db.child('Cities').child('Jerusalem').child('Places').update(places.jerusalem)
fb.db.child('Cities').child('Netanya').child('Places').update(places.netanya)
fb.db.child('Cities').child('Netivot').child('Places').update(places.netivot)
fb.db.child('Cities').child('Ramat Gan').child('Places').update(places.ramat_gan)
fb.db.child('Cities').child('Tel Aviv').child('Places').update(places.tel_aviv)
fb.db.child('Cities').child('Tsfat').child('Places').update(places.tsfats)
fb.db.child('Cities').child('Tveria').child('Places').update(places.tveria)
fb.db.child('Cities').child('Haifa').child('Places').update(places.haifa)