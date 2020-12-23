"""
    Hoang Nguyen
    METCS 521 O2
    Term Project

    Project Description: The program is designed to take the csv file, store in
    the dictionary. The class contains several methods to calculate size of
    the data, the average magnitude, and show top ten earthquakes with
    local time, magnitude and depth information. The dataset is a single
    location in Salt Lake City, Utah.
"""
from collections import Counter

""" Class Quake Reader has the constructor stores mag, dep and a private
    attributes location. The class has the following methods in the class;
    total_quake, highest magnitude, average magnitude, string, and repr method.
"""
class Quake_Reader:
    # Constructor store magnitude, depth and private location
    def __init__(self, mag, dep, __location='Salt Lake City'):
        self.depth = dep
        self.magnitude = mag
        self.location = __location

    """ __get location method returns the private location"""
    def __get_location(self):
        return self.location

    """ Total Quake method returns the total size in the dataset """
    def total_quake(self):
        return len(quake_list)

    """ This method returns the max value of magnitude and depth in the dataset 
    """
    def highest_mag(self):
        max_value = max(quake_list.values())
        return max_value

    """ 
        Top five magnitude method shows the top 5 magnitude that occurred
        at a local time, mangnitude and depth in km.
    """
    def five_largest(self):
        k = Counter(quake_list)
        high = k.most_common(5)
        print("According to the dataset, there were 5 largest quakes "
              "occured at:")
        print("Local Time: %-*s  Magnitude: %s Depth in km: " % (0, "", ""))
        print("-" * 35)
        [print(key, value) for key, value in high]

    """ 
        Average magnitude method calculates the average magnitude in the 
        dataset store in a dictionary. The function return the average.
    """
    def avg_magn(self):
        sum = 0
        for key in quake_list.keys():
            sum = float(sum) + float(len(quake_list[key]))
        average = float(sum / float(len(quake_list)))
        return average

    """
        Quake category method determines earthquake category based on the 
        average magnitude using the if condition. When the method is called it 
        will print the earthquake category.
    """
    def quake_category(self):
        if self.avg_magn() > 8:
            print("The magnitude was great.")
        elif 7 < self.avg_magn() < 8:
            print("The magnitude was a major earthquake.")
        elif 6 < self.avg_magn() < 6.9:
            print("It was a strong earthquake.")
        elif 5 < self.avg_magn() < 5.9:
            print("It was a moderate earthquake.")
        elif 4 < self.avg_magn() < 4.9:
            print("It was a light earthquake.")
        else:
            print("It was a minor earthquake.")

    """ 
        String method calls the total quake method to print out the size of
        data, calls the highest magnitude and depth method to print the 
        magnitude and depth, and calls the average magnitude method to display 
        the average magnitude and earthquake category of the average magnitude.   
    """
    def __str__(self):
        print("The total of {} earthquakes in the dataset"
              .format(self.total_quake()))
        print("The highest magnitude and depth in km was {}"
              .format(self.highest_mag()))
        print("The average magnitude is", self.avg_magn()), \
            self.quake_category()
        print("***" * 22)

    """ repr method return the __str__ method """
    def __repr__(self):
        return self.__str__()


""" 
    Unit Tests. Test data size method check the total_quake method in the class
    is greater than 0 and print the size. Test category test method check the
    magnitude is at least 0 or greater
"""
def test_data_size(total_quake):
    assert total_quake > 0
    print("Test the total size of", total_quake.__sizeof__())

def test_category(quake_category):
    assert quake_category >= 0
    print("Test the magnitude value of", quake_category.__repr__())


""" 
    Main function opens the csv file and check to make sure the file is existed.
    If the file exits, the program read the dataset and stores in a dictionary
    of class quake reader. The main function calls the methods of the class and
    print the result of the calculation and information from the class.
"""
if __name__ == '__main__':
    # instantiate quake reader class
    qr = Quake_Reader(0, 0, "City")
    try:
        # create an empty dictionary
        quake_list = dict()
        # open the source data
        with open('earthquakes.csv', 'r') as csv_file:
            # loop through the file and store the data in an empty quake
            # dictionary
            for key, value in enumerate(csv_file):
                line, *lines = value.split(',')
                lines = [float(value) for value in lines]
                if line in quake_list:
                    quake_list[key] = lines
                else:
                    quake_list[line] = lines
            # # closed the input file
            csv_file.close()
    except FileNotFoundError:
        print("File doesn't exist.")
        exit()
    # Call the string method in the quake reader class to print the earthquake
    # information
    qr.__str__()
    # Call top five method in the quaker reader class to print the top 5 largest
    # earthquake occurred at local time, magnitude and depth in km
    qr.five_largest()
    print()

    # call the unit tests to make sure the data size and earthquake category
    # method works
    print("Unit tests call")
    print("***"*9)
    test_data_size(1)
    test_category(5.4)
