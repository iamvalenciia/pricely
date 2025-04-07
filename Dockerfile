# Builder stage - you can use other AWS runtimes and python versions
FROM public.ecr.aws/lambda/python:3.12-x86_64 as builder

# Install Python packages (replace as needed)
RUN pip install --no-cache-dir requests numpy pandas tweepy dotenv --target "/var/task"

# Final stage
FROM public.ecr.aws/lambda/python:3.12-x86_64

# Copy necessary files from the builder stage - add whatever code you need
COPY --from=builder /var/task /var/task
COPY lambda_function.py ./

# Set the CMD to your lambda_function
CMD ["lambda_function.lambda_handler"]