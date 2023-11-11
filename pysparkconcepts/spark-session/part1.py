import Common as c
print(c.spark.version)
print(c.spark.sparkContext.version)
# print(help(c.spark.range)) # way of printing spark range details
'''
range(start: int, end: Optional[int] = None, step: int = 1, numPartitions: Optional[int] = None) -> pyspark.sql.dataframe.DataFrame method of pyspark.sql.session.SparkSession instance
    Create a :class:`DataFrame` with single :class:`pyspark.sql.types.LongType` column named
    ``id``, containing elements in a range from ``start`` to ``end`` (exclusive) with
    step value ``step``.
    
    .. versionadded:: 2.0.0
    
    Parameters
    ----------
    start : int
        the start value
    end : int, optional
        the end value (exclusive)
    step : int, optional
        the incremental step (default: 1)
    numPartitions : int, optional
        the number of partitions of the DataFrame
    
    Returns
    -------
    :class:`DataFrame`
    
    Examples
    --------
    >>> spark.range(1, 7, 2).collect()
    [Row(id=1), Row(id=3), Row(id=5)]
    
    If only one argument is specified, it will be used as the end value.
    
    >>> spark.range(3).collect()
    [Row(id=0), Row(id=1), Row(id=2)]

None
'''
df=c.spark.range(1,10,2) # 1- starting point | 2- ending point | 3- interval
print(type(df))
df.show()
df.printSchema()
print(df.rdd.getNumPartitions()) # getting 1 partition [Ideally: default partition should be 2]
