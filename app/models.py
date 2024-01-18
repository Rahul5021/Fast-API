from pydantic import BaseModel, Field, EmailStr

class BlogsSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(default=None)
    content: str = Field(default=None)
    class Config:
        schema_extra = {
            "blog_demo " : {
                "title" : "title about the blog",
                "content" : "content of that blog"
            }
        }

class UserSchema(BaseModel):
    fullname: str = Field(default= None)
    email: EmailStr = Field(default= None)
    password: str = Field(default= None)
    class Config:
        the_schema = {
            "user_demo" : {
                "fullname": "John Doe",
                "email":"john.doe@gmail.com",
                "password":"1234567890"
            }
        }

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(default= None)
    password: str = Field(default= None)
    class Config:
        the_schema = {
            "user_demo" : {
                "email":"john.doe@gmail.com",
                "password":"1234567890"
            }
        }