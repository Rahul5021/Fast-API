from fastapi import Depends, FastAPI, Body
from app.models import BlogsSchema, UserLoginSchema, UserSchema
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import jwtBearer

blogs = [
    {
        "id":1,
        "title":"My first blog",
        "content":"This is my first blog post"
    },
    {
        "id":2,
        "title":"My second blog",
        "content":"This is my second blog post"
    },
    {
        "id":1,
        "title":"My third blog",
        "content":"This is my third blog post"
    }
]

users = []
app = FastAPI()

@app.get("/", tags=["test"])
def greet():
    return {"message": "Hello World"}

@app.get("/blogs", tags=["blogs"])
def get_posts():
    return {"data" : blogs}

@app.get("/blogs/{id}", tags=["blogs"])
def get_one_post(id : int):
    if id > len(blogs):
        return {
            "error": "Blog with this id doesn't exist"
        }
    for blog in blogs:
        if blog['id'] == id:
            return {
                "data" : blog
            }

@app.post("/blogs/", dependencies=[Depends(jwtBearer())], tags=["blogs"])
def add_blog(blog: BlogsSchema):
    blog.id = len(blogs) + 1
    blogs.append(blog.model_dump())
    return{
        "info" : "Blog Added Successfully"
    }

@app.post("/user/signup/", tags=["user"])
def user_signup(user: UserSchema = Body(default=None)):
    users.append(user)
    return signJWT(user.email)

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False
    
@app.post("/user/sigin/", tags=["user"])
def user_login(user: UserLoginSchema = Body()):
    if check_user(user):
        return signJWT(user.email)
    else:
        return{
            "error": "Invalid Credentials"
        }