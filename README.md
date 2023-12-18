# Language-Distribution-Map

Python project to plot language speaker distributions on a map

```bash
# Requires the pandas, plotly, and pycountry modules
pip install -r requirements.txt
# Use langScraper.py to get the language data JSON from the CIA language database website.
python3 langScraper.py 
```

Then you can use the plotLangs.ipynb to
 * plot the given language map or get a breakdown of the languages spoken in a country.
 * an interactive barplot using bokeh and javascript which lets you choose a language, and shows the percentage of the population in several countries which speak that language

