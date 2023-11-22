def is_season(type, season):
    type, season = type.lower(), season.lower()
    if type == "fruits":
        if season == "hiver":
            print("orange, mandarine et kiwi")
        elif season == "ete":
            print("poire, fraise, cassis")
    elif type == "legumes":
        if season == "hiver":
            print("carotte, topinambour, endive")
        elif season == "ete":
            print("artichaut, aubergine, navet")
    else:
        print("ERROR: enter a valid season ('hiver' or 'ete' /type of plant")

is_season("fruits", "hiver")
is_season("legumes", "ete")
is_season("sdq", "sqdgsq")