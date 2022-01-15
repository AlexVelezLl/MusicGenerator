
# Train the model using Google AI Platform

For running the training you need:

* The single file dataset
* The lookup_table with the keys needed to represent the notes

For running the train you must first set the following environment variables:

* IMAGE_URI (Your docker image uri format: "gcr.io/[project_id]/[image_repo_name]:image_tag")
* MODEL_DIR (Your model output direction on Cloud Storage)
* JOB_NAME (The name of the job that will execute the train)

Example:

```bash
export IMAGE_URI=gcr.io/bda-espol/ai-model:music-generator
export MODEL_DIR=gs://ai-model-h5/model_$(date +%Y%m%d_%H%M%S).h5
export JOB_NAME=job_$(date +%Y%m%d_%H%M%S)
```

For building the docker you can execute the following command:

```bash
docker build -f Dockerfile -t $IMAGE_URI ./
```

After building the model you must push it to the Google Container Registry. (First, run `gcloud auth configure-docker` if you have not already done so).

```bash
docker push $IMAGE_URI
```

Finally, to run the training you can run the following command:

```bash
gcloud ai-platform jobs submit training $JOB_NAME \
  --region us-central1 \
  --master-image-uri $IMAGE_URI \
  -- \
  --model $MODEL_DIR \
  --epochs 64
```

After this, you can find your model trained at $MODEL_DIR in Google Cloud Storage, donwload the file, and replace the current model with it (Or copy it into the project and change the constant variable DEFAULT_MODEL_PATH on AIModel/constants).

Notes:

* You must generate the variables MODEL_DIR and JOB_NAME before running the training command in order to avoid duplicated jobs/models names.
* If you change the code, you must build and push the docker container again.
