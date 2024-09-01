class RailwayForm:
    # formType = "RailwayForm" # Not must
   #  name = ""  # If we don't use this, self.name, self.train
   #  train = "" # will have red mark
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")
Sagnik_Application = RailwayForm()
Sagnik_Application.name = "Sagnik"
Sagnik_Application.train = "Rajdhani Express"
Sagnik_Application.printData()
'''This code defines a Python class named `RailwayForm` and then creates an instance of that class. It sets specific attributes for the instance, and it calls a method to print information related to a railway application. Here's a step-by-step explanation of the code:

1. `class RailwayForm:`: This line defines a class named `RailwayForm`. Within this class, there are two components:
   - `formType = "RailwayForm"`: This is a class variable, shared by all instances of the class. It defines a class-level attribute `formType` with the value "RailwayForm," which is the default form type for all instances of this class.
   - `def printData(self):`: This is a method defined within the class. It's an instance method that takes `self` as its first parameter, which represents the instance it's called on. This method prints information related to the railway application, specifically the name and train attributes of the instance.

2. `Sagnik_Application = RailwayForm()`: This line creates an instance of the `RailwayForm` class and assigns it to the variable `Sagnik_Application`. This instance is now a specific representation of a railway application form.

3. `Sagnik_Application.name = "Sagnik"`: This line sets the `name` attribute of the `Sagnik_Application` instance to "Sagnik." This attribute is specific to this instance.

4. `Sagnik_Application.train = "Rajdhani Express"`: This line sets the `train` attribute of the `Sagnik_Application` instance to "Rajdhani Express." Like the `name` attribute, this attribute is specific to this instance.

5. `Sagnik_Application.printData()`: This line calls the `printData` method on the `Sagnik_Application` instance. Inside the `printData` method, it prints the name and train attributes of the instance using the `self` parameter. So, it will print:
   - "Name is Sagnik"
   - "Train is Rajdhani Express"

In summary, this code defines a class for a railway application form, creates an instance of that class, sets specific attributes for the instance, and then calls a method to print information related to the railway application using those attributes. The class-level attribute `formType` is shared among all instances, while the `name` and `train` attributes are specific to each instance.'''