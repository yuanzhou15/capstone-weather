#  Gen_loss_Gan

The measures are:<br/>
gen_loss_GAN : predict_fake
gen_loss_L1 : targets vs outputs
discrim_loss : predict real vs predict fake<br/>
The gradients are on:<br/>
discrim_loss : predict real vs predict fake
gen_loss : weight average of predict_fake and targets vs outputs<br/>
The code below is trying to make predict fake go down so that the gen_loss_GAN goes up:<br/>
with tf.name_scope("discriminator_loss"):
    \# minimizing -tf.log will try to get inputs to 1
    \# predict_real => 1
    \# predict_fake => 0
    discrim_loss = tf.reduce_mean(-(tf.log(predict_real + EPS) + tf.log(1 - predict_fake + EPS)<br/>
This works because the predict_real and predict_fake use the same discriminator respectively on actual targets and outputs from generator<br/>
with tf.variable_scope("discriminator", reuse=True):<br/>
Then the second which has the code below is trying to make predict fake go up so that gen_loss_GAN goes down:<br/>
with tf.name_scope("generator_loss"):
    \# predict_fake => 1
    \# abs(targets - outputs) => 0
    gen_loss_GAN = tf.reduce_mean(-tf.log(predict_fake + EPS))
    gen_loss_L1 = tf.reduce_mean(tf.abs(targets - outputs))
    gen_loss = gen_loss_GAN * a.gan_weight + gen_loss_L1 * a.l1_weight<br/>
We can see the discriminator is trying to minimize predict_fake, and the other to maximize predict_fake.<br/>
Predict fake is:<br/>
with tf.variable_scope("discriminator", reuse=True):
    \# 2x [batch, height, width, channels] => [batch, 30, 30, 1]
    predict_fake = create_discriminator(inputs, outputs)<br/>
    Predict fake outputs are:<br/>
    with tf.variable_scope("generator"):
    out_channels = int(targets.get_shape()[-1])
    outputs = create_generator(inputs, out_channels)<br/>
The mean predict_fake is directly linked to generator.
So the discriminator is trying to minimize the generator, and the other to maximize the generator.
    


