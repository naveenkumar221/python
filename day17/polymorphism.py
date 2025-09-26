# Polymorphism: function with same name behaving differently in different classes.

# Abstraction: it is a phenom



# class Dog():
#     def speak(self):
#         return "Woof!"

# class cat():
#     def speak(self):
#         return "Meow!"

# class lion():
#     def speak(self):
#         return "Roar!"

# def animal_sound(animal):
#     print(animal.speak())

# dog = Dog()
# cat = cat()
# lion = lion()   

# animal_sound(dog)
# animal_sound(cat)
# animal_sound(lion)
    


class SendSMG():
    def send(self,Message):
        print(f'sending message: {Message}')

class SendEmail():
    def send(self,Message):
        print(f'sending email: {Message}')

class SendNotification():
    def send(self,Message):
        print(f'sending notification: {Message}')

def send_message(sender, Message):
    sender.send(Message)


send_message(SendSMG(),"hi your otp is 34567")
send_message(SendEmail(),"hi your otp is 34567")
send_message(SendNotification(),"hi your otp is 34567")



# Example usage
sms_sender = SendSMG()
email_sender = SendEmail()
notification_sender = SendNotification()


send_message(sms_sender, "Hello via SMS!")
send_message(email_sender, "Hello via Email!")
send_message(notification_sender, "Hello via Notification!")

# Example of polymorphism with different classes        
# This code demonstrates polymorphism by using different classes that implement the same method `send`.
# Each class has its own implementation of the `send` method, but they can all be used interchangeably in the `send_message` function.
# Example of polymorphism with a single class
# class MessageSender():
#     def send(self, Message):
#         print(f'sending message: {Message}')  
# def send_message(sender, Message):
#     sender.send(Message)      

# # Example usage
# sender = MessageSender()
# send_message(sender, "Hello, this is a message!")
# This code demonstrates polymorphism by using a single class that implements the `send` method.
# The `send_message` function can accept any object that has a `send` method, allowing for flexibility in how messages are sent.



