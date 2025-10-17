import marimo

__generated_with = "0.17.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r""" """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Exploratory Data Analysis""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Exploratory Data Analysis (EDA) is an approach to analyzing data sets to summarize their main characteristics, often using statistical graphics and other data visualization methods.""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Types of Structured Data""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    * Numeric: Data that are expressed on a numeric scale.
        * Continous: Data that can take on any value in an interval. Ex: Weight, Height of a person etc...
        * Discrete: Data that can take on only integer values, such as counts. Ex: Number of cars, Number of students etc...

    * Categorical: Data that can take on only a specific set of values representing a set of possible categories.
        * Binary: A special case of categorical data with just two categories of values. Ex: 0/1, true/false.
        * Ordinal: Categorical data that has an explicit ordering. Ex: Sizes of Shirt (XS, S, M, L, XL) etc...
    """
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
