class SingletonClass:
    _instance = None

    # override this function
    def __new__(cls):
        if cls._instance is None:
                # create an object only if it has not been initalized before
            cls._instance = super(SingletonClass, cls).__new__(cls)
        return cls._instance
    def some_method(self):
        print("This is a method inside the SingletonClass")
# try it out
singleton1 = SingletonClass()
singleton2 = SingletonClass()
# check if they are the same object
print(singleton1 is singleton2)  # Output: True