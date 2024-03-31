path = ".\temp_project"

# try:
#     f = open("myfile.txt", "x", encoding="utf-8" )
#     f.close()
# except FileExistsError:
#     print('File already exists.')


def write_log_to_file(file_name, text):
    try:
        with open(file_name, "a", encoding="utf-8" ) as f:
            f.write(text)
    except (BaseException,) as e:
        print(e)


def read_log(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            my_text = f.read()
        return my_text
    except (BaseException,) as e:
        print(e)


f_name = "test_file.txt"
text = "Test 2: 9:54pm\n"
# write log
write_log_to_file(file_name=f_name, text=text)
# read log
my_text_data = read_log(f_name)
print(my_text_data)
