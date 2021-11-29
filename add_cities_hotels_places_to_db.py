"""
import firebase as fb

import places_db
import hotels_db

# hotels

fb.db.child("Cities").child("Jerusalem").child('Hotels').update(hotels_db.jerusalem)
fb.db.child("Cities").child("Tel Aviv").child('Hotels').update(hotels_db.tel_aviv)
fb.db.child("Cities").child("Ashdod").child('Hotels').update(hotels_db.ashdod)
fb.db.child("Cities").child("Netanya").child('Hotels').update(hotels_db.netanya)
fb.db.child("Cities").child("Tveria").child('Hotels').update(hotels_db.tveria)
fb.db.child("Cities").child("Beer Sheva").child('Hotels').update(hotels_db.beer_sheva)
fb.db.child("Cities").child("Ramat Gan").child('Hotels').update(hotels_db.ramat_gan)
fb.db.child("Cities").child("Tsfat").child('Hotels').update(hotels_db.tsfat)
fb.db.child("Cities").child("Netivot").child('Hotels').update(hotels_db.netivot)
fb.db.child("Cities").child("Arad").child('Hotels').update(hotels_db.arad)
fb.db.child("Cities").child("Bat Yam").child('Hotels').update(hotels_db.bat_yam)
fb.db.child("Cities").child("Eilat").child('Hotels').update(hotels_db.eilat)
fb.db.child("Cities").child("Haifa").child('Hotels').update(hotels_db.haifa)

# places
fb.db.child('Cities').child('Ashdod').child('Places').update(places_db.ashdod)
fb.db.child("Cities").child("Arad").child('Hotels').update(places_db.arad)
fb.db.child('Cities').child("Bat Yam").child('Places').update(places_db.bat_yam)
fb.db.child("Cities").child("Beer Sheva").child("Places").update(places_db.beer_sheva)
fb.db.child('Cities').child('Eilat').child('Places').update(places_db.eilat)
fb.db.child('Cities').child('Jerusalem').child('Places').update(places_db.jerusalem)
fb.db.child('Cities').child('Netanya').child('Places').update(places_db.netanya)
# fb.db.child('Cities').child('Netivot').child('Places').update(places_db.netivot)
fb.db.child('Cities').child('Ramat Gan').child('Places').update(places_db.ramat_gan)
fb.db.child('Cities').child("Tel Aviv").child('Places').update(places_db.tel_aviv)
fb.db.child('Cities').child('Tsfat').child('Places').update(places_db.tsfats)
fb.db.child('Cities').child('Tveria').child('Places').update(places_db.tveria)
fb.db.child('Cities').child('Haifa').child('Places').update(places_db.haifa)

# fb.db.child('Cities').child('Silent Hill').update({'test': '0'})
# fb.db.child('Cities').child('Silent Hill').remove()
"""
