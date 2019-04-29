# Builder
FROM node:latest as builder
WORKDIR /usr/src/app
COPY package*.json ./ 
RUN npm install
COPY . .
RUN npm run build

# Server
FROM nginx:latest
COPY --from=builder /usr/src/app/dist/* /var/share/nginx/html/

EXPOSE 80