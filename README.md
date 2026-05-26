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

## 05.05 - class. first time actual Data Statistics - in Lab 5 & 6 in enauczanie course & univariate statistics in the e-book
**Notes:**
- GOAL THIS WEEK - learn how to interpret data statistics for ONE variable
- first task: plot - showing prices by room type - price by room type
- - what kind of plot? - quantative / logarythmic prices by room type - HISTOGRAM or BINS
  - how to show 3 histograms on one plot? - use alpha transparency, kde = true (shapes), automatic legend. in seaborn you can use hue or kde = true
  - alternatively - several box plots
- self test open - preparation for next weeks Quiz - starting now, quiz every week - OPEN 24 HOURS
- great reference for making seaborn plots - https://seaborn.pydata.org/examples/index.html <- gallery with pictures and code snippets
- TABLE: price usd
- - statistics: mean, median, Q1, Q3 (quart-le), min & max ->
  - Private, shared & apartaments v
  - use describe or tabulate to create table - use groupby roomtype
  - - important - data wrangling, transformations, mistakes in data, imputations - make sure everything is checked properly, or else result won't be accurate
    - teacher highlights the importance - all work we've done so far shows in this stage
  - this section is shown in the "univariate analysis" ebook sections: "summary statistics" and "cross-sectional analysis"
  - - Results: 87,8 ; 71 ; 207 ;; 70 ; 50 ; 160
    - First step: prepare rich value with the middle value. - find biggest difference between types - Shared Rooms have biggest difference
    - - What does it mean? - SKEWEDNESS, VARIABILITY
      - Re:Variability - Range: the difference between the “maximum” and “minimum” value. - low is small difference, high is big difference
    - how to interpret the Median? - 50% of rooms is cheaper and the other 50% is more expensive
- TOMORROW: WE WILL PLOT SOMETHING ON A PIECE OF PAPER - then after a few minutes teacher shows correct solution. - this isn't graded
- lab 6 has practice exercises (optional)

## 12.05 - class. Quiz day. Bivariate Statistics (relationships of data)
**Notes:**
- today, we will focus on CONTINUOUS DISTRIBUTIONS - showing how two distributions relate to each other - relationships
- this week's task: find some significant strong relationships between two variables, so they can be both quantitative or continuous
- - if there is a nice linear relationship between ex. price and rating (scatter plot in seaborn):
  - - sns.scatterplot(data=airbnb, y='price', x='rating')
    - graph ends up messy, unreadable. fix -> logarythm
    - - > airbnb['price']=airbnb['price'].re[;ace(0, np.nan) -> airbnb['logprice']=np.log(airbnb['price']); sns.scatterplot, data=airbnb, y='logprice', x='rating');
        > seaborn scatterplot. read documentation
        > ended up with no correlation
- - quantitative: could be a linear or nonlinear / ordinal relationship
  - if no relationship - that means there is no relationship
  - sometimes, one could be quantitative and another ordinal
- two key properties: sign & magnitude (the latter has a formula) - with standard (unheard)
- logarythm of price (log price) log y = b0 + b1x
- - y = exponential function (b0 +b1x)
  - no measure of coreelation possibility for descriptive statistics
- Starting today: until end of semester + next - using **sciy.stats**
- - now: print correlation coefficient
  - hitmap: ss.pearsonr(dr_height['Father'], df_height['Son'])
  - ss.pearson(airbnb['logprice'], airbnb['racing')
  - airbnb2 = airbnb.dropna()
- if its not statistically structured. do not wrap it up
- types of rank correlations
- sorting/ranking by levels - Tay Kendalk's
- spearman.k - for price vs number of reviews
- calling the parameters - corr {person, kendall spearman) - airbnb.corr(airbnb, method='kendal' ..
- heatmap - default name, not fully correct
- - creating a heatmap
  - rememner s ha,e
- skewed data
?? ok i think my notes for this session are not the Best. my apologies to reader (& future me)

## 19.05 - class. Lab 7. Bivariate statistics
**Notes:**
- notebook in lab 7: plot relationship about total bills and tips - joinplot - scatterplot
- - linearization
  - everything done on the "Tips" file - uploaded here
- data cleansing and piping homework

## 26.05 - class. Lab 8. Multivariate statistics
**Notes:**
- file attached "Regression.ipynb" - main file
