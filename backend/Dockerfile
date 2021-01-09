FROM openjdk:8-jdk-alpine
ARG WAR_FILE=build/libs/StockSafe_Spring-0.0.1-SNAPSHOT.war
COPY ${WAR_FILE} myboot.jar
ENV TZ Asia/Seoul
ENTRYPOINT ["java","-jar", "-Dspring.profiles.active=prod" ,"/myboot.jar"]
