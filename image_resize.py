from PIL import Image

WIDTH = 25
HEIGHT = 50


# print('❂❂❂❂❂❂❂❂❂❂❂❂❂❂❂❂❂❂❂❂❂❂❂❂\nWelcome to ye old Resize Machine\n❂❂❂❂❂❂❂❂❂❂❂❂❂❂❂❂❂❂❂❂❂❂❂❂')
#
# while True:
#     file_name = input('what is the name of the file (including the file extension) you would like to resize?')
#     width = input('What is the desired width (in pixels)?')
#     height = input('What is the desired height (in pixels)?')
#     new_file_name = input('what would you like to rename your file to (including the file extension)?')
#     image = Image.open('images/'+file_name)
#     image = image.resize((width,height))
#     image.save(fp='images/'+new_file_name)
#     print('your new image has been created!')
#     next_image = input('Type y or n to continue resizing images')
#     if next_image == 'n':
#         break










image = Image.open('images/bullet.png')
image = image.resize((15,30))
image.save(fp='images/bullet_small.png')