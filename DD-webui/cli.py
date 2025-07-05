import click
import tensorflow as tf
import DD_tools
import logging
logging.getLogger("tensorflow").setLevel(logging.ERROR)
tf.config.set_soft_device_placement(True)
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)


gpus = tf.config.experimental.list_physical_devices('GPU')

# 如果有 GPU 可用，启用 GPU 并设置动态分配内存
if gpus:
    try:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
        print("Using GPU for model loading and training.")
    except RuntimeError as e:
        print(e)
else:
    print("No GPU available. Using CPU instead.")

model = tf.keras.models.load_model("./model/model-resnet_custom_v3.h5", compile=False)
tags = DD_tools.load_tags("./model/tags.txt")

@click.group()
def cli():
    """The DD-web-demo CLI"""
    pass

@cli.command()
@click.argument('photo_path',  type=str)
def predict(photo_path):
    """
    Predict the survival of a passenger based on their input data\n
    The input arg is photo_path
    """
    click.echo(DD_tools.get_mark(photo_path, model, tags, 0.5, False))


    

if __name__ == '__main__':

    cli()