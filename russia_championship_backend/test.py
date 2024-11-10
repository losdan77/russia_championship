import asyncio

def delete_password_and_role(func):
    async def wrapper():
        user_dict = await func()
        exclude_key = ['hashed_password', 'role']
        for key in user_dict.copy():
            if key in exclude_key:
                del user_dict[key]
        return user_dict
    return wrapper

@delete_password_and_role
async def return_dict():
    test_dict = {
  "id": 1,
  "email": "user@example.com",
  "hashed_password": "$2b$12$cpFI8Lgg2v2FG3VOonuzKufdWevMS7OcH.H4.EcHSUNk35wt7JLci",
  "role": None,
  "created_at": "2024-11-02T20:46:49.640575",
  "photo_url": None
}
    return test_dict

result = asyncio.run(return_dict())
print(result)

# test_dict = {
#   "id": 1,
#   "email": "user@example.com",
#   "hashed_password": "$2b$12$cpFI8Lgg2v2FG3VOonuzKufdWevMS7OcH.H4.EcHSUNk35wt7JLci",
#   "role": None,
#   "created_at": "2024-11-02T20:46:49.640575",
#   "photo_url": None
# }

# exclude_key = ['hashed_password', 'role']

# for key in test_dict.copy():
#     if key in exclude_key:
#         del test_dict[key]

# print(test_dict)