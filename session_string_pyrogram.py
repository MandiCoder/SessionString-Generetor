from pyrogram import Client
import asyncio

async def stringGenerate():
    api_id = input("Api ID: ")
    api_hash = input("Api Hash: ")
    client = Client("memory", api_id, api_hash)
    await client.connect()
    
    bolean = input("You have double factor? y/n: ")
    
    phone_number = input("Insert your phone number: ")
    
    if bolean == 'y':
        password = input('Insert your double factor: ')
        await client.check_password(password=password)
        
    print("Sending code to telegram... \n")
    code = await client.send_code(phone_number)
    
    phone_code_msg = input("Insert registration code: ")
    
    await client.sign_in(phone_number, code.phone_code_hash, phone_code_msg)
    
        
    
    
    string_session = await client.export_session_string()
    
    with open('string_session.txt', 'w') as r: 
        r.write(string_session)
        
    print(f"Session String:\n\n{string_session}")
    
    
if __name__ == "__main__":
    asyncio.run(stringGenerate())