FROM public.ecr.aws/lambda/python:3.10

COPY app.py requirements.txt ./

RUN pip install -r requirements.txt

CMD ["app.lambda_handler"]