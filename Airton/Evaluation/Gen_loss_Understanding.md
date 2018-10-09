#  Gen_loss_Gan

<p>The measures are:</p>
    gen_loss_GAN : predict_fake
    gen_loss_L1 : targets vs outputs<br/>
    discrim_loss : predict real vs predict fake<br/>
<p>The gradients are on:</p>
    discrim_loss : predict real vs predict fake<br/>
    gen_loss : weight average of predict_fake and targets vs outputs<br/>
<p>The code below is trying to make predict fake go down so that the gen_loss_GAN goes up:</p>
    with tf.name_scope("discriminator_loss"):<br/>
        \# minimizing -tf.log will try to get inputs to 1<br/>
        \# predict_real => 1<br/>
        \# predict_fake => 0<br/>
       discrim_loss = tf.reduce_mean(-(tf.log(predict_real + EPS) + tf.log(1 - predict_fake + EPS)<br/>
<p>This works because the predict_real and predict_fake use the same discriminator respectively on actual targets and outputs from generator</p>
    with tf.variable_scope("discriminator", reuse=True):<br/>
<p>Then the second which has the code below is trying to make predict fake go up so that gen_loss_GAN goes down:</p>
    with tf.name_scope("generator_loss"):<br/>
        \# predict_fake => 1<br/>
        \# abs(targets - outputs) => 0<br/>
        gen_loss_GAN = tf.reduce_mean(-tf.log(predict_fake + EPS))<br/>
        gen_loss_L1 = tf.reduce_mean(tf.abs(targets - outputs))<br/>
        gen_loss = gen_loss_GAN * a.gan_weight + gen_loss_L1 * a.l1_weight<br/>
<p>We can see the discriminator is trying to minimize predict_fake, and the other to maximize predict_fake.</p>
<p>Predict fake is:</p>
    with tf.variable_scope("discriminator", reuse=True):<br/>
        \# 2x [batch, height, width, channels] => [batch, 30, 30, 1]<br/>
        predict_fake = create_discriminator(inputs, outputs)<br/>
<p>Predict fake outputs are:</p>
    with tf.variable_scope("generator"):<br/>
    out_channels = int(targets.get_shape()[-1])<br/>
    outputs = create_generator(inputs, out_channels)<br/>
<p>The mean predict_fake is directly linked to generator.
So the discriminator is trying to minimize the generator, and the other to maximize the generator.</p>
    


