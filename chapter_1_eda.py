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
    mo.md(
        r"""Exploratory Data Analysis (EDA) is an approach to analyzing data sets to summarize their main characteristics, often using statistical graphics and other data visualization methods."""
    )
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
def _(mo):
    mo.md(r"""## Rectangular Data""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    The typical frame of reference for an analysis in data science is a rectangular data object, like a spreadsheet or database table.

    Rectangular data is the general term for a 2-dimensional matrix with rows indicating records (cases) and columns indicating features (variables); dataframe is the specific format in R and Python. The data doesn't always start in this form: Un-structured data (ex: text) must be processed and manipulaterd so that it can be represented as a set of features in the rectangular data.
    """
    )
    return


@app.cell
def _(mo):
    mo.ui.table(
        data={
            "Dataframe": "Rectangular data (like a spreadsheet) is the basic data structure for statistical and machine learning models",
            "Feature": "A Column within a table is commonly referred to as a feature",
            "Outcome": "Many Data science projects involve predicting an outcome - often yest/no outcome. The features are sometimes used to predict the outcome in an experiment or a study",
            "Records": "A Row within a table is commonly referred to as a record.",
        }
    )
    return


@app.cell
def _(mo):
    mo.md(r"""### A typical DataFrame format""")
    return


@app.cell
def _():
    import polars as pl

    return (pl,)


@app.cell
def _(pl):
    pl.read_csv("./data/state.csv")
    return


@app.cell
def _(mo):
    mo.md(r"""## Non Rectangular Data Structures""")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
