cd backend
docker build -t sweng_backend .

cd ../frontend
docker build -t sweng_frontend .

cd ..
docker run -d -p 80:80 sweng_backend
docker run -d -p 3000:3000 sweng_frontend