
def ping(s):
    if s.status_code == 200:
        pass
    else:
        print(f'error with {s}')


def alcohol_by_volume(avol,abv,e=0,ice=1):
    #standard dilution allowance 
    # 0 = no dilution allowance
    # 1 = normal shake @ 10% 
    # 2 = normal stired @ 25% 
    # 3 = wipe shake @  5% 
    vol = (avol + e)
    if ice == 1:
        tvol = vol * 1.1
    elif ice == 2:
        tvol = vol * 1.25
    elif ice == 3:
        tvol = vol * 1.05
    elif ice == 4:
        tvol = vol * 1.075
    else:
        tvol = vol
    volcalc = round(((avol*(abv/100)/(tvol))),ndigits=3)
    units = alc_units(volcalc,(tvol))
    uk = uk_proof(volcalc)
    us = us_proof(volcalc)
    return volcalc,units,uk,us,tvol

def alc_units(abv,avol):
    return round((((abv/100) * avol) * 10),ndigits=3)

def uk_proof(abv):
    return round(((abv / 0.5706) * 100),ndigits=2)

def us_proof(abv):
    return round(((abv / 0.5) * 100),ndigits=2)

def aclcohol_pct(vol,abv):
    return vol * (abv/100)
    
