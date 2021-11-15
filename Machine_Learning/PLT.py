"""
PARAMETER KIND:
    - LINE = line plot (default)
    - bar = vertical bar plot
    - barh = horizontal bar plot
    - hist = histogram
    - box = box plot
    - kde = Krenel Density Estimation plot
    - density = same as kde
    - area = area plot
    - pie = pie plot
    - scatter = scatter plot
    - hexbin = hexbin plot
""" 

#plot line chart
df.column.plot(figsize = (20,6)) #(width,height)

#plot histogram
df.column.plot(kind = "hist", title = "Name", fontsize = 12)

#plot histogram with defined number of bins
df.column.hist(bins = 50)

#plot 2 columns in the same chart
df[[column,column]].plot(figsize = (20,4))

#plot bar based on groupby and mean
df.groupby(column).mean()[supervising_column].plot(kind = "bar")

df.groupby(column)[["yearBuilt","YrSold"]].mean().plot(kind = "bar", grid = True)

#BOX plot
#notch = True = confidence interval
#whis = nastavi hodnotu vzdialenosti fuzov, default je 1.5 * IQR
df.column.plot.box()

df.boxplot(column =  [column], by = column_name, figsize= (10,6), grid = False)

#SCATTER PLOT
df.plot.scatter(x=column, y = column, c = column, figsize= (10,8))

sns.pairplot(df, hue = column)

df4.plot.hist(stacked=True, bins=20)
df4["a"].plot.hist(orientation="horizontal", cumulative=True)

df2.plot.bar(stacked=True)

df.plot.area(stacked=False)

ždf.plot.hexbin(x="a", y="b", C="z", reduce_C_function=np.max, gridsize=25);