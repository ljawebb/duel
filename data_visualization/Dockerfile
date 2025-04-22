FROM node:23-slim AS build
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN npm install
CMD ["npm", "run", "start-docker"]