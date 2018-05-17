# PPMSplot README

## Installing
Simply run `pip install PPMSplot` to install PPMSplot tpo your machine

## Plotting Data
To plot data you can execute PPMSplot by running `PPMSplot <config json filepath>`

To generate a PPMSplot config.json file, simply run `PPMSconfig`


## config.json syntax
### Fields
#### plotSettings
The field `plotSettings` is an object which sets all the global plot settings
+ `outputFilename` - string, sets the filename for the generated graph. Can support eps, pdf, pgf, png, ps, raw, rgba, svg, svgz
+  `figureTitle` - optional - string, title for the figure
+  `xTitle` - optional - string, x axis title
+  `yTitle` - optional - string, y axis title
+  `legend` - bool, controls whether legend is drawn
+ `flipX` - bool, controls flipping x axis
+ `flipY` - bool, controls flipping x axis
+ `xMin` - number, sets minimum x of plot frame
+ `xMax` - number, sets maximum x of plot frame
+ `yMin` - number, sets minimum y of plot frame
+ `yMax` - number, sets maximum y of plot frame
+ `grid` - bool, enables drawing of grid

#### files
The `files` field is a list of any number of file objects. Each file object extracts data from a single file. It can produce multiple series from a single file columnwise.
+ `filename` - string, the filepath to a datafile
+ `rowStart` - integer, line number to start extracting data at
+ `rowEnd` - integer, line number to stop extracting data at. Set to 0 to extract till end of file
+ `series` - list, the `series` field is a list of objects which define the properties for individual series 

##### series
+ `label` - string, the label to show in the legend
+ `style` - string, a matplotlib styling string. Can change both colour and marker style. See *style* section for more info.
+ `xColumnIndex` - integer, the column in the file to be used for the x axis in this series
+ `yColumnIndex` - integer, the column in the file to be used for the y axis in this series
+ `xMin` - number, minimum x value to trim series at
+ `xMax` - number, maximum x value to trim series at

#### style
The `style` field can contain up to two characters. The first describing the marker, the second describing the colour. If only a single character is specified the unspecified style-setting will result to default.

**marker style**
+ **-** line plot (default)
+ **--** dashed line plot
+ **.** scatter plot

**colour style**
By default colour will be unique for each series
+ **r** red
+ **g** green
+ **b** blue
+ **k** black

**combined style examples**
+ **-r** red line
+ **.k** black scatter plot


### Example config.json
```json
{
    "plotSettings": {
        "outputFilename": "example.png",
        "figureTitle": "Figure title",
        "xTitle": "x axis",
        "yTitle": "y axis",
        "legend": true,
        "flipX": false,
        "flipY": false,
        "xMin": 0,
        "xMax": 100,
        "yMin": 0,
        "yMax": 100,
        "grid": false
    },
    "files": [
        {
            "filename": "example.dat",
            "rowStart": 36,
            "rowEnd": 0,
            "series": [
                {
                    "label": "example",
                    "style": "-",
                    "xColumnIndex": 2,
                    "yColumnIndex": 4,
                    "xMin": 0,
                    "xMax": 3200
                }
            ]
        }
    ]
}```