HEX_COLOUR_TO_CODE = {"absolute zero": "#0048ba", "aqua": "#00ffff", "baby pink": "#f4c2c2", "black": "#000000",
                      "blonde": "#faf0be", "blue": "#0000ff", "gray": "#bebebe", "green": "#1cac78",
                      "yellow": "	#ffff00",
                      "white": "#ffffff"}

colour_name = input("What is the colour?").lower()
while colour_name != "":
    print(f"The Code of the colour {colour_name} is {HEX_COLOUR_TO_CODE.get(colour_name)}")
    colour_name = input("What is the colour?").lower()
