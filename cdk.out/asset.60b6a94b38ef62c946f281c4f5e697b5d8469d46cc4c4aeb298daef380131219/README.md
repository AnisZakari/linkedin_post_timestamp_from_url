## build
docker build -t linkedin-time-app .

## test locally:

```bash
payload='{"linkedin_url":"https://www.linkedin.com/posts/alliekmiller_goodbye-mouse-clicks-othersideai-hyperwrite-ugcPost-7093310227491500032-TQ81?utm_source=share&utm_medium=member_desktop"}'
docker run -p 9000:8080 linkedin-time-app:latest & curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d $payload
```
