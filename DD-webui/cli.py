import click
import warnings
warnings.simplefilter("ignore")

@click.group()
def cli():
    """The DD-web-demo CLI"""
    pass

@cli.command()
@click.argument('photo_path',  type=str)
def predict(photo_path):
    """
    Predict the tags of a photo\n
    The input arg is photo_path
    Usage:
        python cli.py predict <photo_path>
    """
    click.echo("Loading model...")

    import tensorflow as tf
    import DD_tools
    model = tf.keras.models.load_model("./model/model-resnet_custom_v3.h5", compile=False)

    print("Done...\nPredicting...")
    tags = DD_tools.load_tags("./model/tags.txt")
    click.echo(DD_tools.get_mark(photo_path, model, tags, 0.75, False))


    

if __name__ == '__main__':

    cli()
