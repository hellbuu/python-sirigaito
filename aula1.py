# variáveis 

# não precisa informar tipo
v_e = "CBERS-1"
#e = 0.0004025  
#perigee = 779
#apogee = 785
in_service = False

# status do satélite
if in_service:
    status = "is currently in service."
else:
    status = "is no longer in service."

print(f"The {v_e} satellite {status}")
