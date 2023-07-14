# FROM node:16-alpine as build-stage
FROM node:18.12.1-buster-slim AS build-stage


WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install
COPY . .
COPY public/ public/
COPY src/ src/
RUN npm ci
RUN npm run build
RUN npm run build


# FROM nginx:1.21.6-alpine
FROM nginx:1.23.2-alpine


COPY ./nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build-stage /app/build /usr/share/nginx/html
RUN touch /var/run/nginx.pid
RUN chown -R nginx:nginx /var/run/nginx.pid /usr/share/nginx/html /var/cache/nginx /var/log/nginx /etc/nginx/conf.d
USER nginx
EXPOSE 5000
CMD ["nginx", "-g", "daemon off;"]

