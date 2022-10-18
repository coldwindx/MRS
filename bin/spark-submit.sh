ModelType=demo

CUR_PATH=$(cd "$(dirname "$0")";pwd)
echo $CUR_PATH

SPARK_PATH=/opt/spark
YARN_QUEUE=

DEPLOY_MODE=cluster
DEPLOY_MODE=client

input_path_train=hdfs://
input_path_test=hdfs://
output_path=hdfs://datasets/${ModelType}

hadoop fs -rmr $output_path

${SPARK_PATH}/bin/spark-submit \
 --master spark://192.168.152.129:7070 \
 --name "spark_demo" \
 --queue ${YARN_QUEUE} \
 --deploy-mode ${DEPLOY_MODE} \
 --driver-memory 6g \
 --driver-cores 4 \
 --executor-memory 12g \
 --executor-cores 15 \
 --num-executors 10 \
 --archives ./source/py27.zip#python_env \
 --conf spark.default.parallelism=150 \
 --conf spark.executor.memoryOverhead=4g \
 --conf spark.driver.memoryOverhead=2g \
 --conf spark.yarn.maxAppAttempts=3 \
 --conf spark.yarn.submit.waitAppCompletion=true \
 --conf spark.pyspark.driver.python=./source/py27/bin/python2 \
 --conf spark.yarn.appMasterEnv.PYSPARK_PYTHON=./python_env/py27/bin/python2 \
 --conf spark.pyspark.python=./python_env/py27/bin/python2 \
 ./${ModelType}.py $input_path_train $input_path_test $output_path