import tensorflow as tf

with tf.name_scope('netTesla'):

    with tf.name_scope('train_data'):
    # the input data should be normalized, both x and y
        x_input = tf.placeholder(dtype=tf.float32,shape=[None,66,200,3])
        y_input = tf.placeholder(dtype=tf.float32,shape=[None,1])
    with tf.name_scope('layers'):
        conv1 = tf.layers.conv2d(x_input,24,5,2,activation=tf.nn.relu,use_bias=True,kernel_initializer=tf.truncated_normal_initializer(stddev=0.1),)
        conv1 = tf.layers.batch_normalization(conv1)
        conv2 = tf.layers.conv2d(conv1,36,5,2,activation=tf.nn.relu,use_bias=True,kernel_initializer=tf.truncated_normal_initializer(stddev=0.1))
        conv2 = tf.layers.batch_normalization(conv2)
        conv3 = tf.layers.conv2d(conv2,48,5,2,activation=tf.nn.relu,use_bias=True,kernel_initializer=tf.truncated_normal_initializer(stddev=0.1))
        conv3 = tf.layers.batch_normalization(conv3)
        conv4 = tf.layers.conv2d(conv3,64,3,1,activation=tf.nn.relu,use_bias=True,kernel_initializer=tf.truncated_normal_initializer(stddev=0.1))
        conv4 = tf.layers.batch_normalization(conv4)
        conv5 = tf.layers.conv2d(conv4,64,3,1,activation=tf.nn.relu,use_bias=True,kernel_initializer=tf.truncated_normal_initializer(stddev=0.1))
        conv5 = tf.layers.batch_normalization(conv5)
        flatten = tf.reshape(conv5,[-1,18*64])

        fc6 = tf.layers.dense(flatten,200)
        fc7 = tf.layers.dense(fc6,50)
        fc8 = tf.layers.dense(fc7,10)

        output = tf.layers.dense(fc8,1)

    with tf.name_scope('loss'):
        loss = tf.losses.mean_squared_error(y_input,output)

    with tf.name_scope('train'):
        train_step = tf.train.AdagradOptimizer(learning_rate=0.001).minimize(loss)