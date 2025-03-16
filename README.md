Folder structure:
```
.
├── app
│   ├── __init__.py
│   └── main.py
├── Dockerfile
├── requirements.txt
└── env
```
Build image:
```bash
docker build -t fastapi_learn .
```
Launch app:
```
docker run -d -p 8000:80 fastapi_learn
```  

Visit:
1. http://127.0.0.1:8000/ 
1. http://127.0.0.1:8000/docs


