# Descriptive Statistics with Python

<img src="img/ds.png" alt="Descriptive Statistics 2026" style="width: 40%; height: auto;" />

## 17.03.26 - Day of fork.
**Notes:**
- get git ( https://git-scm.com/ )
- add collaborators to work together
- log github into vscode
- copying repo into vscode (local clone)
- installing thru git bash terminal - pip install dfply
- things done in class will not be the same as things at home (no time for everything)
- everything else in 02-piping file on the repo. read it
- do exercises
- learn how to push git updates .

## 31.03 - class. working with "airbnb" data file
**Notes:**
- create new jupiter notebook file - "31.03.ipynb" in main branch
- follow teachers instructions.
- - how do i make it so i dont have to repeat "import"s every time i make a python cell ?
- connecting on google collab notebook


## 21.04 - seaborn and matplotlib - back in person
**Notes:**
- install matplotlib and seaborn
- standardialization vs normalization - Normalization rescales data to a fixed range, while standardization transforms both data and range
- - methods of normalization: minmax, z score ...
  - why each method? "what you want to do with it" vs "regression" ?
- data binning; how to aggregate prices?
- - percent of data to be put into bins
  - Create In Pandas Own Frequency Table
  - Price & Frequency
  - bins & n (number)
  - - cutting prices into equal length of categories
    - pretty binning - your OWN limits, design, ex. 0-1000, 1000-3000
    - functions: pd.qcut (pandas quantiy cut), pd.cut (pandas cut)
    - price_cat = pd.cut() << - write formula with labels, formula for price category PRACTICE AT HOME
    - value-counts = how many frequences per label are there
    - freq function python
    - - next lecture Plots
      - next week co()tative plots & grids of plots
      - then after interactive plots possible in python
HOMEWORK: frequency table, price_cat, no plot yet | until NEXT WEEK | airbnb data used earlier
- bins: bars representing each bin / category for plot
9 more days to do data cleansing with team !!

## 24.04 - class. working with "airbnb" data file, barplots
**Notes:**
- started with short quiz
- reviewing homework - highlighting barplot significance
- - qualitative barplots
```
airbnb['price_cat'].value_counts()

f, ax = plt subplots (figsize = (7,5
sns.despine(f)

sns.hisplot(
        diamonds,
        x="price", hue = "cut"
        multiple="stack
        palette="light:m_r"
        edgecolor=".3",
        linewidth=".5",
        log_scale=True,
)

# maybe i should start doing notes in a jupyter notebook instead...
```
- - seaborn relplot displot catplot
  - seaborn > matplotlib in difficulty
  - Rating vs log price Scatter Plot
  - visualization of distribution of prices
  - Data Visualization Report: The Dataset - listing_id, description, host_id, host_name, neighbourhood_full, coordinates, listing added, room_type, rating, price ...
  - HOMEWORK: find interesting facts about the airbnb from plots alone - in teams
LOOK AT THE GOOGLE COLAB NOTEBOOK - TEACHER'S FILE
