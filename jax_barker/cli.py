"""Console script for jax_barker."""

import click


@click.command()
def main():
    """Main entrypoint."""
    click.echo("jax_barker")
    click.echo("=" * len("jax_barker"))
    click.echo("Formulas to tell you when the price is right")


if __name__ == "__main__":
    main()  # pragma: no cover
