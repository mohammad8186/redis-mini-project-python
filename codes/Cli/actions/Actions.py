
import redis
from Cli.actions.utils import encrypt
from Cli.actions.utils.encrypt import AESCipher
from Cli.actions.utils.encrypt import AESCipher
import json
#from redis_manager import  RedisManager




class Actions():
    CREATE = 'create'
    READ = 'read'
    UPDATE = 'update'
    LIST = 'list'
    DELETE = 'delete'
    REMAIN = 'rem'

    def __str__(self):
        return self.value.lower()





    
class Action():
    def __init__(self) -> None:
        self.r = redis.Redis(host='localhost', port=6379, decode_responses=True)
        #self.r = RedisManager.get_redis_connection()
        self._cipher = AESCipher()

    
    def create(self, name, description, key, exp):

        try:
            # Connect to Redis (adjust host and port as needed)


            # Encrypt the key (use your actual encryption method)
            encrypted_key = AESCipher().encrypt(key)  # Placeholder function

            # Create a dictionary with password properties
            password_object = {
                'name': name,
                'description': description,
                'encrypted_key': encrypted_key,
                'expiration_time': exp,
            }

            # Convert to JSON and store in Redis
            serialized_password = json.dumps(password_object)
            print(f"Serialized password: {serialized_password}")  # Debug statement
            self.r.setex(name, exp, serialized_password)

            # Print the corresponding password (for demonstration purposes)
            print(f"your Password is encrypted to  {encrypted_key}")

        except Exception as e:
            print(f"Error saving password: {str(e)}")





    def read(self, name):
        try:
            # Connect to Redis (adjust host and port as needed)


            # Retrieve the serialized JSON object by name
            serialized_password = self.r.get(name)
            print(serialized_password)
            if serialized_password:
                # Deserialize the JSON object
                password_object = json.loads(serialized_password)

                # Print password details
                print(f"Name: {password_object['name']}")
                print(f"Description: {password_object['description']}")
                print(f"Encryption password: {password_object['encrypted_key']}")
                print(f"Expiration Time (seconds): {password_object['expiration_time']}")
            else:
                print(f"No password found for name: {name}")

        except Exception as e:
            print(f"Error reading password: {str(e)}")





    def update(self, name, new_key):
        try:


            # Retrieve the existing password object
            existing_password_json = self.r.get(f"{name}")

            if not existing_password_json:
                print(f"Password with name '{name}' not found.")
                return

            existing_password = json.loads(existing_password_json)
            new_encrypted_key = AESCipher().encrypt(new_key)
            existing_password['encrypted_key'] = new_encrypted_key

            # Update the password object
            self.r.set(f"{name}", json.dumps(existing_password))

            print(f"your new encryption value is : {new_encrypted_key}")

        except Exception as e:
            print(f"Error updating password: {str(e)}")


    
    def delete(self, name):
        try:
            # Retrieve the existing password object
            redis_key = name
            existing_password_json = self.r.get(redis_key)

            if not existing_password_json:
                print(f"Password with name '{name}' not found.")
                return

            # Delete the password object
            self.r.delete(redis_key)

            print(f"Password deleted successfully")

        except Exception as e:
            print(f"Error deleting password: {str(e)}")




    def list(self):
        try:
        # Get all keys (encrypted keys) in the Redis database
         all_keys = self.r.keys()

         if all_keys:

            for encrypted_key in all_keys:
                password_object = self.r.get(encrypted_key)
                if password_object:
                    password_info = json.loads(password_object)
                    print(f"Name:  {password_info['name']} \n Description:  {password_info['description']} \n  Encryipted_password:  {password_info['encrypted_key']} \n  Expiration time: {password_info['expiration_time']}")
                    print("\n")
                else:
                    print(f"Error retrieving password for key: {encrypted_key}")
         else:
            print("No passwords found in the Redis cache.")

        except Exception as e:
         print(f"Error listing passwords: {str(e)}")



    def get_remaining_time(self , name):

        try:

            print(f"Checking remaining time for key: {name}")  # Debug statement
            # Retrieve the encrypted key associated with the given name
            encrypted_key = self.r.get(name)
            print(encrypted_key)
            if encrypted_key is not None:
                # Get the remaining time (in seconds) until expiration
                remaining_time = self.r.ttl(name)
                print(remaining_time)

                if remaining_time >= 0:
                    print(f"Remaining time for '{name}' is : {remaining_time} seconds")
                else:
                    print(f"'{name}' has already expired and been deleted.")
            else:
                print(f"No password found for '{name}'.")

        except Exception as e:
            print(f"Error retrieving remaining time: {str(e)}")
