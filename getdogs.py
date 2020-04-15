
# import urllib.request # python 3
import urllib # python 2
import os
## from config import output_folder

output_folder = "dogs/"
base_dog_url = "https://images-na.ssl-images-amazon.com/images/G/01/error/"

def get_dog_url(dog_number):
    return base_dog_url + str(dog_number) + "._TTD_.jpg"

def store_single_dog(dog_number, output_folder):
    dog_image_url = get_dog_url(dog_number)
    # urllib.request.urlretrieve(input_path, output_folder + "Dog_" + str(dog_number) + ".jpg") # python 3
    dog_image_path = output_folder + "Dog_" + str(dog_number) + ".jpg"
    
    if not os.path.isdir(output_folder):
        os.mkdir(output_folder)

    if os.path.isfile(dog_image_path):
        print "Warning: Image for dog #" + str(dog_number) + " already exists in " + output_folder + ". Skipping"
    else:
        urllib.urlretrieve(dog_image_url, dog_image_path)

failure = False
dog_index = 1
print "hi"
while (not failure):
    try:
        print "Trying dog # " + str(dog_index)
        store_single_dog(dog_index, output_folder)
        print "Dog # " + str(dog_index) + " successfuly stored."
        dog_index = dog_index + 1
    except Exception, e: # works on python 2.x
        print " ----- failed dog # " + str(dog_index) + "\n" + str(e)
        failure = True


print "Terminating"