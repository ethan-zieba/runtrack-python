def what_carreer(langage):
    match langage.lower():
        case "javascript":
            print("Tu es un développeur web")
        case "python":
            print("Tu es un dévelopeur IA")
        case "java":
            print("Tu es un développeur logiciel")
        case "reactjs":
            print("Tu es un développeur mobile")
        case _:
            print("Tu es un sorcier Harry")

what_carreer("JavaScript")
what_carreer("Expecto Patronum")
what_carreer("python")
what_carreer("n'importe quoi")