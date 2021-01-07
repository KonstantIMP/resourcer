import user_interface
import resourcer

if __name__ == "__main__" :
    user_interface.print_hello()

    input_file = user_interface.get_input_file()
    output_file = user_interface.get_output_file()

    out_type = user_interface.choose_option("Choose array type",
            ["C-style signed array\t\t(char arr [])",
             "C-style unsigned array\t(unsigned char arr [])",
             "C++-style signed array\t(std::int8_t arr [])",
             "C++-style unsigned array\t(std::uint8_t arr [])",
             "D-style signed array\t\t(byte [] arr)",
             "D-style unsigned array\t(ubyte [] arr)"])

    arr_name = user_interface.get_array_name()

    resourcer.resourcer(input_file, output_file, out_type, arr_name)