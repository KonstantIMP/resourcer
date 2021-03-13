def dec_to_hex(n) :
    out = ""

    if n == 0 : return "0x00"

    while n > 0 :
        if n % 16 < 10 : out += str(n % 16)
        else :
            if n % 16 == 10 : out += 'a'
            elif n % 16 == 11 : out += 'b'
            elif n % 16 == 12 : out += 'c'
            elif n % 16 == 13 : out += 'd'
            elif n % 16 == 14 : out += 'e'
            elif n % 16 == 15 : out += 'f'

        n = n // 16

    out = out[::-1]

    if len(out) < 2 : out = '0' + out

    return "0x" + out

def resourcer(input_f, output_f, arr_style, arr_name) :
    out = open(output_f, "w")

    if arr_style == 1 :
        out.write("char " + arr_name + " [] = {\n    ")
    elif arr_style == 2 :
        out.write("unsigned char " + arr_name + " [] = {\n    ")
    elif arr_style == 3 :
        out.write("std::int8_t " + arr_name + " [] = {\n    ")
    elif arr_style == 4 :
        out.write("std::uint8_t " + arr_name + " [] = {\n    ")
    elif arr_style == 5 :
        out.write("module " + arr_name + ";\n\n")
        out.write("byte [] " + arr_name + " = [\n    ")
    else :
        out.write("module " + arr_name + ";\n\n")
        out.write("ubyte [] " + arr_name + " = [\n    ")

    counter = 0

    with open(input_f, "rb") as inp :
        while True :
            byte = inp.read(1)
            if len(byte) == 0 : break

            if counter != 0 and counter % 16 == 0 : out.write(",\n    ")
            elif counter != 0 : out.write(', ')

            out.write(dec_to_hex(ord(byte)))
            counter = counter + 1

    if arr_style == 1 or arr_style == 2 or arr_style == 3 or arr_style == 4 :
        out.write(", 0x00\n};\n")
    else :
        out.write(", 0x00\n];\n")