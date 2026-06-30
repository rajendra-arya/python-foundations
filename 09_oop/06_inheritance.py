# class BaseChai:
#     def __init__(self, type_):
#         self.type = type_
    
#     def prepare(self):
#         print(f"Preparing {self.type} chai ...")

# #inheritance
# class MasalaChai(BaseChai): #inhereting Base Chai
#     #cant call this method  directly as it doesnt have constructor so self wont get any context
#     # either call it via the class, but how u will pass the context for self
#     # either create a obj and then call it
#     def add_spices(self):
#         print('Adding cardamom, ginger , cloves')

# #composition : taking refrence of class without inherting it : 
# class ChaiShop:
#     chai_cls = BaseChai #composition - holding the ref, which can used to create obj , to access the method of base class
#     # chai_cls = BaseChai() #creating the obj
#     def __init__(self):
#         self.chai = self.chai_cls("Regular") #creating obj from ref class just by passing it and storing it in a var
    
#     def serve(self): #now that obj can be used anywhere
#         print(f"Serving {self.chai.type} chai in the shop")
#         self.chai.prepare()


# class FancyChaiShop(ChaiShop): #inherting
#     chai_cls = MasalaChai #composition #compositing as well

# shop = ChaiShop()
# fancy = FancyChaiShop()

# shop.serve()
# # # chai shop class -> 
# # 1.get refrence of base chai(composition) -> 
# # 2.create obj of base chai  -> 
# # 3. access all properites var(type) & methods(prepare) from the base class refrence
# # 4. run current class methods with the help of base class obj propeties.

# fancy.serve()
# # fancyChaiShop ->
# # 1. inherit chai shop poperties 
# # 2. stores reference of Masala Chai class (composition)
# # 3. chaiShop class contains serve method which inherits properties of base class
#     # # chai shop class -> 
#     # 3.1.get refrence of base chai(composition) -> 
#     # 3.2.create obj of base chai  -> 
#     # 3.3. access all properites var(type) & methods(prepare) from the obj created by base class refrence -> 
#     # 3.4. run current class methods with the help of base class obj propeties.


# # self need to know who is calling it, so it can run accordingly with the current obj context.
# # # fancy.chai_cls.add_spices() #err:it needs to know which obj is calling
# fancy.chai.add_spices() #we gave context of inherited obj(chai) therefore the add_spices method got the context of the obj and ran the code successfully.

class Parent(): #shared memory allocation No, you cannot pass parameters during object creation without a constructor.
    msg = 'hello from parents'

class Base:
    def __init__(self): #unique memory allocation
        self.msg = "hello from base"

class Child(Parent):
    def __init__(self):
        self.ref_class = Base()

child_obj = Child()
print(child_obj.msg)
base_obj = Base()
print(base_obj.msg)

print(child_obj.ref_class.msg)