FROM public.ecr.aws/lambda/python:3.8

COPY ./requirements.txt .

RUN pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"
#https://docs.datadoghq.com/serverless/installation/python/?tab=containerimage
COPY --from=public.ecr.aws/datadog/lambda-extension:latest /opt/extensions/ /opt/extensions

COPY lambda.py ${LAMBDA_TASK_ROOT}
COPY logging.conf ${LAMBDA_TASK_ROOT}
COPY ./helloworld ${LAMBDA_TASK_ROOT}/helloworld

ARG DD_KEY
ARG APP_VERSION

ENV DD_LAMBDA_HANDLER="lambda.handler"
ENV DD_SITE="us5.datadoghq.com"
ENV DD_API_KEY="142951d5205dd5db431314539ed069a9"
ENV DD_VERSION="$APP_VERSION"
ENV DD_TRACE_ENABLED="true"
CMD [ "datadog_lambda.handler.handler" ]