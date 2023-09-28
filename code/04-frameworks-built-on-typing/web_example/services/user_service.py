from typing import Optional

# why argon?
# https://research.redhat.com/blog/article/how-expensive-is-it-to-crack-a-password-derived-with-argon2-very/
from passlib.handlers.argon2 import argon2 as crypto

from models.user import User, Location

crypto.default_rounds = 25  # about 225ms of work


async def user_count() -> int:
    return await User.count()


async def create_user(name: str, email: str, password: str,
                      profile_image_url: Optional[str], location: Location) -> User:
    email = email.lower().strip()
    name = name.strip()
    password = password.strip()

    if await user_by_email(email):
        raise Exception(f"User already exists with {email}.")

    hash_password = crypto.encrypt(password)
    user = User(name=name, email=email, hash_password=hash_password,
                profile_image_url=profile_image_url, location=location)

    await user.save()

    return user


async def user_by_email(email: str) -> Optional[User]:
    email = email.lower().strip()
    return await User.find_one(User.email == email)
