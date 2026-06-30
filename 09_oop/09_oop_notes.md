# OOP
- Object Oriented Programming is a paradigm of writing code means its just another way(evolved from C++ era and adopted by other lang)
- Class is a blueprint used to create objects.
- naming convention : 
    - for class : CapWords (PascalCase) 
        - Pascal Case originated from the Pascal programming language,
    - for instance: snake_case
- define class : `class Class_name:`
- create object : `object1  = Class_name()`
- inside class u can have anything generator , function etc, its just a wrapper.
- variable inside the class are called properties
- ```py
    class Class_name:
        pass
    
    object1  = Class_name()
    ```

> Note: Everything in python is an object, it's an object lang(even though u see class dataype but internally it's  an obj)

## Namespace
- Each object has its own namespace, which is isolated from another objects(made from same class)
- you can modify existing class properties or can add multiple propeties.
- the base class will be act as a template only.
- code example left:
    - ```py
        class Chai:
        origin = "India"

        print(Chai.origin) #India

        #adding new property in the class from outside
        Chai.is_hot = True
        print(Chai.is_hot) #True


        # creating obj from class chai
        masala = Chai() 
        print(masala) # print chai class obj refrence
        
        print(f'Masala {masala.origin}')
        print(f'Masala {masala.is_hot}')
        #<__main__.Chai object at 0x0000021F4EB96F90>
        # Masala India
        # Masala True

        # modifing default value
        masala.is_hot = False

        print(f'Masala {masala.origin}')
        print(f'Masala {masala.is_hot}')

        # Masala India
        # Masala False

        #-> each namespace has its own namespace

        # adding one more prop in the the obj
        masala.flavour = "Masala"
        print(masala.flavour)
        #Masala
    ```


## Attribute Shadowing
- Attribute are variable in the class
- Attribute Shadowing: 
    - Attribute shadowing in Python occurs when an instance attribute shares the exact same name as a class attribute. 
    - Because Python looks up names on the instance level before checking the class level, the instance attribute hides (shadows) the class attribute during lookup.
    - 
- How Attribute Shadowing Works technically:
    - When you access object.attribute, Python follows a specific lookup chain (Namespace):
        1. It first checks the instance's own dictionary (self.__dict__).
        2. If it is not found there, it falls back to the class dictionary (Class.__dict__).

- Why its called Shadowing?
    - It is called "shadowing" because it mimics how a physical object blocks light. The newer, inner-scope attribute stands "in front of" the original outer-scope attribute.

- Usecase:
    1. When u modify a already existing parent class attribute value
        - delete that class attribute from that object
        - it falls back to its orignal class attribute whenever u call it.
        - means the shadow of class attribue always there as a fallback option. 
        - it means it act as fallback value, which removes error
    2. If u create new attribue which doesn't exist in the class
        - delete that attribute from that object
        - it will give error 
        - beacasue that attribute doesn't exist in the class in the firstplace.
        - attribute shadowing can't happen here.

    - example :
    ```py

    class Chai:
        temp = "hot"
        stength = "Strong"

    cutting = Chai()
    print(cutting.temp)

    cutting.temp = 'Mild'
    print('After changing temp: ', cutting.temp) # Mild
    print('Original Class temp: ', Chai.temp)    # hot

    # deleting obj propety using deletion operator(del)
    del cutting.temp
    print('After del temp from Cutting : ', cutting.temp)  #will fall back to orginal class attribute
    #hot

    #adding new prop to obj
    cutting.cup = 'small'
    print('cup size is', cutting.cup)

    del cutting.cup
    print('cup size is', cutting.cup) #will throw errror, as its not in orginal class too so no fallback
    # > AttributeError: 'Chai' object has no attribute 'cup'
    ```


## Self argument
- functions inside the class are called methods
- `self` :  used in class method as an argument
    - gives the refrence(access) of class properties(var) inside the class methods.
- we can call the method using 
    - obj.methoname()
    - classname.methodname(objname) #as it need to context otherwise throw error
- Why self is Required? :
    - When you define a regular method inside a class, its first argument must be self. 
    - This parameter acts as a placeholder for a specific, individual object instance.
    - Instance Call: 
        - When you run `cup_obj.describe()`
        - Python automatically converts that under the hood to `Chaicup.describe(cup_obj)`
        - The object `cup_obj` passes itself in as the self argument automatically.
    - Class Call: 
        - When you run `Chaicup.describe()`, you are calling the method directly on the blueprint (the class), without an instance refrence. 
        - Because no object exists in this context, Python has nothing to pass into self. 
        - It looks for that required argument, finds nothing, and throws the TypeError.

- ```py
    class Chaicup:
    size = 150 #ml

    def describe(self):
        # return print(f'A chai cup of {self.size} ml.') # print display and return none (remember)
        return f'A chai cup of {self.size} ml.'
    

    cup_obj = Chaicup()
    print(cup_obj.describe()) # passes the cup obj to self argument automatically

    # print(Chaicup.describe()) # trigger error as it needs context 
    # TypeError: Chaicup.describe() missing 1 required positional argument: 'self'

    print(Chaicup.describe(cup_obj)) 


    cup2_obj = Chaicup()
    cup2_obj.size = 50
    print(cup2_obj.describe())
    print(Chaicup.describe(cup2_obj))

    #output
    #A chai cup of 150 ml.
    #A chai cup of 150 ml.
    #A chai cup of 50 ml.
    #A chai cup of 50 ml.

    ```

- **Findings : The Fix :**
    - If you want a method to run directly from the class without an object, use the `@staticmethod` decorator to remove the need for self.


## Constructors and init
- whenever an obj is created its always created via the constructor 
- if its not present explicitly the class automatically create a constructor bts.
 - __init__ aka initialization creates a constructor.
    - __init__ Initialises Data: It does not create the object.
    - it only sets up its attributes automatically upon creation.
 - Python syntax requires self as the first argument in class methods so the method knows which object's data to use
     - `self ` is a Pointer: It must be the first argument so methods know exactly which object's data to use.
- constructor runs by default whenever a new instance/obj created by that class.
- we can intialize the class with any values by passing it in constructor
- Dynamic Customisation: You can pass unique data into the class brackets to customise each individual object.
- Default  - Values: You can set fallback values in __init__ parameters (e.g., size=150) in case data is missing.
-  You cannot pass parameters during object creation without a constructor.

 > common practice in production using Trailing Underscore (type_), it's a standard (PEP 8) to avoid clashing with Python's reserved keywords.

 ```py
    class ChaiOrder:
        # Runs automatically to initialize object data
        def __init__(self, type_, size):
            self.type = type_  # Trailing underscore avoids reserved keyword clash
            self.size = size   # self references the specific instance created
        
        # Method to read instance data using self
        def summary(self):
            return f"{self.size} ml of {self.type} chai."

    # Instantiates first object (self maps to order_1)
    order_1 = ChaiOrder('Masala', 150)
    print(order_1.summary())

    # Instantiates second object (self maps to order_2)
    order_2 = ChaiOrder('Lemon', 100)
    print(order_2.summary())
 
 ```

## Inheritance and Composition
24,25/06/2026
### inheritance :
- passing propeties of one class to another.
- "is-a" relationship (e.g., a Dog is an Animal).
- The child class automatically gets the methods and properties of the parent class.
- `class ChildClass(ParentClass):`
    - 
    - ```py
        class BaseClass:
            def __init__(self):
                self.property = "Hello from Base"

        # Inheriting from BaseClass
        class ClassName(BaseClass):
            pass

        # Usage
        obj = ClassName()
        print(obj.property)  # Prints: Hello from Base
        ```

### composition :
- "has-a" relationship (e.g., a Car has an Engine).
- Instead of inheriting, we instantiate the other class inside our new class
- creating the obj of one class in another class. 
- `self.variable = OtherClass()`
- ```py
        class BaseClass:
            def __init__(self):
                self.property = "Hello from Base"

        # Composing with BaseClass
        class ClassName:
            def __init__(self):
                # Create an instance of BaseClass inside this class
                self.ref_class = BaseClass() 

        # Usage
        obj = ClassName()
        print(obj.ref_class.property)  # Prints: Hello from Base


    ```
- when taking refence of a class, u dont need parentheses.
- creating obj(with parenthes) vs creating classes(without parenthes) are two different story one taking reference and other creating obj.

- ```py
    class BaseChai:
        def __init__(self, type_):
            self.type = type_
        
        def prepare(self):
            print(f"Preparing {self.type} chai ...")

    # #inheritance
    class MasalaChai(BaseChai): #inhereting Base Chai
    #     # can't call this method  directly as it doesn't have constructor so self wont get any context
    #     # either call it via the class, but how u will pass the context for self
    #     # u can create a obj and then call it
        def add_spices(self):
            print('Adding cardamom, ginger , cloves')

    #composition : taking refrence of class without inherting it  
    class ChaiShop:
        chai_cls = BaseChai #composition - holding the ref, which can used to create obj , to access the method of base class
        # chai_cls = BaseChai() #creating the obj
        def __init__(self):
            self.chai = self.chai_cls("Regular") #creating obj from ref class just by passing it and storing it in a var
        
        def serve(self): #now that obj can be used anywhere
            print(f"Serving {self.chai.type} chai in the shop")
            self.chai.prepare() #calling method of base class using composed obj of class


    class FancyChaiShop(ChaiShop): #inhertance
        chai_cls = MasalaChai #composition #compositing as well

    shop = ChaiShop()
    fancy = FancyChaiShop()

    shop.serve()
    # working: chai shop class -> 
    # 1.get refrence of Base chai class (composition) -> 
    # 2.create obj of base chai  -> 
    # 3. access all properites var(type) & methods(prepare) from the base class refrence
    # 4. run current class methods with the help of base class obj propeties.

    fancy.serve()
    # working: FancyChaiShop ->
    # 1. inherit chai shop poperties 
    # 2. stores reference of Masala Chai class (composition)
    # 3. chaiShop class contains serve method which inherits properties of base class
        # # chai shop class -> 
        # 3.1. get refrence of base chai(composition) -> 
        # 3.2. create obj of base chai  -> 
        # 3.3. access all properites var(type) & methods(prepare) from the obj created by base class refrence -> 
        # 3.4. run current class methods with the help of base class obj propeties.


    # imp : self need to know who is calling it, so it can run accordingly with the current obj context.

    fancy.chai_cls.add_spices() #err:it needs to know which obj is calling

    # giving self a context (even inherited obj works)
    fancy.chai.add_spices() #we gave context of inherited obj(chai) therefore the add_spices method got the context of the obj and ran the code successfully.

    ```
- Extra notes:
> "Favor object composition over class inheritance." — Design Patterns (Gang of Four)
> - Use Inheritance only when a child class is a strict subtype of the parent and will never need to drop its inherited traits.
> - Use Composition for everything else to keep your code modular, scalable, and easy to update.
> **_Composition is preferred in modern software design because it creates loosely coupled, flexible code that does not break when requirements change_**

- Difference worth reading of Class Attribute (No Constructor) and Instance Attribute (Inside Constructor):

| Feature | Class Attribute (No Constructor) |  Instance Attribute (Inside Constructor) |
|--|--|--|
| Memory Allocation | Allocated once per class definition | Allocated fresh for every single object |
| Initial Values | Exactly the same for all objects | Can change per object via arguments |
| Primary Use Case | Constants, configuration, global state | Object state, unique properties, setup |



## 3 ways to access Base Class
- For accessing base properties and adding more properties in new class we use 3 appoches:
```py
    #Base Class 
    class BaseChai:
        def __init__(self, type_, strength):
            self.type = type_
            self.strength = strength
```

1. Code Duplication
    - we repeat same code in the child class too
    - not recommended
    - ```py
        # Approch 1: Code duplication 
        class GingerChai(BaseChai):
            def __init__(self, type_, strength, spice_level):
                self.type = type_ #code repetition
                self.strength = strength #code repetition
                self.spice_level = spice_level

        obj = GingerChai('s','strong','light')
        print(obj.spice_level)
        ```
2. Explicit call
    - we call the base class constructor explicitly to get existing attributes
    - ```py
        # Approch 2: Explicit Call
        class GingerChai(BaseChai):
            def __init__(self, type_, strength, spice_level):
                BaseChai.__init__(self,type_, strength) #explicitly calling the constructor of the inhereted class
                self.spice_level = spice_level

        obj = GingerChai('s','strong','light')
        print(obj.spice_level) #output: light
        ```
3. Super()
    - we use super method which automatically calls the base class constructor
    - removes the need of writing base class explicitly.
    - **its most used method for accesing parent/base class**.
    - ```py
        # Approch 3: Super (most preferred)
        class GingerChai(BaseChai):
            def __init__(self, type_, strength, spice_level):
                super().__init__(type_, strength) #calling the base call using super()
                self.spice_level = spice_level #adding additional propeties

        obj = GingerChai('s','strong','light')
        print(obj.spice_level) #output: light
        ```

## MRO : Multi Resolution Order
- Helps to understand priorty order of inheritance in Multiple inheritance scenario.
- it tells which class property will be inherited in multiple inheriance.
- Rule : it picks the property from the first inhereted class(i.e first class parameter) 
- concept:
    ```py 
        class C(A,B):
            pass
        obj = C()
        #here class A propeties will be inhereited 
        ```
        
- ```py
    # Method Resolution Order(mro)
    class A:
        label = "A: Base Class"

    class B(A):
        label = "B: Masala blend (inherited A)" #overwrites label

    class C(A):
        label = "C: Herbal blend (inherited A)" # B: overwrites label

    class D(B, C): #inheriting B and C
        pass  #it doesn't have any label so it will look in inherited class

    cup = D()
    print(D.label) # B: Masala blend (inherited A)
    # it picks the property from the first inhereted class so position matters.

    print(D.__mro__) #mro dunder
    # (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
    # inhertance chain : D -> B -> C -> A 
    ```
    - usecase : can be helpful when u manipulating the internals of frameworks like fastapi.

## Static methods (@staticmethod)
- `@staticmethod` is a built-in decorator placed directly above the method inside the class.
- State Independent: It defines a method that is completely independent of any specific class instance (self) or class state (cls)
- No Object creation Required: 
    - u can call the method directly using the classname without creating object.
    - It does not require object creation to function.
    - it turns the method into a plain, regular function inside the class namespace.
- Flexible Calling: 
    - You can call the method directly using the classname (`Class.method()`), 
    - but Python also allows you to call it via an instance (instance.method()) without crashing.
- No Hidden Arguments: Internally, it triggers Python's descriptor protocol to ensure zero implicit arguments (like `self`) are passed to the function when executed.
-  ```py
    # class ChaiUtils:
    #     def clean_ingredients(self, text):
    #         return [item.strip() for item in text.split(',')]

    # raw = "    water,     milk ,  giner  ,   honey      "

    # cleaned = ChaiUtils()
    # print(cleaned.clean_ingredients(raw)) 
    # Output: ['water', 'milk', 'giner', 'honey']


    #with static method
    class ChaiUtils:
        def clean_ingredients(text): # No self here!
            return [item.strip() for item in text.split(',')]

    raw = "    water,     milk ,  giner  ,   honey      "

    cleaned = ChaiUtils.clean_ingredients(raw)
    print(cleaned) #['water', 'milk', 'giner', 'honey']
    ```
<!-- - From python 3 - The Rule
    - For Class call for properties:
        - (ChaiUtils.method()): Decorator is optional.
    - Instance call  for propeties
        - Decorator is mandatory
        - (obj.method()): Decorator is mandatory. -->
- The Accurate Rule for Python 3 Methods
    - Class Calls (ChaiUtils.method())
        - No Decorator: Works fine only if the method behaves like a plain function and takes no self or cls arguments.
        - @classmethod Decorator: Mandatory if the method needs to access class properties via the cls argument.
    - Instance Calls (obj.method())
        - No Decorator: Standard behavior. No decorator is needed for normal methods because Python automatically passes obj into the self argument.
        - @staticmethod Decorator: Mandatory only if the method does not have self in its arguments, to stop Python from crashing.

## Class methods (@classmethod)
- static methods are never designed to initialize any obj
- class method are used to control the intilization
- it modify the constructor using class method
- the `cls` contains the reference of the class
- the class method also doesn't need obj creation just like static method.
- `__dict__` : gives class contructor values in dictonary format
- class doesn't get `self` just lie static method
- ```py
    class ChaiOrder:
        def __init__(self, tea_type, sweetness, size ): #constructor
            self.tea_type = tea_type
            self.sweetness = sweetness
            self.size = size
        
        @classmethod # modifying constructor properties on initlization by calling following method
        def from_dict(cls, data): # cls gives the refrence of class, also this method doesnt need obj creation
            return cls(
                data['tea_type'],
                data['sweetness'],
                data['size']
            )
        
        @classmethod # modifying constructor properties on initlization by following method
        def from_string(cls, data): #first argument is always cls not self and it doesn't need obj creation
            tea_type, sweetness, size = data.split(',')
            return cls(tea_type, sweetness, size) #returs cls
        
        @staticmethod # method without need of creation of obj
        def welcome(): #it doesn't need any argument
            return 'Namaste! How may i help you?'


    obj1 = ChaiOrder('masala','low','md')
    # print(obj1) #__main__.ChaiOrder object at 0x00000219C2D56F90>
    # print(obj1.__dict__) #{'tea_type': 'masala', 'sweetness': 'low', 'size': 'md'}

    # order 2 #calling without obj creation
    print(ChaiOrder.from_dict({'tea_type':'ginger','sweetness':'medium','size':'sm'}).__dict__)

    print(ChaiOrder.from_string('lemon,low,lg').__dict__) # {'tea_type': 'masala', 'sweetness': 'low', 'size': 'md'}

    print(ChaiOrder.welcome()) #Namaste! How may i help you?
    ```

## Property Decorators (getter and setter)
- aka properties, getters and setters
- it solves the purpose of controling the elements.
- Reading and setting value can be controlled using it.
    - we can hide the class value and also add restriction/rule in modifying the class attriute.
- _ means this property should not to be read directly, python also knows this
    - it's kinda a secrete handshake between programers that this is how we define it, anything with that starts with _ means it needs to have getter and setters.

- Mail Goal :
    1. how we read the propety values. eg. a -> a+2
    2. how we edit the propety values. eg. add conditon for editing

-   ```py
    class TeaLeaf:
    def __init__(self, age):
        self._age = age #_ as prefix for hiding the value , python treat this as "age" only

    @property #getter - for reading
    def age(self): #python knows this attribute and treat this as "age" only
        return self._age + 2
    
    @age.setter #setter - for editing , also py make the 'age' a decorator automatically
    def age(self, age): 
        if (1<=age<=5): #adding condition for editing
            self._age = age
        else:
            raise ValueError("Tea Leaf age must be between 1 to 5 years.")
            
    #getting value
    leaf = TeaLeaf(3)
    print(leaf.age) #5

    #setting value
    leaf.age = 11
    print(leaf.age) #throw our defined error

    ```

