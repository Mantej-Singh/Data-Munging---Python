#Here i am using RegEx to split a cell 


## Before:
[![screenshot_1486744855.png](https://s19.postimg.org/xp3gdq62b/screenshot_1486744855.png)](https://postimg.org/image/6r9jbzlf3/)

##After:
[![screenshot_1486744936.png](https://s19.postimg.org/5dhwgom5v/screenshot_1486744936.png)](https://postimg.org/image/ey1j3kbhr/)

##Code:
```
df["Campaign_Title"]=df.Campaign_Name.str.split('_').apply(lambda x: x[2] + '_' + x[3]+x[4])
```



#ReIndexing:

##Before:
[![screenshot_1486745113.png](https://s19.postimg.org/fou99cdv7/screenshot_1486745113.png)](https://postimg.org/image/ld0k08i7j/)

##After:
[![screenshot_1486745137.png](https://s19.postimg.org/5st69p837/screenshot_1486745137.png)](https://postimg.org/image/n63gok3e7/)

Code:
```
df.set_index([[2,3,4,0,1]],inplace=True)
df=df.sort_index()
df.head()
```
- - - -

#Special thanks to my teachers:
    * Kevin Markham <kevin@dataschool.io>
    * Swarupa @rsmaitreyi <The Data Incubator>
