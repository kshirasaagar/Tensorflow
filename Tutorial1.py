
#Pointing to the right Google project
gcloud config set project ml-learning-1987

#Install the latest version of TensorFlow (1.0, RC2) with the following 2 command lines.
pip download tensorflow
pip install --user -U tensorflow*.whl

#List models available
gcloud ml-engine models list

#Copying Youtube repo
git clone https://github.com/google/youtube-8m.git

python --version
python -c 'import tensorflow as tf; print(tf.__version__)'

gcloud ml-engine local train \
--package-path=youtube-8m --module-name=youtube-8m.train -- \
--train_data_pattern='gs://youtube8m-ml/1/video_level/train/train*.tfrecord' \
--train_dir=/tmp/yt8m_train --model=LogisticModel --start_new_model

# Downloads 55MB of data.
gsutil cp gs://us.data.yt8m.org/1/video_level/train/traina[0-9].tfrecord .
