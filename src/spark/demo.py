from pyspark import SparkConf, SparkContext

if __name__ == "__main__":
    conf = SparkConf().setAppName('test')
    sc = SparkContext(conf=conf)
    sc.stop()